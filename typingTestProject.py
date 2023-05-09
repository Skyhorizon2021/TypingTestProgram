from tkinter import *
import random
import tkinter

# Setup
root = Tk()
root.title('Type Speed Test')

# Setting the starting window dimensions
root.geometry('700x700')

# Setting the Font for all Labels and Buttons
root.option_add("*Label.Font", "consolas 30")
root.option_add("*Button.Font", "consolas 30")


# Helper function
def resetWritingLabels():
    # Text List
    possibleTexts = [
        'No matter how hard he tried, he could not give her a good explanation about what had happened. It did not even really make sense to him. All he knew was that he froze at the moment and no matter how hard he tried to react, nothing in his body allowed him to move. It was as if he had instantly become a statue and although he could see what was taking place, he could not move to intervene. He knew that was not a satisfactory explanation even though it was the truth.',
    ]
    # Chosing one of the texts randomly with the choice function
    text = random.choice(possibleTexts).lower()

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

    root.after(60000, stopTest)
    root.after(1000, addSecond)


def stopTest():
    global writeable
    writeable = False

    # calculates amount of words typed
    amountWords = len(labelLeft.cget('text').split(' '))

    timeLeftLabel.destroy()
    currentLetterLabel.destroy()
    labelRight.destroy()
    labelLeft.destroy()

    global resultLabel
    resultLabel = Label(root, text=f'Words per Minute: {amountWords}', fg='black')
    resultLabel.place(relx=0.5, rely=0.4, anchor=CENTER)

    # button to restart
    global resultButton
    resultButton = Button(root, text=f'Retry', command=restart)
    resultButton.place(relx=0.5, rely=0.6, anchor=CENTER)


def restart():
    resultLabel.destroy()
    resultButton.destroy()

    resetWritingLabels()


def addSecond():
    global secondsPassed
    secondsPassed += 1
    timeLeftLabel.configure(text=f'{secondsPassed} Seconds')

    if writeable:
        root.after(1000, addSecond)


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


resetWritingLabels()

root.mainloop()
