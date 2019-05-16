import random

'''
@param self:
'''
class stringDatabase:


    def getInputFromFile(self):
        mylist = []
        with open("four_letters.txt", "r+") as f:
            fdata = f.readlines()

        for line in fdata:
            y = line.split()
            for i in y:
                mylist.append(i)

        f.close()
        return mylist