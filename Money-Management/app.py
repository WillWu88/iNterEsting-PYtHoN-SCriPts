#reads and writes a file to keep record of my money

#opens a hidden file names .checkbook.txt, if it doesnt exist, create a new one
filename = ".checkbook.txt"
try:
    checkbook = open(filename, "r")
except:
    checkbook = open(filename, "w+")


class User:
    #constructor
    def __init__(self, monthly_allowance, number_of_months, name):
        self.monthly_allowance = monthly_allowance
        self.number_of_months = number_of_months
        self.name = name

    def printVar(var):
        '''debug func
        '''
        print(self.var)
    def addOne():
        '''takes no arguments
        add one to the number of month
        '''
        number_of_months += 1
    def printInfo():
        '''prints info at every log in'''


#testing

willWu = User(0, 0, "Hi")
willWu.addOne
