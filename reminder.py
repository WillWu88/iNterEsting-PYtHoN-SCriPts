'''
This is a simple, lightweight reminder app that keeps tracks of
my time

Interacion: command by inputing lines/gui

dev note: needs autopep8 on windows

Check:
1. Time and how to format

Key Features:
[] 1. Add/delete tasks/reminders into categories
[] 2. Edit existing tasks
[] 3. Notify due dates, send reminders via sms or email
[] 4. Add notes/contacts in reminders
[] 5. Store reminders in local files
[] 6. Run on raspberry pi server, send daily sms/email reminders
[] 7. Multi-User features
[] 8. GUI?
[] 9. Executable Command Line Binary

More features to come
'''

# Important: index should all be +1


class User():
    '''docstring for User'''

    def __init__(self, age=0, profession='',
                 name='', taskNum=0, tasks=0):
        self.age = age
        self.profession = profession
        self.name = name
        self.taskNum = taskNum
        self.tasks = tasks
        self.archived = []
        self.categories = []
        self.due_today_list = []

    def changeProperties(self, input, target_Var):
        '''
        changes the object's property
        target var is the name
        '''
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
        '''
        print cases that contains KeyWord given
        '''
        for number in range(len(self.tasks)):
            if KeyWord.lower() in self.tasks[number][0].lower():
                print('Case: Todo #' + str(number + 1) + ': '
                      + self.tasks[number][0])

    def deleteTask(self, index):
        '''remove a task under the given index'''
        print('Todo: ' + str(self.tasks.pop(index)) + 'removed')

    def editNote(self, note, index):
        '''edit the reminder note'''
        self.tasks[index][1] = str(note)
        print('Note added: todo #' + str(index + 1))

    def dueToday(self):
        '''returns a boolean
        if the item(a compound list from self.tasks) is due today
        this includes dued objects as well
        '''
        # needs work on time
        return true

    def remind(self):
        '''run through the list at 8 every morning, est
        adds a new list with everything due today'''
        for num in len(self.tasks):
            test = self.dueToday(self.tasks[num])
            if (test):
                self.due_today_list.append(self.due_today_list[num])
        heads_up = 'You have' + str(len(self.due_today_list)) + 'due today'
        return heads_up

    def setDueDate(self, index):
        '''
        set the due date of a object to a ? representing time
        data structure to be determined
        this function can be used to update due date as well
        '''
        pass

    def newCategory(self, name):
        '''adds a new category to the categories list
        the new category is always appended,
        so the len()-1 is the index'''
        self.categories.append([str(name)])
        return len(self.categories) - 1

    def addToCategory(self, todo_index, category_index):
        '''store the index of the target todo in the category array
        returns the category array index
        '''
        self.categories[category_index].append(todo_index)
        return category_index

    def displayCategory(self, category_index):
        '''return a string with the names of the todos in the category
        list
        '''
        # the category sub arrays first item is always the 'tag'/name
        string_to_print = ''
        for index in range(1, len(self.categories[category_index])):
            string_to_print += str(self.tasks
                                   [self.categories
                                    [category_index][index]][0]) + ' '
        return string_to_print

    def sitRap(self):
        pass
        # sit_rap_message = ('You have' + str(self.taskNum)
        #                     + 'tasks to do.')
        # return


# test case
a = User(13, 'Student', 'Will Wu', 0, [])
a.changeProperties(14, a.age)
a.addTask('Homework')
a.addTask('SmartHome')
a.editTask('Home', 1)
a.addTask('Sports')
a.addTask('Hommy')
a.findTask('Home')
a.editNote('1', 1)
a.newCategory('Physics')
a.addToCategory(2, 0)
a.addToCategory(0, 0)
print(a.categories)
print(a.displayCategory(0))
