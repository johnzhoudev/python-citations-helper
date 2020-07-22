#! /opt/anaconda3/bin/python
import pyperclip

# Open file containing input and read
table_data_file = open('./auto_table_3.txt', 'r')
table_data = table_data_file.readlines()
table_data_file.close()

table_str = ""
for i in range(len(table_data)):

    #split by "-"

    strings = table_data[i].split("–")

    rest = ""
    for j in range(1, len(strings) - 1):
        rest += strings[j].strip(" \n") + " "
    rest += strings[len(strings) - 1].strip(" \n")

    table_str += "<tr>\n"
    table_str += "\t<td>" + strings[0].strip(" \n") + "</td>\n"
    table_str += "\t<td>" + rest + "</td>\n"
    table_str += "</tr>\n"


print("copying table")
pyperclip.copy(table_str)


