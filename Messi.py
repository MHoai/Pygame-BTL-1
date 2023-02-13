import pygame, random, math, time

#Initialize pygame
pygame.init()

#Set display surface
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 528
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("FOOTBALL GAME (basically)")

#Set FPS and clock
FPS = 60
clock = pygame.time.Clock()

#Set fonts
font = pygame.font.Font("Franxurter.ttf", 32)

#Colors
YELLOW = (248, 231, 28)
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

#Set hub
player_live = PLAYER_STARTING_LIVES
score_text = font.render("Score: " + str(score), True, YELLOW)
score_rect = score_text.get_rect()
score_rect.topleft = (5, 10)

player_text = font.render("Live: " + str(PLAYER_STARTING_LIVES), True, YELLOW)
player_rect = player_text.get_rect()
player_rect.topleft = (5, 40)

hit_text = font.render("Hit ratio: " + str(hit_ratio) + "%", True, YELLOW)  
hit_rect = hit_text.get_rect()
hit_rect.topright = (WINDOW_WIDTH - 5, 10)

game_over_text = font.render("GAMEOVER", True, BLUE, YELLOW)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 - 64)

continue_text = font.render("Press space to play again", True, YELLOW, BLUE)
continue_rect = continue_text.get_rect()
continue_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

score_record_text = font.render("Your score is: " + str(score), True, YELLOW, BLUE)
score_record_rect = score_record_text.get_rect()
score_record_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 64)

#Set images
#background image
background_image = pygame.image.load("background.jpg")
background_rect = background_image.get_rect()
background_rect.topleft = (0, 0)

#Messi image
mob_image = pygame.image.load("Zombie.png")
mob_image = pygame.transform.scale(mob_image, (mob_image.get_width()/8, mob_image.get_height()/8))
mob_rect = mob_image.get_rect()
#Make the first appearance out of screen
mob_rect.x = -100
mob_rect.y = -100

blue_mob_image = pygame.image.load("Blue_Zombie.png")
blue_mob_image = pygame.transform.scale(blue_mob_image, (blue_mob_image.get_width()/8, blue_mob_image.get_height()/8))
blue_mob_rect = blue_mob_image.get_rect()
#Make the first appearance out of screen
blue_mob_rect.x = -100
blue_mob_rect.y = -100

#Hammer image
hammer_image = pygame.image.load("hammer.png")
hammer_image_x = hammer_image.get_width()
hammer_image = pygame.transform.scale(hammer_image, (hammer_image.get_width()/8, hammer_image.get_height()/8))
hammer_rect = hammer_image.get_rect()
#Make the first appearance out of screen
hammer_rect.centerx = -100
hammer_rect.centery = -100

#Create a matrix to store mouse easily
#0: nothing here
#1: Messi = 1 (+1 when hit)
#2: Zombie = -1 (-1 when hit)
list_matrix = [0,1,2]

#Set sound and music
hit_sound = pygame.mixer.Sound("Hit_sound.wav")
lose_sound = pygame.mixer.Sound("Lose_sound.wav")
game_over_sound = pygame.mixer.Sound("Gameover_sound.mp3")
pygame.mixer.music.load("background.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1, 0.0)

running = True
while running:  
    
    current_time = pygame.time.get_ticks()
    while (current_time - pass_time > 2000):
        pass_time = current_time
        #1 is green
        #-1 is blue
        blue_or_green = random.choice([1, 2, 3])
        
        #decide where Mob will spawn
        mob_x = random.choice(list_matrix)
        mob_y = random.choice(list_matrix)
        
        if blue_or_green == 1 or blue_or_green == 2:
            mob_rect.centerx = 140*mob_x + 195
            mob_rect.centery = 140*mob_y + 220
            
        else:
            blue_mob_rect.centerx = 140*mob_x + 195
            blue_mob_rect.centery = 140*mob_y + 220
        
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
                #Draw another mob
                pass_time = current_time
                
                blue_or_green = random.choice([1, 2, 3])
        
                #decide where Mob will spawn
                mob_x = random.choice(list_matrix)
                mob_y = random.choice(list_matrix)
        
                if blue_or_green == 1 or blue_or_green == 2:
                    mob_rect.centerx = 140*mob_x + 195
                    mob_rect.centery = 140*mob_y + 220
            
                else:
                    blue_mob_rect.centerx = 140*mob_x + 195
                    blue_mob_rect.centery = 140*mob_y + 220
            
            #Hit normal mob
            if hammer_rect.collidepoint(mob_rect.centerx, mob_rect.centery):
                hit_sound.play()
                score += 1
                hit += 1
                hit_ratio = round(hit/(hit + miss) * 100)
                
                #Draw another mob
                pass_time = current_time
                
                blue_or_green = random.choice([1, 2, 3])
        
                #decide where Mob will spawn
                mob_x = random.choice(list_matrix)
                mob_y = random.choice(list_matrix)
        
                if blue_or_green == 1 or blue_or_green == 2:
                    mob_rect.centerx = 140*mob_x + 195
                    mob_rect.centery = 140*mob_y + 220
            
                else:
                    blue_mob_rect.centerx = 140*mob_x + 195
                    blue_mob_rect.centery = 140*mob_y + 220
            else:
                lose_sound.play()
                miss += 1
                hit_ratio = round(hit/(hit + miss) * 100)
                player_live -= 1
         
    #Update HUD
    score_text = font.render("Score: " + str(score), True, YELLOW)    
    player_text = font.render("Live: " + str(player_live), True, YELLOW)   
    hit_text = font.render("Hit ratio: " + str(hit_ratio) + "%", True, YELLOW)    
    score_record_text = font.render("Your score is: " + str(score), True, YELLOW, BLUE)
    
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
     
                #The player wants to quit
                if event.type == pygame.QUIT:
                    is_paused = False
                    running = False
          
    #Blit the background
    display_surface.blit(background_image, background_rect)        
                 
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