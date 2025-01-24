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
        # Open the CSV file
        with open(file_name, 'r') as f:
            raw_csv = f.readlines()

        header = raw_csv[:1][0].strip().split(',')
        for _, row_as_string in enumerate(raw_csv[1:]):
            exploded_row = row_as_string.replace("\n", "").split(",")
            current_key = exploded_row[0]
            for index, key in enumerate(header):
                tmp_dict[key] = exploded_row[index]
            information_dict[current_key] = tmp_dict
            tmp_dict = {}

        return information_dict

    except Exception as e:
        print(e)
        return {"Error": e}


def update_properties(target, new, key):
    for property in new[key]:
        if target.get(key) is not None:
            target[key][property] = new[key][property]
        else:
            target[key] = new[key]


def theThing():
    vocabulary_file_path = '../csv/' + sys.argv[1] + ".csv"
    update_filepath = sys.argv[2]

    vocabulary_dict = csv_to_dict(vocabulary_file_path)
    update_dict = csv_to_dict(update_filepath)
    new_dict = dict(vocabulary_dict)

    for up_id in update_dict:
        update_properties(new_dict, update_dict, up_id)

    sorted_new_dict = dict(sorted(new_dict.items()))

    with open(vocabulary_file_path, 'r') as f:
        header = csv.DictReader(f).fieldnames

    with open(vocabulary_file_path, 'w', newline='') as f:
        writer = csv.DictWriter(f, header)
        writer.writeheader()
        
        for _, value in sorted_new_dict.items():
            writer.writerow(value)


theThing()
