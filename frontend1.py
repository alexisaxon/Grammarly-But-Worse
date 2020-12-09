import module_manager
module_manager.review()
from cmu_112_graphics import *
import grammar as g
import PIL
import dictionaries
import copy

def appStarted(app):
    app.cursorLocation = 0 #string index
    app.cursorChar = "|"
    startButtons(app)
    startTextBox(app)
    startWords(app)
    app.fullTextWithCursor = app.cursorChar + app.fullText
    app.highlight = None
    #tuple with index of first and last words to highlight
    app.typingMode = []
    #[u, b] indicates that new words should be underlined and bold
    app.clipboard = ""
    app.image = None
    app.lastTried = []
    app.theLabel = ""
    app.lastAbbrev = ""
    app.theLabel = ""

def startTextBox(app):
    app.textboxSelected = False
    app.maxChars = int(round(app.width/11.5)) #occasionally goes off text box
    app.textboxBorders = (13, 25 + app.height//15 + app.buttonMargin + app.buttonHeight, \
        app.width//2 - 13, app.height - 20)
    # (x0, y0, x1, y1) of textbox borders
    app.distanceBtwnLines = 15
    app.topOfTextbox = 25 + app.height//15 + app.buttonMargin + app.buttonHeight
    #whereWordsStart

def startButtons(app):
    app.buttons = []
    app.buttonLocations = [] #(x, y) of top left for each button
    app.buttonMargin = 10
    app.buttonHeight = 30
    app.textButtons = ["Bold", "Italicize", "Underline", "Copy", "Paste", "Save"]

def startWords(app):
    app.selectedWord = 0
    app.words = ["Insert", "your", "text", "here."] #list of words in document
    app.wordsRepr = ["|Insert", "your", "text", "here."] #includes escape sequences
    app.fullText = "Insert your text here."
    app.textLines = ["Insert your text here."]
    app.lineLengths = [len(app.textLines[0])]
    app.wordFeatures = [[], [], [], []]
    #an entry of [i,b] would indicate that word is italicized and bolded

#returns True if user clicked button with 'text', false otherwise    
def buttonClicked(app, text, x, y):
    buttonWidth = 10*len(text)
    #when we're in app.buttons, rather than word features
    try:
        i = app.buttons.index(text)
        left = app.buttonLocations[i][0]
        top = app.buttonLocations[i][1]
        if x >= left and x <= left + buttonWidth and y >= top and y <= top + app.buttonHeight:
            return True
        return False
    #when we're in word features
    except:
        i = app.textButtons.index(text)
        #update below if change other constants
        startWidths = [20, 70, 170, 270, 320, 380]
        top = app.height // 15 + 25
        left = startWidths[i]
        if x >= left and x <= left + buttonWidth and y >= top and y <= top + app.buttonHeight:
            return True
        return False

def typeACharacter(app, c):
    app.fullText = app.fullText[0:app.cursorLocation] + c + \
        app.fullText[app.cursorLocation:]
    app.cursorLocation += 1
    app.fullTextWithCursor = app.fullText[0:app.cursorLocation] + app.cursorChar + \
        app.fullText[app.cursorLocation:]
    createWordList(app, app.fullText)
    app.wordsRepr = app.fullTextWithCursor.split(" ")

#updates app.words with new words and app.wordsRepr, which includes \n
#also updates list of textlines
def createWordList(app, text):
    app.words = app.fullText.split(" ")
    for i in range(len(app.words)):
        if "\n" in app.words[i]:
            temp = app.words[i]
            index = temp.find("\n")
            app.words[i] = temp[0:index]
            app.words.insert(i+1,temp[index+1:])
            app.wordFeatures.insert(i+1, copy.copy(app.wordFeatures[i]))
    app.wordsRepr = app.fullText.split(" ")
    calculateTextLines(app)

#shifts all buttons starting at 'first' index and ending just before
#'last' index until they are center aligned
def buttonShiftRow(app, first, last, shiftBy):
    for i in range(first, last):
        app.buttonLocations[i] = (app.buttonLocations[i][0] + shiftBy, \
            app.buttonLocations[i][1])

#should call when new word selected
def calculateButtonLocations(app):
    if len(app.buttons) != 0:
        app.buttonLocations = []
        startWidth = app.width//2 + app.buttonMargin*4
        startHeight = 25 + app.height//15
        firstButtonInRow = 0
        for i in range(len(app.buttons)):
            text = app.buttons[i]
            buttonWidth = len(text) * 10
            if startWidth + buttonWidth > app.width - app.buttonMargin:
                startWidth = app.width//2 + app.buttonMargin*4
                startHeight += app.buttonMargin + app.buttonHeight
                if i != 0: #since prevEnd not meaningfully defined yet
                    buttonShiftRow(app, firstButtonInRow, i, (app.width//2 - app.buttonMargin -\
                        prevEnd//2))
                firstButtonInRow = i
            app.buttonLocations.append((startWidth, startHeight))
            prevEnd = startWidth + buttonWidth
            startWidth += buttonWidth + app.buttonMargin
        buttonShiftRow(app, firstButtonInRow, len(app.buttons), (app.width - app.buttonMargin -\
                        prevEnd)//2) 
        #shift last row since we've always been one behind current

def calculateTextLines(app):
    lineTotal = 0
    currentLine = 0
    textLines = [""]
    app.lineLengths = []
    for word in app.wordsRepr:
        if "\n" in word:
            index = word.find("\n")
            word1, word2 = word[0:index], word[index+1:]
            if lineTotal + len(word1) > app.maxChars:
                textLines.append(word1)
                app.lineLengths.append(lineTotal)
                lineTotal = len(word1)
                currentLine += 1
            else:
                textLines[currentLine] += " " + word1
                lineTotal += len(word1) + 1
            textLines.append(word2)
            app.lineLengths.append(lineTotal)
            lineTotal = len(word2)
            currentLine += 1
        else:
            if lineTotal + len(word) > app.maxChars:
                textLines.append(word)
                app.lineLengths.append(lineTotal)
                lineTotal = len(word)
                currentLine += 1
            else:
                textLines[currentLine] += " " + word
                lineTotal += len(word) + 1
    app.lineLengths.append(lineTotal)
    toPrint = ""
    for line in textLines:
        toPrint += line + "\n"
    app.textLines = toPrint.splitlines()
    return toPrint

#returns index of nearest char to (x,y)
def findNearestChar(app, x, y):
    distancesFromY = []
    for i in range(0,len(app.textLines)):
        positionOfLine = app.topOfTextbox + app.distanceBtwnLines*i
        distancesFromY.append(abs(y - positionOfLine))
    lineNum = distancesFromY.index(min(distancesFromY))
    distancesFromX = []
    for i in range(0, app.lineLengths[lineNum]):
        positionOfChar = 15 + len(app.textLines[lineNum][0:i])*4
        distancesFromX.append(abs(x-positionOfChar))
    try:
        charPixel = min(distancesFromX)
    except:
        charPixel = 0
    charNumInLine = distancesFromX.index(charPixel)
    total = 0
    for line in app.textLines[0:lineNum]:
        total += len(line)
    total += charNumInLine
    #flag is false if quite far away
    if charPixel > 20 or min(distancesFromY) > 20:
        flag = False
    else:
        flag = True
    return (total, flag)

#calculates index of first letter in word in app.fullText based on index in app.words
def calculateIndexOfWord(app, index):
    startIndex = 0
    for word in app.words[0:index]:
        startIndex += 1 + len(word)
    return startIndex

#From 112 website (Animations Part 3), modified slightly to say app rather than self
def saveImage(app):
    snapshotImage = app.getSnapshot()
    app.image = app.scaleImage(snapshotImage, 0.4)
    app.saveSnapshot()
#--------------------------------CONTROL-----------------------------------------

#returns index of fullText highlight starts on and its length in characters
def findHighlight(app):
    lenOfHighlight = 0
    for word in app.words[app.highlight[0]:app.highlight[1] + 1]:
        lenOfHighlight += len(word) + 1
    startIndex = calculateIndexOfWord(app, app.highlight[0])
    return startIndex, lenOfHighlight

#allows user to type in textbox
#Professor Kosbie gave me high-level advice on how to implement the textbox in 112 Graphics
def keyPressed(app, event):
    wasHighlighted = False
    if app.highlight != None and event.key != "Left" and event.key != "Right":
        app.wordFeatures = copy.copy(app.wordFeatures[0:app.highlight[0]]) + \
            copy.copy(app.wordFeatures[app.highlight[1] + 1:])
        wasHighlighted = True
        startIndex, lenOfHighlight = findHighlight(app)
        app.fullText = app.fullText[0:startIndex] + \
            app.fullText[startIndex + lenOfHighlight + 1:]
        app.cursorLocation = startIndex
        createWordList(app, app.fullText)
        app.wordsRepr = app.fullText.split(" ")
        app.highlight = None
    if (app.textboxSelected or wasHighlighted) and app.theLabel != "Please select an option before continuing":
        if event.key in "abcdefghijklmnopqrstuvwxyz./,!@#$%^&*()_-+=\][}{';:><?\"\'\\" or\
        event.key in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            typeACharacter(app, event.key)
        elif event.key == "Space":
            typeACharacter(app, " ")
        elif event.key == "Enter":
            app.fullText = app.fullText[0:app.cursorLocation] + "\n" + \
                app.fullText[app.cursorLocation:]
            app.cursorLocation += 1
            createWordList(app, app.fullText)
            app.wordsRepr = app.fullText.split(" ")
        elif event.key == "Backspace" and app.cursorLocation != 0:
            app.fullText = app.fullText[0:app.cursorLocation - 1] + \
                app.fullText[app.cursorLocation:]
            app.cursorLocation -= 1
            createWordList(app, app.fullText)
        elif event.key == "Left" and app.cursorLocation != 0:
            app.cursorLocation -= 1
        elif event.key == "Right" and app.cursorLocation < len(app.fullText):
            app.cursorLocation += 1
        if event.key in ";:\".?!" or event.key == "Enter" or event.key == "Space":
            app.selectedWord = findWordIndexWithChar(app, app.cursorLocation - 1)
            while app.selectedWord >= len(app.words) or (app.words[app.selectedWord] == "" \
                and app.selectedWord > 0):
                app.selectedWord -= 1
            focusWord = app.words[app.selectedWord]
            focusWord = focusWord.strip("\n")
            focusWord = focusWord.strip(",\'\":;.?/!")
            if focusWord != "" and "\n" not in focusWord:
                runThroughChecks(app,focusWord)
            elif "\n" in focusWord:
                index = focusWord.find("\n")
                app.words.insert(app.selectedWord + 1, focusWord[index+1:])
                app.words[app.selectedWord] = focusWord[0:index]
                app.wordFeatures.insert(app.selectedWord + 1, copy.copy(app.wordFeatures[app.selectedWord]))
                runThroughChecks(app, focusWord[0:index])
                runThroughChecks(app, focusWord[index+1:])
    while len(app.words) > len(app.wordFeatures):
        app.wordFeatures.insert(app.cursorLocation - 1, copy.copy(app.typingMode))
    if len(app.buttons) != 0:
        app.theLabel = "Please select an option before continuing"

def runThroughChecks(app, focusWord):
    focusWord = focusWord.strip("\n")
    focusWord = focusWord.strip(",\'\":;.?/!")
    tempLst = g.isWordOrName(focusWord)
    wordStatus, abbrevStatus = tempLst[0], tempLst[1]
    if not wordStatus:
        tempLst = g.correctWord(focusWord, abbrevStatus)
        app.buttons, app.lastTried = tempLst[0], tempLst[1]
        app.lastCorrections = copy.copy(app.buttons)
        calculateButtonLocations(app)
    app.lastAbbrev = abbrevStatus

def saveStuff(app):
    while True:
        choice = app.getUserInput("Would you like to save as a text or image file?" +\
        " Type 'i' for image and 't' for text")
        try:
            if choice.lower() == "i":
                saveImage(app)
                app.message = "Save successful!"
                break
            elif choice.lower() == "t":
                fileName = app.getUserInput("What do you want to call your file?")
                file1 = open(rf"{fileName}.txt", "w")
                for i in range(len(app.textLines)):
                    file1.write(app.textLines[i])
                file1.close()
                app.message = "Save successful!"
                break
        except:
            pass

def mousePressed(app, event):
    x0, y0, x1, y1 = app.textboxBorders
    features = {"Underline":"u", "Bold":"b", "Italicize":"i"}
    if event.x < 1.1 * app.width//2 and event.y < app.topOfTextbox:
        for text in app.textButtons:
            if buttonClicked(app, text, event.x, event.y):
                if text == "Save":
                    saveStuff(app)
                if text == "Paste":
                    app.fullText = app.fullText[0:app.cursorLocation] + app.clipboard + \
                        app.fullText[app.cursorLocation:]
                    for i in range(len(app.clipboard.split(" "))):
                        app.wordFeatures.insert(app.cursorLocation, copy.copy(app.typingMode))
                    app.cursorLocation += len(app.clipboard)
                    app.words = app.fullText.split(" ")
                    createWordList(app, app.fullText)
                    break
                if app.highlight != None:
                    for i in range(app.highlight[0], app.highlight[1] + 1):
                        try:
                            if features[text] not in app.wordFeatures[i]:
                                app.wordFeatures[i].append(features[text])
                            else:
                                app.wordFeatures[i].remove(features[text])
                        except: 
                            #means button is copy
                            app.clipboard = ""
                            for i in range(app.highlight[0], app.highlight[1] + 1):
                                app.clipboard += app.words[i] + " "
                            app.clipboard = app.clipboard[:len(app.clipboard) - 1]
                else:
                    try:
                        if features[text] not in app.typingMode:
                            app.typingMode.append(features[text])
                        else:
                            app.typingMode.remove(features[text])
                    except: #oddly occurs after saving successfully
                        app.showMessage("Your save was successful!")
                break
    #don't do button checks if on other side of canvas
    elif event.x > app.width//2: 
        app.textboxSelected = False
        specialButtons = {"Ignore", f"Add '{app.words[app.selectedWord]}' to Personal Dictionary", \
                "Keep searching"}
        for text in app.buttons:  
            if buttonClicked(app, text, event.x, event.y):
                app.theLabel = ""
                if text not in specialButtons and not text.endswith("Personal Dictionary") and \
                    isinstance(app.buttons, list):
                    app.words = app.words[0:app.selectedWord] + \
                        [text] + app.words[app.selectedWord + 1:]
                    app.fullText = ""
                    for word in app.words:
                        app.fullText += " " + word
                    app.fullText = app.fullText[1:]
                    createWordList(app, app.fullText)
                    app.buttons = []
                    app.buttonLocations = []
                elif text.endswith("Personal Dictionary"):
                    dictionaries.personalDictionary.add(app.words[app.selectedWord])
                    app.buttons = []
                    app.buttonLocations = []
                elif text == "Keep searching":
                    app.theLabel = "This may take a minute"
                    app.buttons = []
                    app.buttonLocations = []
                    results, app.lastTried = g.keepSearching(app.lastTried, app.lastAbbrev)
                    for element in results:
                        for element1 in element:
                            if element1 not in specialButtons and not element1.endswith("Personal Dictionary"):
                                if(element1 in dictionaries.mostCommonWords or element1 in dictionaries.personalDictionary):
                                    app.buttons.insert(0,element1)
                                else:
                                    wordStatus, abbrevStatus = g.isWordOrName(element1) 
                                    if wordStatus and abbrevStatus == app.lastAbbrev:
                                        app.buttons.append(element1)
                    app.buttons.append("Ignore")
                    app.buttons.append("Keep searching")
                    calculateButtonLocations(app)
                    app.theLabel = ""
                elif text == "Ignore":
                    app.buttons = []
                    app.buttonLocations = []
                elif not isinstance(app.buttons, list):
                    app.words = app.words[0:app.selectedWord] + \
                        [app.buttons] + app.words[app.selectedWord + 1:]
                    app.fullText = ""
                    for word in app.words:
                        app.fullText += " " + word
                    app.fullText = app.fullText[1:]
                    createWordList(app, app.fullText)
                    app.buttons = []
                    app.buttonLocations = []
                break
    elif x1 >= event.x >= x0 and y1 >= event.y >= y0:
        app.textboxSelected = True
        app.cursorLocation = findNearestChar(app, event.x, event.y)[0] + 1
    else:
        app.textboxSelected = False
    app.highlight = None

#takes index of char and returns index of word it's in
def findWordIndexWithChar(app, index):
    total = i = 0
    #exit with i as one line past nearestLetter
    calculateTextLines(app)
    while total < index and i < len(app.textLines):
        total += len(app.textLines[i])
        i += 1
    i -= 1
    calculateTextLines(app)
    try:
        total -= app.lineLengths[i]
    except:
        pass #last line must have length zero anyways
    cumLineLength = 0
    cumWordTotal = 0
    for j in range(i):
        if len(app.textLines) < j:
            cumLineLength += len(app.textLines[j])
            cumWordTotal += len(app.textLines[j].split(" "))
    while cumLineLength < index:
        cumWordTotal += 1
        cumLineLength += 1 + len(app.words[cumWordTotal - 2])
    return cumWordTotal - 1

#for highlighting text
def mouseDragged(app, event):
    x, y = event.x, event.y
    x0, y0, x1, y1 = app.textboxBorders
    if(x0<x<x1 and y0<y<y1):
        #index
        nearestLetter, flag = findNearestChar(app, x, y)
        #index
        if flag:
            nearestWord = findWordIndexWithChar(app, nearestLetter)
            if app.highlight == None or app.highlight == (nearestWord, nearestWord):
                app.highlight = (nearestWord, nearestWord)
            elif app.highlight[0] > nearestWord:
                app.highlight = (nearestWord, app.highlight[1])
            elif app.highlight[1] < nearestWord:
                app.highlight = (app.highlight[0], app.highlight[1] + 1)
            elif app.highlight[0] == nearestWord or app.highlight[1] == nearestWord:
                pass
            elif app.highlight[0] + 1 == nearestWord:
                app.highlight = (app.highlight[0] + 1, app.highlight[1])
            elif app.highlight[1] - 1 == nearestWord:
                app.highlight = (app.highlight[0], app.highlight[1] - 1)
            else:
                app.highlight = (nearestWord, nearestWord)
        if app.highlight != None:
            if app.highlight[0] == -1:
                app.highlight = (0, app.highlight[1])
            if app.highlight[1] == -1:
                app.highlight = (app.highlight[0], 0)
    
#----------------------------------VIEW------------------------------------------

def drawSingleButton(app, canvas, label, startWidth, startHeight):
    buttonWidth = len(label) * 10
    canvas.create_rectangle(startWidth, startHeight, startWidth + buttonWidth, \
        startHeight + app.buttonHeight, fill="lightblue", outline="lightblue")
    canvas.create_text(startWidth + buttonWidth//2, startHeight + app.buttonHeight//2,\
        text=label)

#buttons are dynamically sized and formatted based on length
def drawButtons(app, canvas):
    textButtons = app.textButtons
    startWidth = app.buttonMargin * 2
    startHeight = app.height // 15 + 25
    for button in textButtons:
        drawSingleButton(app, canvas, button, startWidth, startHeight)
        startWidth += app.buttonMargin + len(button) * 10
    #draws buttons for misspelled words
    if not isinstance(app.buttons, list):
        startWidth, startHeight = app.buttonLocations[0]
        drawSingleButton(app, canvas, app.buttons, startWidth, startHeight)
    else:
        for i in range(len(app.buttons)):
            startWidth, startHeight = app.buttonLocations[i]  
            drawSingleButton(app, canvas, app.buttons[i], startWidth, startHeight)


def drawTextbox(app, canvas):
    startHeight = app.topOfTextbox
    if app.textboxSelected:
        canvas.create_rectangle(app.textboxBorders, fill='lightgrey', \
            outline='gold',width=2)
    else:
        canvas.create_rectangle(app.textboxBorders, fill='lightgrey', \
            width=0)
    drawText(app, canvas)

def featureTranslation(features):
    ret = ""
    if "b" in features:
        ret += " bold"
    if "u" in features:
        ret += " underline"
    if "i" in features:
        ret += " italic"
    return ret

#my project mentor, Natalie, told me how to find the bounding box of text objects
def drawText(app, canvas):
    startX = 15
    startY = app.topOfTextbox
    index = 0
    for i in range(len(app.textLines)):
        for word in app.textLines[i].split(" "):
            if word == "":
                index -= 1
                next
            if app.words != [""]:
                features = app.wordFeatures[index]
                f = featureTranslation(features)
                objID = canvas.create_text(startX, startY, text=word, anchor="nw",\
                    font="Arial 8"+f)
                x0, y0, x1, y1 = canvas.bbox(objID)
                if app.highlight != None and app.highlight[0] <= index <= app.highlight[1]:
                    drawHighlightRedux(app, canvas, x0, y0, x1, y1, word, f)
                startX = x1 + 5
                index += 1
        startY += app.distanceBtwnLines
        startX = 15
    index = 0

def drawHighlightRedux(app, canvas, x0, y0, x1, y1, word, f):
    canvas.create_rectangle(x0 - 3, y0, x1 + 3, y1, fill="lightyellow", outline="lightyellow")
    canvas.create_text(x0, y0, text=word, anchor="nw", font="Arial 8"+f)

#also includes top label
def drawBorders(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height, outline="lightyellow", fill="lightyellow")
    canvas.create_rectangle(5, 5, app.width - 5, app.height - 5, outline='red')
    canvas.create_rectangle(6, 6, app.width - 6, app.height - 6, outline='orange')
    canvas.create_rectangle(7, 7, app.width - 7, app.height - 7, outline='red')
    canvas.create_rectangle(13, 13, app.width - 13, 13 + app.height//15, outline='black', \
        width=3)
    fontSize = int(round(app.height/22.86))
    canvas.create_text(app.width//2, app.height//30 + 13, text="Grammarly But Worse", \
        font=f"Times {fontSize} bold")
    canvas.create_text(app.width//2 + 10, app.height//2, text=app.theLabel, anchor="nw")

def redrawAll(app, canvas):
    drawBorders(app, canvas)
    drawButtons(app, canvas)
    drawTextbox(app, canvas)

runApp(width=800, height=600)