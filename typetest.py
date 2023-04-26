#Name: Loc Nguyen, Colin McGough, Priyanshu 
#Date: 04/26/2023
'''Objective: Create a typing test program with Tkinter'''

import tkinter as tk,time,threading, random

#define graphical user interface
class TypingGUI:
    
    def __init__(self):
        #initilize the tK module
        self.root = tk.Tk()
        self.root.title("Typing Test")
        self.root.geometry("800X600")
        
        #open file containing text user have to type
        #we can have multiple textfile and randomize which one user have to type
        self.text = open("textfile.txt","r").read().split("\n")

        self.sample_label = tk.Label(self.root, text="Sample Text")
        pass