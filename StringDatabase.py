
class stringDatabase:

    '''
    Performs all the disk I/O tasks.
    '''

    def getInputFromFile(self):

        '''
        Reads the entire four_letters.txt file and stores it into a list
        :return: The list containing all the 4 letter words
        '''

        mylist = []
        with open("four_letters.txt", "r+") as f:
            fdata = f.readlines()

        for line in fdata:
            y = line.split()
            for i in y:
                mylist.append(i)

        f.close()
        return mylist