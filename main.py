import random
import tkinter as tk
import tkinter.simpledialog as tkSimpleDialog
from functools import partial
from tkinter import *
import sys
x1 = -1
y1 = -1
x2 = -1
y2 = -1
letterScores = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
letterDistribution = [9, 2, 2, 4, 12, 2, 3, 2, 9, 1, 1, 4, 2, 6, 8, 2, 1, 6, 4, 6, 4, 2, 2, 1, 2, 1]
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
           "W", "X", "Y", "Z"]


class Bag(object):
    def __init__(self):
        self.bag = []

    def createBag(self):  # creaza cele 98 de litere
        # k = 0
        for i in range(26):
            for j in range(letterDistribution[i]):
                self.bag.append(letters[i])
                # k += 1

    def assign(self, tiles):
        tilesDrawn = []
        for i in range(0, tiles):
            number = random.randint(0, len(self.bag) - 1)
            tile = self.bag.pop(number)
            tilesDrawn.append(tile)
        return tilesDrawn

    def exchange(self, tile):
        self.bag.append(tile)


class Game:
    def __init__(self, window):
        self.scores = letterScores
        Dict = open("dictionary.txt")
        self.validWords = []
        for word in Dict:
            self.validWords.append(word.strip())
        self.canvas = Canvas(window, bg="#A9BCD0", width=500, height=600)
        self.canvas.grid(row=0, column=0)
        self.canvas2 = Canvas(window, bg="#D8DBE2", width=500, height=600)
        self.canvas2.grid(row=0, column=1)
        self.letters = Bag()
        self.letters.createBag()
        self.player = 1
        self.player1hand = self.letters.assign(7)
        self.player2hand = self.letters.assign(7)
        self.oldWords = []
        #self.createGame()
        #if self.mode == 0 or self.mode == 1:
        self.createBoard()
        self.createFrame()
        self.showOldWords()
        menubar = Menu(window)
        play = Menu(menubar, tearoff=0)
        play.add_command(label="vsComputer")
        play.add_command(label="vsPlayer",command=self.createGamevsPlayer)
        play.add_command(label="Exit", command=window.destroy)
        menubar.add_cascade(label="Play", menu=play)
        window.config(menu=menubar)
        self.getCoordinatesBoard()

    def createGamevsPlayer(self):
        if self.player ==1:
            print("heyhey")
            self.displayTiles(self.player)
        elif self.player ==2:
            self.displayTiles(self.player)

    def createBoard(self):
        for i in range(1, 16):
            for j in range(1, 16):
                if i == 8 and j == 8:
                    self.canvas.create_rectangle((10 + i * 28, 10 + j * 28, 38 + i * 28, 38 + j * 28), fill="#E4DFDA")
                    self.canvas.create_text((248, 250), text="Start")
                elif i == 1 and j == 1 or i == 8 and j == 1 or i == 15 and j == 1 or i == 1 and j == 8 or i == 15 and j == 8 or i == 1 and j == 15 or i == 8 and j == 15 or i == 15 and j == 15:
                    self.canvas.create_rectangle((10 + i * 28, 10 + j * 28, 38 + i * 28, 38 + j * 28), fill="#C75146")
                elif i == 2 and j == 2 or i == 3 and j == 3 or i == 4 and j == 4 or i == 5 and j == 5 or i == 2 and j == 14 or i == 3 and j == 13 or i == 4 and j == 12 or i == 5 and j == 11 or i == 14 and j == 2 or i == 13 and j == 3 or i == 12 and j == 4 or i == 11 and j == 5 or i == 14 and j == 14 or i == 13 and j == 13 or i == 12 and j == 12 or i == 11 and j == 11:
                    self.canvas.create_rectangle((10 + i * 28, 10 + j * 28, 38 + i * 28, 38 + j * 28), fill="#DEA47E")
                elif i == 1 and j == 4 or i == 1 and j == 12 or i == 3 and j == 7 or i == 3 and j == 9 or i == 4 and j == 1 or i == 4 and j == 8 or i == 4 and j == 15 or i == 7 and j == 3 or i == 7 and j == 7 or i == 7 and j == 9 or i == 7 and j == 13 or i == 8 and j == 4 or i == 8 and j == 12 or i == 9 and j == 3 or i == 9 and j == 7 or i == 9 and j == 9 or i == 9 and j == 13 or i == 12 and j == 1 or i == 12 and j == 8 or i == 12 and j == 15 or i == 13 and j == 7 or i == 13 and j == 9 or i == 15 and j == 4 or i == 15 and j == 12:
                    self.canvas.create_rectangle((10 + i * 28, 10 + j * 28, 38 + i * 28, 38 + j * 28), fill="#77A6B6")
                elif i == 2 and j == 6 or i == 2 and j == 10 or i == 6 and j == 2 or i == 6 and j == 6 or i == 6 and j == 10 or i == 6 and j == 14 or i == 10 and j == 2 or i == 10 and j == 6 or i == 10 and j == 10 or i == 10 and j == 14 or i == 14 and j == 6 or i == 14 and j == 10:
                    self.canvas.create_rectangle((10 + i * 28, 10 + j * 28, 38 + i * 28, 38 + j * 28), fill="#4D7298")
                else:
                    self.canvas.create_rectangle((10 + i * 28, 10 + j * 28, 38 + i * 28, 38 + j * 28), fill="#E4DFDA")
        self.canvas.create_rectangle((25, 475, 50, 500), fill="#C75146")
        self.canvas.create_text((100, 485), text="Triple Word")
        self.canvas.create_rectangle((25, 500, 50, 525), fill="#DEA47E")
        self.canvas.create_text((100, 510), text="Double Word")
        self.canvas.create_rectangle((25, 525, 50, 550), fill="#77A6B6")
        self.canvas.create_text((100, 535), text="Double Letter")
        self.canvas.create_rectangle((25, 550, 50, 575), fill="#4D7298")
        self.canvas.create_text((100, 560), text="Triple Letter")

    def createFrame(self):
        self.canvas2.create_text((80, 40), text="Words used in game: ", font="Helvetica 11 ")
        i = 0
        for word in self.oldWords:
            nr = tk.Label(self.canvas2, text=word, font="Helvetica 9", background="#D8DBE2")
            nr.place()
        self.canvas2.create_text((345, 150), text="Score player 1: ", font="Helvetica 12 bold")
        self.canvas2.create_text((345, 175), text="Score player 2 : ", font="Helvetica 12 bold")
        self.canvas2.create_text((345, 215), text="Tiles left : ", font="Helvetica 12 bold")
        nr = Label(self.canvas2, text=len(self.letters.bag), font="Helvetica 15 bold", background="#D8DBE2")
        nr.place(x=400, y=200)
        self.canvas2.create_text((265, 300), text="Player's    turn", font="Helvetica 15 bold")
        nr = Label(self.canvas2, text=self.player, font="Helvetica 15 bold", background="#D8DBE2")
        nr.place(x=275, y=285)
        for i in range(1, 8):
            self.canvas2.create_rectangle((80 + i * 40, 350, 120 + i * 40, 400), fill="white",
                                          outline="black")
        btn = tk.Button(self.canvas2, text="Play", bd='3', bg="#548C2F", width=10)
        btn.place(x=105, y=450)
        btn = tk.Button(self.canvas2, text="Pass", bd='3', bg="#F9A620", width=10)
        btn.place(x=185, y=450)
        btn = tk.Button(self.canvas2, text="Undo", bd='3', bg="#F9A620", width=10)
        btn.place(x=265, y=450)
        btn = tk.Button(self.canvas2, text="Exchange", bd='3', bg="#F9A620", width=10)
        btn.place(x=345, y=450)

    def showOldWords(self):
        self.canvas2.create_text((80, 40), text="Words used in game: ", font="Helvetica 11 ")
        i = 0
        j = 0
        for word in self.oldWords:
            nr = tk.Label(self.canvas2, text=word, font="Helvetica 8", background="#D8DBE2")
            if i <= 15:
                nr.place(x=5, y=50 + i * 15)
                i += 1
            else:
                nr.place(x=45, y=50 + j * 15)
                j += 1

    def displayTiles(self, player):
        if player == 1:
            i = 0
            for letter in self.player1hand:
                self.canvas2.create_text((140 + i * 40, 375), text=letter, font="Helvetica 11 bold")
                i += 1
        if player == 2:
            i = 0
            for letter in self.player2hand:
                self.canvas2.create_text((140 + i * 40, 375), text=letter, font="Helvetica 11 bold")
                i += 1

    def display(self, eventorigin):
        global x1,y1
        x1 = eventorigin.x
        y1 = eventorigin.y
        #print(x, y)

    def displayBoard(self, eventorigin):
        global x2,y2
        x2 = eventorigin.x
        y2 = eventorigin.y

    def getCoordinatesHand(self):
        self.canvas2.bind('<Button-1>', self.display)
    def getCoordinatesBoard(self):
        self.canvas.bind('<Button-1>', self.displayBoard)
    #def getLetter(self):



window = Tk()
window.title("Scrabble Game")
cri = Game(window)
window.mainloop()