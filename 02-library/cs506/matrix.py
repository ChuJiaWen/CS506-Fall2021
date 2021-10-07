import numpy as np

def get_determinant(matrix):
    num_row = len(matrix)
    num_col = len(matrix[0])
    if num_row < 2 or num_col < 2:
        return ValueError("To calculate the determinant the matrix must at least be 2x2")
    elif (num_row != num_col):
        return ValueError("To calculate the determinant the matrix must be square")
    elif num_col == 2 and num_row == 2:
        return (matrix[0][0]*matrix[1][1]) - (matrix[0][1]*matrix[1][0])
    else:
        minor = np.array(matrix[1:])
        det = 0
        for index in range(num_col):
            include_col = np.delete(np.arange(num_col),index)
            print("I'm calculating column:",index, "and the columns to be included in minor is: ", include_col)
            minor_matrix = minor[:,include_col]
            print("Calculating determinant on minor matrix:", minor_matrix)
            if (index % 2 == 0):
                det += matrix[0][index] * get_determinant(minor_matrix)
            else:
                det -= matrix[0][index] * get_determinant(minor_matrix)
        return det

def main():
    matrix1 = [[1,2],[3,4]]
    print(get_determinant(matrix1))

    matrix2 = [[1,2,3],[2,3,4],[4,5,6]]
    print(get_determinant(matrix2))

    matrix3 = [[1,3,2],[4,1,3],[2,5,2]]
    print(get_determinant(matrix3))
main()



