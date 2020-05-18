import sys, pygame, snake_func, apple
pygame.init()

RIGHT= 0
DOWN= 1
LEFT= 2
UP= 3

#STUB :
def snake_movement():
    pass
def movement_effect():
    pass

#Affichage de la fenêtre avec une dimension de 440 * 440 donc 40 pixels par case.
size = width, height = 880, 880
black = 0,0,0 # -> Noir = 0
brown = 117,88,71 # -> Marron = 1
red = 255,0,0 # -> Rouge = 2
green = 0,128,0 # -> Vert = 3

#color matrix and screen
color_matrix = snake_func.Matrix(13,13)
screen = pygame.display.set_mode(size)

#apple exemple
#!!!!! à modifier avec la vrai direction et vrai pos de la tête
apple=apple.Apple(3,RIGHT,(8,8),13,13)
apple.setNewApple(color_matrix,3)

#Fonction pour reset l'écran en noir si besoin
def reset_screen_in_black():
    pygame.display.flip()
    screen.fill(black)

#Déf de fonction coloré une case
def color_case_xy(x,y,color): #x,y sont les coordonnés directement, pas le numéro de la case.
    case=pygame.Surface((80, 80))
    case.fill((color))
    screen.blit(case, (x, y))

#Pour changer la couleur d'une case, changez les de x=1 à 11 et y=1 à 11, ne pas toucher 0 et 12 avec color_matrix.setByPosMatrix
def color_case(case_in_x,case_in_y,color): #case de 0 à 10 (11 cases) pour x et y
    color_case_xy(case_in_x*80,case_in_y*80,color)

#Définition du titre de l'app
pygame.display.set_caption('Snake Game')
#Fermeture de l'app
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    #STUB
    snake_movement()
    movement_effect()
    #code d'affichage
    reset_screen_in_black()
    for x in range (1,color_matrix.getNumberOfLigne()-1):
        for y in range (1,color_matrix.getNumberOfColumns()-1):
            if color_matrix.getMatrix()[x][y]==-1:
                color_case(x-1,y-1,red)
            if color_matrix.getMatrix()[x][y]==0:
                color_case(x-1,y-1,black)
            if color_matrix.getMatrix()[x][y]==1:
                color_case(x-1,y-1,brown)  
            if color_matrix.getMatrix()[x][y]==2:
                color_case(x-1,y-1,red)
            if color_matrix.getMatrix()[x][y]==3:
                color_case(x-1,y-1,green)

