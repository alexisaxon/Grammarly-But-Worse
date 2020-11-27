import module_manager
module_manager.review()
from cmu_112_graphics import *
import tkinter as tk
import tkinter.scrolledtext as st 
from tkinter import ttk 

def appStarted(app):
    app.buttons = []
    app.buttonLocations = [] #(x, y) of top left for each button
    app.buttonMargin = 10
    app.selectedWord = None #will be index
    app.words = [] #list of words in document
    app.buttonHeight = 30

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

def mousePressed(app, event):
    #don't do button checks if on other side of canvas
    if event.x > app.width//2 + app.buttonMargin: 
        for text in app.buttons:
            if buttonClicked(app, text, event.x, event.y):
                try:
                    app.words = app.words[0:app.selectedWord] + \
                        app.words[app.selectedWord:].replace(app.words[app.selectedWord], text, 1)
                except:
                    print("Error: selectedWord probably not defined")

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
        print(app.buttonLocations)
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

def redrawAll(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height, outline="lightyellow", fill="lightyellow")
    canvas.create_rectangle(5, 5, app.width - 5, app.height - 5, outline='red')
    canvas.create_rectangle(6, 6, app.width - 6, app.height - 6, outline='orange')
    canvas.create_rectangle(7, 7, app.width - 7, app.height - 7, outline='red')
    canvas.create_rectangle(13, 13, app.width - 13, 13 + app.height//15, outline='black', \
        width=3)
    fontSize = int(round(app.height/22.86))
    canvas.create_text(app.width//2, app.height//30 + 13, text="Grammarly But Worse", \
        font=f"Times {fontSize} bold")
    drawButtons(app, canvas)

runApp(width=800, height=600)