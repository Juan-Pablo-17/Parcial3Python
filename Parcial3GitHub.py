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


A = SquareMatrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
B = Matrix([[1, 0, -2], [0, 1, 0], [1, 2, -2]])
C_1 = SquareMatrix([[-11, 5, -4, 3], [10, -3, 4, -2], [6, -2, 2, -1]])
print(A * B * C_1)
print()
print(A+B)
print()
print(A.transpuesta())
print()

#==============================================================
#Gráficas
#==============================================================

fig = plt.figure('Gráfica')
ax = Axes3D(fig)

x = np.linspace(-4, 4, 50)
y = np.linspace(-4, 4, 50)

def z(x, y):
    return np.sin(np.sqrt(x**2 + y**2))

ax.plot(x, y, z(x, y))
plt.show()