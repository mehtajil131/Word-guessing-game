import StringDatabase as sdb
import game


class guess:

    '''
    Contains the calling of game class
    '''

    def word_guessing_game(self):
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



myguess = guess()
myguess.word_guessing_game()
