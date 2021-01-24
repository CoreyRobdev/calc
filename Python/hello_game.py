import pygame
pygame.init()

# Draw window
screen = pygame.display.set_mode((500, 500))

# Game loop
running = True
while running:
 #Exit
 for event in pygame.event.get():
  if event.type == pygame.QUIT:
   running = False
 
 #Fill bg with rgb values
 screen.fill((255, 255, 255))

 #Draws a blue circle at the center of screen with a radius of 75
 pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

 pygame.display.flip()

pygame.quit()