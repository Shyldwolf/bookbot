import sys

from stats import count_words
from stats import get_book_text
from stats import count_characters
from stats import sort_characters

# This script is designed to analyze a book file and count the number of words and characters in it.
# It also sorts the characters by their frequency of appearance in the text.
def main():
    
    # Check if the correct number of command line arguments is provided.
    # If not, print usage instructions and exit the program.
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    # Get the file path from the command line arguments.
    path_to_file = sys.argv[1]
    book_text = get_book_text(path_to_file)    
    num_words = count_words(book_text)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book: found in {path_to_file}")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    # Count and sort the number of characters in the book text.
    num_characters = count_characters(book_text)
    sorted_characters = sort_characters(num_characters)
    
    # Print the sorted characters and their counts.
    # The characters are sorted in descending order based on their frequency.
    for character in sorted_characters:
        print(f"{character['char']}: {character['num']}")
              
# The main function is defined to encapsulate the script's functionality.
    
# This is the entry point of the script. It calls the main function to execute the program.    
if __name__ == "__main__":
    main()
        