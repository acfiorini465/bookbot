def word_count(text_as_string):
    words = str.split(text_as_string)
    return len(words)
def character_num(text_as_string):
    text = text_as_string.lower()
    character_track = {}
    for character in text:
        if character.isspace() and character != " ":
            continue
        if character in character_track:
            character_track[character] += 1
        else:
            character_track[character] = 1
    return character_track
def sort_dicts(character_track):
    def sort_on(character_track):
        return character_track["num"]
    sorted_dicts = [
        {character: ""}
    ]