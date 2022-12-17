import pygame
import random
pygame.init()

class Gun_Shot:
    def __init__(self,img):
        self.img = img
        self.speed = 20
        self.rect = img.get_rect(midbottom = (0, 0))

    def change(self,x,y):
        self.rect.x = x
        self.rect.y = y

    def move(self,sign):
        if sign == "+":
            self.rect.x += self.speed
        elif sign == "-":
            self.rect.x -= self.speed

    def draw(self):
        surface.blit(self.img, self.rect)

    def check(self,p,f):
        if self.rect.colliderect(p):
            f()

width = 800
height = 400
pc = 10
ec = 10
gunsp = []
gunse = []
tile_size = 50
rects_ground = []
speed = 5
gravity = 5
health_width1 = 200
health_height1 = 30
HP_color1 = [0,255,0]
health1 = 500
health_width2 = 200
health_height2 = 30
HP_color2 = [0,255,0]
health2 = 500
key_up = False
chest_open = False
space_war = False
enter = False
ground = [
        [0,3,0,0,0,0,3,3,0,3,0,0,0,0,0,0],
        [0,3,0,3,3,0,3,3,0,0,0,0,0,0,0,0],
        [0,3,0,3,3,0,3,3,0,3,0,0,0,0,0,0],
        [0,0,0,3,3,0,3,3,0,3,0,0,0,0,0,0],
        [0,3,0,3,3,0,3,3,0,3,0,3,3,0,0,0],
        [0,3,0,3,3,0,0,0,0,3,0,0,0,0,0,0],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
        ]

color = (0,0,0)

surface = pygame.display.set_mode((width,height))
pygame.display.set_caption("Space War")

icon = pygame.image.load("assets/icon.png")
pygame.display.set_icon(icon)

black_tiles = pygame.image.load("assets/black_tiles.png")
black_tiles = pygame.transform.scale(black_tiles,(tile_size,tile_size))

font = pygame.font.Font("assets/font1.ttf",26)
text1 = font.render("Made by Black Tiles",True,color)
text2 = font.render("Black Tiles owner: Yashi Khandelwal",True,color)
font2 = pygame.font.Font("assets/font1.ttf",46)
text3 = font2.render("Press Enter Dot(.) to Start the game",True,color)
text4 = font.render("PLAYER2's CHANCE",True,(255,255,255))
text5 = font.render("Press o for opening the chest",True,(255,255,255))
text6 = font.render("Press s to start the SPACE WAR",True,(255,255,255))
text7 = font.render(f"{health1}",True,HP_color1)
text8 = font.render(f"{health2}",True,HP_color2)

#text3 = pygame.transform.scale(text3,(800,400))

tile1 = pygame.image.load("assets/Tiles/tile_0022.png")
tile1 = pygame.transform.scale(tile1,(tile_size,tile_size))

tile2 = pygame.image.load("assets/Tiles/tile_0122.png")
tile2 = pygame.transform.scale(tile2,(tile_size,tile_size))

tile3 = pygame.image.load("assets/Tiles/tile_0073.png")
tile3 = pygame.transform.scale(tile3,(tile_size,tile_size))

tile4 = pygame.image.load("assets/Tiles/tile_0029.png")
tile4 = pygame.transform.scale(tile4,(tile_size,tile_size))

key = pygame.image.load("assets/Tiles/tile_0027.png")
key = pygame.transform.scale(key,(tile_size,tile_size))

chest = pygame.image.load("assets/Tiles/tile_0028.png")
chest = pygame.transform.scale(chest,(tile_size,tile_size))

ship = pygame.image.load("assets/Characters/character_0017.png")
ship = pygame.transform.scale(ship,(tile_size*2,tile_size*2))
ship = pygame.transform.rotate(ship,90)

char1 = pygame.image.load("assets/Characters/character_0000.png")
char1 = pygame.transform.scale(char1,(tile_size,tile_size))

rect_char1 = char1.get_rect(bottomleft = (0,150))
rect_key = key.get_rect(topleft = (550,0))
rect_chest = chest.get_rect(topleft = (600,150))
rect_ship = ship.get_rect(topleft = (550,122))

mirror = pygame.image.load("assets/Tiles/tile_0089.png")
mirror = pygame.transform.scale(mirror,(tile_size,tile_size))
rect_mirror = mirror.get_rect(topleft = (350,250))

player = pygame.image.load("assets/Characters/character_0017.png")
player = pygame.transform.scale(player,(tile_size*2,tile_size*2))
player = pygame.transform.rotate(player,270)
rect_player = player.get_rect(topleft = (0,100))

enemy = pygame.image.load("assets/Characters/character_0017.png")
enemy = pygame.transform.scale(enemy,(tile_size*2,tile_size*2))
enemy = pygame.transform.rotate(enemy,90)
rect_enemy = enemy.get_rect(topright = (800,100))

ammo = pygame.image.load("assets/Tiles/tile_0157.png")
ammo = pygame.transform.scale(ammo,(tile_size,tile_size))

p1 = pygame.image.load("assets/p1.png")
p1 = pygame.transform.scale(p1,(width,height))

p2 = pygame.image.load("assets/p2.png")
p2 = pygame.transform.scale(p2,(width,height))

def function():
    global enter,text3
    keys = pygame.key.get_pressed()
    if keys[pygame.K_PERIOD] or keys[pygame.K_KP_PERIOD]:
        enter = True
    if enter == False:
        surface.fill((255,255,255))
        surface.blit(text3,(0,170))
    elif enter == True:
        draw_ground()
        chest_key()
        player_func()
        player_change()
        draw_player()
        
def player_change():
    global tile_size,char1,text4
    surface.blit(mirror,rect_mirror)
    if rect_char1.colliderect(rect_mirror):
        char1 = pygame.image.load("assets/Characters/character_0004.png")
        char1 = pygame.transform.scale(char1,(tile_size,tile_size))
        surface.blit(text4,(350,350))

def draw_ground():
    global ground,tile_size,rects_ground
    rects_ground = []
    index_Y = 0
    for layers in ground:
        index_X = 0
        for tile in layers:
            if tile == 0:
                x = tile_size*index_X
                y = tile_size*index_Y
                surface.blit(tile3,(x,y))
            if tile == 1:
                x = tile_size*index_X
                y = tile_size*index_Y
                rect = pygame.Rect(x,y,50,50)
                rects_ground.append(rect)
                surface.blit(tile1,(x,y))
            if tile == 2:
                x = tile_size*index_X
                y = tile_size*index_Y
                rect = pygame.Rect(x,y,50,50)
                rects_ground.append(rect)
                surface.blit(tile2,(x,y))
            if tile == 3:
                x = tile_size*index_X
                y = tile_size*index_Y
                rect = pygame.Rect(x,y,50,50)
                rects_ground.append(rect)
                surface.blit(tile4,(x,y))
            index_X+=1
        index_Y+=1

def draw_player():
    surface.blit(char1,rect_char1)

def chest_key():
    global key_up,chest_open,space_war
    if key_up == False:
        surface.blit(key,rect_key)
    if chest_open == False:
        surface.blit(chest,rect_chest)
    elif chest_open == True:
        surface.blit(ship,rect_ship)
        surface.blit(text6,(350,350))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s]:
            space_war = True
        

def player_func():
    global rects_ground,key_up,chest_open,text5
    movement = {"right":False,"left":False,"up":False,"down":True}
    
    if rect_char1.left < 0:
        rect_char1.left = 0
    elif rect_char1.right > 800:
        rect_char1.right = 800
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        movement["left"] = True
        rect_char1.x -= speed
    if keys[pygame.K_RIGHT]:
        movement["right"] = True
        rect_char1.x += speed
    for rect_ground in rects_ground:
        if rect_char1.colliderect(rect_ground):
            if movement["right"] == True:
                rect_char1.right = rect_ground.left
            elif movement["left"] == True:
                rect_char1.left = rect_ground.right
    if rect_char1.top < 0:
        rect_char1.top = 0
    elif rect_char1.bottom > 800:
        rect_char1.bottom = 800
    rect_char1.y += gravity
    if keys[pygame.K_UP]:
        movement["up"] = True
        rect_char1.y -= speed*2
    if keys[pygame.K_DOWN]:
        movement["down"] = True
        rect_char1.y += speed
    for rect_ground in rects_ground:
        if rect_char1.colliderect(rect_ground):
            if movement["up"] == True:
                rect_char1.top = rect_ground.bottom
            elif movement["down"] == True:
                rect_char1.bottom = rect_ground.top
    if rect_char1.colliderect(rect_key):
        key_up = True
        
    if rect_char1.colliderect(rect_chest) == 1:
        if chest_open == False:
            if key_up == True:
                surface.blit(text5,(350,350))
                keys = pygame.key.get_pressed()
                if keys[pygame.K_o]:
                    chest_open = True

def check_out():
    global health1,health2
    if health1 == 0:
        surface.blit(p2,(0,0))
    elif health2 == 0:
        surface.blit(p1,(0,0))

def health_bar_decrease1():
    global health_width1,health1,text7,HP_color1
    if health1 > 0:
        health1 -= 5
    health_width1 = 200/500*health1
    if HP_color1[1] > 0:
        HP_color1[1] -= 2
    if HP_color1[0] < 254:
        HP_color1[0] += 2
    text7 = font.render(f"{health1}",True,HP_color1)

def health_bar_decrease2():
    global health_width2,health2,text8,HP_color2
    if health2 > 0:
        health2 -= 5
    health_width2 = 200/500*health2
    if HP_color2[1] > 0:
        HP_color2[1] -= 2
    if HP_color2[0] < 255:
        HP_color2[0] += 2
    text8 = font.render(f"{health2}",True,HP_color2)

def health_bar():
    global HP_color1,HP_color2,text7
    health_rect1 = pygame.Rect(50,50,health_width1,health_height1)
    health_bound1 = pygame.Rect(50,50,200,health_height1)
    health_rect2 = pygame.Rect(550,50,health_width2,health_height2)
    health_bound2 = pygame.Rect(550,50,200,health_height2)
    
    pygame.draw.rect(surface,HP_color1,health_rect1)
    pygame.draw.rect(surface,(0,0,0),health_bound1,4)
    pygame.draw.rect(surface,HP_color2,health_rect2)
    pygame.draw.rect(surface,(0,0,0),health_bound2,4)

    surface.blit(text7,(10,50))
    surface.blit(text8,(510,50))

def draw_players():
    surface.blit(player,rect_player)
    surface.blit(enemy,rect_enemy)

def player_f():
    global rect_player,ammo,pc,gunsp,rect_enemy
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        rect_player.y -= speed
    if keys[pygame.K_s]:
        rect_player.y += speed
    if rect_player.top < 0:
        rect_player.top = 0
    if rect_player.bottom > 400:
        rect_player.bottom = 400
    if keys[pygame.K_SPACE]:
        if pc >= 0:
            gun = Gun_Shot(ammo)
            gun.change(rect_player.x,rect_player.y)
            gunsp.append(gun)
    for i in gunsp:
        i.move("+")
        i.draw()
        i.check(rect_enemy,health_bar_decrease2)
        

def enemy_f():
    global rect_enemy,ammo,ec,gunse,rect_player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        rect_enemy.y -= speed
    if keys[pygame.K_DOWN]:
        rect_enemy.y += speed
    if rect_enemy.top < 0:
        rect_enemy.top = 0
    if rect_enemy.bottom > 400:
        rect_enemy.bottom = 400
    if keys[pygame.K_KP_PERIOD]:
        if ec > 0:
            gun = Gun_Shot(ammo)
            gun.change(rect_enemy.x,rect_enemy.y)
            gunse.append(gun)
    for i in gunse:
        i.move("-")
        i.draw()
        i.check(rect_player,health_bar_decrease1)

def draw_stars():
    star = pygame.image.load("assets/Tiles/tile_0157.png")
    for i in range(20):
        x = random.randint(0,800)
        y = random.randint(0,400)
        surface.blit(star,(x,y))

def draw_text():
    global text1,text2
    surface.blit(text1,(300,330))
    surface.blit(text2,(200,360))
    surface.blit(black_tiles,(100,340))

FPS = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    if space_war == False:
        function()
    else:
        if health1 > 0 and health2 > 0:
            surface.fill((0,0,0))
            draw_stars()
            player_f()
            enemy_f()
            draw_players()
            health_bar()
        else:
            surface.fill((255,255,255))
            check_out()
            draw_text()
    pygame.display.update()
    FPS.tick(30)


    
