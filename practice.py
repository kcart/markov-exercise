my_file = open('green-eggs.txt')

def make_chains(input_file):
    we_read_text = input_file.read()
    string_text = we_read_text.split()
    bigram_list = []
    for i in range(len(string_text)-1): 
        bigram_list.append((string_text[i], string_text[i+1]))
    print bigram_list

    
    #return {}
make_chains(my_file)