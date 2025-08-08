''' Link (https://www.youtube.com/watch?v=2C_YaOQ2yGg&list=PLpp8-k7G_6Y3Wj1suZQ-9lATFzFuGw93x&index=3)
min. 13:27
'''
import pygame
import sys
import os
import random
import math


pygame.init()
pygame.display.set_caption("Snake Game")
pygame.font.init()
random.speed()


# we will declare global constant definitions

SPEED = 0.30
SNAKE_SIZE = 9
APPLE_SIZE = SNAKE_SIZE # we will keep both food and size of snake same
SEPARATION = 10 # separation between two pixels
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800
FPS = 25
KEY = {"UP":1, "DOWN":2, "LEFT":3, "RIGHT":4}


# we will initialise screen
screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_HEIGHT), pygame.HWSURFACE)

# we have used hw surface which stands for hardware surface refers to using memory on the video card for storing
# draw as opposed to main memory

# Resources
score_font = pygame.font.Font(None, 38)
score_numb_font = pygame.font.Font(None, 28)
game_over_font = pygame.font.Font(None, 48)
play_again_font = score_numb_font
score_msg = score_font.render("Score : ", 1, pygame.color("green"))
score_msg_size = score_font.size("Score")
background_color = pygame.Color(0, 0, 0) # we will fill background color as black
black = pygame.Color(0, 0, 0)

# for clock at the left corner
gameClock = pygame.time.Clock()

def checkCollision(posA, As, posB, Bs): # As is the size of a and Bs is the size of b
    if (posA.x < posB.x + Bs and posA.x + As > posB.x and posA.y < posB.y + Bs and posA.y + As > posB.y):
        return True
    return False        

# to check the boundaries here we are not limiting boundaries like it can pass through screen and come from other side
def checkLimits(snake):
    if(snake.x > SCREEN_WIDTH):
        snake.x = SNAKE_SIZE
    if(snake.x < 0): # this will be checked when some part of sanke is on other side and some on opposite side
        snake.x = SCREEN_WIDTH - SNAKE_SIZE
    if(snake.y > SCREEN_HEIGHT):
        snake.y = SNAKE_SIZE
    if(snake.y < 0): # this also same half half
	    snake.y - SCREEN_HEIGHT - SNAKE_SIZE


# we will make class for food of the snake let's name it as apple
class Apple:
    def __init__(self, x, y, state):
        self.x = x
        self.y = y
        self.state = state
        self.color = pygame.color.color("orange") # Color of food

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, APPLE_SIZE, APPLE_SIZE), 0)

class segment: # 13:32 min.
    # Initally snake will move in up direction 
    self.x = x
    self.y = y
    self.direction = KEY["UP"]
    self.color = "white"

class snake:
    def __init__(self, x, y):
        self.x = x
        self.y = y 
        self.direction = KEY["UP"]
        self.stack = []
        self.stack.append(self)
        blackBox = segment(self.x, self.y + SEPARATION)
        blackBox.direction = KEY["UP"]
        blackBox.color = "NULL"
        self.stack.append(blackBox)

# We will define move of the snake
    def move(self):
        last_element = len(self.stack) - 1
        while (last_element != 0):
            self.stack[last_element].direction = self.stack[last_element].direction
            self.stack[last_element].x = self.stack[last_element - 1].x 
            self.stack[last_element].y = self.stack[last_element - 1].y
            last_element -= 1
        if (len(self.stack) < 2): # 16:41 min.
            last_segment = self
        else:
            last_segment = self.stack.pop(last_element)
        last_element.direction = self.stack[0].direction
        if(self.stack[0].direction == KEY["UP"]):
            last_segment.y = self.stack[0].y  - (SPEED * FPS)
        elif(self.stack[0].direction == KEY["DOWN"]):
            last_segment.y = self.stack[0].y  + (SPEED * FPS)
        if(self.stack[0].direction == KEY["LEFT"]):
            last_segment.x = self.stack[0].x  - (SPEED * FPS)
        if(self.stack[0].direction == KEY["RIGHT"]):
            last_segment.x = self.stack[0].x  + (SPEED * FPS)
        self.stack.insert(0, last_segment)

    def getHead(self): # Head of the snake
        return(self.stack[0]) # It will be always 0 index

    # Now when snake it´s food it will grow so for that we will add that food to stack 17:50 min.

    def grow(self):
        last_element = len(self.stack) - 1
        self.stack[last_element].direction = self.stack[last_element].direction
        if(self.stack[last_element].direction == KEY["UP"]):
            newSegment = segment(self.stack[last_element].x, self.stack[last_element].y - SNAKE_SIZE)
            blackBox = segment(newSegment.x, newSegment.y - SEPARATION)

        elif(self.stack[last_element].direction == KEY["DOWN"]):
            newSegment = segment(self.stack[last_element].x, self.stack[last_element].y + SNAKE_SIZE)
            blackBox = segment(newSegment.x, newSegment.y + SEPARATION)

        elif(self.stack[last_element].direction == KEY["LEFT"]):
            newSegment = segment(self.stack[last_element].x - SNAKE_SIZE, self.stack[last_element].y)
            blackBox = segment(newSegment.x - SEPARATION, newSegment.y)

        elif(self.stack[last_element].direction == KEY["RIGHT"]):
            newSegment = segment(self.stack[last_element].x + SNAKE_SIZE, self.stack[last_element].y)
            blackBox = segment(newSegment.x - SEPARATION, newSegment.y)

        blackBox.color = "NULL"
        self.stack.append(newSegment)
        self.stack.append(blackBox)

    def iterateSegments(self, delta):
        pass

    def setDirection(self, direction):
        if(self.direction == KEY["RIGHT"] and direction == KEY["LEFT"] or self.direction == KEY["LEFT"]
            and direction  == KEY["RIGHT"]):
            pass
        if(self.direction == KEY["UP"] and direction == KEY["DOWN"] or self.direction == KEY["UP"]
            and direction == KEY["DOWN"]):
            pass
        else:
            self.direction = direction

    def get_rect(self): # Get the rectangle shape
        rect = (self.x, self.y)
        return rect

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    # We will make the function of crashing when the snake eats itself 21:51 min.



# we will define keys
def getKey():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                return KEY["UP"]
            elif event.key == pygame.K_DOWN:
                return KEY["DOWN"]
            elif event.key == pygame.K_LEFT:
                return KEY["LEFT"]
            elif event.key == pygame.K_RIGHT:
                return KEY["RIGHT"]

            # for exit
            if event.key == pygame.K_ESCAPE:
                return "exit"

            # if we want continue playing again
            elif event.key == pygame.K_y:
                return "yes"

            # if we don't want play game
            elif event.key == pygame.K_n:
                return "no"
        
        if event.type == pygame.QUIT:
            sys.exit(0)

def endGame():
    message = game_over_font.render("Game over", 1, pygame.Color("white"))
    message_play_again = play_again_font.render("Play again? (Y/N)", 1, pygame.Color("green"))
    screen.blit(message, (320, 240))
    screen.blit(message_play_again, (320 + 12, 240 + 40))

    pygame.display.flip()
    pygame.display.update()

    mkey = getKey()
    while(mkey != "exit"):
        if (mkey == "yes"):
            main()
        elif(mkey == "no"):
            break

        mkey = getKey()
        gameClock.tick(FPS)
    sys.exit(0)

def drawScore(score):
    score_numb = score_numb_font.render(str(score), 1, pygame.Color("red"))
    screen.blit(score_msg, (SCREEN_WIDTH - score_msg_size[0] - 60 , 10))
    screen.blit(score_numb, (SCREEN_WIDTH - 45, 14))

def drawGameTime(gameTime):
    game_time = score_font.render("Time:", 1, pygame.Color("white"))
    game_time_numb = score_numb_font.render(str(gameTime/1000), 1, pygame.Color("white"))
    screen.blit(game_time, (30, 10))
    screen.blit(game_time_numb, (105, 14))

def exitScreen():
    pass

def main():
    score = 0