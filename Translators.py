# Extensions to the PrimTable
from PrimTable import Table, Row

import csv

# returns a table
def from_csv(csv_filepath):
    table = Table("CSV Test")
    with open(csv_filepath, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            table.append_row(Row(row))

    return table
