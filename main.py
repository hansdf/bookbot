def main():
    text_path = "books/frankenstein.txt"
    text = book_text(text_path) 

    num_of_words(text) 
    num_of_chars(text)

def book_text(path):
    with open(path, 'r') as f:
        return f.read()

def num_of_words(any_string):
    words = any_string.split()
    counter = len(words) 
    print(f"This text file contains {counter} words.")

def num_of_chars(any_string):
    list_chars = list(any_string)
    chars = [character.lower() for character in list_chars]
    chars_dict = {}
    for char in chars:
        if char not in chars_dict:
            chars_dict[char] = 0
        else:
            chars_dict[char] += 1
    print("the following is a dictionary of how many times each character appears in the text:")
    print(f"{chars_dict}")



main()
