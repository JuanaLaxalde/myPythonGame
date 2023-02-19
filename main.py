# FAIRY BINGO RULES:
# - You will be assigned a bingo board
# - Possible board contents will be randomly generated
# - If that randomly generated response matches your board, it will be deleted
# - Once you delete all the items in the board you will be assigned a prize
# - The prize will vary depending on how many tries it took you to clear the board

# FAIRY CHARACTERS:
# Faer; Dasy; Qige; Ezen; Lena; Yani; Bezo

import random
import time

# STEP 1 - Setting up functions and format

board_example = """
*----------*----------*----------*----------*----------*
*    B     *    I     *    N     *    G     *    O     *
*----------*----------*----------*----------*----------*
*   Faer   *   Dasy   *   Qige   *   Ezen   *   Bezo   *
*----------*----------*----------*----------*----------*
*   Yani   *   Lena   *   Yani   *   Dasy   *   Qige   *
*----------*----------*----------*----------*----------*
*   Bezo   *   Qige   *   Ezen   *   Faer   *   Yani   *
*----------*----------*----------*----------*----------*
"""

characters = {1: "Faer", 2: "Yani", 3: "Bezo", 4: "Dasy", 5: "Lena",
              6: "Qige", 7: "Ezen"}


class Board:
    # Generate Random Placements
    def __init__(self):
        self.b1 = random.choice(list(characters.values()))
        self.b2 = random.choice(list(characters.values()))
        self.b3 = random.choice(list(characters.values()))

        self.i1 = random.choice(list(characters.values()))
        self.i2 = random.choice(list(characters.values()))
        self.i3 = random.choice(list(characters.values()))

        self.n1 = random.choice(list(characters.values()))
        self.n2 = random.choice(list(characters.values()))
        self.n3 = random.choice(list(characters.values()))

        self.g1 = random.choice(list(characters.values()))
        self.g2 = random.choice(list(characters.values()))
        self.g3 = random.choice(list(characters.values()))

        self.o1 = random.choice(list(characters.values()))
        self.o2 = random.choice(list(characters.values()))
        self.o3 = random.choice(list(characters.values()))

    def __repr__(self):
        print("*----------*----------*----------*----------*----------*")
        print("*    B     *    I     *    N     *    G     *    O     *")
        print("*----------*----------*----------*----------*----------*")
        print(
            "*   " + self.b1 + "   *   " + self.i1 + "   *   " + self.n1 + "   *   " + self.g1 + "   *   " + self.o1 + "   *")
        print("*----------*----------*----------*----------*----------*")
        print(
            "*   " + self.b2 + "   *   " + self.i2 + "   *   " + self.n2 + "   *   " + self.g2 + "   *   " + self.o2 + "   *")
        print("*----------*----------*----------*----------*----------*")
        print(
            "*   " + self.b3 + "   *   " + self.i3 + "   *   " + self.n3 + "   *   " + self.g3 + "   *   " + self.o3 + "   *")
        print("*----------*----------*----------*----------*----------*")
        return " "

    def __set__(self, letter, name):
        if letter == 'B':
            if self.b1 == name:
                self.b1 = '----'
                print("YOU GOT IT! Here's your updated board:")
                print(new_board)
            elif self.b2 == name:
                self.b2 = '----'
                print("YOU GOT IT! Here's your updated board:")
                print(new_board)
            elif self.b3 == name:
                self.b3 = '----'
                print("YOU GOT IT! Here's your updated board:")
                print(new_board)

        elif letter == 'I':
            if self.i1 == name:
                self.i1 = '----'
                print("YOU GOT IT! Here's your updated board:")
                print(new_board)
            elif self.i2 == name:
                self.i2 = '----'
                print("YOU GOT IT! Here's your updated board:")
                print(new_board)
            elif self.i3 == name:
                self.i3 = '----'
                print("YOU GOT IT! Here's your updated board:")
                print(new_board)

        elif letter == 'N':
            if self.n1 == name:
                self.n1 = '----'
                print("YOU GOT IT! Here's your updated board:")
                print(new_board)
            elif self.n2 == name:
                self.n2 = '----'
                print("YOU GOT IT! Here's your updated board:")
                print(new_board)
            elif self.n3 == name:
                self.n3 = '----'
                print("YOU GOT IT! Here's your updated board:")
                print(new_board)

        elif letter == 'G':
            if self.g1 == name:
                self.g1 = '----'
                print("YOU GOT IT! Here's your updated board:")
                print(new_board)
            elif self.g2 == name:
                self.g2 = '----'
                print("YOU GOT IT! Here's your updated board:")
                print(new_board)
            elif self.g3 == name:
                self.g3 = '----'
                print("YOU GOT IT! Here's your updated board:")
                print(new_board)

        elif letter == 'O':
            if self.o1 == name:
                self.o1 = '----'
                print("YOU GOT IT! Here's your updated board:")
                print(new_board)
            elif self.o2 == name:
                self.o2 = '----'
                print("YOU GOT IT! Here's your updated board:")
                print(new_board)
            elif self.o3 == name:
                self.o3 = '----'
                print("YOU GOT IT! Here's your updated board:")
                print(new_board)


class NewBall():
    faeries = ["Faer", "Dasy", "Qige", "Ezen", "Lena", "Yani", "Bezo"]
    letters = ["B", "I", "N", "G", "O"]

    def __init__(self):
        self.name = random.choice(self.faeries)
        self.letter = random.choice(self.letters)

    def __repr__(self):
        return "Your new ball is: " + self.letter + " " + self.name


# STEP 2 - Create interaction with player

# 0
print("""
************************************
WELCOME TO THE FANTASTIC FAERY BINGO
************************************

   _   vvvvvvvvv   _
  ( `-._\...../_.-' )
   \   ((('_')))   /
    )   ))) (((   (
   (   ((( v )))   )
    )`--' )X( `-._(
   /   _./   \._   \\
  /  .' /     \ `.  \\
 (__/  /       \  \\__)
 
*A fairy princess by Joan Stark*
 """)
# 1
print("Please enter your desired USERNAME:")
username = input()
# 2
print("Hello " + username + "! We are creating your own personal bingo board")
time.sleep(2)

# 3
print("""
Let's get started with the Faery Bingo
    
HERE IS YOUR BRAND NEW BINGO BOARD: """)
new_board = Board()
print(new_board)
# 4
print("""
Whenever you're ready, type 'ROLL' to get a Faery Ball and start completing your board""")
play = input().upper()

count = 0
while play == 'ROLL':
    new_ball = NewBall()
    print(new_ball)
    new_board.__set__(new_ball.letter, new_ball.name)
    print("Type 'ROLL' to get another Faery Ball.  >>> or Type 'DONE' once your board is complete:")
    play = input().upper()
    count += 1

print(new_board)
print("CONGRATULATIONS, YOU COMPLETED THE BOARD")
print("It took you", count, "guesses to win the game")

