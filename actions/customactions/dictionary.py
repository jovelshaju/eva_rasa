import requests
import json

def getMeaning(word):
    word = word.split()[0]
    try:
        resp = requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/en_US/{word}')
        data = resp.json()
        meanings = data[0]['meanings']
        definitions = meanings[0]['definitions']
        definition = definitions[0]['definition']
        result = f"{word.capitalize()} in definition is {definition.lower()}"
        print(result)
        return result
    except:
        return "Sorry, Couldn't find the meaning"

getMeaning('Car')