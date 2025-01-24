# This script updates the keys in a given file with the provided values.
#
# Depends on Python 3
#
# Install dependencies:
#   pip install -r requirements.txt
#
#
#   Params:
#    - [which]: Name of csv file to update
#               (e.g. 'recapCustomerCodes', 'organizations').
#    - [updateInfo] Name of csv file with values to update
import sys
import csv

def csv_to_dict(file_name:str) -> dict:
    """
    Pass the filename and column number of the CSV file that you would like to make the keys in the
    dictionary. For example Column One is 1 and Column five is 5.
              usage: csv_to_dict("example.csv", 2)
    :param file_name: string
    :param column_as_key: integer
    :return: dictionary
    """
    information_dict = {}
    tmp_dict = {}

    try:
        # Open the CSV file
        with open(file_name, 'r') as f:
            raw = f.readlines()

        header = raw[:1][0].strip().split(',')
        for i, line in enumerate(raw[1:]):
            tmp = line.replace("\n", "").split(",")
            current_key = tmp[0]
            try:
                for x, key in enumerate(header):
                    tmp_dict[key] = tmp[x]
            except Exception as e:
                if e is None:
                    print(e)
            information_dict[current_key] = tmp_dict
            tmp_dict = {}

        return information_dict

    except Exception as e:
        print(e)
        return {"Error": e}


def update_properties(target, new, key):
    for property in new[key]:
        if target[key] is not None:
            target[key][property] = new[key][property]


def theThing():
    vocabulary_file = '../csv/' + sys.argv[1] + ".csv"
    update_filepath = sys.argv[2]
    vocabulary_dict = csv_to_dict(vocabulary_file)
    update_dict = csv_to_dict(update_filepath)
    new_dict = dict(vocabulary_dict)
    for v_id in vocabulary_dict:
        for up_id in update_dict:
            if up_id not in vocabulary_dict:
                new_dict[up_id] = update_dict[up_id]
            if v_id == up_id:
                update_properties(new_dict, update_dict, v_id)
    sorted_new_dict = dict(sorted(new_dict.items()))
    with open(vocabulary_file, 'r') as f:
        header = csv.DictReader(f).fieldnames
    with open('meatballs.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, header)
        writer.writeheader()
        for _, value in sorted_new_dict.items():
            writer.writerow(value)


theThing()
