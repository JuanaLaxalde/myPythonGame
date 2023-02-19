# FAERY BINGO RULES:
# - You will be assigned a bingo board with random and unique content.
# - Balls will also be randomly generated. If they match the position of your board, they will be deleted.
# - Once you delete all the items in the board you will be assigned a prize.
# - You have 40 attempts to delete all items from your board.
# - You may exit the game before those 40 attempts are finished.
# - The prize will vary depending on how many faeries you have eliminated by the time you exit the game, or finish.

import random
import time

# STEP 1 - Setting up functions and format

characters = {1: "Faer", 2: "Yani", 3: "Bezo", 4: "Dasy", 5: "Lena",
              6: "Qige", 7: "Ezen"}


class Board:
    # Generate Random Placements
    def __init__(self):
        self.all_values = {}

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

    # Create __repr__ to print formatted table
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

    # Create function to eliminate faeries that have been selected by the ball
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

    # Create function to store resulting values into a dictionary
    def store_values(self):
        self.all_values = {"B": [self.b1, self.b2, self.b3],
                           "I": [self.i1, self.i2, self.i3],
                           "N": [self.n1, self.n2, self.n3],
                           "G": [self.g1, self.g2, self.g3],
                           "O": [self.o1, self.o2, self.o3]}
        return self.all_values


# Create Ball Roller
class NewBall():
    faeries = ["Faer", "Dasy", "Qige", "Ezen", "Lena", "Yani", "Bezo"]
    letters = ["B", "I", "N", "G", "O"]

    def __init__(self):
        self.name = random.choice(self.faeries)
        self.letter = random.choice(self.letters)

    def __repr__(self):
        return "Your new ball is: " + self.letter + " " + self.name


# Create prize-calculator
def calculate_guesses(dict):
    guessed = 0
    for i in dict.values():
        for j in i:
            if j == '----':
                guessed += 1
    return guessed


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
print("Hello " + username + "! These are the RULES of the game:")
print('')
print("1 - You get a maximum of 40 balls in your attempt to fill the board")
print("2 - To continue rolling you need to type 'ROLL'")
print("3 - If you want to stop before your 40 attempts finish, just type 'QUIT'")
print("4 - Your reward will depend on how many names you have eliminated from your board")
print('')
print("Type 'OK' to get started...")
start = input().upper()

if start == 'OK':
    print("We are creating your own personal bingo board")
    print('.')
    time.sleep(0.5)
    print('.')
    time.sleep(0.5)
    print('.')
    time.sleep(0.5)

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
# 5
count = 1
while count < 40 and play != 'QUIT':
    new_ball = NewBall()
    print(new_ball)
    new_board.__set__(new_ball.letter, new_ball.name)
    print("You have", 40 - count, "attempts left.")
    print("Type 'ROLL' to get another Faery Ball.  >>> or Type 'QUIT' to exit and claim reward:")
    play = input().upper()
    count += 1
# 7
if count == 40:
    print("You ran out of attempts, here are the results:")
print(new_board)
final_board = new_board.store_values()
print(final_board)
eliminated = calculate_guesses(final_board)
print("You just rolled", count, "times and guessed", eliminated, "out of 15")
