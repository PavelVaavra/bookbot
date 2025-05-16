import sys
from stats import word_counter, char_counter, sort_alpha_chars

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book = get_book_text(sys.argv[1])
    print(  
        "============ BOOKBOT ============\n"
        f"Analyzing book found at {sys.argv[1]}\n"
        "----------- Word Count ----------\n"
        f"Found {word_counter(book)} total words\n"
        "--------- Character Count -------"
    )
    sorted_chars = sort_alpha_chars(char_counter(book))
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")


if __name__ == "__main__":
    main()