from pip._vendor.distlib.compat import raw_input
import StringDatabase as sdb
import game
import random

def freadwrite():

    mydb = sdb.stringDatabase()
    mygame = game.Game()
    mylist = []

    mylist = mydb.getInputFromFile()

    print("** The great guessing game **")
    mygame.play(mylist)

    return

freadwrite()
