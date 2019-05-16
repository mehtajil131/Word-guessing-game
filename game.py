from pip._vendor.distlib.compat import raw_input
import random

def display_result():
    print("Result")

class Game:

    def play(self,mylist):

        print("Current guess : ----")
        user_in = 'm'
        gamecnt = 0
        while(gamecnt < 100):

            if(user_in.__eq__('q')):
                break
            cnt = 0
            wordind = random.randint(0, len(mylist))
            word = mylist[wordind]
            wordlist = list(word)
            str1 = ["-","-","-","-"]
            print(wordlist)

            while(cnt < 26):

                user_in = raw_input("\ng = guess, t = tell me, l for a letter, and q to quit\n")

                if (user_in.__eq__('g')):
                    user_word = raw_input("Enter the word\n")
                    if (user_word.__eq__(word)):
                        print("\nSuccess!! You guessed it right\n")
                        gamecnt = gamecnt + 1
                        break
                    else:
                        print("\nTough Luck!! Wrong word\n")
                elif (user_in.__eq__('t')):
                    print("\nThe correct word is " + word)
                    gamecnt = gamecnt + 1
                    break
                elif (user_in.__eq__('l')):
                    tempcnt = 0
                    occurance = 0
                    temp = ""
                    user_letter = raw_input("Enter Letter\n")
                    if(user_letter in wordlist):
                        occurance = wordlist.count(user_letter)
                        print("\n You found " + str(occurance) + " letter/s" )
                        while(tempcnt < occurance):
                            ind = wordlist.index(user_letter)
                            str1[ind] = user_letter
                            tmep = temp.join(str1)
                            wordlist[ind] = '+'
                            tempcnt = tempcnt+1
                        print("\n\nCurrent Guess is :" + tmep)
                        if ('-' not in tmep):
                            print("*** Congrats You did it!!!! ***")
                            gamecnt = gamecnt + 1
                            break
                    else:
                        print("\nCurrent Guess is :" + tmep)
                        print("\nLetter not present in word !! Try again")

                    cnt = cnt +1
                elif (user_in.__eq__('q')):
                    display_result()
                    break
                else:
                    print("Enter a valid input")

