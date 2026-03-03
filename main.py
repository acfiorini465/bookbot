from stats import word_count, character_num, convert_dict_to_list
def get_book_text(path_to_file): 
    with open(path_to_file) as f:
        text_as_string = f.read()
    return text_as_string
def main():
    path_to_file = "books/frankenstein.txt"
    book_text = get_book_text(path_to_file)
    num_words = word_count(book_text)
    character_dict = character_num(book_text)
    sorted_chars_list = convert_dict_to_list(character_dict)
    print("============ BOOKBOT ============")
    print("Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in sorted_chars_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")
if __name__ == "__main__":
    main()