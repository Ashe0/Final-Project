class Player:
  def __init__(self,color,dim,horzPos,vertPos,speed):
    self.color = color
    self.dim = dim
    self.horzPos = horzPos
    self.vertPos = vertPos
    self.speed = speed
  
  def show_player(self,surf):
    import pygame
    pygame.init()
    playerRect = pygame.draw.rect(surf,self.color,[self.horzPos,self.vertPos,self.dim,self.dim])

