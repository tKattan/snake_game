import sys, random

#11 lignes de 11 car on entoure par une couche set a -1 exprimant la bordure
        #0 : vide
        #1: snake body
        #2: head
        #3: apple
        #-1: border

RIGHT= 0
DOWN= 1
LEFT= 2
UP= 3

class Matrix:
    def __init__(self, nb_lines = 11, nb_columns = 11):  
        # Crée en fonction du nombre de ligne et de colonne que l'on veut une matrice
        # initialisée a 11 de base mais peut être modulable : y = nb_ligne x = nb_colonne 
        self.ligne = nb_lines
        self.colonne = nb_columns
        self.matrix= []

        for i in range(nb_lines):
            self.matrix.append([])
            for j in range(nb_columns):
                if i == 0 or i == nb_lines-1 or j == 0 or j == nb_columns-1 :
                    self.matrix[i].append(-1)
                else:
                    self.matrix[i].append(0)
        
        self.playableLandsize = (self.ligne - 2) * (self.colonne - 2)

    def getMatrix(self):
        return self.matrix

    def printMatrix(self):
        for i in range(self.ligne):
            print("")
            print("[",end='')
            for j in range(self.colonne):
                print(" "+str(self.matrix[i][j]),end='')
            print("]",end='')
    
    def clearMatrix(self):
        for i in range(self.ligne):
            for j in range(self.colonne):
                if i == 0 or i == self.ligne-1 or j == 0 or j == self.colonne-1 :
                    self.matrix[i][j]=-1
                else:
                    self.matrix[i][j]=0

    def setMatrix(self,new_matrix):
        for i in range(self.ligne):
            for j in range(self.colonne):
                self.matrix[i][j]=new_matrix[i][j]

    def setByPosMatrix(self,x,y,valeur):
        self.matrix[y][x]= valeur

    def getByPosMatrix(self,x,y):
        return self.matrix[y][x]

    def getNumberOfLigne(self):
        return self.ligne

    def getNumberOfColumns(self):
        return self.colonne

    def getPlayableCells(self):
        return self.playableLandsize


class Snake:
    #Initialisation de l'Objet snake, on insere sa taille au debut, la position de sa tete (position qui sera mettre dans une matrice donc ce n'est pas en pixel
    # mais en case)
    def __init__(self, size_init, posHead):
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


    def updateSnake(self, direction = RIGHT, speed = 1): #Les constantes de direction sont définies en haut du fichier
        last_head = self.getHead()
        last_tail = self.getTail()
        new_tail = []
        if direction == LEFT:
            self.setHead([last_head[0]-speed,last_head[1]])
        elif direction == RIGHT:
            self.setHead([last_head[0]+speed,last_head[1]])
        elif direction == UP:
            self.setHead([last_head[0],last_head[1]-speed])
        elif direction == DOWN:
            self.setHead([last_head[0],last_head[1]+speed])

        #la premiere partie de Tail va a la pos de l'ancienne position de head,
        new_tail.append([last_head[0],last_head[1]])    
        
        # les autres morceaux de tail vont la place du morceau avant lui exeple : morceau 1 va a la place du morceau 0
        for i in range(self.size-1):
            new_tail.append(last_tail[i])

        self.setTail(new_tail)

    def setHead(self,new_pos):
        self.posHead = new_pos
    def setTail(self,new_tail):
        self.posTail = new_tail
    
    def getHead(self):
        return self.posHead
    def getTail(self):
        return self.posTail


class Apple:
    # x et y sont la taille du terrain, bordure comprise (donc pour terrain jouable 11x11 -> 13x13)
    # attention de respecter une taille minimum de taille exploitable de 1 (ce qui est logique aussi pour le serpent)
    def __init__(self, color_matrix):  
        self.color_matrix = color_matrix
        

    def setNewApple(self, snake_size):
        i = 0

        applepos = random.randint(0, self.color_matrix.getPlayableCells() - snake_size) #genere une pomme aléatoirement sur le terrain

        for x in range(1, self.color_matrix.getNumberOfColumns()):
            for y in range(1, self.color_matrix.getNumberOfLigne()):
                if self.color_matrix.getByPosMatrix(x, y) == 0:
                    i = i + 1
                if i == applepos:
                    self.color_matrix.setByPosMatrix(x, y, 3)

# la taille du serpent doit être actualisé après l'appel de cette fonction
# elle génère directement une nouvelle pomme.
    def isAppleEated(self, futureHeadPos, snake_size):
        if self.color_matrix.getByPosMatrix(futureHeadPos[0], futureHeadPos[1]) == 3:
            self.setNewApple(snake_size)
            return True
        else:
            return False
        