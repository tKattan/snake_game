import sys, pygame, snake_func
pygame.init()

RIGHT = 0
DOWN = 1
LEFT = 2
UP = 3

#STUB :
def snake_movement():
    pass
def movement_effect():
    pass

#Affichage de la fenêtre avec une dimension de 440 * 440 donc 40 pixels par case.
size = width, height = 880, 880
black = 0, 0, 0 # -> Noir = 0
brown = 117, 88, 71 # -> Marron = 1
red = 255, 0, 0 # -> Rouge = 2
green = 0, 128, 0 # -> Vert = 3
#score and start
player_score = 0
in_restart_menu=True

#color matrix and screen
color_matrix = snake_func.Matrix(13,13)
screen = pygame.display.set_mode(size)
press_enter= pygame.image.load('press_enter.png')
score= pygame.image.load('score.png')
numberdraw=[None]*10
numberdraw[0]=pygame.image.load('0.png')
numberdraw[1]=pygame.image.load('1.png')
numberdraw[2]=pygame.image.load('2.png')
numberdraw[3]=pygame.image.load('3.png')
numberdraw[4]=pygame.image.load('4.png')
numberdraw[5]=pygame.image.load('5.png')
numberdraw[6]=pygame.image.load('6.png')
numberdraw[7]=pygame.image.load('7.png')
numberdraw[8]=pygame.image.load('8.png')
numberdraw[9]=pygame.image.load('9.png')

#snake
snake = snake_func.Snake(3, [5, 5])

# apple
apple = snake_func.Apple(color_matrix)

#Fonction pour reset l'écran en noir si besoin
def reset_screen_in_black():
    pygame.display.flip()
    screen.fill(black)

#Déf de fonction coloré une case
def color_case_xy(cord_x,cord_y,color): #x,y sont les coordonnés directement, pas le numéro de la case.
    case=pygame.Surface((80, 80))
    case.fill((color))
    screen.blit(case, (cord_x, cord_y))

#Pour changer la couleur d'une case, changez les de x=1 à 11 et y=1 à 11, ne pas toucher 0 et 12 avec color_matrix.setByPosMatrix
def color_case(case_in_x,case_in_y,color): #case de 0 à 10 (11 cases) pour x et y
    color_case_xy(case_in_x*80,case_in_y*80,color)

#Définition du titre de l'app
pygame.display.set_caption('Snake Game')
#Fermeture de l'app
while 1:
    #in menu
    if in_restart_menu:
        screen.blit(press_enter,(300,400))
        screen.blit(score,(0,0))
        score_len=len(str(player_score))
        print(score_len)
        for draw_score in range (1,score_len+1):
            last_number=player_score%10
            screen.blit(numberdraw[last_number],(200+35*(score_len-draw_score),0))
            player_score=player_score//10
        
    while in_restart_menu==True:
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP_ENTER: 
                    player_score=0
                    clearMatrix()
                    #there is no function to reset the snake here.   *****
                    apple.setNewApple(snake.size)
                    in_restart_menu=False
            if event.type == pygame.QUIT: 
                sys.exit()

    #exiting game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    #STUB
    snake_movement()
    movement_effect()
    #Apple eated
    #futureheadpos is not coded on my part so i set this in comment.  *****
    #if apple.isAppleEated(futureHeadPos, snake_size):                *****
    #    player_score = player_score + 1                              *****

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
    #if gameloose, you just have to put in_restart_menu=true         *****
    #again, its in us5 so we have to add it later.                   *****
    
