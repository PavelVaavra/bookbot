def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def word_counter(s):
    return len(s.split())

def main():
    print(f"{word_counter(get_book_text('books/frankenstein.txt'))} "
            "words found in the document")

if __name__ == "__main__":
    main()