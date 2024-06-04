def main():
    text_path = "books/frankenstein.txt"
    text = book_text(text_path) 

    num_of_words(text)  

def book_text(path):
    with open(path, 'r') as f:
        return f.read()

def num_of_words(any_string):
    words = any_string.split()
    counter = len(words) 
    print(f"This text file contains {counter} words.")

main()
