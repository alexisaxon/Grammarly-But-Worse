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

#Returns 2-tuple where first value is word status (T/F), 2nd is abbreviation status (T/F)
def isWord(word):
    url = "https://www.dictionary.com/browse/" + word + "?s=t"
    req = requests.get(url, headers) #takes .5 seconds
    soup = BeautifulSoup(req.content, 'html.parser')
    if soup.find_all("meta")[1].get("name") == "robots":
        return (False, False)
    if isAbbreviation(word, soup):
        return (True, True)
    return (True, False)

#True if word is an abbreviation, False otherwise
#Word existence assumed
def isAbbreviation(word, soup):
    try:
        text = soup.find("h3", class_="css-xboiwi ea1n8qa0").get_text()
        if (text[0:3] == "or ") and (text[4::2] == "."*len(text[4::2])):
            return True
        else:
            return False
    #occurs when given class not present
    except:
        return False 

#Returns true if word in babynames.com, false otherwise
def isName(word):
   url = "https://www.babynames.com/name/" + word 
   req = requests.get(url, headers)
   soup = BeautifulSoup(req.content, 'html.parser')
   if soup.find("h1").get_text() == "Whoops! Not Found":
       return False
   return True

#Returns tuple with first bool indicating whether it is a word/name, second if it's an abbreviation
#adds word to wordsChecked dictionary with value True if real word, false otherwise
#dictionary meant to increase efficiency by decreasing checks
def isWordOrName(word):
    word = word.strip()
    if word.startswith("\""):
        word = word[1:]
    punctuation = {".", "?", "!", "\"", "\'", ";", ":"}
    for thing in punctuation:
        if word.endswith(thing):
            word = word[:len(word) - 1]
            break
    wordStatus, abbrevStatus = isWord(word)
    if wordStatus or (mayBeName(word) and isName(word)):
        dictionaries.wordsChecked[word] = (True, abbrevStatus)
    else:
        dictionaries.wordsChecked[word] = (False, False)
    return dictionaries.wordsChecked[word]
    
#returns True if first letter is capitalized and others are not
def mayBeName(word):
    return len(word) > 1 and word[0].isupper() and word[1:].islower()

#input misspelled word and T/F for if it's an abbreviation
#output list of real words/names that could be confused with word
def correctWord(word, abbrevStatus):
    if word in dictionaries.completedCorrections:
        return dictionaries.completedCorrections[word]
    corrections = []
    for letter in list(word):
        for option in dictionaries.characters[letter]:
            newWord = word.replace(letter, option, 1)
            if newWord in dictionaries.mostCommonWords:
                #puts common words at front for better user experience
                corrections.insert(0, newWord)
            #if word already checked, use previous result
            elif newWord in dictionaries.wordsChecked:
                if dictionaries.wordsChecked[newWord][0] and \
                    dictionaries.wordsChecked[newWord][1] == abbrevStatus:
                    corrections.append(newWord)
            else:
                newWordStatus, newAbbrevStatus = isWordOrName(newWord)
                if newWordStatus and newAbbrevStatus == abbrevStatus:
                    corrections.append(newWord)
    corrections.append(f"Add '{word}' to Personal Dictionary")
    corrections.append("Keep searching")
    corrections.append("Ignore")
    dictionaries.completedCorrections[word] = corrections
    return corrections

# print(correctWord("wprd", False))