import module_manager
module_manager.review()
from cmu_112_graphics import *
import grammar as g

def appStarted(app):
    app.buttons = []
    app.buttonLocations = [] #(x, y) of top left for each button
    app.buttonMargin = 10
    app.selectedWord = None #will be index
    app.words = ["Insert", "your", "text", "here."] #list of words in document
    app.wordsRepr = ["Insert", "your", "text", "here."] #includes escape sequences
    app.buttonHeight = 30
    app.textboxSelected = False
    app.fullText = "Insert your text here."
    app.maxChars = int(round(app.width/11.5)) #occasionally goes off text box
    app.textboxBorders = (13, 25 + app.height//15, app.width//2 - 13, app.height - 20)
    # (x0, y0, x1, y1) of textbox borders
    app.cursorLocation = 0 #string index
    app.cursorChar = "|"
    app.fullTextWithCursor = app.cursorChar + app.fullText

#returns True if user clicked button with 'text', false otherwise    
def buttonClicked(app, text, x, y):
    buttonWidth = 10*len(text)
    try:
        i = app.buttons.index(text)
        left = app.buttonLocations[i][0]
        top = app.buttonLocations[i][1]
        if x >= left and x <= left + buttonWidth and y >= top and y <= top + app.buttonHeight:
            return True
        return False
    except:
        print("text not in button list")

def typeACharacter(app, c):
    app.fullText = app.fullText[0:app.cursorLocation] + c + \
        app.fullText[app.cursorLocation:]
    app.cursorLocation += 1
    app.fullTextWithCursor = app.fullText[0:app.cursorLocation] + app.cursorChar + \
        app.fullText[app.cursorLocation:]
    createWordList(app, app.fullText)
    app.wordsRepr = app.fullTextWithCursor.split(" ")

def createWordList(app, text):
    app.words = app.fullText.split(" ")
    for i in range(len(app.words)):
        if "\n" in app.words[i]:
            temp = app.words[i]
            index = temp.find("\n")
            app.words[i] = temp[0:index]
            app.words.insert(i+1,temp[index+1:])
    app.wordsRepr = app.fullText.split(" ") 

#allows user to type in textbox
#Professor Kosbie gave me high-level advice on how to implement the textbox in 112 Graphics
#To do: figure out how to implement shift+letter for uppercase
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
            print("yay")
            wordStatus, abbrevStatus = g.isWordOrName("womsn")
            if not wordStatus:
                print("hi")
                app.buttons = g.correctWord("womsn", abbrevStatus)
                print(app.buttons)
                calculateButtonLocations(app)
                print(app.buttonLocations)

def mousePressed(app, event):
    x0, y0, x1, y1 = app.textboxBorders
    #don't do button checks if on other side of canvas
    if event.x > app.width//2 + app.buttonMargin: 
        app.textboxSelected = False
        for text in app.buttons:
            if buttonClicked(app, text, event.x, event.y):
                try:
                    app.words = app.words[0:app.selectedWord] + \
                        app.words[app.selectedWord:].replace(app.words[app.selectedWord], text, 1)
                except:
                    print("Error: selectedWord probably not defined")
    elif x1 >= event.x >= x0 and y1 >= event.y >= y0:
        app.textboxSelected = True
    else:
        app.textboxSelected = False

#should call when new word selected
def calculateButtonLocations(app):
    startWidth = app.width//2 + app.buttonMargin
    startHeight = 25 + app.height//15
    for text in app.buttons:
        buttonWidth = len(text) * 10
        if startWidth + buttonWidth > app.width - app.buttonMargin:
            startWidth = app.width//2 + app.buttonMargin
            startHeight += app.buttonMargin + app.buttonHeight
        app.buttonLocations.append((startWidth, startHeight))
        startWidth += buttonWidth + app.buttonMargin

#buttons are dynamically sized and formatted based on length
def drawButtons(app, canvas):
    for i in range(len(app.buttons)):
        startWidth, startHeight = app.buttonLocations[i]
        buttonWidth = len(app.buttons[i] * 10)
        canvas.create_rectangle(startWidth, startHeight, startWidth + buttonWidth, \
            startHeight + app.buttonHeight, fill="lightblue", outline="lightblue")
        canvas.create_text(startWidth + buttonWidth//2, startHeight + app.buttonHeight//2,\
            text=app.buttons[i])

#may want to move the calculations elsewhere
def drawTextbox(app, canvas):
    startHeight = 25 + app.height//15
    canvas.create_rectangle(app.textboxBorders, fill='lightgrey', \
        outline='lightgrey')
    lineTotal = 0
    startX = 15
    startY = startHeight
    currentLine = 0
    textLines = [""]
    for word in app.wordsRepr:
        if lineTotal + len(word) > app.maxChars:
            textLines.append(word)
            lineTotal = len(word)
            currentLine += 1
        else:
            textLines[currentLine] += " " + word
            lineTotal += len(word) + 1
    toPrint = ""
    for line in textLines:
        toPrint += line + "\n"
    canvas.create_text(startX, startY, text=toPrint, anchor="nw")

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