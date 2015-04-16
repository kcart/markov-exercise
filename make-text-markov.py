from sys import argv

script, corpus = argv 
print script
print corpus

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

new_dictionary = make_chains(corpus) 

def make_text(chains):
    print chains
    """Takes dictionary of markov chains; returns random text."""
  
 # return "Here's some random text."
 
make_text(new_dictionary)