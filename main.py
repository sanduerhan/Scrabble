import random
import tkinter as tk
import tkinter.simpledialog as tkSimpleDialog
from functools import partial
from tkinter import *
import sys

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
        self.frame2 = Frame(window, bg="#D8DBE2", width=500, height=600)
        self.frame2.grid(row=0, column=1)
        self.createBoard()
        self.createGame()

    def createGame(self):
        self.letters = Bag()
        self.player = 0
        self.mode = tkSimpleDialog.askinteger("Start the Game", "Introduce the mode: 0 - vsComputer, 1 - vs Player")

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


window = Tk()
window.title("Scrabble Game")
cri = Game(window)

# doubleLetter = ((0, 3), (0,11), (2,6), (2,8), (3,0), (3,7), (3,14), (6,2), (6,6), (6,8), (6,12), (7,3), (7,11), (8,2), (8,6), (8,8), (8, 12), (11,0), (11,7), (11,14), (12,6), (12,8), (14, 3), (14, 11))
# tripleWord = ((0,0), (7, 0), (14,0), (0, 7), (14, 7), (0, 14), (7, 14), (14,14))
# doubleWord = ((1,1), (2,2), (3,3), (4,4), (1, 13), (2, 12), (3, 11), (4, 10), (13, 1), (12, 2), (11, 3), (10, 4), (13,13), (12, 12), (11,11), (10,10))
# tripleLetter = ((1,5), (1, 9), (5,1), (5,5), (5,9), (5,13), (9,1), (9,5), (9,9), (9,13), (13, 5), (13,9))
