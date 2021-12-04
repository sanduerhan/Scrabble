import random
import tkinter
from functools import partial
from tkinter import *
import sys

letterScores = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
letterDistribution = [9, 2, 2, 4, 12, 2, 3, 2, 9, 1, 1, 4, 2, 6, 8, 2, 1, 6, 4, 6, 4, 2, 2, 1, 2, 1]
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
           "W", "X", "Y", "Z"]
choosed = False
selectedX = -1
selectedY = -1
bag = [None] * 98
doubleLetter = ((0, 3), (0,11), (2,6), (2,8), (3,0), (3,7), (3,14), (6,2), (6,6), (6,8), (6,12), (7,3), (7,11), (8,2), (8,6), (8,8), (8, 12), (11,0), (11,7), (11,14), (12,6), (12,8), (14, 3), (14, 11))
tripleWord = ((0,0), (7, 0), (14,0), (0, 7), (14, 7), (0, 14), (7, 14), (14,14))
doubleWord = ((1,1), (2,2), (3,3), (4,4), (1, 13), (2, 12), (3, 11), (4, 10), (13, 1), (12, 2), (11, 3), (10, 4), (13,13), (12, 12), (11,11), (10,10))
tripleLetter = ((1,5), (1, 9), (5,1), (5,5), (5,9), (5,13), (9,1), (9,5), (9,9), (9,13), (13, 5), (13,9))

dictionary = sys.argv[1]


def createBag():  # creaza cele 98 de litere
    global bag
    k = 0
    for i in range(26):
        for j in range(letterDistribution[i]):
            bag[k] = letters[i]
            k += 1


def assign(n):
    temp = [None] * n
    choice = random.sample(range(0, 98), n)
    for i in range(0, n):
        temp[i] = bag[choice[i]]
    return temp


createBag()
print(assign(7))

def wordScore(word):
    score = 0
    for letter in word:
        score += letterScores[letters.index(letter)]

def drawMenu(window):
    window.geometry("600x600")
    window.config(bg='#f2e9e4')
    label = Label(window, text="Welcome to Scrabble", bg='#f2e9e4', pady=50)
    label.pack()
    option1 = Button(window, text='vs Player', bg='#c9ada7', command=vsPlayer)
    option1.place(x=270, y=200)
    option2 = Button(window, text='vs Computer', bg='#c9ada7', command=vsComputer)
    option2.place(x=260, y=250)
    window.mainloop()


def buttonSelect(i, j):
    global choosed, selectedX, selectedY
    choosed = True
    selectedX = i
    selectedY = j

# def drawBoard():
#   tiles = [None] * 225
#   for i in range(15):
#       tiles.append([])
#       for j in range(15):
#           tiles.append(Button(window, width=1, height=1, bg='green', highlightbackground="black",
#                              borderwidth=0, activebackground="green", command=partial(buttonSelect,i,j)))


# def vsPlayer():
# drawBoard()


# def vsComputer():
# drawBoard()


# window = Tk()
# window.title("Scrabble Game")
# drawMenu(window)
