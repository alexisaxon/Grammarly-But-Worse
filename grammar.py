import module_manager
module_manager.review()
import requests
from bs4 import BeautifulSoup
import string

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
    req = requests.get(url, headers)
    soup = BeautifulSoup(req.content, 'html.parser')
    if soup.find_all("meta")[1].get("name") == "robots":
        return False
    return True

#Returns true if name in babynames.com, false otherwise
def isName(word):
   url = "https://www.babynames.com/name/" + word 
   req = requests.get(url, headers)
   soup = BeautifulSoup(req.content, 'html.parser')
   if soup.find("H1").get_text() == "No names found.":
        return False
    return True

#Returns true if word is a valid word or name, false otherwise
def isWordOrName(word):
    word = word.lowercase()
    return isWord(word) or isName(word)


def correctWord(word):
    


print(isName("Erin"))
    
    

