#   It uses the `get_book_text` function to open and read the file, and then return the content.
def get_book_text(filepath):
    with open(filepath) as f:
        contenido = f.read()
        return (contenido)    
    
# This function takes a string of text as input and counts the number of words in it.        
def count_words(text):
    words = text.split()
    return len(words)
    
# This function takes a string of text as input and counts the number of characters in it.
def count_characters(text):
    characters = {}
    
    for char in text:
        char = char.lower()
        if char in characters:
            characters[char] += 1
        else:   
            characters[char] = 1
    return characters

# This function takes a dictionary of characters and their counts, sorts them, and returns a sorted list of tuples.
def sort_characters(characters):
    sorted_characters = []
    for key, value in characters.items():
        if key.isalpha():
            char_dict = {"char": key, "num": value}
            sorted_characters.append(char_dict)
    sorted_characters.sort(key=lambda item: item["num"], reverse=True)
    return sorted_characters
        
    