# FAIRY BINGO
# - You will be assigned a bingo board
# - Possible board contents will be randomly generated
# - If that randomly generated response matches your board, it will be deleted
# - Once you delete all the items in the board you will be assigned a prize
# - The prize will vary depending on how many tries it took you to clear the board


# BINGO FAIRY CHARACTERS -
# Faer
# Dasy
# Qige
# Ezen
# Lena
# Yani
# Bezo

import random

board = """
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


def print_board():
    # Generate Random Placements
    b1 = characters.get(random.randint(1, 7))
    b2 = characters.get(random.randint(1, 7))
    b3 = characters.get(random.randint(1, 7))

    i1 = characters.get(random.randint(1, 7))
    i2 = characters.get(random.randint(1, 7))
    i3 = characters.get(random.randint(1, 7))

    n1 = characters.get(random.randint(1, 7))
    n2 = characters.get(random.randint(1, 7))
    n3 = characters.get(random.randint(1, 7))

    g1 = characters.get(random.randint(1, 7))
    g2 = characters.get(random.randint(1, 7))
    g3 = characters.get(random.randint(1, 7))

    o1 = characters.get(random.randint(1, 7))
    o2 = characters.get(random.randint(1, 7))
    o3 = characters.get(random.randint(1, 7))

    # Format Board
    line_1 = "*----------*----------*----------*----------*----------*"
    line_2 = "*    B     *    I     *    N     *    G     *    O     *"
    line_3 = "*----------*----------*----------*----------*----------*"
    line_4 = "*   {B1}   *   {I1}   *   {N1}   *   {G1}   *   {O1}   *".format(B1=b1, I1=i1, N1=n1, G1=g1, O1=o1)
    line_5 = "*----------*----------*----------*----------*----------*"
    line_6 = "*   {B2}   *   {I2}   *   {N2}   *   {G2}   *   {O2}   *".format(B2=b2, I2=i2, N2=n2, G2=g2, O2=o2)
    line_7 = "*----------*----------*----------*----------*----------*"
    line_8 = "*   {B3}   *   {I3}   *   {N3}   *   {G3}   *   {O3}   *".format(B3=b3, I3=i3, N3=n3, G3=g3, O3=o3)
    line_9 = "*----------*----------*----------*----------*----------*"

    print(line_1)
    print(line_2)
    print(line_3)
    print(line_4)
    print(line_5)
    print(line_6)
    print(line_7)
    print(line_8)
    print(line_9)
    return "Good Luck!"

new_board = print_board()



