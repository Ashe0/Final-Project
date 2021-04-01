#Asher Sonntag & Griffan Girvan-Morris
#Started on 3/31/21
#Last Edited on 3/31/21
#RPG Dungeoncrawler Pygame

#IMPORTS
import pygame
from player import Player
pygame.init()
pygame.display.init()

#COLORS
WHITE = (255,255,255)
BLACK = (0,0,0)

#Frames and Tick Variables
FPS = 30
FPSCLOCK = pygame.time.Clock()

#Screen Variables
screenHeight = 340
screenWidth = 600
DISPLAYSURF = pygame.display.set_mode((screenWidth,screenHeight))

#Player
player = Player(WHITE,25,0,0,5)

#Current Speed
vertSpeed = 0
horzSpeed = 0

#Loop variables
run = True
 
#Loop
while run:
  for event in pygame.event.get():
    #If Exit
    if event.type == pygame.QUIT:
      run = False
    #When a key is held down:
    if event.type == pygame.KEYDOWN:
      #If key is W
      if event.key == pygame.K_w:
        #Move up
        vertSpeed = -1
      #If key is a
      elif event.key == pygame.K_a: 
        #Move left
        horzSpeed = -1
      #If key is s
      elif event.key == pygame.K_s:
        #Move down
        vertSpeed = 1
      #If key is d
      elif event.key == pygame.K_d: 
        #Move Right
        horzSpeed = 1
    #When Key is released
    elif event.type == pygame.KEYUP:
      #If key is W and s is not also held
      if event.key == pygame.K_w and pygame.key.get_pressed()[pygame.K_s] != 1:
        #Stop Vertical speed
        vertSpeed = 0
      #If key is S and w is not also held
      if event.key == pygame.K_s and pygame.key.get_pressed()[pygame.K_w] != 1:
        #Stop Vertical speed
        vertSpeed = 0
      #If key is a and d is not also held
      if event.key == pygame.K_a and pygame.key.get_pressed()[pygame.K_d] != 1:
        #Stop Horizontal Speed
        horzSpeed = 0
      #If key is d and a is not also held
      if event.key == pygame.K_d and pygame.key.get_pressed()[pygame.K_a] != 1:
        #Stop Horizontal Speed
        horzSpeed = 0
  #If player will not go out of bounds vertically
  if player.vertPos + vertSpeed * player.speed <= screenHeight - player.dim and player.vertPos + vertSpeed * player.speed >= 0:
    #Move them vertically
    player.vertPos += vertSpeed * player.speed
  #If player will not go out of bounds horizontally
  if player.horzPos + horzSpeed * player.speed <= screenWidth - player.dim and player.horzPos + horzSpeed * player.speed >= 0:
    #Move them horizontally
    player.horzPos += horzSpeed * player.speed
  #show background
  DISPLAYSURF.fill(BLACK)
  #reshow player
  player.show_player(DISPLAYSURF)
  #update + tick
  pygame.display.update()
  FPSCLOCK.tick(FPS)
