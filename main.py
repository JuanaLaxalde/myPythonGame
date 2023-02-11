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


class CreateBoard:
    # Generate Random Placements
    def __init__(self):
        self.b1 = characters.get(random.randint(1, 7))
        self.b2 = characters.get(random.randint(1, 7))
        self.b3 = characters.get(random.randint(1, 7))

        self.i1 = characters.get(random.randint(1, 7))
        self.i2 = characters.get(random.randint(1, 7))
        self.i3 = characters.get(random.randint(1, 7))

        self.n1 = characters.get(random.randint(1, 7))
        self.n2 = characters.get(random.randint(1, 7))
        self.n3 = characters.get(random.randint(1, 7))

        self.g1 = characters.get(random.randint(1, 7))
        self.g2 = characters.get(random.randint(1, 7))
        self.g3 = characters.get(random.randint(1, 7))

        self.o1 = characters.get(random.randint(1, 7))
        self.o2 = characters.get(random.randint(1, 7))
        self.o3 = characters.get(random.randint(1, 7))

        # Format Bingo Table
        self.line_1 = "*----------*----------*----------*----------*----------*"
        self.line_2 = "*    B     *    I     *    N     *    G     *    O     *"
        self.line_3 = "*----------*----------*----------*----------*----------*"
        self.line_4 = "*   {B1}   *   {I1}   *   {N1}   *   {G1}   *   {O1}   *".format(B1=self.b1, I1=self.i1, N1=self.n1, G1=self.g1, O1=self.o1)
        self.line_5 = "*----------*----------*----------*----------*----------*"
        self.line_6 = "*   {B2}   *   {I2}   *   {N2}   *   {G2}   *   {O2}   *".format(B2=self.b2, I2=self.i2, N2=self.n2, G2=self.g2, O2=self.o2)
        self.line_7 = "*----------*----------*----------*----------*----------*"
        self.line_8 = "*   {B3}   *   {I3}   *   {N3}   *   {G3}   *   {O3}   *".format(B3=self.b3, I3=self.i3, N3=self.n3, G3=self.g3, O3=self.o3)
        self.line_9 = "*----------*----------*----------*----------*----------*"

    def get_board(self):
        print(self.line_1)
        print(self.line_2)
        print(self.line_3)
        print(self.line_4)
        print(self.line_5)
        print(self.line_6)
        print(self.line_7)
        print(self.line_8)
        print(self.line_9)
        return "LET'S GET STARTED!"

    def modify_board(self, letter, name):
        if letter == 'B':
            self.line_4 = "*   {B1}   *   {I1}   *   {N1}   *   {G1}   *   {O1}   *".format(B1=self.b1, I1=self.i1,
                                                                                            N1=self.n1, G1=self.g1,
                                                                                            O1=self.o1)
            self.line_6 = "*   {B2}   *   {I2}   *   {N2}   *   {G2}   *   {O2}   *".format(B2=self.b2, I2=self.i2,
                                                                                            N2=self.n2, G2=self.g2,
                                                                                            O2=self.o2)
            self.line_8 = "*   {B3}   *   {I3}   *   {N3}   *   {G3}   *   {O3}   *".format(B3=self.b3, I3=self.i3,
                                                                                            N3=self.n3, G3=self.g3,
                                                                                            O3=self.o3)

def bingo_ball():
    faeries = ["Faer", "Dasy", "Qige", "Ezen", "Lena", "Yani", "Bezo"]
    letters = ["B", "I", "N", "G", "O"]
    name = faeries[random.randint(0, 6)]
    letter = letters[random.randint(0, 4)]
    return "Faery: " + name + " In placement: " + letter


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
    new_board = CreateBoard()
    new_board.get_board()
#4
print("""
Whenever you're ready, type 'ROLL' to get a Faery Ball and start completing your table""")
roll = input()

if roll == 'ROLL':
    new_ball = bingo_ball()
    print("""HERE IS YOUR FIRST BALL
    """ + new_ball)

def trying_out_changes:
    pass



