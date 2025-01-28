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
#    - [updateInfo] Name of csv file with values to update.
#          * The first row of the file should match the header row of the
#            target CSV.
#          * The csv only need contain the rows you want to update,
#            not the entire csv.
#          * Empty fields do not overwrite existing
#            fields; you only have to provide the single value you are
#            interested in updating. In that case, you still need to
#            make sure you have the correct number of commas.
#          * An example with valid inputs to update the organizations csv is
#            provided at vocabularies/scripts/example-update-csv.csv.
#          * If you are adding a new row to the csv, the values must be
#            provided in the order specified by the header of the csv.
# 
import sys
import csv


def csv_to_dict(file_name: str) -> dict:
    output_dict = {}
    with open(file_name, 'r') as f:
        raw_csv = f.readlines()
        primary_key_name = raw_csv[0].split(',')[0]
        f.seek(0)
        rows = csv.DictReader(f)
        for row in rows:
            primary_key = row[primary_key_name]
            output_dict[primary_key] = row

        return output_dict


# target and new are both dicts with keys that correspond to the first value
# of every row in the provided csvs. The values are each row, converted into
# a dict by csv.DictReader().
# ie:
    # {'mab': {'skos:notation': 'mab', 'skos:prefLabel': 'Rose Reading Room'
    # ...},
    # 'map32': {'skos:notation': 'map32', 'skos:prefLabel': 'Map room',
    # 'skos:altLabel': 'Map room 123,'...}
    # ...}
def get_updated_vocabulary(target, new):
    for key, update_data_row in new.items():
        for property in update_data_row:
            if update_data_row[property] == '':
                # don't overwrite values that are not provided
                continue
            # spreadsheets automatically convert booleans to all caps. Let's
            # make the transistion painless for all.
            if update_data_row[property] == "TRUE" or update_data_row[property] == "FALSE":
                update_data_row[property] = update_data_row[property].lower()
            if target.get(key) is not None:
                target[key][property] = update_data_row[property]
            else:
                # If we are adding a new key to the csv, we assume it has all
                # of the fields included in the header row, in the expected
                # order.
                target[key] = update_data_row
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
            writer.writerow(value)


if __name__ == '__main__':
    main()
