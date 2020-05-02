import sys, pygame

#13 lignes de 13 car on entoure par une couche set a 3 exprimant la bordure
        #0 : vide
        #1: snake body
        #2: head
        #3: apple
        #-1: border
class Matrix:
    def __init__(self,x=11,y=11):   #Crée en fonction du nombre de colonne et de ligne que l'on veut une matrice
                            #initialisée a 11 de baes mais peut être modulable : y = nb_colonne x = nb_ligne
        self.colonne= y
        self.ligne= x
        self.matrix= []
        for i in range(y):
            self.matrix.append([])
            for j in range(x):
                if i == 0 or i == y-1 or j == 0 or j == x-1 :
                    self.matrix[i].append(-1)
                else:
                    self.matrix[i].append(0)

    def getMatrix(self):
        return self.matrix

    def printMatrix(self):
        for i in range(self.colonne):
            print("")
            print("[",end='')
            for j in range(self.ligne):
                print(" "+str(self.matrix[i][j]),end='')
            print("]",end='')

    def setMatrix(self,new_matrix):
        for i in range(self.colonne):
            for j in range(self.ligne):
                self.matrix[i][j]=new_matrix[i][j]

    def setByPosMatrix(self,y,x,valeur):
        self.matrix[y][x]= valeur

matrix=Matrix()
matrix.printMatrix()
