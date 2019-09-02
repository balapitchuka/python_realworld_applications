import json
from difflib import get_close_matches

data = json.load(open('data.json'))

def find_meaning(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        close_match = get_close_matches(word, data.keys())[0]
        choice = input(f"Did you mean '{get_close_matches(word, data.keys())[0]}' instead?, (Y/N) : ")
        if choice == 'y' or choice == 'Y':
            return data[get_close_matches(word, data.keys())[0]]
        elif choice == 'N' or choice == 'n':
            return "Word does not exists. Please double check and try again."
        else:
            return "Did not get your input. Exiting..."
    else:
        print("Word does not exists. Please double check and try again.")


word = input("Enter a word to know it's meaning : ")
meaning = find_meaning(word)
if meaning:
    print(meaning)
else:
    pass
