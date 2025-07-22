def get_book_text(path_to_file): 
    with open(path_to_file) as f:
        text_as_string = f.read()
    return text_as_string
def main():
    path_to_file = "bookbot/books/frankenstein.txt"
    book_text = get_book_text(path_to_file)
    print(book_text)
if __name__ == "__main__":
    main
    

    

