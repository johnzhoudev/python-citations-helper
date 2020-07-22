#! /opt/anaconda3/bin/python
import pyperclip

#Prep Citation Files
#open citation data for reading and writing
cite_data_file = open("/Users/johnzhou/Documents/Coding-Projects/Python/Random/citations/cite_data.txt", "r")
cite_data = cite_data_file.readlines()

#close cite_data_file and open for writing
cite_data_file.close()
cite_data_file = open('/Users/johnzhou/Documents/Coding-Projects/Python/Random/citations/cite_data.txt', 'w')

#get number of citations
num_citations = len(cite_data) // 3

#format counters
for i in range (len(cite_data) // 3):
    cite_data[3 * i + 1] = int(cite_data[3 * i + 1])
    cite_data[3 * i + 2] = int(cite_data[3 * i + 2])

#open citation output text file as append
cite_output_file = open('/Users/johnzhou/Documents/Coding-Projects/Python/Random/citations/cite_output.txt', "a")


#Prep Footnote files
#open footnote data for reading and writing
footnote_data_file = open("/Users/johnzhou/Documents/Coding-Projects/Python/Random/citations/footnote_data.txt", "r")
footnote_data = footnote_data_file.readlines()

#close footnote_data_file and open for writing
footnote_data_file.close()
footnote_data_file = open('/Users/johnzhou/Documents/Coding-Projects/Python/Random/citations/footnote_data.txt', 'w')

#get number of footnotes
num_footnotes = len(footnote_data) // 3

#format counters
for i in range (len(footnote_data) // 3):
    footnote_data[3 * i + 1] = int(footnote_data[3 * i + 1])
    footnote_data[3 * i + 2] = int(footnote_data[3 * i + 2])

#open footnote output text file as append
footnote_output_file = open('/Users/johnzhou/Documents/Coding-Projects/Python/Random/citations/footnote_output.txt', "a")


#prep figures files
#open figure history file
figure_history_file = open('/Users/johnzhou/Documents/Coding-Projects/Python/Random/citations/figure_history.txt', 'a')

#make functions for Citations
def init_citation(cite_str, ref_num):
    cite_data.append(cite_str)
    cite_data.append(ref_num)
    cite_data.append(1)

def make_intext_reference(ref_num, ref_count):

    intext_citation = "<sup id='ref" + str(ref_num) + "-" + str(ref_count) + "-rf'><a class='fn-lnk' href='#ref" + str(ref_num) + "'><span class='wb-inv'>Reference </span>" + str(ref_num) + "</a></sup>"

    print('Copied: ' + intext_citation + ' to clipboard')
    pyperclip.copy(intext_citation)

def make_bottom_reference(cite_str, ref_num):

    ref_str1 = "<dt>Reference " + str(ref_num) + "</dt>\n"
    ref_str2 = "\t<dd id='ref" + str(ref_num) + "'>\n"
    ref_str3 = "\t\t<p>" + cite_str.strip(' \n') + "</p>\n"
    ref_str4 = "\t\t<p class='fn-rtn'><a href='#ref" + str(ref_num) + "-1-rf'><span class='wb-inv'>Return to reference </span>" + str(ref_num) + "<span class='wb-inv'> referrer</span></a></p>\n"
    ref_str5 = "\t</dd>\n\n"

    ref_str = ref_str1 + ref_str2 + ref_str3 + ref_str4 + ref_str5

    cite_output_file.write(ref_str)
    
def add_citation(cite_str):
    for i in range ((len(cite_data)) // 3):
        if (cite_str == cite_data[i * 3]):

            cite_data[i * 3 + 2] += 1

            make_intext_reference(cite_data[i * 3 + 1], cite_data[i * 3 + 2])

            return
    
    #If not found, add
    global num_citations
    num_citations += 1
    init_citation(cite_str, num_citations)
    make_intext_reference(num_citations, 1)
    make_bottom_reference(cite_str, num_citations)



#make functions for Footnotes
def init_footnote(footnote_str, ref_num):
    footnote_data.append(footnote_str)
    footnote_data.append(ref_num)
    footnote_data.append(1)

def to_roman(num):
    assert(num <= 3999 and num > 0)
    roman_str = ""
    roman_numerals = {
        1 : "i",
        4 : "iv",
        5 : "v",
        9 : "ix",
        10 : "x",
        40 : "xl",
        50 : "L",
        90 : "XC",
        100 : "C",
        400 : "CD",
        500 : "D",
        900 : "CM",
        1000 : "M"
    }

    numeral_nums = [1,4,5,9,10,40,50,90,100,400,500,900,1000]

    digit_num = -1

    for i in range (0, 13):
        if (num < numeral_nums[i]):
            digit_num = numeral_nums[i - 1]
            break
    
    if (digit_num < 1):
        print("Invalid digit_num!")
        return ""

    digit_char = roman_numerals.get(digit_num)

    roman_str += digit_char
    
    new = num - digit_num
    if (new > 0):
        roman_str += to_roman(new)

    return roman_str

def make_intext_footnote(ref_num, ref_count):

    intext_footnote = "<sup id='fn" + str(ref_num) + "-" + str(ref_count) + "-rf'><a class='fn-lnk' href='#fn" + str(ref_num) + "'><span class='wb-inv'>Footnote " + str(ref_num) + "</span>" + to_roman(ref_num) + "</a></sup>"

    print('Copied: ' + intext_footnote + ' to clipboard')
    pyperclip.copy(intext_footnote)

#<sup id='fn1-1-rf'><a class='fn-lnk' href='#fn1'><span class="wb-inv">Footnote 1</span>i</a></sup>


def make_bottom_footnote(footnote_str, ref_num):

    ref_str1 = "<dt>Footnote " + str(ref_num) + "</dt>\n"
    ref_str2 = "\t<dd id='fn" + str(ref_num) + "'>\n"
    ref_str3 = "\t\t<p>" + footnote_str.strip(' \n') + "</p>\n"
    ref_str4 = "\t\t<p class='fn-rtn'><a href='#fn" + str(ref_num) + "-1-rf'><span class='wb-inv'>Return to footnote " + str(ref_num) + " </span>" + to_roman(ref_num) + "<span class='wb-inv'> referrer</span></a></p>\n"
    ref_str5 = "\t</dd>\n\n"

    ref_str = ref_str1 + ref_str2 + ref_str3 + ref_str4 + ref_str5

    footnote_output_file.write(ref_str)


# <dt>Footnote 1</dt>
# 		<dd id="fn1">
# 			<p>
# 				footnote text
# 			</p>
# 			<p class="fn-rtn"><a href="#fn1-1-rf"><span class="wb-inv">Return to footnote 1 </span>i<span class="wb-inv"> referrer</span></a></p>
# 		</dd>

def add_footnote(footnote_str):
    for i in range ((len(footnote_data)) // 3):
        if (footnote_str == footnote_data[i * 3]):

            footnote_data[i * 3 + 2] += 1

            make_intext_footnote(footnote_data[i * 3 + 1], footnote_data[i * 3 + 2])

            return
    
    #If not found, add
    global num_footnotes
    num_footnotes += 1
    init_footnote(footnote_str, num_footnotes)
    make_intext_footnote(num_footnotes, 1)
    make_bottom_footnote(footnote_str, num_footnotes)

def write_citations_data_to_output():
    #format counters
    for i in range (len(cite_data) // 3):
        make_bottom_reference(cite_data[i * 3], cite_data[i * 3 + 1])


def add_figure(id, srcs, cap):
    str1 = '<div tabindex="-1" id="figure-' + id + '">\n'
    str2 = '\t<figure>\n'

    str3 = ''
    for i in range (len(srcs)):
        str3 += '\t\t<img class="img-responsive thumbnail center-block" alt="See description below" src="Images/' + srcs[i] + '" />\n'

    str4 = '\t\t<figcaption>\n'
    str5 = '\t\t\t<strong>Figure ' + id + '</strong>: ' + cap + '\n'
    str6 = '\t\t<figcaption>\n'
    str7 = '\t</figure>\n'
    str8 = '</div>\n'
    str9 = '<br />\n'

    figure_html = str1 + str2 + str3 + str4 + str5 + str6 + str7 + str8 + str9

    print('Copied Figure HTML to clipboard')
    pyperclip.copy(figure_html)

    #add to history file
    figure_html += '\n'
    figure_history_file.write(figure_html)
    

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

while (True):

    #strips spaces and newlines from end and adds one newline
    input_str = input('Citation: ')
    input_str = input_str.strip(' \n') + '\n'

    if (input_str == 'quit\n'):

        #format counters
        for i in range (len(cite_data) // 3):
            cite_data[3 * i + 1] = str(cite_data[3 * i + 1]) + '\n'
            cite_data[3 * i + 2] = str(cite_data[3 * i + 2]) + '\n'
        
        for i in range (len(footnote_data) // 3):
            footnote_data[3 * i + 1] = str(footnote_data[3 * i + 1]) + '\n'
            footnote_data[3 * i + 2] = str(footnote_data[3 * i + 2]) + '\n'

        #Write all data to new file
        cite_data_file.writelines(cite_data)
        footnote_data_file.writelines(footnote_data)        
        #close files
        cite_output_file.close()
        cite_data_file.close()
        footnote_output_file.close()
        footnote_data_file.close()
        figure_history_file.close()

        print('Remember to backup cite and footnote files!!!')

        break

    #footnote handler
    elif (input_str == "fn\n"):
        footnote = input("Footnote Text: ")
        footnote = footnote.strip(' \n') + '\n'
        add_footnote(footnote)
    
    elif (input_str == "fig\n"):
        fig_id = input("Figure ID: ")
        fig_srcs = []
        while (1):
            fig_src = input("Fig Sources (Images/) ('done' when finished): ")
            fig_src = fig_src.strip(' \n')

            if (fig_src == 'done'):
                break
            else:
                fig_srcs.append(fig_src)
                print('Fig src added')


        fig_cap = input("Caption: ")

        fig_id = fig_id.strip(' \n')
        fig_cap = fig_cap.strip(' \n')

        add_figure(fig_id, fig_srcs, fig_cap)

    elif (input_str == 'tb\n'):
        make_table_row()

    else:
        add_citation(input_str)


#/opt/anaconda3/bin/python /Users/johnzhou/Documents/Coding-Projects/Python/Random/citations/citation.py
#/opt/anaconda3/bin/python /Users/johnzhou/Documents/Coding-Projects/Python/Random/citations/auto_table.py

# <div tabindex="-1" id="figure-2.5">
# 	<figure>
# 		<img class="img-responsive thumbnail center-block" alt="See description below" src="Images/figure-2.5.png" />
# 		<figcaption>
# 			<strong>Figure 2.5</strong>: Locations (similar to locations listed in NBCC Table C-2) that are used to summarize regional projections for each climate design variable. Unfortunately, locations north of 75°N cannot currently be included because they fall outside the CanRCM4 domain.
# 		</figcaption>
# 	</figure>
# </div>
# <br />



# 			<tr>
# 				<th>Change in Surface Mean Air Temp. [&#8451;]</th>
# 				<th colspan='3'>Global warming level</th>
# 			</tr>
# 			<tr>
# 				<th>Region</th>
# 				<th>+1&#8451;</th>
# 				<th>+2&#8451;</th>
# 				<th>+3&#8451;</th>
# 			</tr>
# 		</thead>
# 		<tbody>
# 			<tr>
# 				<td>Quebec</td>
# 				<td>1.6 (1.5, 1.7)</td>
# 				<td>3.1 (3.0, 3.2)</td>
# 				<td>4.6 (4.5, 4.6)</td>
# 			</tr>
# 		<tfoot>
# 			<tr>
# 				<td>Canada</td>
# 				<td>1.6 (1.5, 1.6)</td>
# 				<td>3.0 (2.9, 3.0)</td>
# 				<td>4.3 (4.3, 4.4)</td>
# 			</tr>
# 		</tfoot>
# 	</table>