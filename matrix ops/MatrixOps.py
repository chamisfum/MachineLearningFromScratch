from random import randint
import time

class MatrixOps:
    def __init__(self, row, col):
        self.row = row
        self.col = col
    
    def zeroMatrix(row, col):
        return [[0]*(row) for _ in range(col)] # make zero matrix

    def matrixBuilder(row, col):
        Matrix = MatrixOps.zeroMatrix(row, col)
        for i in range(len(Matrix)):
            for j in range(len(Matrix[i])):
                Matrix[i][j] = randint(0,100) # random matrix element
        return Matrix

    def transpose(data):
        result = MatrixOps.zeroMatrix(len(data), len(data[0]))
        for i in range(len(data)):
            for j in range(len(data[0])):
                result[j][i] = data[i][j]
        return result
    
    def transposeType2(data):
        return map(list, zip(*data))
    
    def multiplySQ(data1, data2):
        if len(data1) == len(data2) and len(data1[0]) == len(data2[0]):
            result = [[sum(a*b for a,b in zip(x_row, y_col)) for y_col in zip(*data2)] for x_row in data1]
            return result
        else:
            return False
    
    def sumMatrix(data1, data2):
        if len(data1) == len(data2) and len(data1[0]) == len(data2[0]):
            result = [[data1[i][j] + data2[i][j]for j in range(len(data1[0]))] for i in range(len(data1))]
            return result
        else:
            return False
    
    def subtractMatrix(data1, data2):
        if len(data1) == len(data2) and len(data1[0]) == len(data2[0]):
            result = [[data1[i][j] - data2[i][j]for j in range(len(data1[0]))] for i in range(len(data1))]
            return result
        else:
            return False

    def getMatrixMinor(m,i,j):
        return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

    def getMatrixDeternminant(m):
        #base case for 2x2 matrix
        if len(m) == 2:
            return m[0][0]*m[1][1]-m[0][1]*m[1][0]

        determinant = 0
        for c in range(len(m)):
            determinant += ((-1)**c)*m[0][c]*MatrixOps.getMatrixDeternminant(MatrixOps.getMatrixMinor(m,0,c))
        return determinant

    def getMatrixInverse(m):
        determinant = MatrixOps.getMatrixDeternminant(m)
        #special case for 2x2 matrix:
        if len(m) == 2:
            return [[m[1][1]/determinant, -1*m[0][1]/determinant],
                    [-1*m[1][0]/determinant, m[0][0]/determinant]]

        #find matrix of cofactors
        cofactors = []
        for r in range(len(m)):
            cofactorRow = []
            for c in range(len(m)):
                minor = MatrixOps.getMatrixMinor(m,r,c)
                cofactorRow.append(((-1)**(r+c)) * MatrixOps.getMatrixDeternminant(minor))
            cofactors.append(cofactorRow)
        cofactors = MatrixOps.transposeType2(cofactors)
        for r in range(len(cofactors)):
            for c in range(len(cofactors)):
                cofactors[r][c] = cofactors[r][c]/determinant
        return cofactors

data = MatrixOps.matrixBuilder(5,2)
data2 = MatrixOps.matrixBuilder(5,2)
print(MatrixOps.getMatrixDeternminant(data2))
print(data2)