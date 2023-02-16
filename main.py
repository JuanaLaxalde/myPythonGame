# FAIRY BINGO RULES:
# - You will be assigned a bingo board
# - Possible board contents will be randomly generated
# - If that randomly generated response matches your board, it will be deleted
# - Once you delete all the items in the board you will be assigned a prize
# - The prize will vary depending on how many tries it took you to clear the board

# FAIRY CHARACTERS:
# Faer; Dasy; Qige; Ezen; Lena; Yani; Bezo

import random

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

        # Format Bingo Table
        self.line_1 = "*----------*----------*----------*----------*----------*"
        self.line_2 = "*    B     *    I     *    N     *    G     *    O     *"
        self.line_3 = "*----------*----------*----------*----------*----------*"
        self.line_4 = "*   {B1}   *   {I1}   *   {N1}   *   {G1}   *   {O1}   *".format(B1=self.b1, I1=self.i1,
                                                                                        N1=self.n1, G1=self.g1,
                                                                                        O1=self.o1)
        self.line_5 = "*----------*----------*----------*----------*----------*"
        self.line_6 = "*   {B2}   *   {I2}   *   {N2}   *   {G2}   *   {O2}   *".format(B2=self.b2, I2=self.i2,
                                                                                        N2=self.n2, G2=self.g2,
                                                                                        O2=self.o2)
        self.line_7 = "*----------*----------*----------*----------*----------*"
        self.line_8 = "*   {B3}   *   {I3}   *   {N3}   *   {G3}   *   {O3}   *".format(B3=self.b3, I3=self.i3,
                                                                                        N3=self.n3, G3=self.g3,
                                                                                        O3=self.o3)
        self.line_9 = "*----------*----------*----------*----------*----------*"

    def __repr__(self):
        print(self.line_1)
        print(self.line_2)
        print(self.line_3)
        print(self.line_4)
        print(self.line_5)
        print(self.line_6)
        print(self.line_7)
        print(self.line_8)
        print(self.line_9)
        return " "

    def __set__(self, letter, name):
        if letter == 'B':
            if self.b1 == name:
                self.b1_new = '---'
                self.line_4 = "*   {B1}   *   {I1}   *   {N1}   *   {G1}   *   {O1}   *".format(B1=self.b1_new, I1=self.i1,
                                                                                                N1=self.n1, G1=self.g1,
                                                                                                O1=self.o1)
                print("YOU GOT IT! Here's your updated board:")
                print(new_board)
            elif self.b2 == name:
                self.b2_new = '---'
                self.line_6 = "*   {B2}   *   {I2}   *   {N2}   *   {G2}   *   {O2}   *".format(B2=self.b2_new, I2=self.i2,
                                                                                                N2=self.n2, G2=self.g2,
                                                                                                O2=self.o2)
                print("YOU GOT IT! Here's your updated board:")
                print(new_board)
            elif self.b3 == name:
                self.b3_new = '---'
                self.line_8 = "*   {B3}   *   {I3}   *   {N3}   *   {G3}   *   {O3}   *".format(B3=self.b3_new, I3=self.i3,
                                                                                                N3=self.n3, G3=self.g3,
                                                                                                O3=self.o3)
                print("YOU GOT IT! Here's your updated board:")
                print(new_board)

        elif letter == 'I':
            if self.i1 == name:
                self.i1_new = '---'
                self.line_4 = "*   {B1}   *   {I1}   *   {N1}   *   {G1}   *   {O1}   *".format(B1=self.b1,
                                                                                                I1=self.i1_new,
                                                                                                N1=self.n1, G1=self.g1,
                                                                                                O1=self.o1)
                print("YOU GOT IT! Here's your updated board:")
                print(new_board)
            elif self.i2 == name:
                self.i2_new = '---'
                self.line_6 = "*   {B2}   *   {I2}   *   {N2}   *   {G2}   *   {O2}   *".format(B2=self.b2, I2=self.i2_new,
                                                                                                N2=self.n2, G2=self.g2,
                                                                                                O2=self.o2)
                print("YOU GOT IT! Here's your updated board:")
                print(new_board)
            elif self.i3 == name:
                self.i3_new = '---'
                self.line_8 = "*   {B3}   *   {I3}   *   {N3}   *   {G3}   *   {O3}   *".format(B3=self.b3, I3=self.i3_new,
                                                                                                N3=self.n3, G3=self.g3,
                                                                                                O3=self.o3)
                print("YOU GOT IT! Here's your updated board:")
                print(new_board)

        elif letter == 'N':
            if self.n1 == name:
                self.n1_new = '---'
                self.line_4 = "*   {B1}   *   {I1}   *   {N1}   *   {G1}   *   {O1}   *".format(B1=self.b1,
                                                                                                I1=self.i1,
                                                                                                N1=self.n1_new, G1=self.g1,
                                                                                                O1=self.o1)
                print("YOU GOT IT! Here's your updated board:")
                print(new_board)
            elif self.n2 == name:
                self.n2_new = '---'
                self.line_6 = "*   {B2}   *   {I2}   *   {N2}   *   {G2}   *   {O2}   *".format(B2=self.b2, I2=self.i2,
                                                                                                N2=self.n2_new, G2=self.g2,
                                                                                                O2=self.o2)
                print("YOU GOT IT! Here's your updated board:")
                print(new_board)
            elif self.n3 == name:
                self.n3_new = '---'
                self.line_8 = "*   {B3}   *   {I3}   *   {N3}   *   {G3}   *   {O3}   *".format(B3=self.b3, I3=self.i3,
                                                                                                N3=self.n3_new, G3=self.g3,
                                                                                                O3=self.o3)
                print("YOU GOT IT! Here's your updated board:")
                print(new_board)

        elif letter == 'G':
            if self.g1 == name:
                self.g1_new = '---'
                self.line_4 = "*   {B1}   *   {I1}   *   {N1}   *   {G1}   *   {O1}   *".format(B1=self.b1,
                                                                                                I1=self.i1,
                                                                                                N1=self.n1,
                                                                                                G1=self.g1_new,
                                                                                                O1=self.o1)
                print("YOU GOT IT! Here's your updated board:")
                print(new_board)
            elif self.g2 == name:
                self.g2_new = '---'
                self.line_6 = "*   {B2}   *   {I2}   *   {N2}   *   {G2}   *   {O2}   *".format(B2=self.b2, I2=self.i2,
                                                                                                N2=self.n2,
                                                                                                G2=self.g2_new,
                                                                                                O2=self.o2)
                print("YOU GOT IT! Here's your updated board:")
                print(new_board)
            elif self.g3 == name:
                self.g3_new = '---'
                self.line_8 = "*   {B3}   *   {I3}   *   {N3}   *   {G3}   *   {O3}   *".format(B3=self.b3, I3=self.i3,
                                                                                                N3=self.n3, G3=self.g3_new,
                                                                                                O3=self.o3)
                print("YOU GOT IT! Here's your updated board:")
                print(new_board)

        elif letter == 'O':
            if self.o1 == name:
                self.o1_new = '---'
                self.line_4 = "*   {B1}   *   {I1}   *   {N1}   *   {G1}   *   {O1}   *".format(B1=self.b1,
                                                                                                I1=self.i1,
                                                                                                N1=self.n1,
                                                                                                G1=self.g1,
                                                                                                O1=self.o1_new)
                print("YOU GOT IT! Here's your updated board:")
                print(new_board)
            elif self.o2 == name:
                self.o2_new = '---'
                self.line_6 = "*   {B2}   *   {I2}   *   {N2}   *   {G2}   *   {O2}   *".format(B2=self.b2, I2=self.i2,
                                                                                                N2=self.n2,
                                                                                                G2=self.g2,
                                                                                                O2=self.o2_new)
                print("YOU GOT IT! Here's your updated board:")
                print(new_board)
            elif self.o3 == name:
                self.o3_new = '---'
                self.line_8 = "*   {B3}   *   {I3}   *   {N3}   *   {G3}   *   {O3}   *".format(B3=self.b3, I3=self.i3,
                                                                                                N3=self.n3, G3=self.g3,
                                                                                                O3=self.o3_new)
                print("YOU GOT IT! Here's your updated board:")
                print(new_board)

        else:
            print("No luck, try again")


class NewBall():
    faeries = ["Faer", "Dasy", "Qige", "Ezen", "Lena", "Yani", "Bezo"]
    letters = ["B", "I", "N", "G", "O"]

    def __init__(self):
        self.name = random.choice(self.faeries)
        self.letter = random.choice(self.letters)

    def __repr__(self):
        return "Your new ball is: " + self.letter + " " + self.name


# def check_ball(bingo_ball, board):


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
print("Hello " + username + "! Are you ready to start playing?")
print("Enter 'Y' for yes or 'N' for no")
answer = input()
# 3
if answer != 'Y' and answer != 'N':
    print("That is not a correct answer, please enter 'Y' for yes or 'N' for no")
    answer = input()
elif answer == 'N':
    print("Well then... see you another time :(")
elif answer == 'Y':
    print("""
Yiiihhhi, let's get started with the Faery Bingo
    
HERE IS YOUR BRAND NEW BINGO BOARD: """)
    new_board = Board()
    print(new_board)
# 4
print("""
Whenever you're ready, type 'ROLL' to get a Faery Ball and start completing your table""")
play = input()

while play == 'ROLL':
    new_ball = NewBall()
    print(new_ball)
    new_board.__set__(new_ball.letter, new_ball.name)
    print("Type 'ROLL' to get another Faery Ball:")
    play = input()

print("out of loop")
