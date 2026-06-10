import csv
import argparse


class SheetRow:
    def __str__(self):
        return f'{self.id()} ({self.institution})' \
            + (f', EDD enabled' if self.edd else '') \
            + (f' => {', '.join(self.deliverable_to)}' if len(self.deliverable_to) else '')

    def id(self):
        prefix = f'{self.depository}:' if self.depository != 'recap' else ''
        return f'{prefix}{self.code}'

    @staticmethod
    def from_row(row, depository):
        inst = SheetRow()

        inst.depository = depository
        inst.code = row['CUSTOMER CODE']
        inst.institution = row['OWNING INSTITUTION']
        inst.label = row['DESCRIPTION']
        if inst.institution == 'NEW YORK':
            inst.deliverable_to = [code for code in row['DELIVERY_RESTRICTIONS'].split(',') if code]
        else:
            inst.deliverable_to = [code for code in row['NEW YORK - CROSS_PARTNER_DELIVERY_RESTRICTIONS'].split(',') if code]
        inst.edd = 'EDD' in row['RECAP_DELIVERY_RESTRICTIONS'].split(',')

        return inst


def spreadsheet_rows(path):
    depository = 'recap'
    with open(path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = []
        for row in reader:
            code = row.get('CUSTOMER CODE', '')
            if code.startswith('HD LAS values start here'):
                depository = 'hd'
            elif len(code) == 2:
                row['depository'] = depository
                rows.append(SheetRow.from_row(row, depository))

    # We only care about entries belonging to partner institutions:
    rows = [r for r in rows if len(r.institution) and not r.institution.startswith('ReCAP')]

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


def main(args):
    rows = spreadsheet_rows(args.csvfile)

    print('Rows:')
    for r in rows:
        print(r)

    write_outfile(rows, args.outfile)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('csvfile')
    parser.add_argument('-o', '--outfile')
    parser.add_argument('-v', '--verbose', action='store_true')

    args = parser.parse_args()

    main(args)
