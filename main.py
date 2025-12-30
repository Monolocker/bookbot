from stats import word_count

book_path = "books/frankenstein.txt" # use relative path books/frankenstein.txt, in global scope

# book_path can also be in scope of main function 
def main(): 
    text = get_book_text(book_path)
    num_words = word_count(text)
    print(f"Found {num_words} total words")


def get_book_text(book_path):
    with open(book_path) as f:
        read_frankenstein = f.read() # can make this simply return f.read()
    
    return read_frankenstein

main()
