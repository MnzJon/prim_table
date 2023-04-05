from PrimTable import Table
from PrimTable import Row

row1 = Row([2,2,4,5])
row2 = Row([1,1,1,9])
row3 = Row([9,5,3,4])
row4 = Row([7,5,4,3])

table = Table("Test Table")
table.append_row(row1)
table.append_row(row2)
table.append_row(row3)
table.append_row(row4)

print(table)

table[0][1] = 39
print(table)

columnd_data = [
        [4,"TIMES"],
        [2,"HI"],
        [1,"DUDES"],
        [9,"TIMES"],
        [3,"TIMES"],
        [7,"FLIES"],
        ]

print("Preparing to append rows")
table.insert_column_data(1,columnd_data)
print(table)
print("Test")

subset_table = table.subset_of([0,2])
print(subset_table)
