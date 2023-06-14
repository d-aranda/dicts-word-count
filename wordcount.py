"""Count words in file."""

# with open("test.txt") as file:

import sys
file = open(sys.argv[1])



def tokenize(filename):
    """Returns a list of words from the file"""
  
    words_list = []

    for line in file:
        line = line.rstrip().split(" ")
        for word in line:
            words_list.append(word)


    return words_list


def count_words(words):
    """Takes in a list of strs and returns a dictionary of each str 
    and the number of time it appears in the list"""

    repetitions = {}

    for word in words:
        repetitions[word] = repetitions.get(word, 0) + 1
    
    
    return repetitions


def print_word_counts(word_counts):
    """Takes in a dictionary of word counts and prints each key and value"""
    
    for keys, values in word_counts.items():


        print(keys, values)





words = tokenize(file)
word_counts = count_words(words)
print_word_counts(word_counts)

