'''
This is a simple, lightweight calendar app that keeps tracks of
your time

Key Features:
1. Add/delete tasks/reminders
2. Notify due dates
3. Add notes/contacts in reminders
4. Store reminders in local files

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
        self.tasks.append(str(tasks))
        self.taskNum += 1
        print("todo #" + len(tasks) + " added")


# test case
# a = User(13, "Student", "Will Wu", 0, [])
# a.changeInput(14, a.age)
