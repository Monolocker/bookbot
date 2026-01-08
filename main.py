from stats import word_count
from stats import char_count
from stats import text_report

book_path = "books/frankenstein.txt" # use relative path books/frankenstein.txt

# book_path can also be in local scope of main function 
def main(): 
    text = get_book_text(book_path)
    num_words = word_count(text)
    char_dict = char_count(text)
    print(f"Found {num_words} total words")
    print(char_count(text))
    print(text_report(char_dict))

def get_book_text(book_path):
    with open(book_path) as f:
        read_frankenstein = f.read() # can make this simply return f.read()
    
    return read_frankenstein

main()