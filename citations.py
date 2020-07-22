import sys
sys.path.insert(1, 'scan_texts')

from scan_texts import scan_fr_for_citations, scan_eng_intext_citation
import json

# if true, updates ref_instance.json
check_instance = True

# build references dictionary
json_file = open("references.json")
authors_dict = json.load(json_file)
json_file2 = open("num_to_name.json")
num_to_name = json.load(json_file2)

# Read in ref_instance information
json_file3 = open("ref_instance.json")
ref_instance = json.load(json_file3)

json_file.close()
json_file2.close()
json_file3.close()

# Save previous instance information
# Write new json instance information
with open("ref_instance_prev.json", "w") as file:
    json.dump(ref_instance, file)
    file.close()

def read_data(filename):
    data_file = open(filename, "r")
    lines = []
    while (True):
        line = data_file.readline()
        if (line == "DONE\n"):
            break
        elif (line[0] == "<"):
            continue

        lines.append(line.strip())

    return lines

def replace_phrase(phrase, replacement, text, phrase_not_found=None):
    beginning_i = text.find(phrase)
    if (beginning_i == -1):
        if (phrase_not_found):
            phrase_not_found()
            return
        else:
            print("Phrase " + phrase + " not found in " + text + "\n")
            return
    end_i = beginning_i + len(phrase)

    return text[0:beginning_i] + replacement + text[end_i:]
    

def main():
    # Read in data
    en_lines = read_data("en-data.txt")
    fr_lines = read_data("fr-data.txt")
    # Check if num paragraphs are equal
    if (len(en_lines) != len(fr_lines)):
        print("Paragraphs not equal in data\n")
        return
    
    # For each paragraph
    paragraph_count = 0

    # Error counter
    errors = 0
    
    output_file = open("output/out1.txt", "w")
    errors_file = open("output/errors1.txt", "w")

    for i in range(len(en_lines)):
        paragraph_count += 1
        en_paragraph = en_lines[i]
        fr_paragraph = fr_lines[i]

        citation_arr_en = scan_eng_intext_citation(en_paragraph)
        fr_text, fr_citation_keys = scan_fr_for_citations(fr_paragraph)

        # Compare lengths of citations in english and citations found in french
        if (len(citation_arr_en) != len(fr_citation_keys)):
            # print("Citations not equal for paragraph " + str(paragraph_count) + "\n")

            errors += 1

            # Write ***CITATIONS NOT ADDED***
            output_file.write("***CITATIONS NOT ADDED - NOT EQUAL LENGTH***\n<p>\n\t" + fr_text + "\n</p>\n")

            # Write error information
            errors_file.write("Citations not equal in paragraph " + str(paragraph_count) + "\nENG CITATIONS:\n")
            
            for citation in citation_arr_en:
                errors_file.write(num_to_name[str(citation["ref_num"])] + "   ")
                errors_file.write(citation["intext"] + "\n")

            errors_file.write("FRENCH CITATIONS:\n")
            for key in fr_citation_keys:
                errors_file.write(key + "\n")

            errors_file.write("\n")

            continue

        # Confirm citation numbers and write each citation to paragraph if confirmed
        for i in range(len(citation_arr_en)):
            en_citation = citation_arr_en[i]
            fr_citation_key = fr_citation_keys[i]
            
            # Shouldn't occur, but just in case there's an order mismatch
            if (en_citation["ref_num"] != authors_dict[fr_citation_key]):
                #print(fr_citation_key + " citation not correspnding to ref num " + str(en_citation["ref_num"] + " in paragraph " + str(paragraph_count)) + "\n")
                errors += 1

                output_file.write("***CITATION NOT ADDED - REF NUM MISMATCH***\n")

                errors_file.write(fr_citation_key + " citation not correspnding to ref num " + str(en_citation["ref_num"] + " in paragraph " + str(paragraph_count)) + "\n\n")

                continue
            
            if (check_instance):

                # If new citation instance, insert counter into dict with fr_citation_key
                if (fr_citation_key not in ref_instance):
                    ref_instance[fr_citation_key] = 0

                # Check if reference instance of intext citation matches internal insert count
                if (en_citation["instance"] != (ref_instance[fr_citation_key] + 1)):
                    # print(fr_citation_key + " intext citation in paragraph " + str(paragraph_count) + "\n" + en_citation["intext"] + "\nnot matching instance num\n" + "FR internal: " + str(ref_instance[fr_citation_key] + 1) + "\nENG intext: " + str(en_citation["instance"]) + "\n")
                    errors += 1

                    output_file.write("***CITATION NOT ADDED - DIF INSTANCE COUNT***\n")
                    errors_file.write(fr_citation_key + " intext citation in paragraph " + str(paragraph_count) + "\n" + en_citation["intext"] + "\nnot matching instance num\n" + "FR internal: " + str(ref_instance[fr_citation_key] + 1) + "\nENG intext: " + str(en_citation["instance"]) + "\n\n")

                    continue

                # Increment reference instance
                ref_instance[fr_citation_key] += 1
            
            # Write reference into text
            fr_text = replace_phrase("###ref" + str(i + 1) + "###", en_citation["intext"], fr_text)
            
        # Write french text
        output_file.write("<p>\n\t" + fr_text + "\n</p>\n")

    # Print error statement
    print("Completed with " + str(errors) + " error(s). See error file for more details. Make sure to update the instances json file!")

    # Close all files
    output_file.close()
    errors_file.close()

    # Write new json instance information
    with open("ref_instance.json", "w") as file:
        json.dump(ref_instance, file)
        file.close()
    
main()


    
    


