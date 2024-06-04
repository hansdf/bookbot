with open("books/frankenstein.txt") as f:
    file_contents = f.read()

def main():
    def num_of_words():
        words = file_contents.split()
        counter = 0
        for word in words:
            counter += 1
        print(f"This text file contains {counter} words.")

    num_of_words()
        

main()
