import random
import tkinter as tk
from tkinter import messagebox
from tkinter import *

x1 = -1
y1 = -1
x2 = -1
y2 = -1
start = 0
LETTER_VALUES = {"A": 1,
                 "B": 3,
                 "C": 3,
                 "D": 2,
                 "E": 1,
                 "F": 4,
                 "G": 2,
                 "H": 4,
                 "I": 1,
                 "J": 1,
                 "K": 5,
                 "L": 1,
                 "M": 3,
                 "N": 1,
                 "O": 1,
                 "P": 3,
                 "Q": 10,
                 "R": 1,
                 "S": 1,
                 "T": 1,
                 "U": 1,
                 "V": 4,
                 "W": 4,
                 "X": 8,
                 "Y": 4,
                 "Z": 10}
TRIPLE_WORD_SCORE = ((1,1), (8, 1), (15,1), (1, 8), (15, 8), (1, 15), (8, 15), (15,15))
DOUBLE_WORD_SCORE = ((2,2), (3,3), (4,4), (5,5), (2, 14), (3, 13), (4, 12), (5, 11), (14, 2), (13, 3), (12, 4), (11, 5), (14,14), (13, 13), (12,12), (11,11))
TRIPLE_LETTER_SCORE = ((2,6), (2, 10), (6,2), (6,6), (6,10), (6,14), (10,2), (10,6), (10,10), (10,14), (14, 6), (14,10))
DOUBLE_LETTER_SCORE = ((1, 4), (1,12), (3,7), (3,9), (4,1), (4,8), (4,15), (7,3), (7,7), (7,9), (7,13), (8,4), (8,12), (9,3), (9,7), (9,9), (9, 13), (12,1), (12,8), (12,15), (13,7), (13,9), (15, 4), (15, 12))
play = True
endTurn = False
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
        self.player1score = 0
        self.player2score = 0
        self.oldWords = {}
        self.textsId = []
        self.texts2Id = []
        self.words = {}
        self.board = [[None for x in range(15)] for y in range(15)]
        self.tilesOccupied = []
        self.lettersPlaced = []
        self.createBoard()
        self.createFrame()
        self.showOldWords()
        self.firstTurn = 1
        self.letterThisTurn = []
        self.letterToPlace = ''
        self.getCoordinatesHand()
        self.getCoordinatesBoard()
        self.started = 0
        self.word = ''
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
        self.started = 1
        self.player1hand = self.letters.assign(7)
        self.player2hand = self.letters.assign(7)
        self.displayTiles()
        self.gamevsPlayer()



    def createBoard(self):
        global start
        for i in range(1, 16):
            for j in range(1, 16):
                if i == 8 and j == 8:
                    self.canvas.create_rectangle((10 + i * 28, 10 + j * 28, 38 + i * 28, 38 + j * 28), fill="#E4DFDA")
                    start = self.canvas.create_text((248, 250), text="Start")
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
        btn = tk.Button(self.canvas2, text="Play", bd='3', bg="#548C2F", width=10, command=self.playTurn)
        btn.place(x=105, y=450)
        btn = tk.Button(self.canvas2, text="Pass", bd='3', bg="#F9A620", width=10, command=self.passTurn)
        btn.place(x=185, y=450)
        btn = tk.Button(self.canvas2, text="Undo", bd='3', bg="#F9A620", width=10, command=self.undoLetter)
        btn.place(x=265, y=450)
        btn = tk.Button(self.canvas2, text="Exchange", bd='3', bg="#F9A620", width=10, command=self.exchangeTiles)
        btn.place(x=345, y=450)

    def gamevsPlayer(self):
        self.playOrder()
        self.displayScores()
        if self.player == 1:
            endTurn = False
            self.displayTilesLeft()
            if x1 != -1 and y1 != -1 and self.started == 1:
                self.letterToPlace = self.getLetter()
                self.letterThisTurn.append(self.letterToPlace)
                #print(self.letterToPlace)
            if x2 != -1 and y2 != -1 and self.started == 1:
                tileX, tileY = self.getTile()
                #print(tileX,tileY)
                thisTuple = (tileX,tileY)
                if thisTuple not in self.tilesOccupied:
                    self.tilesOccupied.append(thisTuple)
                    self.placeLetter(tileX, tileY, self.letterToPlace, self.player)
            if endTurn == True:
                #print("Endturn")
                self.changePlayer()
        elif self.player == 2:
            endTurn = False
            self.displayTilesLeft()
            if x1 != -1 and y1 != -1 and self.started == 1:
                #print("here")
                self.letterToPlace = self.getLetter()
                self.letterThisTurn.append(self.letterToPlace)
                #print(self.letterToPlace)
            if x2 != -1 and y2 != -1 and self.started == 1:
                tileX, tileY = self.getTile()
                thisTuple = (tileX, tileY)
                if thisTuple not in self.tilesOccupied:
                    self.tilesOccupied.append(thisTuple)
                    self.placeLetter(tileX, tileY, self.letterToPlace, self.player)
            if endTurn == True:
                self.changePlayer()
        window.after(10,self.gamevsPlayer)

    def displayScores(self):
        nr = Label(self.canvas2, text=self.player1score, font="Helvetica 15 bold", background="#D8DBE2")
        nr.place(x=400, y=135)
        nr = Label(self.canvas2, text=self.player2score, font="Helvetica 15 bold", background="#D8DBE2")
        nr.place(x=400, y=160)


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
        self.textsId.clear()
        self.texts2Id.clear()
        if self.player == 1:
            i = 0
            for letter in self.player1hand:
                textId = self.canvas2.create_text((140 + i * 40, 375), text=letter, font="Helvetica 11 bold")
                i += 1
                self.textsId.append(textId)
        if self.player == 2:
            i = 0
            for letter in self.player2hand:
                text2Id = self.canvas2.create_text((140 + i * 40, 375), text=letter, font="Helvetica 11 bold")
                i += 1
                self.texts2Id.append(text2Id)

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
        self.board[x-1][y-1] = letter
        if x == 8 and y == 8:
            self.canvas.delete(start)
        if player == 1:
            index = self.player1hand.index(letter)
            self.canvas2.delete(self.textsId[index])
        elif player == 2:
            index = self.player2hand.index(letter)
            self.canvas2.delete(self.texts2Id[index])

    def undoLetter(self):
        letterToUndo = self.lettersPlaced.pop()
        coordinates = self.canvas.coords(letterToUndo)
        #print(letterToUndo)
        x = round(coordinates[0])
        y = round(coordinates[1])
        self.canvas.delete(letterToUndo)
        self.displayTiles()

    def playTurn(self):
        global endTurn
        self.validatePlay()
        self.calculateWordScore()
        endTurn = True
        self.reload()
        print(self.player1hand)
        self.hideTiles()
        self.changePlayer()
        self.displayTiles()
        self.playOrder()
        self.displayTilesLeft()

    def changePlayer(self):
        if self.player == 1:
            self.player = 2
        elif self.player == 2:
            self.player = 1

    def passTurn(self):
        global endTurn
        self.hideTiles()
        self.reload()
        endTurn = True
        self.changePlayer()
        self.displayTiles()
        self.playOrder()
        self.displayTilesLeft()

    def exchangeTiles(self):
        global endTurn
        if self.player == 1:
            self.hideTiles()
            self.player1hand = self.letters.assign(7)
            endTurn = True
            self.changePlayer()
            self.displayTiles()
            self.playOrder()
            self.displayTilesLeft()
        elif self.player == 2:
            self.hideTiles()
            self.player2hand = self.letters.assign(7)
            endTurn = True
            self.changePlayer()
            self.displayTiles()
            self.playOrder()
            self.displayTilesLeft()

    def reload(self):

        if self.player == 1:
            self.player1hand = [e for e in self.player1hand if e not in self.letterThisTurn]
            if 7 - len(self.player1hand) > len(self.letters.bag):
                new = self.letters.assign(len(self.letters.bag))
            else:
                new = self.letters.assign(7 - len(self.player1hand))
            for letter in new:
                self.player1hand.append(letter)
        elif self.player == 2:
            self.player2hand = [e for e in self.player2hand if e not in self.letterThisTurn]
            if 7 - len(self.player2hand) > len(self.letters.bag):
                new = self.letters.assign(len(self.letters.bag))
            else:
                new = self.letters.assign(7 - len(self.player2hand))
            for letter in new:
                self.player2hand.append(letter)
        self.letterThisTurn.clear()

    def validatePlay(self):
        self.words = self.getWordsBoard()
        beginning = []
        end = []
        if self.firstTurn == 1:
            beginning.append(self.words[self.word][1])
            beginning.append(self.words[self.word][2])
            end.append(self.words[self.word][3])
            end.append(self.words[self.word][4])
            if beginning[0] > 8 or end[0] < 8:
                messagebox.showerror("Error", "First play should be in center")
                self.firstTurn = 0
        for word in self.words:
            if word not in self.validWords:
                messagebox.showerror("Error", word + " not in dictionary")
                return False
        lastRound = {}
        for word in self.oldWords.keys():
            if word in self.words.keys():
                if self.oldWords[word] == self.words[word]:
                    lastRound[word] = self.words[word]
        for word in lastRound:
            if lastRound[word] == self.words[word]:
                self.words.pop(word)
        for word in self.words:
            for x_y in self.words[word]:
                if x_y == (7, 7):
                    return True
                for oldWord in self.oldWords:
                    for x_y2 in self.oldWords[oldWord]:
                        if x_y == x_y2:
                            return True
        return False

    def getWordsBoard(self):
        found = False
        for i in range(15):
            for j in range(15):
                if self.board[i][j] != None:
                    dir = self.direction(i, j)
                    if dir == 2:
                        #print("Is it down?")
                        self.word = self.board[i][j].strip()
                        x_y = [dir,j+1, i+1]
                        j2 = j
                        while found == False:
                            if self.board[i][j2+1] != None:
                                self.word += self.board[i][j2+1].strip()
                            else:
                                found = True
                                x_y.append(j2+1)
                                x_y.append(i+1)
                            j2 += 1
                        self.words[self.word] = x_y
                    if dir == 3:
                        self.word = self.board[i][j].strip()
                        #print("Aici ai venit?")
                        x_y = [dir,j+1, i+1]
                        i2 = i
                        while found == False:
                            if self.board[i2+1][j]!= None:
                                self.word += self.board[i2+1][j].strip()
                            else:
                                found = True
                                x_y.append(j+1)
                                x_y.append(i2+1)
                            i2 += 1
                        self.words[self.word] = x_y
        #print(self.words)
        return self.words



    def direction(self, i, j):
        down = 0
        right = 0
        left = 0
        up = 0
        if i == 1 and j == 1:
            if self.board[i][j+1] != None:
                down = 1
            if self.board[i + 1][j] != None:
                right = 1
        if self.board[i-1][j] != None:
            left = 1
        if self.board[i][j-1] != None:
            up = 1
        if left == 0 and up == 0:
            if self.board[i+1][j] != None:
                right = 1
            if self.board[i][j+1] != None:
                down = 1
        elif left == 0:
            if self.board[i+1][j] != None:
                right = 1
        elif up == 0:
            if self.board[i][j + 1] != None:
                down = 1
        # if down == 1 and right == 1:
        # return 1
        if down == 1:
            return 2
        elif right == 1:
            return 3
        else:
            return 0

    def calculateWordScore(self):
        if self.word not in self.oldWords:
            wordScore = 0
            beginning = []
            end = []
            double,triple = 0,0
            beginning.append(self.words[self.word][1])
            beginning.append(self.words[self.word][2])
            end.append(self.words[self.word][3])
            end.append(self.words[self.word][4])
            direction = self.words[self.word][0]
            for letter in self.word:
                if direction == 2:
                    if tuple(beginning) in DOUBLE_LETTER_SCORE:

                        wordScore += LETTER_VALUES[letter]*2
                    elif tuple(beginning) in TRIPLE_LETTER_SCORE:
                        wordScore += LETTER_VALUES[letter]*3
                    elif tuple(beginning) in DOUBLE_WORD_SCORE:
                        double = 1
                    elif tuple(beginning) in TRIPLE_WORD_SCORE:
                        triple = 1
                    else:
                        wordScore+= LETTER_VALUES[letter]
                    beginning[0] = beginning[0]+1
                elif direction == 3:
                    if tuple(beginning) in DOUBLE_LETTER_SCORE:
                        wordScore += LETTER_VALUES[letter]*2
                    elif tuple(beginning) in TRIPLE_LETTER_SCORE:
                        wordScore += LETTER_VALUES[letter]*3
                    elif tuple(beginning) in DOUBLE_WORD_SCORE:
                        double = 1
                    elif tuple(beginning) in TRIPLE_WORD_SCORE:
                        triple = 1
                    else:
                        wordScore += LETTER_VALUES[letter]
                    beginning[1] = beginning[1]+1
            if double == 1:
                wordScore *= 2
            elif triple == 1:
                wordScore *= 3
        if self.player == 1:
            self.player1score+= wordScore
        elif self.player == 2:
            self.player2score+= wordScore
        return wordScore

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
            if x1 > (80 + i * 40) and x1 < (120 + i * 40) and y1 > 350 and y1 < 400:
                return self.player1hand[i - 1]

    def getTile(self):
        for i in range(1, 16):
            for j in range(1, 16):
                if x2 > (10 + i * 28) and x2 < (38 + i * 28) and y2 > (10 + j * 28) and y2 < (38 + j * 28):
                    return (i, j)


window = Tk()
window.title("Scrabble Game")
cri = Game(window)
window.mainloop()
