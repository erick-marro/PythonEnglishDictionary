## English Dictionary Program

This is a simple command-line Python program that allows users to search for the definitions of English words. The program loads a dictionary of English words and their corresponding definitions from a JSON file. Users can perform word searches, view search history, and exit the program.

### Instructions to Execute the Program:

1. **Python Installation**: Ensure you have Python 3.x installed on your computer. If you don't have it, you can download and install it from the official Python website (https://www.python.org/downloads/).

2. **Download the Code**: Download the Python code for the English Dictionary program and save it as `main.py` in a convenient location.

3. **Dictionary Data**: The program requires a JSON file containing the English dictionary data. Ensure you have a file named `english_dictionary.json` located in the `data` directory relative to the program file (`english_dictionary.py`). The JSON file should have the following structure:

```json
{
    "word1": "definition1",
    "word2": "definition2",
    ...
}
```

You can customize the dictionary by adding or modifying word-definition pairs in the JSON file.

4. **Run the Program**: Open a terminal (or command prompt) in the same directory where the `main.py` file is located.

5. **Execute the Program**: Type the following command to run the program:

```
python main.py
```

6. **Menu Options**: After executing the program, you will see a menu with three options:

    - **Option 1: Search word**: Allows you to search for the definition of a specific word.
    
    - **Option 2: Print history**: Displays the search history, showing the timestamp and the word definition searched in previous sessions.
    
    - **Option 3: Exit**: Terminates the program.

7. **Word Search**: To search for a word, select option 1 from the menu and enter the word you want to search. The program will display the definition if the word is found in the dictionary; otherwise, it will notify you that the word is not found.

8. **Search History**: You can view the search history by selecting option 2 from the menu. The program will display the timestamp and word definition for each word you searched in previous sessions.

9. **Exiting the Program**: To exit the program, select option 3 from the menu. The program will display a thank-you message and terminate.

That's it! You can now use the English Dictionary program to search for word definitions and explore the search history of previous sessions. Enjoy exploring words and their meanings!
