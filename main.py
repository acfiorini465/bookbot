from stats import word_count, character_num
def get_book_text(path_to_file): 
    with open(path_to_file) as f:
        text_as_string = f.read()
    return text_as_string
def main():
    path_to_file = "books/frankenstein.txt"
    book_text = get_book_text(path_to_file)
    num_words = word_count(book_text)
    character_dict = character_num(book_text)
    print(f"{num_words} words found in the document")
    print(character_dict)
if __name__ == "__main__":
    main()
