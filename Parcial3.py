###Pide al usuario el rango de la matríz y, cada elemento por 
###componente de fila y columna. 
def matriz (filas, columnas):
    matriz=[]
    for i in range(filas):
        matriz.append([])
        for j in range(columnas):
            valor=eval(input("Fila {}, Columna {} :".format(i+1, j+1)))
            matriz[i].append(valor)
    return matriz
### Imprime las o la matríz ingresada en la función anterior 
### Necesario para visualizar la función anterior
def imprimir_matriz (matriz):
    for fila in matriz:
        print("[", end=(""))
        for elemento in fila:
            print("{:8.2f}".format(elemento), end=(""))
        print("]")
###Ejemplo: from Lineal import matriz, imprimir_matriz
###         A=matriz(2,2) - Definne el rango de la matriz A.
###         B=matriz(2,2) - Define el rango de la matriz B. 
###         imprimir_matriz(A) - Imprime la matríz A.
###         print() - Separción entre matrices. 
###         imprimir_matriz(B) - Imprime la matríz matríz B.

### Suma dos matrices sacadas con la primera función de matrices.
def suma (matriz1, matriz2):
    if len(matriz1)==len(matriz2) and len(matriz1[0])==len(matriz2[0]):
        C=[]
        for i in range (len(matriz1)):
            C.append([])
            for j in range (len(matriz1[0])):
                C[i].append(matriz1[i][j]+matriz2[i][j])
        return C

###Imprime la función "suma" (Necesario para visualizar.)
def imprimir_suma (suma):
    for matriz3 in suma:
        print("[", end=(""))
        for elemento in matriz3:
            print("{:8.2f}".format(elemento), end=(""))
        print("]")
###Ejemplo:  from Lineal import matriz, imprimir_matriz, suma, imprimir_suma
###          A=matriz(2,2) - Matríz A
###          B=matriz(2,2) - Matríz B
###          imprimir_matriz(A) - Imprime la metríz A
###          print() - Separación entre matríces.
###          imprimir_matriz(B) - Imprime la matríz B
###          print() - Separación entre matríces
###          e=suma(A,B) - Nueva matríz, resultado de A+B.
###          imprimir_suma(e) - Imprime la nueva matríz.

### Multiplica dos matrices de igual rango (matrices de la primera función.)
def mult_matriz(mat1, mat2):
    if len(mat1)==len(mat2[0]): 
        mat3=[]
        for i in range(len(mat1)):
            mat3.append([])
            for j in range(len(mat1[0])):
                mat3[i].append(0)

        for i in range (len(mat1[0])):
            for j in range (len(mat2)):
                for k in range (len(mat1[0])):
                    mat3[i][j] += mat1[i][k]*mat2[k][j]
        return mat3

### Imprime la función "mult_matriz" (Necesario importar para ver el resultado.)
def imprimir_mult (mult_matriz):
    for matriz4 in mult_matriz:
        print("[", end=(""))
        for elemento in matriz4:
            print("{:8.2f}".format(elemento), end=(""))
        print("]")

### Ejemplo: from Lineal import matriz, imprimir_matriz, mult_matriz, imprimir_mult
A=matriz(2,2) #- Matríz A solicitada de rango 2x2
B=matriz(2,2) #- Matriz B solicitada de rango 2x2
imprimir_matriz(A) #- Imprime la matriz A
print() #- Espacio de sepación entre matrices
imprimir_matriz(B) #- Imprime la matríz B
print() #- Espacio de separación entre matrices
C=mult_matriz(A,B) #- Función que multiplica las matrices A*B (importante ponerla como varible.)
imprimir_mult(C)#- Imprime la multiplicación entre A*B