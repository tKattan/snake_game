import sys, pygame, random
#prérequis : avoir générer la map et le serpent avant
RIGHT= 0
DOWN= 1
LEFT= 2
UP= 3

class Apple:
    #x et y sont la taille du terrain, bordure comprise (donc pour terrain jouable 11x11 -> 13x13)
    #attention de respecter une taille minimum de taille exploitable de 1 (ce qui est logique aussi pour le serpent)
    def __init__(self,snake_size,direction,snake_head_pos,x=13,y=13):  
        self.ligne= y
        self.colonne= x
        self.landsize=(x-2)*(y-2)-1 #on fait -2 pour enlever les bordures.
        self.snake_size=snake_size

    def searchRandomEmptyCase(self,color_matrix,snake_size):
        i=0
        applepos=random.randint(1,self.landsize-snake_size-1) #genere une pomme aléatoirement sur le terrain
        for x in range (1,self.colonne-1):
            for y in range (1,self.ligne-1):
                if color_matrix.matrix[x][y]==0:
                    i=i+1
                if i==applepos:
                    return x,y

    def setNewApple(self,color_matrix,snake_size):
        x,y=self.searchRandomEmptyCase(color_matrix,snake_size)
        color_matrix.matrix[x][y]=3

#la taille du serpent doit être actualisé après l'appel de cette fonction
#elle génère directement une nouvelle pomme.
    def isAppleEated(self,color_matrix,direction,snake_head_pos,snake_size):
        x,y=snake_head_pos
        if direction==UP:
            y=y-1
        elif direction==DOWN:
            y=y+1
        elif direction==LEFT:
            x=x-1
        elif direction==RIGHT:
            x=x+1    
        if color_matrix[x][y]==3:
            self.setNewApple(color_matrix,snake_size)
            return True
        else:
            return False
        