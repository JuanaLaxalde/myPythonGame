# myPythonGame

"Faery Bingo" is an interactive terminal game.
The idea is to replicate the concept of the original Bingo Game, only in a digital manner, and to add some creativity to it by using a faery theme.

There are 7 faery characters = {1: "Faer", 2: "Yani", 3: "Bezo", 4: "Dasy", 5: "Lena", 6: "Qige", 7: "Ezen"}
And 5 letters in the board = {1: "B", 2: "I", 3: "N", 4: "G", 5: "O"}
<there are 35 possible combinations (balls)>
Each letter (column) will be assigned 3 faeries (rows).
<the board contains 15 combinations>
You get to draw a maximum of 40 balls.
<chances of eliminating all faeries from the board are quite tight>

              
## The rules of the game are as follows:

1 - You get a maximum of 40 balls in your attempt to eliminate all faeries from the board.
2 - To continue rolling you need to type 'ROLL': If the ball is not a match to your board, 
    nothing will happen. If if is, your updated board will be printed.
3 - If you want to stop before you have finished your 40 attempts, just type 'QUIT'.
4 - Your reward will depend on how many faeries you have eliminated from your board.

## Structure of the code:

1 - class Board():

This class consists of an __init__, __repr__, __set__ & store_values functions.
The init assigns a random choice from a dictionary that contains all the faery's names to each section of the board (of which there are 15).
The repr prints 9 formatted strings that together conform the visual representation of the board.
The set will replace the originally assigned faery of a certain section of the board with the string '----'. It will do so only when a ball
has been drawn which actually exists within the player's board.
The store_values function records all the eliminated and non eliminated sections of the board into a dictionary that looks like this:
final_result = {'B': ['----', '----', '----'], 
                'I': ['----', '----', 'Ezen'], 
                'N': ['Qige', 'Qige', '----'], 
                'G': ['Dasy', 'Bezo', '----'], 
                'O': ['Yani', 'Bezo', '----']}

2 - class NewBall():

This class contains two class variables, faeries and letters, which are lists of all the characters and letters conforming the game.
There are two functions in this class __init__ and __repr__.
The init function creates two new randomly assigned class variables (name and letter) which are chosen from the list variables.
The repr function returns a string that represents the randomly generated combination of name and letter (the ball).

3 - function calculate_guesses():

This function loops through each key in the final_result's dictionary (which is taken as an argument) and through each item within the values 
and adds one to the variable 'guesses' whenever it matches the string '----'

4 - function assign_prize():

This function takes as an argument the number of guesses returned by calculate_guesses and uses an if statement to return one of three strings
that contain ascii art: one_to_five, six_to_ten and eleven_to_fifteen.

5 - interaction with player:

The remaining lines of the code consist of print statements, input calls, while loops, function calls and class calls which all together
create the visuals of the game.









