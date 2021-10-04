import pygame
import random
import sys
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((1000,570)) 

pygame.display.set_caption("Mario Game")

icon = pygame.image.load("/Users/aadarsh/Documents/VS Code/Mario_Game/images/icon.png")
pygame.display.set_icon(icon)
icon = pygame.transform.scale(icon,(100,100))

background = pygame.image.load("/Users/aadarsh/Documents/VS Code/Mario_Game/images/background.png")

base = pygame.image.load("/Users/aadarsh/Documents/VS Code/Mario_Game/images/base.png")
base = pygame.transform.scale(base,(1000,120))

start = pygame.image.load("/Users/aadarsh/Documents/VS Code/Mario_Game/images/start1.png")
start = pygame.transform.scale(start,(300,300))

pipe = pygame.image.load("/Users/aadarsh/Documents/VS Code/Mario_Game/images/pipe.png")
pipe = pygame.transform.scale(pipe,(100,300))

digits ={}
digits['numbers'] = [ 
        pygame.image.load('/Users/aadarsh/Documents/VS Code/Mario_Game/images/0.png').convert_alpha(),
        pygame.image.load('/Users/aadarsh/Documents/VS Code/Mario_Game/images/1.png').convert_alpha(),
        pygame.image.load('/Users/aadarsh/Documents/VS Code/Mario_Game/images/2.png').convert_alpha(),
        pygame.image.load('/Users/aadarsh/Documents/VS Code/Mario_Game/images/3.png').convert_alpha(),
        pygame.image.load('/Users/aadarsh/Documents/VS Code/Mario_Game/images/4.png').convert_alpha(),
        pygame.image.load('/Users/aadarsh/Documents/VS Code/Mario_Game/images/5.png').convert_alpha(),
        pygame.image.load('/Users/aadarsh/Documents/VS Code/Mario_Game/images/6.png').convert_alpha(),
        pygame.image.load('/Users/aadarsh/Documents/VS Code/Mario_Game/images/7.png').convert_alpha(),
        pygame.image.load('/Users/aadarsh/Documents/VS Code/Mario_Game/images/8.png').convert_alpha(),
        pygame.image.load('/Users/aadarsh/Documents/VS Code/Mario_Game/images/9.png').convert_alpha(),
    ]
for i in range(10):
    digits['numbers'][i]=pygame.transform.scale(digits['numbers'][i],(64,64))

playerx =200 
playery =350
pipex1 =1000
pipey1=200
pipex2 =1500
pipey2=200

def display_background(x,y):
  screen.blit(background,(x,y))
def display_base(x,y):
  screen.blit(base,(x,y))
def display_player(x,y):
  screen.blit(icon,(x,y))
def display_pipe(x,y):
  screen.blit(pipe,(x,y))
def display_start(x,y):
  screen.blit(start,(x,y))

def collide(a,b,c,d):
    a+=100
    b+=100
    if c+50<=a<=c+60 and b>d:
        return True
    return False

def overlapp(a,b,c,d):
    b+=100
    if a+100 > c and a<c+100 and d-9<=b<=d:
        return True
    return False  

def check_score(a,b,c,d):
    if c<a<=c+6:
        return True
    return False

def UI():
    while True:
        display_background(0,0)
        display_start(350,100)
        display_base(0,450)
        display_player(playerx,playery)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type==KEYDOWN and event.key == K_ESCAPE):
               pygame.quit()
               sys.exit()
            if event.type == KEYDOWN and event.key==K_SPACE:
               return

    

def Game():
    pipechangex1=0
    pipechangey1=100
    pipechangex2=0
    pipechangey2=50
    playerchangey=0
    accelerate=9
    air=False
    score=0
    pygame.mixer.Sound("/Users/aadarsh/Documents/VS Code/Mario_Game/sounds/background.mp3").play()
    while True:
        font=pygame.font.Font(pygame.font.get_default_font(), 100)
        result = font.render("SCORE : " + str(score),True,(255,0,0))
        screen.blit(result,(400,400))
        print(score)
        for event in pygame.event.get():
           if event.type == pygame.QUIT or (event.type==KEYDOWN and event.key == K_ESCAPE):
               pygame.quit()
               sys.exit()
           if event.type == KEYDOWN and event.key==K_SPACE:
               air=True

        display_background(0,0)
        display_player(playerx,playery-playerchangey)
        display_pipe(pipex1-pipechangex1,pipey1+pipechangey1)
        display_pipe(pipex2-pipechangex2,pipey2+pipechangey2)
        display_base(0,450)
        pipechangex1+=6
        if pipex1-pipechangex1<-150:
            pipechangex1=0
            pipechangey1=random.randint(0,150)
        pipechangex2+=6
        if pipex2-pipechangex2<-150:
            pipechangex2=500
            pipechangey2=random.randint(0,150)
        if air:
            playerchangey+=accelerate
            if playery-playerchangey <=50:
                accelerate = -accelerate
            if playery-playerchangey>=350:
                accelerate=-accelerate
                air=False
            
        if collide(playerx,playery-playerchangey,pipex1-pipechangex1,pipey1+pipechangey1):
            pygame.mixer.pause()
            pygame.mixer.Sound("/Users/aadarsh/Documents/VS Code/Mario_Game/sounds/gameover.mp3").play()
            break
        if collide(playerx,playery-playerchangey,pipex2-pipechangex2,pipey2+pipechangey2):
            pygame.mixer.pause()
            pygame.mixer.Sound("/Users/aadarsh/Documents/VS Code/Mario_Game/sounds/gameover.mp3").play()
            break
        if overlapp(playerx,playery-playerchangey,pipex1-pipechangex1,pipey1+pipechangey1) and accelerate<0:
            playerchangey-=accelerate
        if overlapp(playerx,playery-playerchangey,pipex2-pipechangex2,pipey2+pipechangey2) and accelerate<0:
            playerchangey-=accelerate
        pygame.display.update()
        if check_score(playerx,playery-playerchangey,pipex1-pipechangex1,pipey1+pipechangey1):
            score+=1
        if check_score(playerx,playery-playerchangey,pipex2-pipechangex2,pipey2+pipechangey2):
            score+=1
        myDigits = [int(x) for x in list(str(score))]
        width = 0
        for digit in myDigits:
            width += digits['numbers'][digit].get_width()
            Xoffset = (1000 - width)/2

        for digit in myDigits:
            screen.blit(digits['numbers'][digit], (Xoffset, 480))
            Xoffset += digits['numbers'][digit].get_width()
        pygame.display.update()
        

while True:
    UI()
    Game()
    
