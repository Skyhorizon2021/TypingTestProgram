from tkinter import *
import random
import tkinter

# Setup
root = Tk()
root.title('Type Speed Test')

# Setting the starting window dimensions
root.geometry('1440x1080')

# Setting the Font for all Labels and Buttons
root.option_add("*Label.Font", "consolas 30")
root.option_add("*Button.Font", "consolas 30")

global totalTime
totalTime = 60000

def titleScreen():
    global titleLogo
    titleLogo = Label(root, text=f'Typing Test', fg='black')
    titleLogo.place(relx=0.5, rely=0.3, anchor=N)

    global modeSelection
    modeSelection = Label(root, text=f'Duration: {int(totalTime/1000)}', fg='black')
    modeSelection.place(relx=0.5, rely=0.4, anchor=N)

    global startTest
    startTest = Button(root, text=f'Start', command=resetWritingLabels)
    startTest.place(relx=0.5, rely=0.6, anchor=CENTER)

    global sixty
    sixty = Button(root, text=f'60 Secs', command=lambda: setTime(60000))
    sixty.place(relx=0.7, rely=0.7, anchor=W)

    global thirty
    thirty = Button(root, text=f'30 Secs', command=lambda: setTime(30000))
    thirty.place(relx=0.5, rely=0.7, anchor=CENTER)

    global fifteen
    fifteen = Button(root, text=f'15 Secs', command=lambda: setTime(15000))
    fifteen.place(relx=0.2, rely=0.7, anchor=W)


def setTime(time):
    global totalTime
    global modeSelection
    totalTime = time
    modeSelection.destroy()
    modeSelection = Label(root, text=f'Duration: {int(totalTime/1000)}', fg='black')
    modeSelection.place(relx=0.5, rely=0.4, anchor=N)


# Helper function
def resetWritingLabels():
    titleLogo.destroy()
    startTest.destroy()
    sixty.destroy()
    thirty.destroy()
    fifteen.destroy()
    modeSelection.destroy()
    # Text List
    word_list = [
        "mask", "delete", "bishop", "long", "leak", "escape", "colony", "raise", "remedy", "yearn",
        "cake", "shell", "ball", "stake", "menu", "mail", "hill", "prize", "am", "insist", "export",
        "beach", "ensure", "stain", "berry", "tent", "color", "tired", "easy", "helmet", "free",
        "carry", "fork", "future", "swarm", "remind", "fare", "inject", "output", "form", "rally",
        "pest", "video", "angel", "twin", "ladder", "sleep", "bury", "sharp", "lack", "gown", "black",
        "length", "center", "weapon", "aloof", "fail", "host", "union", "lay", "grain", "series",
        "person", "think", "use", "train", "slip", "trace", "shape", "money", "club", "whole",
        "drama", "thaw", "offset", "smell", "essay", "review", "horn", "grudge", "unlike", "member",
        "barrel", "light", "right", "favor", "rich", "drill", "regret", "fur", "will", "pass",
        "late", "turkey", "role", "throne", "settle", "sting", "tune", "preach",
        "island", "flow", "bind", "beat", "strike", "cotton", "weigh", "block", "ridge", "blade",
        "greet", "start", "rear", "occupy", "coffee", "effect", "quiet", "belly", "corpse", "bottom",
        "exotic", "mayor", "full", "light", "punch", "knock", "low", "death", "bacon", "riot", "poem",
        "image", "offend", "pace", "prison", "tent", "global", "grow", "misery", "tap", "upset", "trunk",
        "bolt", "basic", "slam", "snarl", "shiver", "good", "stride", "single"
    ]
    # Chosing one of the texts randomly with the choice function
    listCopy = word_list
    text = ""
    while listCopy:
        temp = random.choice(word_list)
        listCopy.remove(temp)
        text += temp
        text += " "

    # defining where the text is split
    splitPoint = 0
    # where the text is that has already been written
    global labelLeft
    labelLeft = Label(root, text=text[0:splitPoint], fg='grey')
    labelLeft.place(relx=0.5, rely=0.5, anchor=E)

    # text to be written
    global labelRight
    labelRight = Label(root, text=text[splitPoint:])
    labelRight.place(relx=0.5, rely=0.5, anchor=W)

    # shows the user which letter they are on
    global currentLetterLabel
    currentLetterLabel = Label(root, text=text[splitPoint], fg='grey')
    currentLetterLabel.place(relx=0.5, rely=0.6, anchor=N)

    # shows how much time has gone by
    global timeLeftLabel
    timeLeftLabel = Label(root, text=f'0 seconds', fg='grey')
    timeLeftLabel.place(relx=0.5, rely=0.4, anchor=S)

    global writeable
    writeable = True
    root.bind('<Key>', keyPress)

    global secondsPassed
    secondsPassed = 0

    root.after(totalTime, stopTest)
    root.after(1000, addSecond)


def stopTest():
    global writeable
    writeable = False

    # calculates amount of words typed
    amountWords = len(labelLeft.cget('text'))
    wpm = amountWords//5
    if totalTime == 15000:
        wpm *= 4
    elif totalTime == 30000:
        wpm *= 2

    timeLeftLabel.destroy()
    currentLetterLabel.destroy()
    labelRight.destroy()
    labelLeft.destroy()

    global resultLabel
    resultLabel = Label(root, text=f'Words per Minute: {wpm}', fg='black')
    resultLabel.place(relx=0.5, rely=0.4, anchor=CENTER)

    # button to restart
    global resultButton
    resultButton = Button(root, text=f'Retry', command=restart)
    resultButton.place(relx=0.5, rely=0.6, anchor=CENTER)


def restart():
    resultLabel.destroy()
    resultButton.destroy()

    titleScreen()


def addSecond():
    #bypass minor error
    try:
        global secondsPassed
        secondsPassed += 1
        timeLeftLabel.configure(text=f'{secondsPassed} Seconds')

        if writeable:
            root.after(1000, addSecond)
    except:
        pass


def keyPress(event=None):
    try:
        if event.char.lower() == labelRight.cget('text')[0].lower():
            # delete one from right side
            labelRight.configure(text=labelRight.cget('text')[1:])
            # delete from left side as well
            labelLeft.configure(text=labelLeft.cget('text') + event.char.lower())
            # set next letter
            currentLetterLabel.configure(text=labelRight.cget('text')[0])

    except tkinter.TclError:
        pass


titleScreen()

root.mainloop()
