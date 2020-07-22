#! /opt/anaconda3/bin/python
import pyperclip

# Open file containing input and read
table_data_file = open('./auto_table_2.txt', 'r')
table_data = table_data_file.readlines()
table_data_file.close()

#get rid of newlines
count = 0
for i in range(len(table_data)):
    if (table_data[i] == "\n"):
        count += 1

for i in range(count):
    table_data.remove("\n")

table_str = ""
for i in range(len(table_data) // 19):

    table_str += "<tr>\n"

    #make first half
    for j in range(0, 10):
        index = (i * 19) + j
        table_str += "\t<td>" + table_data[index].strip(" \n") + "</td>\n"
    
    table_str += "</tr>\n"
    table_str += "<tr>\n"

    #make second half
    for k in range (10, 19):
        index = (i * 19) + k
        table_str += "\t<td>" + table_data[index].strip(" \n") + "</td>\n"

    table_str += "</tr>\n"

print("copying table")
pyperclip.copy(table_str)


