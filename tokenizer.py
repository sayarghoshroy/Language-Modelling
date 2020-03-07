import numpy as np
import matplotlib.pyplot as plt
import sys
import re
import copy

regex_dict = {
    'url_regex_a' : "(http|ftp|https)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?",
    'url_regex_b' : "(http|ftp|https)://\w*.\w*/\w*",
    'mention_regex' : "@.*",
    'dollar_regex' : "$[0-9]+\.?[0-9]*",
    'rupee_regex' : "Rs\.[0-9]*\.?[0-9]*",
    'hashtag_regex' : "#.+",
    'number_regex' : "[0-9]*[0-9\.][0-9]+",
    'number_comma_regex' : "([0-9]*\,?[0-9]+)+",
    'email_regex' : "\S+@\S+",
    'name_regex' : "(Mr\.|Mrs\.|Ms\.|Smt\.|Shri\.|Sri\.|Shree\.)[a-zA-Z]*",
    'name_middle' : "[A-Z]\."
}

def check(unit):
    for regex in regex_dict.values():
        if re.match(regex, unit):
            return True
    return False

filename = sys.argv[1]
#access the filename as a command line argument
#filename = 'corpus3.txt'
fp = open(filename)
file_string = fp.read()

sentence_list = file_string.split('\n')

tokenized_string = ""
# the final output

tokenized_sentences = []

frequencies = [[], { }, { }, { }, { }, { }, { }]
#To store N-gram counts for N in {1, 2, 3, 4, 5, 6}

def tokenize_sentence(sentence):
    units = sentence.split(" ")
    tokens = []
    for unit in units:
        if check(unit):
            tokens.append(unit)
                
            continue
        
        divider = re.findall(r"[\w']+|[’.,!?;-~`]", unit)
        for elem in divider:
            if elem == '':
                continue

            if "\"" in elem:
                storage = elem.split("\"")
                for item in storage:
                    if "\'" in item:
                        new_storage = item.split("\'")
                        for item_sep in new_storage:
                            tokens.append(item_sep)
                            tokens.append("\'")
                        tokens.pop()
                    else:
                        tokens.append(item)
                        tokens.append("\"")
                tokens.pop()
                            
            elif "\'" in elem:
                new_storage = elem.split("\'")
                for item_sep in new_storage:
                    tokens.append(item_sep)
                    tokens.append("\'")
                tokens.pop()

            else:
                tokens.append(elem)
    
    return tokens

for sentence in sentence_list:
    units = sentence.split(" ")
    tokens = tokenize_sentence(sentence)
    if len(tokens) == 1 and tokens[0] == '' or tokens == []:
        continue
    
    for token in tokens:
        if token in frequencies[1]:
            frequencies[1][token] += 1
        else:
            frequencies[1][token] = 1
        tokenized_string = tokenized_string + " " + str(token)
    
    tokenized_sentences.append(tokens)
        
all_tokens = tokenized_string.split(' ')

for sentence_sep in tokenized_sentences:
    output_line  = ""
    for unit in sentence_sep:
        if unit == " ":
            continue
        output_line = output_line + unit.strip() + " "
    output_line = re.sub(r"  ", r" ", output_line)
    print(output_line)