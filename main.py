def main():
    text_path = "books/frankenstein.txt"
    text = book_text(text_path) 

    word_count = num_of_words(text) 
    char_count = num_of_chars(text)
    text_report(word_count, char_count)

def book_text(path):
    with open(path, 'r') as f:
        return f.read()

def num_of_words(any_string):
    words = any_string.split()
    counter = len(words) 
    return counter

def num_of_chars(any_string):
    list_chars = list(any_string)
    chars = [character.lower() for character in list_chars]
    chars_dict = {}
    for char in chars:
        if char not in chars_dict:
            chars_dict[char] = 1
        else:
            chars_dict[char] += 1
    return chars_dict

def text_report(word_count, char_count):
    print("This is the report of the content inside of the parsed text file")
    print(f"There were {word_count} words in the document")
    print("Each character appears with the frequencie:")
    for char, count in char_count.items():
        if char.isalpha() == False:
            continue
        else:
            print(f"'{char}': {count}")

main()