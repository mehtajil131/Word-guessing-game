from pip._vendor.distlib.compat import raw_input
import random


def display_result(resultString,scorelist):
    finalscore = 0
    print("Game  Word  Status  Bad Guesses  Missed Letters  Score\n")
    print("----  ----  ------  -----------  --------------  -----\n")
    for j in resultString:
        print(j + "\n")
    for i in range(len(scorelist)):
        finalscore = scorelist[i] + finalscore
    print(finalscore)


class Game:

    freq = {'a': 8.17, 'b': 1.49, 'c': 2.78, 'd': 4.25, 'e': 12.70, 'f': 2.23, 'g': 2.02,
            'h': 6.09, 'i': 6.97, 'j': 0.15, 'k': 0.77, 'l': 4.03, 'm': 2.41, 'n': 6.75,
            'o': 7.51, 'p': 1.93, 'q': 0.10, 'r': 5.99, 's': 6.33, 't': 9.06, 'u': 2.76,
            'v': 0.98, 'w': 2.36, 'x': 0.15, 'y': 1.97, 'z': 0.07}

    def play(self,mylist):

        print("Current guess : ----")
        user_in = 'm'
        gamecnt = 0
        resultString = []
        result = ""
        scoreRecord = []
        while(gamecnt < 100):

            if(user_in.__eq__('q')):
                break
            cnt = 0
            score = 0
            wordind = random.randint(0, len(mylist))
            word = mylist[wordind]
            wordlist = list(word)
            guesscnt = 0
            tmep = ""
            misslettercnt = 0
            strfinal = ""
            str1 = ["-","-","-","-"]
            #print(wordlist)

            while(cnt < 26):

                user_in = raw_input("\ng = guess, t = tell me, l for a letter, and q to quit\n")

                if (user_in.__eq__('g')):
                    user_word = raw_input("Enter the word\n")
                    if (user_word.__eq__(word)):
                        tempfreq = 0
                        if(tmep != ""):
                            temp1 = list(tmep)
                            occur = temp1.count('-')
                            for i in range(occur):
                                temp1.remove('-')
                                print(temp1)
                            for i in temp1:
                                tempfreq = Game.freq[i] + tempfreq
                        score = (Game.freq[user_word[0]] + Game.freq[user_word[1]] + Game.freq[user_word[2]]
                        + Game.freq[user_word[3]]) - tempfreq
                        print("\nSuccess!! You guessed it right\n")
                        result = "Success"
                        gamecnt = gamecnt + 1
                        score = round(score, 2)
                        scoreRecord.append(score)
                        strfinal = str(gamecnt) + "     " + str(word) + "  " + result + " " + str(guesscnt) \
                                   + "            " + str(misslettercnt) + "              " + str(score)
                        resultString.append(strfinal)
                        break
                    else:
                        guesscnt = guesscnt + 1
                        score = score - (0.1*score)
                        print("\nTough Luck!! Wrong word\n")
                elif (user_in.__eq__('t')):
                    print("\nThe correct word is " + word)
                    if(tmep != ""):
                        temp2 = tmep
                        occur2 = temp2.count('-')
                        for i in range(4):
                            if(temp2[i].__eq__('-')):
                                score = score - Game.freq[wordlist[i]]
                    else:
                        for j in range(4):
                            gamefreq = Game.freq[wordlist[j]]
                            score = score - gamefreq
                    #print(round(score,2))
                    gamecnt = gamecnt + 1
                    result = "Gave Up"
                    score = round(score, 2)
                    scoreRecord.append(score)
                    strfinal = str(gamecnt) + "     " + str(word) + "  " + result + " " + str(guesscnt) \
                               + "            " + str(misslettercnt) + "              " + str(score)
                    resultString.append(strfinal)
                    break
                elif (user_in.__eq__('l')):
                    tempcnt = 0
                    occurance = 0
                    temp = ""
                    user_letter = raw_input("Enter Letter\n")
                    if(str1.__contains__(user_letter)):
                        print("Already guessed this. Enter new letter")
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
                            score = score + Game.freq[user_letter]
                        if (tmep.__eq__("")):
                            print("\n\nCurrent Guess is : ----")
                        else:
                            print("\n\nCurrent Guess is :" + tmep)
                        if ('-' not in tmep):
                            result = "Success"
                            print("*** Congrats You did it!!!! ***")
                            gamecnt = gamecnt + 1
                            score = round(score, 2)
                            scoreRecord.append(score)
                            strfinal = str(gamecnt) + "     " + str(word) + "  " + result + " " + str(guesscnt) \
                                       + "            " + str(misslettercnt) + "              " + str(score)
                            resultString.append(strfinal)
                            break
                    else:
                        misslettercnt = misslettercnt + 1
                        if (tmep.__eq__("")):
                            print("\n\nCurrent Guess is : ----" )
                        else:
                            print("\n\nCurrent Guess is :" + tmep)
                        print("\nLetter not present in word !! Try again")
                    cnt = cnt +1
                elif (user_in.__eq__('q')):
                    display_result(resultString,scoreRecord)
                    break
                else:
                    print("Enter a valid input")



