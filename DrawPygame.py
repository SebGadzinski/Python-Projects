#Draws a image with pygame - made a logo
import pygame 

pygame.init()

dw = pygame.display.set_mode((48, 56))

dw.fill((255, 255, 255))

pygame.draw.polygon(dw, (55, 148, 201), ((13, 44),(13, 38), (26, 38), (20, 44)))

pygame.draw.polygon(dw,(213, 203, 188), ((22, 44), (35, 44), (35, 38), (28, 38)))

pygame.draw.polygon(dw, (161, 153, 159),((28, 30), (35, 30), (35, 36), (22, 36)))

pygame.draw.polygon(dw, (89, 190, 178), ((30, 28), (35, 28), (35, 23)))

pygame.display.update()

pygame.image.save(dw, "image.png")




