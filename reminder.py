'''
This is a simple, lightweight reminder app that keeps tracks of
my time

Key Features:
1. Add/delete tasks/reminders
2. Edit existing tasks
3. Notify due dates
4. Add notes/contacts in reminders
5. Store reminders in local files
6. Run on raspberry pi server, send daily sms/email reminders
7. Multi-User features
8. GUI?

More features to come
'''


class User():
    """docstring for User"""

    def __init__(self, age=0, profession='',
                 name='', taskNum=0, tasks=0):
        self.age = age
        self.profession = profession
        self.name = name
        self.taskNum = taskNum
        self.tasks = tasks
        self.archived = []

    def changeInput(self, input, target_Var):
        '''target var is the name'''
        self.target_Var = input

    def addTask(self, task):
        '''add a task into the existing task list'''
        self.tasks.append([str(task), 'Note: ', 'Due date: '])
        self.taskNum += 1
        print('Todo #' + str(len(self.tasks)) + ' added')

    def editTask(self, editedVer, index):
        '''edit the name of the task'''
        self.tasks[index][0] = str(editedVer)
        print('Todo #' + str(index) + ' updated')

    def findTask(self, KeyWord):
        for item in self.tasks:
            if KeyWord.lower() in item[0].lower():
                print('Case: ' + item[0])

    def deleteTask(self, index):
        print('Todo: ' + str(self.tasks.pop(index)) + 'removed')
    

# test case
# a = User(13, "Student", "Will Wu", 0, [])
# a.changeInput(14, a.age)
# a.addTask('Homework')
# a.addTask('SmartHome')
# a.editTask('Home', 1)
# a.findTask('Home')
