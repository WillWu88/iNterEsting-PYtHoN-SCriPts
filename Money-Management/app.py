#reads and writes a file to keep record of my money

#opens a hidden file names .checkbook.txt, if it doesnt exist, create a new one
#filename = ".checkbook.txt"
import os

class User:
    #constructor
    def __init__(self, monthly_allowance, number_of_months, name):

        self.monthly_allowance = monthly_allowance
        self.number_of_months = number_of_months
        self.name = input("Log in: > ")
        self.filename = "."+self.name + "ledger.txt"
        try:
            ledger = open(self.filename, "r")
            ledger.close()
        except:
            ledger = open(self.filename, "w+")
            ledger.close()
        #with open(self.filename, "w") as ledger:
        #    ledger.write("0")

    def printVar(self, var):
        '''debug func
        '''
        print(self.var)
    def addOne(self):
        '''takes no arguments
        add one to the number of month
        '''
        number_of_months += 1
    def printInfo(self):
        '''prints info at every log in'''

    def rewriteLine(self, line_num, replace_Str):
        '''replace a line
        going to be an intrinsic founction
        so am not gonna put in user prompts
        '''
        with open(self.filename, "w") as ledger:
            counter = 0
            for lines in ledger:
                if (counter-1 == line_num):
                    ledger.write(line.replace(lines, replace_Str))

    def logIN(self):
        '''writes register info everytime when the user log in
        '''
        if (os.stat(self.filename).st_size == 0):
            with open(self.filename, "w") as ledger:
                ledger.write("1")



#testing

willWu = User(0, 0, "Hi")
willWu.logIN()
'''willWu.rewriteLine(1,"1")'''
