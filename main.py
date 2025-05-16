from stats import word_counter, char_counter, sort_alpha_chars

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    book = get_book_text('books/frankenstein.txt')

    print(  
        "============ BOOKBOT ============\n"
        "Analyzing book found at books/frankenstein.txt...\n"
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