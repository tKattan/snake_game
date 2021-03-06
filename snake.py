import sys
import pygame
import snake_func
import time

pygame.init()
#Affichage de la fenêtre avec une dimension de 440 * 440 donc 40 pixels par case.
size = width, height = 880, 880
screen = pygame.display.set_mode(size)

RIGHT = 0
DOWN = 1
LEFT = 2
UP = 3

#STUB :
def snake_movement(direction):
    if snake.checkHeadInBody(direction):
        return False
        
    new_pos = snake.futureUpdateHead(direction)
    if color_matrix.getByPosMatrix(new_pos[0], new_pos[1]) == -1:
        return False
    return True

def back_in_body(direction):
    new_head = snake.futureUpdateHead(direction)
    if new_head == snake.getTail()[0]:
        return True
    return False

def movement_effect(direction, isAppleEated):
    snake.updateSnake(direction, isAppleEated)
    sTail = snake.getTail()
    for i in sTail:
        color_matrix.setByTuplePosMatrix(i, 1)
    color_matrix.setByTuplePosMatrix(snake.posHead, 2)
    if isAppleEated:
        apple.setNewApple(snake.size)
    else:
        color_matrix.setByTuplePosMatrix(apple.getPos(),3)

black = 0, 0, 0 # -> Noir = 0
brown = 117, 88, 71 # -> Marron = 1
red = 255, 0, 0 # -> Rouge = 2
green = 0, 128, 0 # -> Vert = 3
#score and start
player_score = 0
in_restart_menu = True

#color matrix and screen
color_matrix = snake_func.Matrix(13,13)
press_enter = pygame.image.load('press_enter.png')
score = pygame.image.load('score.png')
numberdraw = [None]*10
numberdraw[0] = pygame.image.load('0.png')
numberdraw[1] = pygame.image.load('1.png')
numberdraw[2] = pygame.image.load('2.png')
numberdraw[3] = pygame.image.load('3.png')
numberdraw[4] = pygame.image.load('4.png')
numberdraw[5] = pygame.image.load('5.png')
numberdraw[6] = pygame.image.load('6.png')
numberdraw[7] = pygame.image.load('7.png')
numberdraw[8] = pygame.image.load('8.png')
numberdraw[9] = pygame.image.load('9.png')

#snake
snake = snake_func.Snake(3, [5, 5])

# apple
apple = snake_func.Apple(color_matrix)

#Fonction pour reset l'écran en noir si besoin
def reset_screen_in_black():
    pygame.display.flip()
    screen.fill(black)
    
#Fonction qui met une case vide si elle n'appartient plus au serpent ou à la pomme
def update_matrix(x_cord,y_cord):
    if not [x_cord,y_cord] in snake.getTail() and not [x_cord,y_cord] == snake.getHead() and apple.getPos() != (x_cord, y_cord):
        color_matrix.setByTuplePosMatrix([x_cord,y_cord],0)
    

#Déf de fonction coloré une case
#x, y sont les coordonnés directement, pas le numéro de la case.
def color_case_xy(cord_x, cord_y, color): 
    case = pygame.Surface((80, 80))
    case.fill((color))
    screen.blit(case, (cord_x, cord_y))

# Pour changer la couleur d'une case, changez les de x=1 à 11 et y=1 à 11, ne pas
# toucher 0 et 12 avec color_matrix.setByPosMatrix
def color_case(case_in_x, case_in_y, color): #case de 0 à 10 (11 cases) pour x et y
    color_case_xy(case_in_x*80,case_in_y*80,color)

#Définition du titre de l'app
pygame.display.set_caption('Snake Game')

directionOfMovement = UP

#actualisation
refreshInS = 0.100
start = time.time()

#Fermeture de l'app
while 1:
    #in menu
    if in_restart_menu:
        screen.blit(press_enter, (300,400))
        screen.blit(score, (0,0))
        if player_score != 0:
            player_score-=3 #queue initiale = 3 
        score_len = len(str(player_score))
        for draw_score in range (1,score_len+1):
            last_number = player_score%10
            screen.blit(numberdraw[last_number],(200+35*(score_len-draw_score),0))
            player_score = player_score//10

    while in_restart_menu == True:
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN: 
                    player_score = 0
                    color_matrix.clearMatrix()
                    snake.resetSnake(3, [5, 5])
                    apple.setNewApple(snake.size)
                    directionOfMovement = RIGHT
                    in_restart_menu=False
            if event.type == pygame.QUIT: 
                sys.exit()

    #exiting game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and not back_in_body(UP):
                directionOfMovement = UP
            if event.key == pygame.K_DOWN and not back_in_body(DOWN):
                directionOfMovement = DOWN
            if event.key == pygame.K_LEFT and not back_in_body(LEFT):
                directionOfMovement = LEFT
            if event.key == pygame.K_RIGHT and not back_in_body(RIGHT):
                directionOfMovement = RIGHT
        
    if time.time()-start >= refreshInS:
        start = time.time()
        if snake_movement(directionOfMovement):
            if apple.isAppleEated(snake.futureUpdateHead(directionOfMovement)):
                movement_effect(directionOfMovement, True)
                player_score = snake.size
            else:
                movement_effect(directionOfMovement, False)
        else:
            in_restart_menu = True
        #code d'affichage

    reset_screen_in_black()
    for x in range (1,color_matrix.getNumberOfLigne()-1):
        for y in range (1,color_matrix.getNumberOfColumns()-1):
            update_matrix(x,y)
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

            
