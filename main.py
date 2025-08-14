from stats import get_book_text
from stats import get_num_words
from stats import get_num_characters
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]
    text = get_book_text(file_path)
    num_words = get_num_words(text)
    
    count_chars = get_num_characters(text)
    list_counts = [{"char": char, "count": count_chars[char]} for char in count_chars]
    list_counts.sort(reverse=True, key=lambda x: x["count"])
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for c in list_counts:
        print(f"{c["char"]}: {c["count"]}") 
main()
