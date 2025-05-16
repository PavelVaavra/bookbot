from stats import word_counter, char_counter, sort_alpha_chars

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    book = get_book_text('books/frankenstein.txt')
    print(f"{word_counter(book)} "
            "words found in the document")
    print(sort_alpha_chars(char_counter(book)))

if __name__ == "__main__":
    main()