def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def get_num_words(text):
    return sum(1 for i in text.split())

def get_num_characters(text):
    d = {}
    for c in text:
        if c.lower() not in d:
            d[c.lower()] = 0
        d[c.lower()] += 1
    return d
