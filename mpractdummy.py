my_file = open('green-eggs.txt')

def make_chains(input_file):
    we_read_text = input_file.read()
    string_text = we_read_text.split()
    bigram_dict = {}

    for i in range(len(string_text)-1): 
        if i == [len(string_text)-1]:
            bigram_dict[(string_text[i-3], string_text[i-2])] = [string_text[i-1]]
        elif i == [len(string_text)-2]:
            bigram_dict[(string_text[i-2], string_text[i-1])] = [string_text[i]]
        else:    
            bigram_dict[(string_text[i-1], string_text[i])] = [string_text[i+1]]
        print bigram_dict     
    
make_chains(my_file)
        
        # if i == [len(string_text)-1]:
        #     bigram_dict[(string_text[i], string_text[0])] = [string_text[1]]
        # elif i == [len(string_text)-2]:
        #     bigram_dict[(string_text[i], string_text[i+1])] = [[string_text[0]] 
        # else: