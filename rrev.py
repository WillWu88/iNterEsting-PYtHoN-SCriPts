import math

#by defaut, each 2d array has the same length 

#3*4 matrix
example_matrix = [[2, 3, 4, 4],[3, 4, 1, 2],[8, 10, 5, 2]]

def setToOne(target_Matrix = [], index = 0):
    ''' sets the given index to 1, while manipulating the equation
    default index is 0, the first element
    '''
    coeff = target_Matrix[0]
    for index in range(len(target_Matrix)):
        target_Matrix[index] /= coeff
    
def zeroRow(target_Matrix = [], column = 0, base_row_index = 0):
    ''' using the base row tozero out the given column
    default is 0 for both column and base row
    '''
    base_row = target_Matrix[base_row_index]
    
    for each_column in range(len(target_Matrix[])):
        



def clear_Row(example_matrix = []):
    pass
    