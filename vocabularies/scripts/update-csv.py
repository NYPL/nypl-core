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

import csv
import sys


def theThing():
    which = '../csv/' + sys.argv[1] + ".csv"
    update_data = sys.argv[2]

    with open(which, 'r+') as vocabulary_file:
        with open(update_data, 'r') as update_data_file:
            vocabulary_dict = csv.DictReader(vocabulary_file)
            update_data_dict = csv.DictReader(update_data_file)
            for vocabulary_row in vocabulary_dict:
                for update_data_row in update_data_dict:
                    if update_data_row['skos:notation'] == vocabulary_row['skos:notation']:
                        for property in update_data_row:
                            value = update_data_row[property]
                            should_update_value = value is not None or value != ''
                            if should_update_value is True:
                                vocabulary_row[property] = update_data_row[property]
                    writer = csv.DictWriter(vocabulary_file, vocabulary_dict.fieldnames)
                    writer.writeheader()
                    writer.writerows(vocabulary_dict)


theThing()
