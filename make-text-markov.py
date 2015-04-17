"""Our final working markov text generator. Code reviewed"""

from sys import argv
from random import choice

script, corpus = argv 


def make_chains(corpus):
    open_file = open(corpus)
    we_read_text = open_file.read()
    string_text = we_read_text.split()
    bigram_dict = {}

    for i in range(len(string_text)-2):
        key = (string_text[i], string_text[i+1]) #assign stings to tuples, make tuples the keys
        value = string_text[i+2] #value to be string following the tuple
        if key not in bigram_dict: #assign key and value 
            bigram_dict[key] = [value]
        else:
            bigram_dict[key].append(value) 
            
            """if key is already there, add value 
            to existing list of values"""

    return bigram_dict     



def make_text(chains):
    word_list =[]
    rand_tuple = choice(chains.keys()) #picks a random key from dictionary, give it name rand_tuple
    for rand_tuple in chains: #for that random key in dictionary
        rand_word = choice(rand_tuple) #picks random word from tuple
        assoc_value = choice(chains[rand_tuple]) #value associated with key rand_tuple
        if (rand_word, assoc_value) in chains: 
            word_list.extend([rand_word, assoc_value])
    return " ".join(word_list)
       


    """Takes dictionary of markov chains; returns random text."""
  

 # return "Here's some random text."
bigram_dict = make_chains(corpus)  

#print bigram_dict

random_text = make_text(bigram_dict)

print random_text