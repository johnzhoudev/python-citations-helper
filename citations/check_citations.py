#Prep Citation Files
#open citation data for reading and writing
cite_data_file = open("/Users/johnzhou/Documents/Coding-Projects/Python/Random/citations/cite_data.txt", "r")
cite_data = cite_data_file.readlines()
cite_data_file.close()

#open all citations
all_cite_file = open("/Users/johnzhou/Documents/Coding-Projects/Python/Random/citations/all_cite.txt", "r")
all_cite_data = all_cite_file.readlines()
all_cite_file.close()

#get number of citations
num_citations = len(cite_data) // 3

for i in range(len(all_cite_data)):
    str_1 = all_cite_data[i].strip(" \n")
    found = False
    for j in range(num_citations):
        str_2 = cite_data[j * 3].strip(" \n")

        if (str_1 == str_2):
            found = True
            break
    
    if (not found):
        print("Did not find " + str_1)

    
