from stats import word_count
from stats import char_count
from stats import char_dict_to_sorted_list
import sys

# check if exactly 2 args provided (script name + book path)
if len(sys.argv) != 2: 
        # show usage instructions if wrong number of args
        print("Usage: python3 main.py <path_to_book>")
        # exit program with error code 1 indicating failure
        sys.exit(1)

# get book path from command line argument
book_path = sys.argv[1]

def main(): 
    text = get_book_text(book_path)
    num_words = word_count(text)
    char_dict = char_count(text)
    char_sorted_list = char_dict_to_sorted_list(char_dict)
    print(f"Found {num_words} total words")
    for item in char_sorted_list: 
        character = item["char"] # extract char
        count = item["num"]      # extract count
        if character.isalpha():  # only include letters
            print(f"{character}: {count}")

def get_book_text(book_path):
    with open(book_path) as f:
        read_frankenstein = f.read() # can make this simply return f.read()
    
    return read_frankenstein

main()
