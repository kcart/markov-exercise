from sys import argv

script, corpus = argv 

def make_chains(corpus):
    open_file = open(corpus)
    we_read_text = open_file.read()
    string_text = we_read_text.split()
    bigram_dict = {}

    for i in range(len(string_text)-2):    
        bigram_dict[(string_text[i], string_text[i+1])] = [string_text[i+2]]

    return bigram_dict     

new_dictionary = make_chains(corpus) 

def make_text(bigram_dict):
   
    """Takes dictionary of markov chains; returns random text."""
  
 # return "Here's some random text."
 
make_text(new_dictionary)