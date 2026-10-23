# Build a "update csv" from the ReCAP Customer Codes sheet
# ( https://docs.google.com/spreadsheets/d/1ewSv5EilkS8LR1Fx51AG7iJwn5o-ZYeynJiCGf48XpU/edit?gid=0#gid=0 )
#
# Usage:
#     - Download CSV export of ReCAP Customer Codes sheet
#     - Run:
#         cd vocabularies/scripts
#         pip install -r requirements.txt
#         python build_recap_customer_code_update_csv.py google-sheet-export.csv --outfile update.csv
#     - Inspect update.csv (potentially manually adding missing labels and other values)
#     - Use update-csv.py to patch the recapCustomerCodes.csv:
#         python update-csv.py recapCustomerCodes update.csv
#     - Proceed with serialization and committing changes for review.

import csv
import argparse


class SheetRow:
    """
    Representing a single row exported from the ReCAP Customer Codes Google Sheet
    """
    def __str__(self):
        return f'{self.id()} ({self.institution})' \
            + (f', EDD enabled' if self.edd else '') \
            + (f', deliverable to {', '.join(self.deliverable_to)}' if len(self.deliverable_to) else '')

    def id(self):
        prefix = f'{self.depository}:' if self.depository != 'recap' else ''
        return f'{prefix}{self.code}'

    @staticmethod
    def from_row(row, depository):
        inst = SheetRow()

        inst.depository = depository
        inst.code = row['CUSTOMER CODE'].rstrip()
        inst.institution = row['OWNING INSTITUTION']
        inst.label = row['DESCRIPTION']
        if inst.institution == 'NEW YORK':
            inst.deliverable_to = [code for code in row['DELIVERY_RESTRICTIONS'].split(',') if code]
        else:
            inst.deliverable_to = [code for code in row['NEW YORK - CROSS_PARTNER_DELIVERY_RESTRICTIONS'].split(',') if code]
        inst.edd = 'EDD' in row['RECAP_DELIVERY_RESTRICTIONS'].split(',')

        return inst


def spreadsheet_rows(path):
    """
    Get all spreadsheet rows for CSV path
    """
    depository = 'recap'
    with open(path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = []
        for row in reader:
            code = row.get('CUSTOMER CODE', '')
            # The HD customer codes are the ones below this message:
            if code.startswith('HD LAS values start here'):
                depository = 'hd'
            elif len(code) in [2, 3]:
                # For now, customer codes expected to be 2 or 3 characters
                row['depository'] = depository
                rows.append(SheetRow.from_row(row, depository))

    # We only care about entries belonging to partner institutions:
    rows = [
        r for r in rows
        if len(r.institution) \
        and not r.institution.startswith('ReCAP') \
        and not r.institution.startswith('HD')
    ]

    return rows


def write_outfile(rows, outfile):
    rows_to_write = [
        { 'id': row.id(), 'nypl:deliverableTo': ';'.join(row.deliverable_to) }
        for row in rows
    ]

    with open(outfile, 'w', newline='') as csvfile:
        fieldnames = ['id', 'nypl:deliverableTo']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, lineterminator='\n')

        writer.writeheader()
        for row in rows_to_write:
            writer.writerow(row)

    print(f'\nWrote to {outfile}')


def main(args):
    rows = spreadsheet_rows(args.csvfile)

    print('Built rows:')
    for r in rows:
        print(r)

    write_outfile(rows, args.outfile)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('csvfile')
    parser.add_argument('-o', '--outfile')

    args = parser.parse_args()

    main(args)
