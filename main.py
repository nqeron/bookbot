from stats import get_book_text
from stats import get_num_words
from stats import get_num_characters

def main():
    text = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(text)
    count_chars = get_num_characters(text)
    print(f"{num_words} words found in the document")
    print(count_chars)

main()
