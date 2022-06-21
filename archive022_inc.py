############################################################
############################################################
# NAME:         NAME SCORES
# AUTHOR:       SCOTT BAILEY
# DESCRIPTION:  COMPUTES THE TOTAL OF ALL NAME SCORES IN A
#               GIVEN LIST OF NAMES. 
# 
#               A NAME SCORE IS THE SUM OF EACH LETTER IN A 
#               NAME'S POSITION IN THE ALPHABET MULTIPLIED
#               BY THE NAME'S POSITION IN THE LIST OF NAMES.
############################################################
############################################################

### INCOMPLETE ###

import requests

# name score = alpha index sum * index in list

# Finds the position of each letter in a given name in
# the alphabet and returns the sum of those positions
def sum_of_letter_positions(name):
    az = list('abcdefghijklmnopqrstuvwxyz')
    letter_positions = 0
    for letter in list(name.lower()):
        letter_positions += az.index(letter) + 1
    return letter_positions

# # Returns the position of a given name in a list of names
# def position_in_name_list(name):
#     response = requests.get('https://projecteuler.net/project/resources/p022_names.txt')
#     data = response.text
#     name_list = data.replace('\"', '').split(',')
#     name_list = sorted(name_list)
#     position_in_list = name_list.index(name) + 1
#     return position_in_list

def position_in_name_list(name, name_list):
    sorted_list = sorted(name_list)
    position_in_list = sorted_list.index(name) + 1
    return position_in_list

# def name_score(name, name_list):
#     score = sum_of_letter_positions(name) * position_in_name_list(name, name_list)
#     return score

# Get list of names from text file
response = requests.get('https://projecteuler.net/project/resources/p022_names.txt')
data = response.text
list_of_names = data.replace('\"', '').split(',')
list_score = 0
for name in list_of_names:
    



print(position_in_name_list('COLIN'))

# list_score = 0
# for name in name_list:
#     list_score += name_score(name)


print(name_score('COLIN'))
# print(len(name_list))
# print(list_score)

# print(sorted(name_list))

