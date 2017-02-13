import pygame
import time

pygame.init()
P1 = input("What is Player 1's name?")
P2 = input("What is Player 2's name?")
display_width = 800     #setting how big the screen is
display_height = 600
screensize = (display_width, display_height)
gameDisplay = pygame.display.set_mode(screensize)
pygame.display.set_caption('Pong Ping')

black = (0, 0, 0)      #just the colour settings
white = (255, 255, 255)
red = (200, 0, 0)
green = (0, 200, 0)
blue = (0, 0, 200)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)
bright_blue = (0, 0, 255)


clock = pygame.time.Clock()

pause = False
Icon = pygame.image.load('bat.png')

pygame.display.set_icon(Icon)

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def button(msg, x, y, w, h, ic, ac, action=None): #message, x value, y value, width, height, inactive colour, active colour, action

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
           action()             #cleaned the function up a bit here

    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    smallText = pygame.font.SysFont("comicsansms", 20)
    TextSurf, TextRect = text_objects(msg, smallText)
    TextRect.center = ((x + (w / 2)), (y + (h / 2)))
    gameDisplay.blit(TextSurf, TextRect)

def quite():
    pygame.quit()
    quit()

def p1():
    if len(P1) == 0:
        largeText = pygame.font.SysFont("comicsansms", 70)
        TextSurf, TextRect = text_objects("Player 1 wins!", largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurf, TextRect)  # to show the message
    else:
        largeText = pygame.font.SysFont("comicsansms", 70)
        TextSurf, TextRect = text_objects( P1+" wins!", largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurf, TextRect)  # to show the message

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #gameDisplay.fill(white)


        button("Play Again!", 150, 450, 150, 50, green, bright_green, main)
        button("Quit", 550, 450, 100, 50, red, bright_red, quite)

        pygame.display.update()
        clock.tick(15)

def p2():
    if len(P2) == 0:
        largeText = pygame.font.SysFont("comicsansms", 70)
        TextSurf, TextRect = text_objects("Player 2 wins!", largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurf, TextRect)  # to show the message
    else:
        largeText = pygame.font.SysFont("comicsansms", 70)
        TextSurf, TextRect = text_objects( P2+" wins!", largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurf, TextRect)  # to show the message

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #gameDisplay.fill(white)


        button("Play Again!", 150, 450, 150, 50, green, bright_green, main)
        button("Quit", 550, 450, 100, 50, red, bright_red, quite)

        pygame.display.update()
        clock.tick(15)

def unpaused():
    global pause
    pause = False

def paused():
    global pause
    pause = True

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        largeText = pygame.font.SysFont("comicsansms", 70)
        TextSurf, TextRect = text_objects("Paused", largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurf, TextRect)  # to show the message

        button("Continue!", 150, 450, 100, 50, green, bright_green, count3)
        button("Quit", 550, 450, 100, 50, red, bright_red, quite)

        pygame.display.update()
        clock.tick(15)

def count3():
    gameDisplay.fill(white)
    largeText = pygame.font.SysFont("comicsansms", 70)
    TextSurf, TextRect = text_objects("3", largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)  # to show the message

    pygame.display.update()

    time.sleep(1)

    count2()


def count2():
    gameDisplay.fill(white)
    largeText = pygame.font.SysFont("comicsansms", 70)
    TextSurf, TextRect = text_objects("2", largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)  # to show the message

    pygame.display.update()

    time.sleep(1)

    count1()


def count1():
    gameDisplay.fill(white)
    largeText = pygame.font.SysFont("comicsansms", 70)
    TextSurf, TextRect = text_objects("1", largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)  # to show the message

    pygame.display.update()

    time.sleep(1)

    count()

def count():
    gameDisplay.fill(white)
    largeText = pygame.font.SysFont("comicsansms", 70)
    TextSurf, TextRect = text_objects("GO!!", largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)  # to show the message

    pygame.display.update()

    time.sleep(1)

    unpaused()

def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        largeText = pygame.font.SysFont("comicsansms", 70)
        TextSurf, TextRect = text_objects("Pong Ping", largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurf, TextRect)  # to show the message

        if len(P1) == 0 and len(P2) == 0:
            largeText1 = pygame.font.SysFont("comicsansms", 15)
            TextSurf1, TextRect1 = text_objects("Player 1 uses arrows(up and down) to move, Player 2 uses w & s to move and p to pause", largeText1)
            TextRect1.center = ((display_width / 2), (370))
            gameDisplay.blit(TextSurf1, TextRect1)  # to show the message
        elif len(P1) == 0:
            largeText1 = pygame.font.SysFont("comicsansms", 15)
            TextSurf1, TextRect1 = text_objects("Player 1 uses arrows(up and down) to move, "+P2+" uses w & s to move and p to pause", largeText1)
            TextRect1.center = ((display_width / 2), (370))
            gameDisplay.blit(TextSurf1, TextRect1)  # to show the message
        elif len(P2) == 0:
            largeText1 = pygame.font.SysFont("comicsansms", 15)
            TextSurf1, TextRect1 = text_objects(P1+" uses arrows(up and down) to move, Player 2 uses w & s to move and p to pause", largeText1)
            TextRect1.center = ((display_width / 2), (370))
            gameDisplay.blit(TextSurf1, TextRect1)  # to show the message
        else:
            largeText1 = pygame.font.SysFont("comicsansms", 15)
            TextSurf1, TextRect1 = text_objects(P1+" uses arrows(up and down) to move, "+P2+ " uses w & s to move and p to pause", largeText1)
            TextRect1.center = ((display_width / 2), (370))
            gameDisplay.blit(TextSurf1, TextRect1)  # to show the message

        button("Play!", 150, 450, 100, 50, green, bright_green, main)
        button("Quit", 550, 450, 100, 50, red, bright_red, quite)

        pygame.display.update()
        clock.tick(15)

class Pong(object):
    def __init__(self, screensize):  #init to start up our object and self to perform it to itself

        self.screensize = screensize  #since the argument of the function is self everything else needs to be start with self
        self.display_height = display_height
        self.display_width = display_width

        self.centerx = int(display_width*0.5) #making it middle of the screen
        self.centery = int(display_height*0.5)

        self.radius = 8 #radius

        self.rect = pygame.Rect(self.centerx-self.radius,
                                self.centery-self.radius,
                                self.radius*2, self.radius*2) #making it a rectangular box but doesn't matter in this game
                                                        #setting the ball size here

        self.color = (100,100,255) #colour setting here - RGB

        self.direction = [1,1]

        self.speedx = 3
        self.speedy = 5

        self.hit_edge_left = False
        self.hit_edge_right = False

    def update(self, player_paddle, ai_paddle):

        self.centerx += self.direction[0]*self.speedx
        self.centery += self.direction[1]*self.speedy

        self.rect.center = (self.centerx, self.centery)

        if self.rect.top <= 0:
            self.direction[1] = 1
        elif self.rect.bottom >= self.display_height-1:
            self.direction[1] = -1

        if self.rect.right >= self.display_width-1:
            self.hit_edge_right = True
        elif self.rect.left <= 0:
            self.hit_edge_left = True


        if self.rect.colliderect(player_paddle.rect):
            self.direction[0] = -1
        if self.rect.colliderect(ai_paddle.rect):
            self.direction[0] = 1

    def render(self, screen):
        pygame.draw.circle(screen, self.color, self.rect.center, self.radius, 0)
        pygame.draw.circle(screen, (0,0,0), self.rect.center, self.radius, 1)


class PlayerPaddle(object):
    def __init__(self, screensize):
        self.screensize = screensize
        self.display_height = display_height
        self.display_width = display_width

        self.centerx = display_width-5
        self.centery = int(display_height*0.5)

        self.height = 100
        self.width = 10

        self.rect = pygame.Rect(0, self.centery-int(self.height*0.5), self.width, self.height)

        self.color = (100,255,100)

        self.speed = 3
        self.direction = 0

    def update(self):
        self.centery += self.direction*self.speed

        self.rect.center = (self.centerx, self.centery)
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > self.display_height-1:
            self.rect.bottom = self.display_height-1

    def render(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, 0)
        pygame.draw.rect(screen, (0,0,0), self.rect, 1)

class AIPaddle(object):
    def __init__(self, screensize):
        self.screensize = screensize
        self.display_height = display_height
        self.display_width = display_width

        self.centerx = 5
        self.centery = int(display_height*0.5)

        self.height = 100
        self.width = 10

        self.rect = pygame.Rect(0, self.centery-int(self.height*0.5), self.width, self.height)

        self.color = (255,100,100)

        self.speed = 3
        self.direction = 0

    def update(self):
        self.centery += self.direction*self.speed

        self.rect.center = (self.centerx, self.centery)
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > self.display_height-1:
            self.rect.bottom = self.display_height-1

    def render(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, 0)
        pygame.draw.rect(screen, (0,0,0), self.rect, 1)

def main():

    ball = Pong(gameDisplay)
    player = PlayerPaddle(gameDisplay)
    enemy = AIPaddle(gameDisplay)

    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player.direction = -1
                elif event.key == pygame.K_DOWN: #just some keys stuff
                    player.direction = 1
                if event.key == pygame.K_w:
                    enemy.direction = -1
                if event.key == pygame.K_s:
                    enemy.direction = 1
                if event.key == pygame.K_p:
                    paused()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP and player.direction == -1: #for multiplayer
                    player.direction = 0
                elif event.key == pygame.K_DOWN and player.direction == 1:
                    player.direction = 0
                if event.key == pygame.K_w and enemy.direction == -1:
                    enemy.direction = 0
                if event.key == pygame.K_s and enemy.direction == 1:
                    enemy.direction = 0

        player.update()
        enemy.update()
        ball.update(player, enemy)

        if ball.hit_edge_left:
            p1()
        elif ball.hit_edge_right:
            p2()

        #rendering phase
        gameDisplay.fill(white)

        enemy.render(gameDisplay)
        player.render(gameDisplay)
        ball.render(gameDisplay)


        pygame.display.update()
        clock.tick(60)  # frames per second


game_intro()