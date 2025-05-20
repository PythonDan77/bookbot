from stats import *
import sys

def get_book_text(filepath: str) -> str:
    with open(filepath, "r") as file:
        contents = file.read()
    return contents

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
     
    text = get_book_text(sys.argv[1])
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(text)} total words")
    print("--------- Character Count -------")
    for key, value in get_chars(text).items():
        if key.isalpha():
            print(f"{key}: {value}")
    print("============= END ===============")

    
main()