from stats import word_counter, char_counter

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    book = get_book_text('books/frankenstein.txt')
    print(f"{word_counter(book)} "
            "words found in the document")
    print(char_counter(book))

if __name__ == "__main__":
    main()