import sys, pygame
pygame.init()

#STUB :
def snake_movement():
    pass
def movement_effect():
    pass

#Affichage de la fenêtre avec une dimension de 440 * 440 donc 40 pixels par case.
size = width, height = 440, 440
black = 0,0,0 # -> Noir = 0
red = 255,0,0 # -> Rouge = 1
green = 0,128,0 # -> Vert = 2
brown = 117,88,71 # -> Marron = 3

#Coloration_Tab :
#Rangés dans l'ordre
#[[colone1],[colone2]...]
Coloration_Tab = [ [ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ] , [ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ] , [ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ] , [ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ] , [ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ] , [ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ] , [ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ] , [ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ] , [ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ] , [ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ] , [ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ] ]
screen = pygame.display.set_mode(size)

#Fonction pour reset l'écran en noir si besoin
def reset_screen_in_black():
    pygame.display.flip()
    screen.fill(black)

#Déf de fonction coloré une case
def color_case_xy(x,y,color): #x,y sont les coordonnés directement, pas le numéro de la case.
    case=pygame.Surface((40, 40))
    case.fill((color))
    screen.blit(case, (x, y))

def color_case(case_in_x,case_in_y,color): #case de 0 à 10 (11 cases) pour x et y
    color_case_xy(case_in_x*40,case_in_y*40,color)

#Définition du titre de l'app
pygame.display.set_caption('Snake Game')

#Fermeture de l'app
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    #STUB
    snake_movement()
    movement_effect()
    #code
    reset_screen_in_black()
    for casex in range (11):
        for casey in range (11):
            if Coloration_Tab[casex][casey]==0:
                color_case(casex,casey,black)
            if Coloration_Tab[casex][casey]==1:
                color_case(casex,casey,red)
            if Coloration_Tab[casex][casey]==2:
                color_case(casex,casey,green)  
            if Coloration_Tab[casex][casey]==3:
                color_case(casex,casey,brown)  

