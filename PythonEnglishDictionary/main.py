import json
import os
import shutil
import datetime

# Constants
FILE_NAME = "english_dictionary.json"
FILE_PATH = os.path.join("data", FILE_NAME)
MENU_OPTIONS = {
    1: "Search word",
    2: "Print history",
    3: "Exit",
}

# Load English dictionary from JSON file
with open(FILE_PATH, "r") as file:
    english_dictionary = json.load(file)

# History dictionary to store search history
history = {}

def print_definition(definition):
    width = shutil.get_terminal_size().columns
    print("\n=== Definition =" + "=" * width + "\n")
    print(definition)
    print("\n================" + "=" * width)

def search_word(word):
    if word in english_dictionary:
        definition = f"{word}: {english_dictionary[word]}"
        history[datetime.datetime.now()] = definition
        print_definition(definition)
    else:
        print("Word not found")

def print_menu():
    print("Choose an option from the menu:")
    for key, value in MENU_OPTIONS.items():
        print(f"{key}- {value}")

def search():
    while True:
        search_term = input("Enter a word to search its definition (write 'n' to cancel): ")
        if search_term.lower() == "n":
            break
        search_word(search_term)
        new_search = input("Do you want to do a new search? (y/n): ")
        if new_search.lower() != "y":
            break

def print_history():
    print("\n=== History =======\n")
    for timestamp, definition in history.items():
        print(f"{timestamp}: {definition}")
    print("\n" + "=" * shutil.get_terminal_size().columns + '\n')

def main():
    while True:
        try:
            print_menu()
            user_selection = int(input("Enter your choice: "))
            if user_selection == 1:
                search()
            elif user_selection == 2:
                print_history()
            elif user_selection == 3:
                print("Thanks for using our program")
                break
            else:
                print("Enter a valid option")
        except ValueError:
            print("Only numbers are allowed!")

if __name__ == "__main__":
    main()
