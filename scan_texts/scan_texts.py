test_str = "	The focus of this report is to assess, at a regional-to-national scale, projected changes in the climatic design data that are defined in NBCC 2015 (NRC, 2015)<sup id='ref1-1-rf'><a class='fn-lnk' href='#ref1'><span class='wb-inv'>Reference </span>1</a></sup> and CHBDC CSA S6 (CSA, 2014)<sup id='ref2-1-rf'><a class='fn-lnk' href='#ref2'><span class='wb-inv'>Reference </span>2</a></sup> – these are the data that are widely used by engineers to calculate the (NRC, hsi nfgeinw) climatic Canada’s Changing Climate Report (Bush and Lemmen, 2019)<sup id='ref3-1-rf'><a class='fn-lnk' href='#ref3'><span class='wb-inv'>Reference </span>3</a></sup> loads affecting (Prein, 2017b) Canada’s B&CPI. (asdfasdfasdf) wkfhewlkefmelw"

test_str_2 = "There are many climate modelling groups around the world that perform simulations with dozens of GCMs. Results are contributed to the World Climate Research Programme’s Coupled Model Intercomparison Project (CMIP; Taylor et al., 2012<sup id='ref6-1-rf'><a class='fn-lnk' href='#ref6'><span class='wb-inv'>Reference </span>6</a></sup>; Eyring et al., 2016<sup id='ref7-1-rf'><a class='fn-lnk' href='#ref7'><span class='wb-inv'>Reference </span>7</a></sup>). The fifth phase of CMIP (CMIP5) informed the IPCC 5th Assessment Report (IPCC, 2013)<sup id='ref4-2-rf'><a class='fn-lnk' href='#ref4'><span class='wb-inv'>Reference </span>4</a></sup> and a sixth phase (CMIP6) will inform the IPCC 6th Assessment Report (planned release, 2021). While based on the same underlying principles, groups may parameterize unresolved physical processes – for example simplified representations of cloud properties and cloud microphysics – in slightly different ways and make different choices about model structure (Alexander and Easterbrook, 2015)<sup id='ref8-1-rf'><a class='fn-lnk' href='#ref8'><span class='wb-inv'>Reference </span>8</a></sup> and horizontal and vertical resolution. The result is that different climate models respond to the same external forcing in somewhat different ways. As an example, <a href='#figure-2.1'>Figure 2.1b</a> shows model resolution and equilibrium climate sensitivity – the long-term global mean temperature change associated with a doubling of CO2 concentration – for 26 CMIP5 climate models. Differences in cloud feedback stemming from differences in model parameterizations of cloud properties and microphysics are responsible for much of the current spread in climate sensitivity (Zelinka et al., 2017)<sup id='ref9-1-rf'><a class='fn-lnk' href='#ref9'><span class='wb-inv'>Reference </span>9</a></sup>. While the spread in climate sensitivity is reducible in principle as our understanding of physical processes and ability to represent them in GCMs improves, the diversity among models is considered a healthy aspect of the climate modelling community and is one source of uncertainty in future climate change projections at global and regional scales."

test_str_2_fr = "De nombreux groupes de modélisation climatique partout dans le monde effectuent des simulations avec des dizaines de MCM. Les résultats sont intégrés au Projet de comparaison de modèles couplés (CMIP) du Programme mondial de recherche sur le climat (Taylor et coll., 2012; Eyring et coll., 2016). La cinquième phase du CMIP (CMIP5) sous-tendait le Cinquième Rapport d’évaluation du Groupe d’experts intergouvernemental sur l’évolution du climat (GIEC) (GIEC, 2013) et une sixième phase (CMIP6) appuiera le Sixième Rapport d’évaluation (dont la publication est prévue pour 2021). Si les principes physiques sous-jacents sont les mêmes, les groupes peuvent paramétrer des processus physiques non résolus : par exemple, des représentations simplifiées des propriétés des nuages et la microphysique des nuages, de façon légèrement différente, pour que des choix puissent être faits par la suite quant à la structure du modèle (Alexander et Easterbrook, 2015) et à la résolution horizontale et verticale. Il s’ensuit que différents modèles climatiques répondent au même forçage externe de façon quelque peu différente. Par (2017) exemple, la figure 2.1b montre la résolution du modèle et la sensibilité du climat à l’équilibre, soit le changement de température annuelle moyenne à long terme associé à un doublement de la concentration de CO2, pour 26 modèles climatiques du CMIP5. Les différences dans la rétroaction nuageuse issues de divergences qui existent entre les modèles en ce qui concerne le paramétrage des propriétés des nuages et de la microphysique expliquent la majeure partie de la variance actuelle de la sensibilité du climat (Zelinka et coll., 2017). Si la variance de la sensibilité du climat peut être réduite en principe, à mesure que notre connaissance des processus physiques et de la capacité de les représenter dans des MCM s’améliore, on considère que la diversité entre les modèles est un aspect sain de la collectivité de la modélisation climatique et que c’est une source d’incertitude dans les projections des changements climatiques à l’échelle mondiale et régionale."

import json

# build references dictionary
json_file = open("references.json")
authors_dict = json.load(json_file)

# takes in paragraph of text and returns array of author-year keys and the text with reference location placeholders
def scan_fr_for_citations(text):

    return_arr = []
    ref_count = 1

    char_i = 0
    while (True):
        if (char_i == len(text)):
            break

        char = text[char_i]
        # print(char)
        if (char == "("):
            # Get authors and years
            authors_years_text = ""
            char_start_index = char_i + 1 # Now ( + 1
            while (True):
                char_i += 1
                char = text[char_i]
                if (char == ")"):
                    break
                authors_years_text += char

            # Split up text by ";"
            authors_years_array = authors_years_text.split(";")

            # Make keys and add reference placeholders
            placeholder_and_reference_text_array = []
            char_end_index = char_i # Now )
            
            found = False

            for author_year in authors_years_array:

                auth_year_partition = author_year.strip().partition(",")
                auth, year = auth_year_partition[0], auth_year_partition[2]
                auth_year_key = auth.strip() + "-" + year.strip()

                # Test key
                if (auth_year_key in authors_dict):
                    return_arr.append(auth_year_key)

                    # Add reference and placeholder
                    placeholder_and_reference_text_array.append(author_year.strip() + "###ref" + str(ref_count) + "###")
                    ref_count += 1 
                    found = True
                    continue

                # If failed, try with just the first word as author (in case multiple authors cited)
                auth_year_key = auth[0: auth.find(" ")].strip() + "-" + year.strip()
                if (auth_year_key in authors_dict):
                    return_arr.append(auth_year_key)

                    # Add reference and placeholder
                    placeholder_and_reference_text_array.append(author_year.strip() + "###ref" + str(ref_count) + "###")
                    ref_count += 1 
                    found = True
                    continue

            if (not found): # Not a citation
                continue
            
            # Add placeholders to original text 

            # If only one citation, add at end of bracket and strip beginning
            if (len(authors_years_array) <= 1):
                char_end_index += 1 # Now ) + 1
                char_start_index = char_end_index
                citation_text = placeholder_and_reference_text_array[0]
                placeholder_and_reference_text_array[0] = citation_text[citation_text.find("###ref"):]

            # Select beginning and end of citation bracket and add
            beginning = text[:char_start_index]
            end = text[char_end_index:]
            for i in range (len(placeholder_and_reference_text_array) - 1):
                beginning += placeholder_and_reference_text_array[i] + "; "
            text = beginning + placeholder_and_reference_text_array[-1] + end

        char_i += 1

    return (text, return_arr)

# Returns array of dictionary items that have a "intext" key, a "ref_num" key and an "instance" key. Use ref_num and keys
#   generated by scan_for_citations() on the french version to verify reference is correct.  
def scan_eng_intext_citation(text):
    # clean text of leading and trailing whitespace
    text = text.strip()

    # Search text for <sup and </sup>
    start = 0
    end = len(text) - 1

    citation_arr = []

    while (True):
        index_start = text.find("<sup id='ref", start, end) #avoids footnotes

        if (index_start == -1):
            break
        
        # Get citation
        index_stop = text.find("</sup>", start, end)
        index_stop += 6 # get to end of </sup>

        intext_citation = text[index_start:index_stop]

        # <sup id='ref6-1-rf'><a class='fn-lnk' href='#ref6'><span class='wb-inv'>Reference </span>6</a></sup>

        # Get ref num and instance
        ref_num_str = intext_citation.strip("<sup id='ref")
        ref_num = int(ref_num_str[:ref_num_str.find("-")])

        ref_instance_str_start = intext_citation[intext_citation.find("-") + 1:]
        ref_instance = int(ref_instance_str_start[:ref_instance_str_start.find("-")])

        

        citation = {
            "intext" : intext_citation,
            "ref_num" : ref_num,
            "instance" : ref_instance
        }

        # increment start to end of citation
        start = index_stop

        # Add citation to array
        citation_arr.append(citation)

    return (citation_arr)

# text, returned = scan_fr_for_citations(test_str_2_fr)
# print(text)
# print(scan_eng_intext_citation(test_str))

