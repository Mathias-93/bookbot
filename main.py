import sys
from stats import get_num_words
from stats import get_num_character
from stats import pretty_print


def main():
    if(len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_chars_dict = get_num_character(text)
    print(f"Found {num_words} total words")
    pretty_print(num_chars_dict)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    


main()