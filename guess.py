import StringDatabase as sdb
import game

def word_guessing_game():
    ''' The main entry point of the game

        This function calls the Game class methods for the game to begin
    '''

    mydb = sdb.stringDatabase()
    mygame = game.Game()
    mylist = []

    mylist = mydb.getInputFromFile()

    print("** The great guessing game **")
    mygame.play(mylist)

    return



word_guessing_game()
