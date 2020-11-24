import module_manager
module_manager.review()
import requests
from bs4 import BeautifulSoup
import string
import dictionaries
import time

#Headers copied from https://hackersandslackers.com/scraping-urls-with-beautifulsoup/
#Used to bypass basic anti-webscraping methods by websites
headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }

#Returns true if word in dictionary.com, false otherwise
def isWord(word):
    url = "https://www.dictionary.com/browse/" + word + "?s=t"
    req = requests.get(url, headers) #takes .5 seconds
    soup = BeautifulSoup(req.content, 'html.parser')
    if soup.find_all("meta")[1].get("name") == "robots":
        return False
    return True

#Returns true if word in babynames.com, false otherwise
def isName(word):
   url = "https://www.babynames.com/name/" + word 
   req = requests.get(url, headers)
   soup = BeautifulSoup(req.content, 'html.parser')
   if soup.find("h1").get_text() == "Whoops! Not Found":
       return False
    return True

#Returns true if word is a valid word or name, false otherwise
#adds word to wordsChecked dictionary with value True if real word, false otherwise
#dictionary meant to increase efficiency by decreasing checks
def isWordOrName(word):
    if (mayBeName(word) and isName(word)) or isWord(word):
        dictionaries.wordsChecked[word] = True
        return True
    dictionaries.wordsChecked[word] = False
    return False

#returns True if first letter is capitalized and others are not
def mayBeName(word):
    return len(word) > 1 and word[0].isupper() and word[1:].islower()

#input misspelled word
#output set of real words/names that could be confused with word
def correctWord(word):
    corrections = set()
    for letter in list(word):
        for option in dictionaries.characters[letter]:
            newWord = word.replace(letter, option, 1)
            #if word already checked, use previous result
            if newWord in dictionaries.wordsChecked:
                if dictionaries.wordsChecked[newWord]:
                    corrections.add(newWord)
            elif isWordOrName(newWord):
                corrections.add(newWord)
    return corrections

t = time.time()
print(correctWord("cabbagd"))
print(time.time() - t)
    
    

