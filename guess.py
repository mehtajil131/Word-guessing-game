from pip._vendor.distlib.compat import raw_input
import StringDatabase as sdb
import game
import random

''' The main entry point of the game
    
    This function calls the Game class methods for the game to begin
'''

def word_guessing_game():

    mydb = sdb.stringDatabase()
    mygame = game.Game()
    mylist = []

    mylist = mydb.getInputFromFile()

    print("** The great guessing game **")
    mygame.play(mylist)

    return



word_guessing_game()
