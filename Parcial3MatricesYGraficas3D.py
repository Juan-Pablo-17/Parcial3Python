import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import copy
from sys import stdin


class Matrix:

    def __init__(self, data: list):
        self.matrix = copy.deepcopy(data)

    def __str__(self):
        answer = ''
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                answer += str(self.matrix[i][j])
                if j != len(self.matrix[i]) - 1:
                    answer += '\t'
            if i != len(self.matrix) - 1:
                answer += '\n'
        return answer

    def size(self):
        return len(self.matrix), len(self.matrix[0])

    def __getitem__(self, key):
        return self.matrix[key]

    def __setitem__(self, key_x, key_y, value):
        self.matrix[key_x][key_y] = value

    def __add__(self, other):
        answer = Matrix(copy.deepcopy(self.matrix))
        if self.size() != other.size():
            raise MatrixError(self, other)
        for i in range(answer.size()[0]):
            for j in range(answer.size()[1]):
                answer[i][j] += other[i][j]
        return answer

    def __mul__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            answer = Matrix(copy.deepcopy(self.matrix))
            for i in range(answer.size()[0]):
                for j in range(answer.size()[1]):
                    answer[i][j] *= other
                    # answer.__setitem__(i, j, answer[i][j] * other)
        else:
            if self.size()[1] != other.size()[0]:
                raise MatrixError(self, other)
            else:
                answer = [[0 for _ in range(other.size()[1])]
                          for k in range(self.size()[0])]
                for i in range(self.size()[0]):
                    for j in range(other.size()[1]):
                        curr_sum = 0
                        for k in range(self.size()[1]):
                            curr_sum += self[i][k] \
                                        * other[k][j]
                        answer[i][j] = curr_sum
                return Matrix(answer)

        return answer

    def __rmul__(self, other):
        if isinstance(other, Matrix):
            answer = other.__mul__(copy.deepcopy(self.matrix))
        else:
            answer = Matrix(copy.deepcopy(self.matrix)).__mul__(other)
        return answer

    def transpuesta(self):
        answer = [[0 for _ in range(self.size()[0])]
                  for __ in range(self.size()[1])]
        for i in range(self.size()[1]):
            for j in range(self.size()[0]):
                answer[i][j] = self[j][i]
        self.matrix.__init__(answer)
        return Matrix(answer)


class MatrixError(Exception):

    def __init__(self, matrix1, matrix2):
        self.matrix1 = matrix1
        self.matrix2 = matrix2


class SquareMatrix(Matrix):

    def __pow__(self, power):
        result = Matrix([[0 for _ in range(self.size()[1])]
                         for k in range(self.size()[0])])
        for i in range(min(self.size()[1], self.size()[0])):
            result[i][i] = 1
        while power > 0:
            if power % 2 == 1:
                result *= self
                power -= 1
            else:
                self *= self
                power //= 2
        return result
    
#Filas de la matriz A
#Puede agregar la fila o columna que plazca, puede leer una matriz mxn

A1 = [3,4,3]
A2 = [-1,2,3]
A3 = [1,-2,3]
A = SquareMatrix([A1, A2, A3])

#Filas de la matriz B

B1 = [-5,2,1]
B2 = [1,-3,2]
B3 = [3,2,-3]
B = Matrix([B1, B2, B3])

C1 = A1+B1
C2 = A2+B2
C3 = A3+B3

print()
print("La matriz A es:")
print()

print(A)
print()
print("La matriz B es:")
print()

print(B)
print()
print("La matriz A+B es:")
print()

print(A + B)
print()
print("La matriz A*B es:")
print()

print(A*B)
print()
print("La traspuesta de A es")
print()
print(A.transpuesta())
print() 

print("La traspuesta de B es")
print()
print(B.transpuesta())
print()

#==============================================================
#Gráficas
#==============================================================

#u = [1,2,3]
#v = [1,0,1]
#q = [0,3,1]

fig = plt.figure('Gráfica')
ax = Axes3D(fig)
ax.set_xlim([-10,10])
ax.set_ylim([-10,10])
ax.set_zlim([-10,10])

#Vectores Matriz A

start = [0,0,0]
ax.quiver(start[0], start[1], start[2], A1[0], A1[1], A1[2])
ax.quiver(start[0], start[1], start[2], A2[0], A2[1], A2[2], color = "g")
ax.quiver(start[0], start[1], start[2], A3[0], A3[1], A3[2], color = "r")

#Vectores Matriz B

ax.quiver(start[0], start[1], start[2], B1[0], B1[1], B1[2])
ax.quiver(start[0], start[1], start[2], B2[0], B2[1], B2[2], color = "g")
ax.quiver(start[0], start[1], start[2], B3[0], B3[1], B3[2], color = "r")

#Suma de los vectores

ax.quiver(start[0], start[1], start[2], C1[0], C1[1], C1[2])
ax.quiver(start[0], start[1], start[2], C2[0], C2[1], C2[2], color = "g")
ax.quiver(start[0], start[1], start[2], C3[0], C3[1], C3[2], color = "r")