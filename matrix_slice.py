# encoding:utf8
import numpy

def slice(array, position):
    """
    :param array: a matrix, ndim(matrix)=2
    :param position: [a, b]
    :return: delete all the data in ath row and bth
    """
    print("your input matrix:")
    print(array)
    print('Here is the position: {0}'.format(position)) 
    print("******************\n")

    array = numpy.array(array)
    dim = array.shape
    # if position > dim(array), return False
    if position[0] >= dim[0] or position[1] >= dim[1]:
        print("position is out of range")
        return False

    # slice on the row
    row = position[0]
    if row == 0:
        row_array = array[1:, ]
    elif row == dim[0]-1:
        row_array = array[-1:, ]
    else:
        first_slice = array[:row, ]
        second_silce = array[row+1:, ]
        # join the two slice
        row_array = numpy.vstack((first_slice, second_silce))

    # slice on the column
    col = position[1]
    if col == 0:
        new_array = row_array[:, 1:]
    elif row == dim[0]-1:
        new_array = row_array[:, -1:]
    else:
        first_slice = row_array[:, :col]
        second_silce = row_array[:, col+1:]
        # join the two slice
        new_array = numpy.hstack((first_slice, second_silce))

    print('here is your new matrix')
    print(new_array)
    return new_array

# demo
list = range(1, 13)
array = numpy.array(list)
array.shape = (3, 4)
slice(array, [1, 2])

