import pygame, random,sys , math, time

#Initialize pygame
pygame.init()

#Set display surface
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 700
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Ronaldo vs Neuer")

#Set FPS and clock
FPS = 60
clock = pygame.time.Clock()

#Set fonts
font = pygame.font.Font("freesansbold.ttf", 32)

#Colors
RED = (255, 0, 0)
BLUE = (1, 175, 209)

#Set initial values
score = 0
hit_ratio = 100
hit = 0
miss = 0
current_time = 2000
pass_time = 0
blue_or_green = 1
PLAYER_STARTING_LIVES = 5
siu_1lan = 1


# backgroung at wait screen
startGame = True
start_game_bg_1 =pygame.image.load('start_game_1.jpg')
start_game_1_rect = start_game_bg_1.get_rect()

start_game_bg_2 =pygame.image.load('start_game_2.png')
start_game_2_rect = start_game_bg_2.get_rect()

#rectangle bound around play button

buttonRect = pygame.Rect(510, 463, 268, 204)


#Set hub
player_live = PLAYER_STARTING_LIVES
score_text = font.render("Score: " + str(score), True, RED)
score_rect = score_text.get_rect()
score_rect.topleft = (5, 10)

player_text = font.render("Live: " + str(PLAYER_STARTING_LIVES), True, RED)
player_rect = player_text.get_rect()
player_rect.topleft = (5, 40)

hit_text = font.render("Hit ratio: " + str(hit_ratio) + "%", True, RED)  
hit_rect = hit_text.get_rect()
hit_rect.topright = (WINDOW_WIDTH - 5, 10)

game_over_text = font.render("GAME OVER", True, BLUE, RED)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 - 64)

continue_text = font.render("Press space to play again", True, RED, BLUE)
continue_rect = continue_text.get_rect()
continue_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

score_record_text = font.render("Your score is: " + str(score), True, RED, BLUE)
score_record_rect = score_record_text.get_rect()
score_record_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 64)

#Set images
# siuuuuu
ronaldo_image = pygame.image.load("ronaldo_siu.png")
ronaldo_image = pygame.transform.scale(ronaldo_image, (ronaldo_image.get_width()*2.5, ronaldo_image.get_height()*2.5))
#background image
background_image = pygame.image.load("sanbong.jpg")
background_rect = background_image.get_rect()
background_rect.topleft = (0, 0)

#score image
score_ronaldo_image = pygame.image.load("anmung.png")
score_ronaldo_image = pygame.transform.scale(score_ronaldo_image, (score_ronaldo_image.get_width()/2, score_ronaldo_image.get_height()/2))
score_ronaldo_rect = score_ronaldo_image.get_rect()
score_ronaldo_rect.bottomright = (1200, 700)


#right enemy image
mob_image = pygame.image.load("khungthanh.png")
mob_image = pygame.transform.scale(mob_image, (mob_image.get_width()/3, mob_image.get_height()/3))
mob_rect = mob_image.get_rect()

#afer click
mob_image_after = pygame.image.load("bongtungluoi.png")
mob_image_after = pygame.transform.scale(mob_image_after, (mob_image_after.get_width()/3, mob_image_after.get_height()/3))

#Make the first appearance out of screen
mob_rect.x = -100
mob_rect.y = -100

#wrong enemy
blue_mob_image = pygame.image.load("neuer_1.png")
blue_mob_image = pygame.transform.scale(blue_mob_image, (blue_mob_image.get_width()/3, blue_mob_image.get_height()/3))
blue_mob_rect = blue_mob_image.get_rect()


#after click
blue_mob_image_after = pygame.image.load("neuer.png")
blue_mob_image_after = pygame.transform.scale(blue_mob_image_after, (blue_mob_image_after.get_width()/3, blue_mob_image_after.get_height()/3))

#Make the first appearance out of screen
blue_mob_rect.x = -100
blue_mob_rect.y = -100

#Hammer image=>>ball
hammer_image = pygame.image.load("quabong.png")
hammer_image_x = hammer_image.get_width()
hammer_image = pygame.transform.scale(hammer_image, (hammer_image.get_width()/8, hammer_image.get_height()/8))
hammer_rect = hammer_image.get_rect()
#Make the first appearance out of screen
hammer_rect.centerx = -100
hammer_rect.centery = -100

#where zombie appearance
appearance_image = pygame.image.load("noixuathien.png")
appearance_rect_1 = pygame.Rect(255-100,100-60,70,70)
appearance_rect_2 = pygame.Rect(255-100,350-60,70,70)
appearance_rect_3 = pygame.Rect(555-100,100-60,70,70)
appearance_rect_4 = pygame.Rect(555-100,350-60,70,70)
appearance_rect_5 = pygame.Rect(255-100,600-60,70,70)
appearance_rect_6 = pygame.Rect(855-100,100-60,70,70)
appearance_rect_7 = pygame.Rect(855-100,600-60,70,70)
appearance_rect_8 = pygame.Rect(555-100,600-60,70,70)
appearance_rect_9 = pygame.Rect(855-100,350-60,70,70)

#Create a matrix to store mouse easily
#0: nothing here
#1: Messi = 1 (+1 when hit)
#2: Zombie = -1 (-1 when hit)
list_matrix = [0,1,2]

inButton = 0
while startGame :
    if not inButton :
        display_surface.blit(start_game_bg_1,background_rect)
    mouse_x, mouse_y = pygame.mouse.get_pos()
    for event in pygame.event.get():
        #Check to see if player move the mouse
        if event.type == pygame.MOUSEMOTION:
            if buttonRect.collidepoint(mouse_x, mouse_y) :
                inButton = 1
                display_surface.blit(start_game_bg_2,background_rect)
            else :
                inButton = 0
        #Check player right click
        if event.type == pygame.MOUSEBUTTONUP:
            if buttonRect.collidepoint(mouse_x, mouse_y) :
                startGame = False
                break
        #Check to see if the user wants to quit
        if event.type == pygame.QUIT:
            #End the game
            pygame.quit() 
            sys.exit()
    pygame.display.update()


#Set sound and music
hit_sound = pygame.mixer.Sound("Hit_sound.wav")
lose_sound = pygame.mixer.Sound("Lose_sound.wav")
game_over_sound = pygame.mixer.Sound("Gameover_sound.wav")
cr7_sound = pygame.mixer.Sound("Ronaldo.wav")
pygame.mixer.music.load("wc_music.wav")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1, 0.0)

running = True
while running:  
    
    current_time = pygame.time.get_ticks()
    while (current_time - pass_time > 1500):
        pass_time = current_time
        #1 is green
        #-1 is blue
        blue_or_green = random.choice([1, 2, 3])
        
        #decide where Mob will spawn
        mob_x = random.choice(list_matrix)
        mob_y = random.choice(list_matrix)
        
        if blue_or_green == 1 or blue_or_green == 2:
            mob_rect.centerx = 300*mob_x + 255
            mob_rect.centery = 240*mob_y + 120
            
        else:
            blue_mob_rect.centerx = 300*mob_x + 255
            blue_mob_rect.centery = 240*mob_y + 90
        
    #get mouse position constantly
    mouse_x, mouse_y = pygame.mouse.get_pos()
    #Attach hammer to mouse
    
    #Check event of the game
    for event in pygame.event.get():
        #Check to see if player move the mouse
        if event.type == pygame.MOUSEMOTION:
            hammer_rect.centerx = mouse_x
            hammer_rect.centery = mouse_y

        #Check to see if the user wants to quit
        if event.type == pygame.QUIT:
            running = False
            
        #Check player right click
        if event.type == pygame.MOUSEBUTTONUP:
            
            #Hit the blue mob
            if hammer_rect.collidepoint(blue_mob_rect.centerx, blue_mob_rect.centery):
                #time.sleep(0.3)
                display_surface.blit(blue_mob_image_after, blue_mob_rect)
                pygame.display.update()
                time.sleep(0.2)
                #Draw another mob
                pass_time = current_time
                
                blue_or_green = random.choice([1, 2, 3])
        
                #decide where Mob will spawn
                mob_x = random.choice(list_matrix)
                mob_y = random.choice(list_matrix)
        
                if blue_or_green == 1 or blue_or_green == 2:
                    mob_rect.centerx = 300*mob_x + 255
                    mob_rect.centery = 240*mob_y + 120
            
                else:
                    blue_mob_rect.centerx = 300*mob_x + 255
                    blue_mob_rect.centery = 240*mob_y + 90
                    
            
            #Hit normal mob
            if hammer_rect.collidepoint(mob_rect.centerx, mob_rect.centery):
                hit_sound.play()
                score += 1
                hit += 1
                hit_ratio = round(hit/(hit + miss) * 100)
                #time.sleep(0.3)#################
                display_surface.blit(mob_image_after, mob_rect)
                display_surface.blit(score_ronaldo_image, score_ronaldo_rect)
                pygame.display.update()
                time.sleep(0.2)
                
                #Draw another mob
                pass_time = current_time
                
                blue_or_green = random.choice([1, 2, 3])
        
                #decide where Mob will spawn
                mob_x = random.choice(list_matrix)
                mob_y = random.choice(list_matrix)
        
                if blue_or_green == 1 or blue_or_green == 2:
                    mob_rect.centerx = 300*mob_x + 255
                    mob_rect.centery = 240*mob_y + 120
            
                else:
                    blue_mob_rect.centerx = 300*mob_x + 255
                    blue_mob_rect.centery = 240*mob_y + 90
            else:
                lose_sound.play()
                miss += 1
                hit_ratio = round(hit/(hit + miss) * 100)
                player_live -= 1
         
    #Update HUD
    score_text = font.render("Score: " + str(score), True, RED)    
    player_text = font.render("Live: " + str(player_live), True, RED)   
    hit_text = font.render("Hit ratio: " + str(hit_ratio) + "%", True, RED)    
    score_record_text = font.render("Your score is: " + str(score), True, RED, BLUE)
    
    center_bg_Rect = pygame.Rect(246,5,400,695)
    if(score == 7) :
      if siu_1lan:
        display_surface.blit(ronaldo_image, center_bg_Rect)  
        cr7_sound.play() 
        siu_1lan = 0
       # pygame.mixer.music.pause()
        pygame.display.update()
        pygame.mixer.music.pause()
        time.sleep(2)
        pygame.mixer.music.unpause()
   
  
    if (player_live == 0):
        pygame.mixer.music.stop()
        game_over_sound.play()
        
        display_surface.fill((0,0,0))
        display_surface.blit(game_over_text, game_over_rect)
        display_surface.blit(continue_text, continue_rect)
        display_surface.blit(score_record_text, score_record_rect)
        pygame.display.update()

        #Pause the game until the player clicks then reset the game
        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                #The player wants to play again.
                if event.type == pygame.KEYDOWN:
                    if (event.key == pygame.K_SPACE):
                        #setup as the begin
                        hammer_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)
                        hit = 0
                        miss = 0
                        hit_ratio = 0
                        score = 0
                        player_live = PLAYER_STARTING_LIVES
                        is_paused = False  
                        game_over_sound.stop()
                        pygame.mixer.music.play(-1, 0.0)          
     
                #The player wants to quit
                if event.type == pygame.QUIT:
                    is_paused = False
                    running = False
          
    #Blit the background
    display_surface.blit(background_image, background_rect)
    display_surface.blit(appearance_image, appearance_rect_1 )
    display_surface.blit(appearance_image, appearance_rect_2 )
    display_surface.blit(appearance_image, appearance_rect_3 )
    display_surface.blit(appearance_image, appearance_rect_4 )
    display_surface.blit(appearance_image, appearance_rect_5 )
    display_surface.blit(appearance_image, appearance_rect_6 )
    display_surface.blit(appearance_image, appearance_rect_7 )
    display_surface.blit(appearance_image, appearance_rect_8 )
    display_surface.blit(appearance_image, appearance_rect_9 )
                     
    #Blit HUD             
    display_surface.blit(score_text, score_rect)
    display_surface.blit(player_text, player_rect)
    display_surface.blit(hit_text, hit_rect)
    
    #Blit assets
    if blue_or_green == 1 or blue_or_green == 2:
        display_surface.blit(mob_image, mob_rect)

    else:
        display_surface.blit(blue_mob_image, blue_mob_rect)
    
    display_surface.blit(hammer_image, hammer_rect) 

           
    #Update the display and tick clock
    pygame.display.update()
    clock.tick(FPS)
    
    
#End the game
pygame.quit()