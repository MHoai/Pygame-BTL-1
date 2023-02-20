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

#SET GAME MODE 
global selectButton

#Set fonts
font = pygame.font.Font("freesansbold.ttf", 32)

#Colors
RED = (255, 0, 0)
BLUE = (1, 175, 209)
YELLOW = (255,255,0)
BLACK = (0, 0, 0)

# background at wait screen
startGame = True
start_game_bg_1 =pygame.image.load('start_game_1.jpg')
start_game_1_rect = start_game_bg_1.get_rect()

start_game_bg_2 =pygame.image.load('start_game_2.png')
start_game_2_rect = start_game_bg_2.get_rect()

# background at select mode
selectMode = True
select_mode_bg_1 =pygame.image.load('select_mode_1.png')
select_mode_rect = select_mode_bg_1.get_rect()

select_mode_bg_2 =pygame.image.load('select_mode_2.png')
select_mode_rect = select_mode_bg_2.get_rect()

select_mode_bg_3 =pygame.image.load('select_mode_3.png')
select_mode_rect = select_mode_bg_3.get_rect()

select_mode_bg_4 =pygame.image.load('select_mode_4.png')
select_mode_rect = select_mode_bg_4.get_rect()

#rectangle bound around play button

buttonRect = pygame.Rect(510, 463, 268, 204)

#rectangle bound around select button

button_normal_rect = pygame.Rect(508, 253, 242, 79)
button_medium_rect = pygame.Rect(508, 371, 242, 79)
button_hard_rect = pygame.Rect(508, 489, 242, 79)

#Set images
#background image
background_image = pygame.image.load("sanbong.jpg")

background_rect = background_image.get_rect()
background_rect.topleft = (0, 0)

lose_background_image = pygame.image.load("lose_background.png")
lose_background_image = pygame.transform.scale(lose_background_image, (WINDOW_WIDTH, WINDOW_HEIGHT))
lose_background_rect = background_image.get_rect()
lose_background_rect.topleft = (0, 0)


#where zombie appearance
appearance_image = pygame.image.load("noixuathien.png")
appearance_rect_1 = pygame.Rect(255-100,100-60,70,70)
appearance_rect_2 = pygame.Rect(255-100,350-60,70,70)
appearance_rect_3 = pygame.Rect(555-100,100-60,70,70)
appearance_rect_4 = pygame.Rect(555-100,350-60,70,70)
appearance_rect_5 = pygame.Rect(855-100,100-60,70,70)
appearance_rect_6 = pygame.Rect(855-100,350-60,70,70)
appearance_rect_7 = pygame.Rect(555-100,600-60,70,70)
appearance_rect_8 = pygame.Rect(855-100,600-60,70,70)
appearance_rect_9 = pygame.Rect(255-100,600-60,70,70)
appearance_rect_10 = pygame.Rect(405-100,225-60,70,70)
appearance_rect_11 = pygame.Rect(405-100,475-60,70,70)
appearance_rect_12 = pygame.Rect(705-100,225-60,70,70)
appearance_rect_13 = pygame.Rect(705-100,475-60,70,70)

#Create a matrix to store mouse easily
#0: nothing here
#1: Messi = 1 (+1 when hit)
#2: Zombie = -1 (-1 when hit)
list_matrix = [0,1,2]

#while start game
def HomeScreen(startGame):
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
    
    
# while select mode 
def SelectScreen(selectMode):
    mouseInbutton = 0
    while selectMode :
        if not mouseInbutton :
            display_surface.blit(select_mode_bg_1,background_rect)
        mouse_x, mouse_y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            #Check to see if player move the mouse
            if event.type == pygame.MOUSEMOTION:
                if button_normal_rect.collidepoint(mouse_x, mouse_y) :
                    mouseInbutton = 1
                    display_surface.blit(select_mode_bg_2,background_rect)
                elif button_medium_rect.collidepoint(mouse_x, mouse_y) :
                    mouseInbutton = 1
                    display_surface.blit(select_mode_bg_3,background_rect) 
                elif button_hard_rect.collidepoint(mouse_x, mouse_y) :
                    mouseInbutton = 1
                    display_surface.blit(select_mode_bg_4,background_rect)   
                else :
                    mouseInbutton = 0
            #Check player right click
            if event.type == pygame.MOUSEBUTTONUP:
                if button_normal_rect.collidepoint(mouse_x, mouse_y) :
                    selectButton = 1
                    selectMode= False
                    break
                elif button_medium_rect.collidepoint(mouse_x, mouse_y) :
                    selectButton = 2
                    selectMode= False
                    break
                elif button_hard_rect.collidepoint(mouse_x, mouse_y) :
                    selectButton = 3
                    selectMode= False
                    break
            #Check to see if the user wants to quit
            if event.type == pygame.QUIT:
                #End the game
                pygame.quit() 
                sys.exit()
        pygame.display.update()
    return selectButton

       
#Set sound and music
hit_sound = pygame.mixer.Sound("Hit_sound.wav")
lose_sound = pygame.mixer.Sound("Lose_sound.wav")
game_over_sound = pygame.mixer.Sound("Gameover_sound.wav")
cr7_sound = pygame.mixer.Sound("Ronaldo.wav")
pygame.mixer.music.load("wc_music.wav")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1, 0.0)

class Game():
    def __init__(self, player_group, mob_group, running_time):
        self.score = 0
        self.hit_ratio = 100
        self.hit = 0
        self.miss = 0
        self.pass_time = 0
        self.STARTING_LIVES = 5
        self.lives = self.STARTING_LIVES
        self.time_to_switch = 2000

        self.player_group = player_group
        self.mob_group = mob_group
    
        self.running_time = running_time
        self.Turn_On_Music = True
    
    def draw(self):
        #Set hub
        player_live = self.STARTING_LIVES
        score_text = font.render("Score: " + str(self.score), True, RED)
        score_rect = score_text.get_rect()
        score_rect.topleft = (5, 10)

        player_text = font.render("Live: " + str(self.lives), True, RED)
        player_rect = player_text.get_rect()
        player_rect.topleft = (5, 40)

        hit_text = font.render("Hit ratio: " + str(self.hit_ratio) + "%", True, RED)  
        hit_rect = hit_text.get_rect()
        hit_rect.topright = (WINDOW_WIDTH - 5, 10)

        self.game_over_text = font.render("GAME OVER", True, YELLOW, BLACK)
        self.game_over_rect = self.game_over_text.get_rect()
        self.game_over_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 - 64)

        self.continue_text = font.render("Press space to play again", True, YELLOW, BLACK)
        self.continue_rect = self.continue_text.get_rect()
        self.continue_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

        self.score_record_text = font.render("Your score is: " + str(self.score), True, YELLOW, BLACK)
        self.score_record_rect = self.score_record_text.get_rect()
        self.score_record_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 64)
        
        self.Music_box_on = pygame.image.load('Music_on.png')
        self.Music_box_on = pygame.transform.scale(self.Music_box_on, (64,64))
        
        self.Music_box_off = pygame.image.load('Music_off.png')
        self.Music_box_off = pygame.transform.scale(self.Music_box_off, (64,64))
        
        self.Music_box_rect = self.Music_box_on.get_rect()
        self.Music_box_rect.topright = (WINDOW_WIDTH - 5, 35)
        
        display_surface.blit(score_text, score_rect)
        display_surface.blit(player_text, player_rect)
        display_surface.blit(hit_text, hit_rect)
        display_surface.blit(self.Music_box_on, self.Music_box_rect)
              
    def update(self):
        self.Add_mob() 
        self.Game_over()
                 
              
    def Add_mob(self):
        #set time to switch
        current_time = pygame.time.get_ticks()
        if (current_time - self.pass_time >= self.time_to_switch):
            self.pass_time = current_time
            
            
            list_matrix = [0,1,2]
            list_matrix_1 = [0,1]
            list_matrix_2 = [0.5,1.5]
            
            #Kiem tra mob sinh ra co tai vi tri da ton tai mob, neu co random lai
            isNotDuplicated = True
            while isNotDuplicated:
                isNotDuplicated = False
                if selectButton == 1 :
                   x = random.choice(list_matrix)
                   y = random.choice(list_matrix_1)
                elif selectButton == 2 :
                   x = random.choice(list_matrix)
                   y = random.choice(list_matrix)
                elif selectButton == 3 :
                    if random.choice([0,1]) :
                       x = random.choice(list_matrix)
                       y = random.choice(list_matrix)
                    else :
                       x = random.choice(list_matrix_2)
                       y = random.choice(list_matrix_2)
                       
                mob_x = 300*x + 255
                mob_y = 240*y + 120
                
                for mob_temp in Mob_group:
                    if mob_x == mob_temp.x and mob_y == mob_temp.y:
                        isNotDuplicated = True
            
            current_time = pygame.time.get_ticks()
            Decide_Mob = bool(random.getrandbits(1))
            
            
            #adjust the time of mob to exist
            time_to_live = 2000
            if (current_time - self.running_time >= 10000 and self.score >= 5):
                    time_to_live = 1800
                    self.time_to_switch = 1800
                
            if (current_time - self.running_time >= 15000 and self.score >= 10):
                    time_to_live = 1600
                    self.time_to_switch = 1600
            # if (current_time - self.running_time >= 20000):
            #         time_to_live = 1000
            # if (current_time - self.running_time > 30000):
            #         time_to_live = 500       
            
            zombie = mob(mob_x, mob_y, current_time, time_to_live ,Decide_Mob)
            Mob_group.add(zombie)
            
    def check_collision(self):
            #Check Music Button
            for player in self.player_group:
                Music_collision = self.Music_box_rect.colliderect(player.rect)
                if Music_collision == True:
                    if self.Turn_On_Music == False:
                        pygame.mixer.music.play(-1, 0.0) 
                        self.Turn_On_Music = True
                    else:
                        pygame.mixer.music.stop()
                        self.Turn_On_Music = False

            #at this point, player pressed left mouse, so we need to do mouse animation
            for Player in self.player_group:
                Player.get_pressed()
               
            collapse_Mobs = pygame.sprite.groupcollide(Mob_group, Player_group, False, False)
            #Tinh toan diem khi da bong trung doi tuong 
            for Mob in collapse_Mobs:
                if (Mob.visited):
                    #Change animation for the mouse
                    
                    Mob.mile_stone = pygame.time.get_ticks()
                    #set time to live cho dead animation
                    Mob.time_to_live = 500
                    Mob.visited = False
                    
                    if (Mob.Good_or_bad == True):
                        hit_sound.play()
                        self.score += 1
                        
                        self.hit += 1
                        self.hit_ratio = round(self.hit / (self.hit + self.miss) * 100)
                    else:
                        lose_sound.play()
                        self.lives -= 1
                        
                        self.miss += 1
                        self.hit_ratio = round(self.hit / (self.hit + self.miss) * 100) 
                Mob.image = Mob.animated_sprites[1]
    def reset(self):
        self.hit = 0
        self.miss = 0
        self.hit_ratio = 0
        self.score = 0
        self.lives = self.STARTING_LIVES
        self.running_time = 0
        self.mob_group.empty()

    
    def Game_over(self):
        global running
            #if gameover
        if (self.lives == 0):
            pygame.mixer.music.stop()
            game_over_sound.play()
            
            display_surface.blit(lose_background_image, lose_background_rect)
            
            pygame.draw.rect(display_surface, BLACK, (340, 250, 525, 225))  
            display_surface.blit(self.game_over_text, self.game_over_rect)
            display_surface.blit(self.continue_text, self.continue_rect)
            display_surface.blit(self.score_record_text, self.score_record_rect)
            pygame.display.update()
            is_paused = True
            while is_paused:
                for event in pygame.event.get():
                    #The player wants to play again.
                    if event.type == pygame.KEYDOWN:
                        if (event.key == pygame.K_SPACE):
                            #setup as the begin
                            self.reset()
                            is_paused = False  
                            game_over_sound.stop()
                            pygame.mixer.music.play(-1, 0.0)          
        
                    #The player wants to quit
                    if event.type == pygame.QUIT:
                        is_paused = False
                        running = False


class mob(pygame.sprite.Sprite):
    def __init__(self, x, y, mile_stone, time_to_live, Good_or_bad):
        super().__init__()
        
        self.x = x
        self.y = y
        self.mile_stone = mile_stone
        self.Good_or_bad = Good_or_bad
        self.visited = True
        self.time_to_live = time_to_live
        self.animated_sprites = []
        
        pic_good = pygame.image.load("khungthanh.png")
        pic_bad = pygame.image.load("khungthanh_neuer.png")
    
        
        pic_good = pygame.transform.scale(pic_good, (pic_good.get_width()/3, pic_good.get_height()/3))
        pic_bad = pygame.transform.scale(pic_bad, (pic_bad.get_width()/2.5, pic_bad.get_height()/2.5))
        
        pic_good_2 = pygame.image.load("bongtungluoi.png")
        pic_bad_2 = pygame.image.load("neuer.png")
        
        pic_good_2 = pygame.transform.scale(pic_good_2, (pic_good_2.get_width()/3, pic_good_2.get_height()/3))
        pic_bad_2 = pygame.transform.scale(pic_bad_2, (pic_bad_2.get_width()/3, pic_bad_2.get_height()/3))
        
        self.pic_bad_3 = pygame.image.load("you_missed.png")
        self.pic_bad_3 = pygame.transform.scale(self.pic_bad_3, (self.pic_bad_3.get_width()/2, self.pic_bad_3.get_height()/2))########################################
            
        if (Good_or_bad == True):
            self.animated_sprites.append(pic_good)
            self.animated_sprites.append(pic_good_2)
        else:
            self.animated_sprites.append(pic_bad)
            self.animated_sprites.append(pic_bad_2)
        
        self.image = self.animated_sprites[0]
        self.rect = self.image.get_rect()
        
        self.rect.centerx = x
        self.rect.centery = y
            
        
    def update(self):
        
        #set time to disappear
        current_time = pygame.time.get_ticks()
        
        #idle animation time is the amount of time to needed before appear taunt animation
        idle_animation_time = self.time_to_live*60/100
        if (current_time - self.mile_stone >= idle_animation_time):
            if self.visited == True and self.Good_or_bad == False:
                self.image = self.pic_bad_3
        
        if (current_time - self.mile_stone >= self.time_to_live):
            self.kill()
        self.rect.center = self.x, self.y
        
        
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        
        #Hammer image=>>ball
        self.x = x;
        self.y = y;
        self.changed_time = 0;
        
        self.pic_1 = pygame.image.load("ball.png")
        self.pic_1 = pygame.transform.scale(self.pic_1, (self.pic_1.get_width()/6, self.pic_1.get_height()/6))
        self.pic_2 = pygame.image.load("pressed_ball.png")
        self.pic_2 = pygame.transform.scale(self.pic_2, (self.pic_2.get_width()/6, self.pic_2.get_height()/6))

        
        self.image = self.pic_1
        self.rect = self.image.get_rect()
        
        #Make the first appearance out of screen
        self.rect.centerx = x
        self.rect.centery = y

    def update(self):
        #after ball get changed an amount of time, get it back to old image
        current_time = pygame.time.get_ticks()
        if (current_time - self.changed_time >= 300):
            self.image = self.pic_1
    
        self.rect.center = pygame.mouse.get_pos()

    def get_pressed(self):
        self.changed_time = pygame.time.get_ticks()
        self.image = self.pic_2
        
        


Player_group = pygame.sprite.Group()
Player_1 = Player(0, 0)
Player_group.add(Player_1)

Mob_group = pygame.sprite.Group()

running_time = pygame.time.get_ticks()
my_game = Game(Player_group, Mob_group, running_time)

#run Home and select Mode
HomeScreen(True)
selectButton = SelectScreen(True)

running = True
while running:        
       
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                my_game.check_collision()
        #bring back to main screen
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                my_game.reset()
                HomeScreen(True)
                selectButton = SelectScreen(True)
                
                
                
                
        
    
                
    display_surface.blit(background_image, background_rect)
    display_surface.blit(appearance_image, appearance_rect_1 )
    display_surface.blit(appearance_image, appearance_rect_2 )
    display_surface.blit(appearance_image, appearance_rect_3 )
    display_surface.blit(appearance_image, appearance_rect_4 )
    display_surface.blit(appearance_image, appearance_rect_5 )
    display_surface.blit(appearance_image, appearance_rect_6 )
    
    if selectButton == 2:
        display_surface.blit(appearance_image, appearance_rect_7 )
        display_surface.blit(appearance_image, appearance_rect_8 )
        display_surface.blit(appearance_image, appearance_rect_9 ) 
    
    elif selectButton == 3:
        display_surface.blit(appearance_image, appearance_rect_7 )
        display_surface.blit(appearance_image, appearance_rect_8 )
        display_surface.blit(appearance_image, appearance_rect_9 ) 
        display_surface.blit(appearance_image, appearance_rect_10 )
        display_surface.blit(appearance_image, appearance_rect_11 )
        display_surface.blit(appearance_image, appearance_rect_12 )
        display_surface.blit(appearance_image, appearance_rect_13 )
        

        
            

    Mob_group.update()
    Mob_group.draw(display_surface)

    Player_group.update()
    Player_group.draw(display_surface)      
    
    my_game.update()
    my_game.draw()
    
    #Update the display and tick clock
    pygame.display.update()
    clock.tick(FPS)
    
    
#End the game
pygame.quit()