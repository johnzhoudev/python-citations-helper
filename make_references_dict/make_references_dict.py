# Read in references text from references.txt and use first author name as key for reference dictionary.
# Also provides methods for confirming reference numbers with reference text

import json

test_intext_ref = "<sup id='ref1-1-rf'><a class='fn-lnk' href='#ref1'><span class='wb-inv'>Reference </span>1</a></sup>"

# Open references.txt and read in all references instances into an array
references_text = open("make_references_dict/references.txt", "r")

# In case it gets stuck in an infinite loop during development, break when count exceeds 200
count = 0

# Instaniate references dictionary
references_dict = { }

# Instantiate nums to names dict
num_to_name = { }

acronyms_dict = {
    "NRC": "CNRC",
    "CSA": "CSAS6",
    "IPCC": "GIEC"
}

def get_year(name_str):
    # Look for first bracketed text
    for i in range(len(name_str)):
        char = name_str[i]
        if (char == "("):
            year_index = i + 1
            char = name_str[year_index]
            num = ""
            while (char != ")"):
                num += char
                year_index += 1
                char = name_str[year_index]

            if (not num[0:4].isnumeric()): # If not a year, first 4 letters (could be 2018a)
                continue
            break
    
    return (num)



while (True):
    line = references_text.readline()

    # Break at end of file
    if (line == "DONE\n"):
        break
    elif (count > 200): # Emergency break
        break

    # Add other lines to temporary array
    lines = [line]
    for i in range(5):
        lines.append(references_text.readline())

    # Get reference number from 2nd line
    ref_num_line = lines[1].strip()
    before, ref_separator, num_str = ref_num_line.partition("ref")

    # Emergency break if ref not found
    if (not num_str):
        print("Ref not found!!!")
        break
    
    # Get number
    while (not num_str.isdigit()):
        num_str = num_str[:-1]
    ref_num = int(num_str)

    # Get name
    name_str = lines[2].strip()
    name_str = name_str.strip("<p>")

    # Read name_str until comma or bracket, and strips space
    char_i = 0
    name = ""
    while (True):
        character = name_str[char_i]
        if (character == "," or character == "(" or character == "["):
            break
        name += character
        char_i += 1
    name = name.strip()

    # get year
    year = get_year(lines[2].strip())

    #check if in dictionary (duplicate?)
    key = name + "-" + year
    if (key in references_dict):
        print(key)
        continue

    # Add to dictionary
    references_dict[key] = ref_num
    num_to_name[ref_num] = key

    # Also add french acronym versions, do not add french to num_to_name
    if (name == "NRC" or name == "CSA" or name == "IPCC"):
        references_dict[acronyms_dict[name] + "-" + year] = ref_num

    count += 1

# Save json file

with open("references.json", "w") as file:
    json.dump(references_dict, file)
    file.close()

with open("num_to_name.json", "w") as file:
    json.dump(num_to_name, file)
    file.close()

# Close all files
references_text.close()

print("Don't forget to delete Whan-2016!")

