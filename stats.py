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

def sort_on(dict_items):
    # helper function for sorting, return "num" value to compare items
    return dict_items["num"]

def char_dict_to_sorted_list(char_dict):
    # convert character dict to list of dicts
    sorted_list = []

    # transform each key-value pair into a dictionary w/ keys "char" and "num"
    for key, value in char_dict.items():
        char_info = {"char": key, "num": value} # value here not to be confused w/ value extracted from item["char"] or item["num"] 
        sorted_list.append(char_info)
    # sort in order of most frequently used to least
    sorted_list.sort(reverse=True, key=sort_on)

    return sorted_list


