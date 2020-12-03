import module_manager
module_manager.review()
from cmu_112_graphics import *
import grammar as g

def appStarted(app):
    app.cursorLocation = 0 #string index
    app.cursorChar = "|"
    startButtons(app)
    startTextBox(app)
    startWords(app)
    app.fullTextWithCursor = app.cursorChar + app.fullText
    app.highlight = None
    #tuple with index of first and last words to highlight

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
    app.textButtons = ["Bold", "Italicize", "Underline", "Copy", "Paste"]

def startWords(app):
    app.selectedWord = 4
    app.words = ["Insert", "your", "text", "here.", "womsn"] #list of words in document
    app.wordsRepr = ["Insert", "your", "text", "here.", "womsn"] #includes escape sequences
    app.fullText = "Insert your text here. womsn"
    app.textLines = ["Insert your text here. womsn"]
    app.lineLengths = [len(app.textLines[0])]

#returns True if user clicked button with 'text', false otherwise    
def buttonClicked(app, text, x, y):
    buttonWidth = 10*len(text)
    i = app.buttons.index(text)
    left = app.buttonLocations[i][0]
    top = app.buttonLocations[i][1]
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
    app.buttonLocations = []
    startWidth = app.width//2 + app.buttonMargin
    startHeight = 25 + app.height//15
    firstButtonInRow = 0
    for i in range(len(app.buttons)):
        text = app.buttons[i]
        buttonWidth = len(text) * 10
        if startWidth + buttonWidth > app.width - app.buttonMargin:
            startWidth = app.width//2 + app.buttonMargin
            startHeight += app.buttonMargin + app.buttonHeight
            if i != 0: #since prevEnd not meaningfully defined yet
                buttonShiftRow(app, firstButtonInRow, i, (app.width//2 - app.buttonMargin -\
                    prevEnd//2))
            firstButtonInRow = i
        app.buttonLocations.append((startWidth, startHeight))
        prevEnd = startWidth + buttonWidth
        startWidth += buttonWidth + app.buttonMargin
    buttonShiftRow(app, firstButtonInRow, i + 1, (app.width - app.buttonMargin -\
                    prevEnd)//2) 
    #shift last row since we've always been one behind current

#updates app.textLines and app.lineLengths
#not currently called anywhere
def calculateTextLines(app):
    lineTotal = 0
    currentLine = 0
    textLines = [""]
    for word in app.wordsRepr:
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
        positionOfChar = 15 + len(app.textLines[lineNum][0:i])*7
        distancesFromX.append(abs(x-positionOfChar))
    charPixel = min(distancesFromX)
    charNumInLine = distancesFromX.index(charPixel)
    total = 0
    for line in app.textLines[0:lineNum]:
        total += len(line)
    total += charNumInLine
    return total

#--------------------------------CONTROL-----------------------------------------

#allows user to type in textbox
#Professor Kosbie gave me high-level advice on how to implement the textbox in 112 Graphics
def keyPressed(app, event):
    if app.textboxSelected:
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
        if event.key in ";:'\".?!" or event.key == "Enter" or event.key == "Space":
            wordStatus, abbrevStatus = g.isWordOrName(app.words[app.selectedWord])
            if not wordStatus:
                app.buttons = g.correctWord(app.words[app.selectedWord], abbrevStatus)
                calculateButtonLocations(app)

def mousePressed(app, event):
    x0, y0, x1, y1 = app.textboxBorders
    #don't do button checks if on other side of canvas
    if event.x > app.width//2 + app.buttonMargin: 
        app.textboxSelected = False
        specialButtons = {"Ignore", f"Add {app.words[app.selectedWord]} to personal dictionary", \
                "Keep searching"}
        for text in app.buttons:  
            if buttonClicked(app, text, event.x, event.y):
                if text not in specialButtons:
                    app.words = app.words[0:app.selectedWord] + \
                        [text] + app.words[app.selectedWord + 1:]
                    app.fullText = ""
                    for word in app.words:
                        app.fullText += " " + word
                    app.fullText = app.fullText[1:]
                    createWordList(app, app.fullText)
                elif text == f"Add {text} to personal dictionary":
                    dictionaries.personalDictionary.add(text)
                elif text == "Keep searching":
                    pass
                app.buttons = []
                app.buttonLocations = []
                break
    elif x1 >= event.x >= x0 and y1 >= event.y >= y0:
        app.textboxSelected = True
    else:
        app.textboxSelected = False

#takes index of char and returns index of word it's in
def findWordIndexWithChar(app, index):
    total = i = 0
    #exit with i as one line past nearestLetter
    while total < index:
        total += app.lineLengths[i]
        i += 1
    i -= 1
    total -= app.lineLengths[i]
    cumLineLength = 0
    cumWordTotal = 0
    for j in range(i):
        cumLineLength += app.lineLengths[j]
        cumWordTotal += len(app.textLines[j].split(" "))
    while cumLineLength < index:
        cumWordTotal += 1
        cumLineLength += 1 + len(app.words[cumWordTotal - 1])
    return cumWordTotal - 1

#for highlighting text
def mouseDragged(app, event):
    x, y = event.x, event.y
    #index
    nearestLetter = findNearestChar(app, x, y)
    #index
    nearestWord = findWordIndexWithChar(app, nearestLetter)
    if app.highlight == None:
        app.highlight = (nearestWord, nearestWord)
    elif app.highlight[0] + 1 == nearestWord:
        app.highlight = (app.highlight[0] + 1, app.highlight[1])
    elif app.highlight[0] - 1 == nearestWord:
        app.highlight = (app.highlight[0] - 1, app.highlight[1])
    elif app.highlight[1] + 1 == nearestWord:
        app.highlight = (app.highlight[0], app.highlight[1] + 1)
    elif app.highlight[1] - 1 == nearestWord:
        app.highlight = (app.highlight[0], app.highlight[1] - 1)
    else:
        app.highlight = (nearestWord, nearestWord)
    
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
    for i in range(len(app.buttons)):
        startWidth, startHeight = app.buttonLocations[i]
        drawSingleButton(app, canvas, app.buttons[i], startWidth, startHeight)

def drawHighlight(app, canvas):
    if app.highlight != None:
        total = 0
        #the ending value of i is the line of first highlighted word
        #ending value of total is first index of line i
        for i in range(len(app.lineLengths)):
            if total + app.lineLengths[i] < app.highlight[0]:
                total += app.lineLengths[i]
            else:
                total += 1
                break
        startX = 15
        startY = i*app.distanceBtwnLines + app.topOfTextbox + 2
        for word in app.textLines[i][0:app.highlight[0]]:
            startX += 25*len(word)
        for index in range(app.highlight[0], app.highlight[1] + 1):
            canvas.create_rectangle(startX, startY, startX + len(app.words[index]) * 8,\
                startY + app.distanceBtwnLines, fill="lightyellow", outline="lightyellow")
            startX += 5*len(app.words[index])
            if index != len(app.words) - 1 and startX + len(app.words[index+1])> app.width - app.textboxBorders[2]:
                startY += app.distanceBtwnLines
                startX = 15 

#may want to move the calculations elsewhere
def drawTextbox(app, canvas):
    startHeight = app.topOfTextbox
    if app.textboxSelected:
        canvas.create_rectangle(app.textboxBorders, fill='lightgrey', \
            outline='gold',width=2)
    else:
        canvas.create_rectangle(app.textboxBorders, fill='lightgrey', \
            width=0)
    drawHighlight(app, canvas)
    '''
    startX = 15
    startY = startHeight
    for i in range(len(app.textLines)):
        canvas.create_text(startX, startY, text=app.textLines[i], anchor="nw")
        startY += app.distanceBtwnLines'''
    drawText(app, canvas)

#looks bad, not currently in use
def drawText(app, canvas):
    startX = 15
    startY = app.topOfTextbox
    for i in range(len(app.textLines)):
        for word in app.textLines[i].split(" "):
            canvas.create_text(startX, startY, text=word, anchor="nw")
            startX += len(word)*7
        startY += app.distanceBtwnLines
        startX = 15

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

def redrawAll(app, canvas):
    drawBorders(app, canvas)
    drawButtons(app, canvas)
    drawTextbox(app, canvas)

runApp(width=800, height=600)