def word_count(text):
    words = text.split()
    return len(words)

def char_count(text):
    lower_text = text.lower()
    char_dict = {}

    for characters in lower_text:
         # iterate through each char in lower_text
        if characters in char_dict: 
            # check if current char is a key already in dict
            # if so, char encountered before
            char_dict[characters] += 1
            # thus char already in dict, increment count by 1
        else: 
            # if char not yet in dict, else block executed
            # first time char encountered
            char_dict[characters] = 1
            # add new char to dict as key and set initial count to 1
    return char_dict

def text_report(char_dict):
    dict_list = []
    
    for key, value in char_dict.items():
        char_info = {"char": key, "num": value}
        dict_list.append(char_info)

    return dict_list

