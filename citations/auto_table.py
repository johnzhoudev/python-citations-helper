#! /opt/anaconda3/bin/python
import pyperclip

# Open file containing input and read
table_data_file = open('./table_data_file.txt', 'r')
table_data = table_data_file.readlines()
def append_heading_row(arr_words):
    return_str = "\t\t<tr>\n\t\t\t"

    for j in range(len(arr_words)):
        arr_words[j] = arr_words[j].replace("°C", "&#8451;")

    for i in range (len(arr_words) - 1):
        return_str += ("<th>" + arr_words[i].strip(' \n') + "</th>\n\t\t\t")
    
    return_str += "<th>" + arr_words[(len(arr_words) - 1)].strip(' \n') + "</th>\n\t\t</tr>\n"
    return return_str


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def append_data_row(arr_words):
    return_str = "\t\t<tr>\n\t\t\t"

    for j in range(len(arr_words)):
        arr_words[j] = arr_words[j].replace("°C", "&#8451;")

    #Append first word, as 1 thing until number detected
    i = 0
    first_str = ""
    while(not is_number(arr_words[i].strip(" \n"))):
        first_str += (arr_words[i].strip(' \n') + " ")
        i += 1

    return_str += "<td>" + first_str.strip(' \n') + "</td>\n\t\t\t"

    #append groups of 3 items as 1 elt, plus check for degree celsius
    for j in range (i, len(arr_words) - 3, 3):
        return_str += ("<td>" + arr_words[j].strip(' \n') + " " + arr_words[j + 1].strip(' \n') + " " + arr_words[j + 2].strip(' \n') + "</td>\n\t\t\t")
    
    return_str += "<td>" + arr_words[len(arr_words) - 3].strip(' \n') + " " + arr_words[len(arr_words) - 2].strip(' \n') + " " + arr_words[len(arr_words) - 1].strip(' \n') + "</td>\n"
    return_str += "\t\t</tr>\n"
    return return_str

#For first line, generate the title with a colspan
first_row = table_data[0].split(" ")
first_line = ""
second_line = ""

for j in range(len(first_row)):
        first_row[j] = first_row[j].replace("°C", "&#8451;")

for i in range(len(first_row)):
    if (first_row[i] == "Global"):
        for j in range (i, len(first_row)):
            second_line += (first_row[j] + " ")
        second_line = second_line.strip(" \n")
        first_line = first_line.strip(" \n")
        break
    else:
        first_line += first_row[i] + " "

line1 = "<table class='wb-table table table-bordered'>\n\t<thead>\n\t\t<tr>\n\t\t\t<th>"
line1 += first_line
line1 += "</th>\n\t\t\t<th colspan='3'>"

line1 += second_line 
line1 += "</th>\n\t\t</tr>\n"

line2 = append_heading_row(table_data[1].split(" "))

#Get all data
master_table_text = line1 + line2 + "\t</thead>\n\t<tbody>\n"
del table_data[0:2]

for line in table_data:
    master_table_text += append_data_row(line.split(" "))

master_table_text += "\t</tbody>\n</table>\n"

print("copying")
pyperclip.copy(master_table_text)


table_data_file.close()

# <table class='wb-table table table-bordered'>
	# 	<thead>
	# 		<tr>
	# 			<th>Change in Degree Days Below 18&#8451; [&#8451; days]</th>
	# 			<th colspan='3'>Global warming level</th>
	# 		</tr>
	# 		<tr>
	# 			<th>Region</th>
	# 			<th>+1&#8451;</th>
	# 			<th>+2&#8541;</th>
	# 			<th>+3&#8541;</th>
	# 		</tr>
	# 	</thead>
	# 	<tbody>
	# 		<tr>
	# 			<td>British Columbia</td>
	# 			<td>-403 (-447, -363)</td>
	# 			<td>-757 (-808, -722)</td>
	# 			<td>-1088 (-1128, -1057)</td>
	# 		</tr>
	# 		<tr>
	# 			<td>Prairies</td>
	# 			<td>-461 (-515, -428)</td>
	# 			<td>-891 (-938, -845)</td>
	# 			<td>-1274 (-1332, -1235)</td>
	# 		</tr>
	# 		<tr>
	# 			<td>Ontario</td>
	# 			<td>-424 (-461, -393)</td>
	# 			<td>-781 (-820, -746)</td>
	# 			<td>-1127 (-1178, -1068)</td>
	# 		</tr>
	# 		<tr>
	# 			<td>Quebec</td>
	# 			<td>-466 (-494, -430)</td>
	# 			<td>-874 (-917, -825)</td>
	# 			<td>-1252 (-1321, -1183)</td>
	# 		</tr>
	# 		<tr>
	# 			<td>Atlantic</td>
	# 			<td>-456 (-489, -420)</td>
	# 			<td>-834 (-861, -795)</td>
	# 			<td>-1194 (-1258, -1127)</td>
	# 		</tr>
	# 		<tr>
	# 			<td>North</td>
	# 			<td>-692 (-740, -629)</td>
	# 			<td>-1328 (-1328, -1274)</td>
	# 			<td>-1917 (-1947, -1835)</td>
	# 		</tr>
	# 	</tbody>
	# 	<tfoot>
	# 		<tr>
	# 			<td>Canada</td>
	# 			<td>-449 (-487, -411)</td>
	# 			<td>-836 (-887, -794)</td>
	# 			<td>-1196 (-1257, -1139)</td>
	# 		</tr>			
	# 	</tfoot>
	# </table>
	# <p>
	# 	<strong>Table 3.1</strong>: Projected changes in heating degree days below 18°C for locations approximating Table C-2 locations in six Canadian regions and Canada as a whole for +1°C, +2°C, and +3°C global warming levels with respect to the 1986-2016 baseline period. Values represent the ensemble projection (25th percentile, 75th percentile) calculated from bias corrected CanRCM4 LE simulations.
	# </p>

def make_table_row():
    print('nrd: new row data, nrh: new row heading, dr: done row, dt: done table')
    while(True):
        input_str = input('Command: ')
        input_str = input_str.strip(' \n')

        if (input_str == 'nrd'):
            row_html = '<tr>\n'
            while(True):

                input_data = input('Data: ')
                input_data = input_data.strip(' \n')

                if (input_data == 'dr'):
                    break

                else:
                    row_html = row_html + '\t<td>' + input_data + '</td>\n'

            row_html += '</tr>\n'
            print('copying row to clipboard')
            pyperclip.copy(row_html)

        elif (input_str == 'nrh'):
            row_html = '<tr>\n'
            while(True):

                input_data = input('Heading: ')
                input_data = input_data.strip(' \n')

                if (input_data == 'dr'):
                    break

                else:
                    row_html = row_html + '\t<th>' + input_data + '</th>\n'

            row_html += '</tr>\n'
            print('copying row to clipboard')
            pyperclip.copy(row_html)

        else:
            print('exiting table constructor')
            break

# Change in July 2.5% Dry Design Temp. [°C] Global warming level
# Region +1°C +2°C +3°C
# British Columbia 2.2 (1.8, 2.6) 4.2 (3.7, 4.8) 6.8 (6.2, 7.4)
# Prairies 2.3 (1.6, 2.7) 4.0 (3.4, 4.7) 6.0 (5.4, 6.5)
# Ontario 1.6 (1.3, 1.9) 3.0 (2.5, 3.4) 4.1 (3.8, 4.5)
# Quebec 1.4 (1.1, 1.7) 3.0 (2.7, 3.3) 4.1 (3.9, 4.5)
# Atlantic 1.3 (1.1, 1.6) 2.8 (2.6, 3.0) 4.1 (3.9, 4.4)
# North 1.7 (1.3, 2.2) 3.2 (2.7, 3.8) 4.7 (4.3, 5.3)
# Canada 1.6 (1.3, 1.9) 3.0 (2.7, 3.5) 4.3 (4.0, 4.6)

# Change in July 2.5% Wet Design Temp. [°C] Global warming level
# Region +1°C +2°C +3°C
# British Columbia 1.8 (1.5, 2.1) 3.5 (3.2, 3.8) 5.3 (5.0, 5.8)
# Prairies 1.8 (1.3, 2.0) 3.1 (2.8, 3.4) 4.6 (4.3, 4.9)
# Ontario 1.2 (1.0, 1.4) 2.3 (2.1, 2.6) 3.2 (3.1, 3.4)
# Quebec 1.1 (0.9, 1.4) 2.4 (2.2, 2.5) 3.3 (3.1, 3.5)
# Atlantic 1.3 (1.2, 1.4) 2.6 (2.4, 2.7) 3.8 (3.6, 3.9)
# North 1.6 (1.3, 1.9) 2.8 (2.5, 3.3) 4.3 (4.0, 4.8)
# Canada 1.3 (1.1, 1.5) 2.5 (2.2, 2.7) 3.6 (3.3, 3.8)