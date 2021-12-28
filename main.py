import random
import tkinter as tk
from tkinter import messagebox
from tkinter import *

x1 = -1
y1 = -1
x2 = -1
y2 = -1
e = 0
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
        self.oldWords = {}
        self.textsId = []
        self.texts2Id = []
        self.tilesOccupied = []
        self.lettersPlaced = []
        self.createBoard()
        self.createFrame()
        self.showOldWords()
        self.firstTurn = 1
        menubar = Menu(window)
        play = Menu(menubar, tearoff=0)
        play.add_command(label="vsComputer")
        play.add_command(label="vsPlayer", command=self.startGame)
        play.add_command(label="Exit", command=self.close)
        menubar.add_cascade(label="Play", menu=play)
        window.config(menu=menubar)

    def close(self):
        global e
        e = 1
        window.destroy()

    def startGame(self):
        self.getCoordinatesHand()
        self.getCoordinatesBoard()
        self.player1hand = self.letters.assign(7)
        self.player2hand = self.letters.assign(7)
        self.gamevsPlayer()

    def gamevsPlayer(self):
        self.lettersPlaced = []
        self.playOrder()
        # self.player == 2
        # while e != 1:
        # print("not here")
        if self.player == 1:
            self.displayTiles()
            self.displayTilesLeft()
            if x1 != -1 and y1 != -1:
                # print("get letter")
                letterToPlace = self.getLetter()
            if x2 != -1 and y2 != -1:
                tileX, tileY = self.getTile()
                self.tilesOccupied.append(tileX)
                self.tilesOccupied.append(tileY)
                self.placeLetter(tileX, tileY, letterToPlace, self.player)
            # self.player = 2
        elif self.player == 2:
            self.displayTiles(self.player)
            self.displayTilesLeft()
            # self.player = 1

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
        for word in self.oldWords:
            nr = tk.Label(self.canvas2, text=word, font="Helvetica 9", background="#D8DBE2")
            nr.place()
        self.canvas2.create_text((345, 150), text="Score player 1: ", font="Helvetica 12 bold")
        self.canvas2.create_text((345, 175), text="Score player 2 : ", font="Helvetica 12 bold")
        self.canvas2.create_text((345, 215), text="Tiles left : ", font="Helvetica 12 bold")
        self.canvas2.create_text((265, 300), text="Player's    turn", font="Helvetica 15 bold")
        for i in range(1, 8):
            self.canvas2.create_rectangle((80 + i * 40, 350, 120 + i * 40, 400), fill="white",
                                          outline="black")
        btn = tk.Button(self.canvas2, text="Play", bd='3', bg="#548C2F", width=10)
        btn.place(x=105, y=450)
        btn = tk.Button(self.canvas2, text="Pass", bd='3', bg="#F9A620", width=10, command=self.passTurn)
        btn.place(x=185, y=450)
        btn = tk.Button(self.canvas2, text="Undo", bd='3', bg="#F9A620", width=10, command=self.undoLetter)
        btn.place(x=265, y=450)
        btn = tk.Button(self.canvas2, text="Exchange", bd='3', bg="#F9A620", width=10, command=self.exchangeTiles)
        btn.place(x=345, y=450)

    def playOrder(self):
        nr = Label(self.canvas2, text=self.player, font="Helvetica 15 bold", background="#D8DBE2")
        nr.place(x=275, y=285)

    def displayTilesLeft(self):
        nr = Label(self.canvas2, text=len(self.letters.bag), font="Helvetica 15 bold", background="#D8DBE2")
        nr.place(x=400, y=200)

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

    def displayTiles(self):
        if self.player == 1:
            i = 0
            for letter in self.player1hand:
                self.textId = self.canvas2.create_text((140 + i * 40, 375), text=letter, font="Helvetica 11 bold")
                i += 1
                self.textsId.append(self.textId)
        if self.player == 2:
            i = 0
            for letter in self.player2hand:
                self.text2Id = self.canvas2.create_text((140 + i * 40, 375), text=letter, font="Helvetica 11 bold")
                i += 1
                self.texts2Id.append(self.text2Id)

    def hideTiles(self):
        if self.player == 1:
            for letter in self.player1hand:
                index = self.player1hand.index(letter)
                self.canvas2.delete(self.textsId[index])
        if self.player == 2:
            for letter in self.player2hand:
                index = self.player2hand.index(letter)
                self.canvas2.delete(self.texts2Id[index])

    def placeLetter(self, x, y, letter, player):
        item = self.canvas.create_text((24 + x * 28, 26 + y * 28), text=letter)
        self.lettersPlaced.append(item)
        print(self.lettersPlaced)
        if player == 1:
            index = self.player1hand.index(letter)
            self.canvas2.delete(self.textsId[index])
        if player == 2:
            index = self.player2hand.index(letter)
            self.canvas2.delete(self.textsId[index])

    def undoLetter(self):
        letterToUndo = self.lettersPlaced.pop()
        coordinates = self.canvas.coords(letterToUndo)
        x = round(coordinates[0])
        y = round(coordinates[1])
        self.canvas.delete(letterToUndo)
        self.displayTiles()

    def getLetterFromBoard(self, x, y):
        overlap = self.canvas.find_overlapping(10 + x * 28, 10 + y * 28, 38 + x * 28, 38 + y * 28)
        letter = self.canvas.itemcget(overlap[1], "text")

    def changePlayer(self):
        if self.player == 1:
            self.player = 2
        elif self.player == 2:
            self.player = 1

    def passTurn(self):
        self.hideTiles()
        self.reload()
        self.changePlayer()
        self.displayTiles()
        self.playOrder()
        self.displayTilesLeft()

    def exchangeTiles(self):
        if self.player == 1:
            self.hideTiles()
            self.player1hand = self.letters.assign(7)
            self.changePlayer()
            self.displayTiles()
            self.playOrder()
            self.displayTilesLeft()
        elif self.player == 2:
            self.hideTiles()
            self.player2hand = self.letters.assign(7)
            self.changePlayer()
            self.displayTiles()
            self.playOrder()
            self.displayTilesLeft()

    def reload(self):
        if self.player == 1:
            if 7 - len(self.player1hand) > len(self.letters.bag):
                new = self.letters.assign(len(self.letters.bag))
            else:
                new = self.letters.assign(7 - len(self.player1hand))
            for letter in new:
                self.player1hand.append(letter)
        if self.player == 2:
            if 7 - len(self.player2hand) > len(self.letters.bag):
                new = self.letters.assign(len(self.letters.bag))
            else:
                new = self.letters.assign(7 - len(self.player2hand))
            for letter in new:
                self.player2hand.append(letter)

    def validatePlay(self):
        words = self.getWordsBoard()
        for word in words:
            if word not in self.validWords:
                messagebox.showerror("Error", word + "not in dictionary")
                return False
        lastRound = {}
        for word in self.oldWords.keys():
            if word in words.keys():
                if self.oldWords[word] == words[word]:
                    lastRound[word] = words[word]
        for word in lastRound:
            if lastRound[word] == words[word]:
                words.pop(word)
        for word in words:
            for x_y in words[word]:
                if x_y == (7,7):
                    return True
                for oldWord in self.oldWords:
                    for x_y2 in self.oldWords[oldWord]:
                        if x_y == x_y2:
                            return True
        return False


    def getWordsBoard(self):
        words = []
        found = False
        for i in range(15):
            for j in range(15):
                if self.containsLetter(i, j):
                    dir = self.direction(i, j)
                    if dir == 2:
                        word = self.getLetterFromBoard(i, j).strip()
                        x_y = (i, j)
                        j2 = j
                        while found == False:
                            if j2 < 15:
                                if self.containsLetter(i, j2 + 1):
                                    word += self.getLetterFromBoard(i, j2 + 1).strip()
                                else:
                                    found = True
                                j2 += 1
                            elif j2 >= 15:
                                found = True
                        words[word] = x_y
                    if dir == 3:
                        word = self.getLetterFromBoard(i, j).strip()
                        x_y = (i,j)
                        i2 = i
                        while found == False:
                            if self.containsLetter(i2 + 1, j):
                                word += self.getLetterFromBoard(i2+1, j).strip()
                            else:
                                found = True
                            i2+=1
                        words[word] = x_y
        return words

    def direction(self, i, j):
        down = 0
        right = 0
        left = 0
        up = 0
        if i == 1 and j == 1:
            if self.containsLetter(i, j + 1):
                down = 1
            if self.containsLetter(i + 1, j):
                right = 1
        if self.containsLetter(i - 1, j):
            left = 1
        if self.containsLetter(i, j - 1):
            up = 1
        if left == 0 and up == 0:
            right = self.containsLetter(i + 1, j)
            down = self.containsLetter(i, j + 1)
        elif left == 0:
            right = self.containsLetter(i + 1, j)
        elif up == 0:
            down = self.containsLetter(i, j + 1)
        # if down == 1 and right == 1:
        # return 1
        if down == 1:
            return 2
        elif right == 1:
            return 3
        else:
            return 0

    def containsLetter(self, x, y):
        overlap = self.canvas.find_overlapping(10 + x * 28, 10 + y * 28, 38 + x * 28, 38 + y * 28)
        if len(overlap) > 1:
            letter = self.canvas.itemcget(overlap[1], "text")
            if letter == "Start":
                return False
            else:
                return True
        return False

    def display(self, eventorigin):
        global x1, y1
        x1 = eventorigin.x
        y1 = eventorigin.y
        print(x1, y1)

    def displayBoard(self, eventorigin):
        global x2, y2
        x2 = eventorigin.x
        y2 = eventorigin.y
        print(x2, y2)

    def getCoordinatesHand(self):
        self.canvas2.bind('<Button-1>', self.display)

    def getCoordinatesBoard(self):
        self.canvas.bind('<Button-1>', self.displayBoard)

    def getLetter(self):
        for i in range(1, 8):
            # print(x1,y1)
            if x1 > (80 + i * 40) and x1 < (120 + i * 40) and y1 > 350 and y1 < 400:
                # print("HEHEHE")
                return self.player1hand[i - 1]

    def getTile(self):
        for i in range(1, 16):
            for j in range(1, 16):
                # print("Salut")
                if x2 > (10 + i * 28) and x2 < (38 + i * 28) and y2 > (10 + j * 28) and y2 < (38 + j * 28):
                    return (i, j)


window = Tk()
window.title("Scrabble Game")
cri = Game(window)
window.mainloop()
