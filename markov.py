from sys import argv
from random import choice 

script, corpus = argv 

def make_chains(corpus):
    open_file = open(corpus)
    we_read_text = open_file.read()
    string_text = we_read_text.split()
    bigram_dict = {}

    for i in range(len(string_text)-2):    
        bigram_dict[(string_text[i], string_text[i+1])] = [string_text[i+2]]

    return bigram_dict     

def make_text(chains):
    

    """Takes dictionary of markov chains; returns random text."""

    return "Here's some random text."


# Change this to read input_text from a file, deciding which file should
# be used by examining the `sys.argv` arguments (if neccessary, see the
# Python docs for sys.argv)

input_text = "Some text"

# Get a Markov chain
chain_dict = make_chains(corpus)
print chain_dict

# Produce random text
# random_text = make_text(chain_dict())

# print random_text
