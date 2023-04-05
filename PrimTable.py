Asdw

class Row():
    def __init__(self, initial):
        if initial != None:
            self.row = initial
        else:
            self.row = []

    def __getitem__(self, column):
        return self.row[column]

    def __setitem__(self, column, value):
        self.row[column] = value

    def __str__(self):
        return "{}".format(self.row)

    def append(self, element):
        self.row.append(element)

    def insert(self, position, element):
        self.row.insert(position, element)

    def remove(self, position):
        self.row.pop(position)

    def length(self):
        return len(self.row)

    def raw_row(self):
        print(self.row)

class Table():
    def __init__(self, table_name):
        self.table_name = table_name
        self.table = []

    def __getitem__(self, row):
        return self.table[row]

    def append_row(self, row):
        self.table.append(row)

    def default_row(self, elements):
        new_row = []
        for i in range(0, elements):
            new_row.append("")
        return Row(new_row)

    def insert_row(self, position, row):
        self.table.insert(position, row)

# Inserts the values of a columns
# The variable 'columns' contains the values of the column
    def insert_column_at(self, column_number, columns):
        total_rows = len(self.table)

        for i in range(0, total_rows):
            row = self.table[i]
            row.insert(column_number, columns[i])

    def contains_value_in_column(self, row_index, column_index, value):
        row_value = self.table[row_index][column_index]
        return row_value == value

# Column Data: [(Label, Value)]
    def insert_column_data(self, position, column_data):
        # Build the new column with empty values
        column = []
        total_rows = len(self.table)
        for i in range(0, total_rows):
            column.append("")

        # Insert the empty column
        self.insert_column_at(position, column)

        # Update the values with the given column data
        row_index = 0

        for row in self.table:
            other_row = column_data[row_index]
            new_value = other_row[1]

            column_label = other_row[0]
            row_label = row[0]
            row_label_index = 0 

            if self.contains_value_in_column( row_index, row_label_index, column_label):
                row[position] = new_value
            else:   # create a new row
                default_row = self.default_row(row.length())
                default_row[0] = column_label
                self.insert_row(row_index,default_row)

            row_index += 1

    # Create a new table with only the specified columns
    def subset_of(self,columns):
        subset_table = Table(self.table_name + "_Subset")
        for row in self.table:
            new_row = Row([])
            for col_id in columns:
                new_row.append(row[col_id]) 
            subset_table.append_row(new_row)

        return subset_table


    def __str__(self):
        s = ""
        for row in self.table:
            #row.raw_row()
            s += "{}\n".format(row)
        return s

