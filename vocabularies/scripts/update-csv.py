# This script updates the keys in a given file with the provided values.
#
# Depends on Python 3
#
# Install dependencies:
#   pip3 install -r requirements.txt
#
#
#   Invocation:
#   cd vocabularies/scripts
#   python3 update-csv.py locations spaghetti.csv
#
#   Params:
#    - [which]: Name of csv file to update
#               (e.g. 'recapCustomerCodes', 'organizations').
#    - [updateInfo] Name of csv file with values to update
import sys
import csv


def csv_to_dict(file_name: str) -> dict:
    information_dict = {}
    tmp_dict = {}

    try:
        with open(file_name, 'r') as f:
            raw_csv = f.readlines()

        header = raw_csv[:1][0].strip().split(',')
        x = []
        for _, row_as_string in enumerate(raw_csv[1:]):
            exploded_row = row_as_string.replace("\n", "").split(",")
            current_key = exploded_row[0]
            for index, key in enumerate(header):
                try:
                    tmp_dict[key] = exploded_row[index]
                except IndexError:
                    # Not every row has the right number of commas. This should
                    # be addressed but should not break the script.
                    print(f'{current_key} is missing value for {key}')
            
            information_dict[current_key] = tmp_dict
            tmp_dict = {}

        return information_dict

    except Exception as e:
        print(e)
        return {"Error": e}


def get_updated_vocabulary(target, new):
    for key, value in new.items():
        for property in value:
            if value[property] == "TRUE" or value[property] == "FALSE":
                value[property] = value[property].lower()
            if target.get(key) is not None:
                target[key][property] = value[property]
            else:
                target[key] = value
    return dict(sorted(target.items()))


def main():
    vocabulary_file_path = '../csv/' + sys.argv[1] + ".csv"
    update_filepath = sys.argv[2]

    vocabulary_dict = csv_to_dict(vocabulary_file_path)
    update_dict = csv_to_dict(update_filepath)
    new_dict = dict(vocabulary_dict)
    
    sorted_new_dict = get_updated_vocabulary(new_dict, update_dict)

    with open(vocabulary_file_path, 'r') as f:
        header = csv.DictReader(f).fieldnames

    with open(vocabulary_file_path, 'w', newline='') as f:
        writer = csv.DictWriter(f, header)
        writer.writeheader()

        for _, value in sorted_new_dict.items():
            try:
                writer.writerow(value)
            except Exception:
                print(value)


if __name__ == '__main__':
    main()
