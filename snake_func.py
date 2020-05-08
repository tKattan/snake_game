import sys, pygame

#13 lignes de 13 car on entoure par une couche set a -1 exprimant la bordure
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

    def setByPosMatrix(self,x,y,valeur):
        self.matrix[y][x]= valeur

    def getNumberOfLigne():
        return self.colonne
        
    def getNumberOfColumns():
        return self.ligne


class Snake:
    #Initialisation de l'Objet snake, on insere sa taille au debut, la position de sa tete (position qui sera mettre dans une matrice donc ce n'est pas en pixel
    # mais en emplacement)
    def __init__(self,size_init=3, posHead = [5,5]):
        self.size = size_init
        self.posTail = []
        self.posHead = posHead
        print(self.posHead[0])
        for i in range(1,size_init+1):
            if posHead[0]-i < 0:
                print("Snake init failed, cause : not enough space for the tail\n(Snake init -> Tail is on the left of the head)")
                sys.exit("System Exit")
            else:
                self.posTail.append([posHead[0]-i,posHead[1]])

    def setHead(self,new_pos):
        self.posHead = new_pos
    def setTail(self,new_pos):
        self.posTail = new_pos

    def getHead(self):
        return self.posHead
    def getTail(self):
        return self.posTail

