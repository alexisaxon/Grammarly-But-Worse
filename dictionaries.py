import requests
from bs4 import BeautifulSoup
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


#represents characters that may be confused with one another
#that is, near each other on keyboard or having a similar sound
characters = {"a": {"q", "w", "s", "z", "e", "u"}, 
            "b": {"v", "g", "h", "n"},
            "c": {"x", "d", "f", "v", "k", "s", "ck"},
            "d": {"s", "e", "r", "f", "c", "x"},
            "e": {"w", "r", "d", "s", "a", "y"},
            "f": {"d", "r", "g", "v", "c"},
            "g": {"f", "t", "h", "b", "v", "j"},
            "h": {"g", "y", "j", "n", "b"},
            "i": {"u", "o", "k", "e"},
            "j": {"u", "i", "k", "m", "n", "h", "g"},
            "k": {"i", "o", "l", "m", "j", "u", "c", "ck"},
            "l": {"o", "p", "k"},
            "m": {"n", "j", "k"},
            "n": {"b", "h", "j", "m"},
            "o": {"p", "l", "k", "i"},
            "p": {"l", "o"},
            "q": {"w","a"},
            "r": {"e","d","f","t"},
            "s": {"a","w","d", "x", "z", "c"},
            "t": {"r","f","g","y"},
            "u":{"y", "j", "i"},
            "v": {"c", "f", "g","b"},
            "w": {"q", "a", "s", "d", "e"},
            "x": {"z","s","d","c"},
            "y":{"e", "t", "h", "u"},
            "z":{"a", "s", "x"}}

#word mapped to tuple with wordStatus, abbrevStatus
wordsChecked = {}

#words user has indicated are "real" to them
personalDictionary = set()

#maps misspellings to the corrections provided
completedCorrections = dict()

def cleanUpText(word, badChar):
    while word.endswith(badChar):
        word = word[:len(badChar) - 1]
    while word.startswith(badChar):
        word = word[len(badChar):]
    return word

#2 lines beginning with "[s.extract()" gotten from 
# https://stackoverflow.com/questions/1936466/beautifulsoup-grab-visible-webpage-text
def makeStarterDict():
    t = time.time()
    mostCommonWords = set()
    url = "https://www.gonaturalenglish.com/1000-most-common-words-in-the-english-language/"
    req = requests.get(url, headers)
    soup = BeautifulSoup(req.content, 'html.parser')
    [s.extract() for s in soup(['style', 'script', '[document]', 'head', 'title'])]
    words = soup.getText()
    words = words.split(" ")
    lst = ["\n", "\xa0", "\xa0–", "–\xa0"]
    for word in words:
        if word == "–" or word == "" or word.startswith("http"):
            next
        for element in lst:
            word = cleanUpText(word, element)
        badChars = "!@#$%^&*()_-=+;:'\"][}{/?><.,"
        word = word.strip('\"')
        word = word.strip("\'")
        word = word.strip(badChars)
        while "\n" in word:
            temp = word
            index = word.find("\n")
            word = word[0: index]
            words.append(temp[index + 1:])
        while len(word) > 0 and (word[0] in badChars or word[0] == '"'):
            word = word[1:]
        while len(word) > 0 and (word[len(word) - 1] in badChars or word[len(word) - 1] == '"'):
            word = word[:len(word)-1]
        if word != "homeenglish":
            mostCommonWords.add(word.lower())
    return mostCommonWords
    
mostCommonWords = makeStarterDict()
print(mostCommonWords)
