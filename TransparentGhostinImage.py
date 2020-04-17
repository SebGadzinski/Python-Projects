import pygame 
import sys

# Ask user if they want instructions
Question = input("Do you want instructions ")
# If user said yes 
if Question == "yes":
	print('You have to input a ghost and background image')
	print('Then Submit the X and Y coordinates you would a ghost with cruches to be')
# If user did not say no or yes, print instructions and exit

elif not Question == "no" or Question == "yes":
	print('You will be given an image of a park')
	print('Submit the X and Y coordinates where you would like a ghost to be')
	sys.exit()
ghost_file = input("Name the file name you would like as your ghost ending in .bmp: ")
background_file = input("Name the file name you would like as your background ending in .bmp: ")
# Get the file names

ghost_image = pygame.image.load(ghost_file)
background_image = pygame.image.load(background_file)

# Display background image
(w, h) = background_image.get_rect().size
(wg, hg) = ghost_image.get_rect().size#wg, hg, the g is for Ghost
display_background_image = pygame.display.set_mode((w,h ))
display_background_image.blit(background_image, (0, 0))
pygame.display.update()

wg_half  = int(wg/2)
hg_half  = int(hg/2)

# Ask for x and y coordinates
while True:
	x_pos = int(input("insert X coordinate: "))
	y_pos = int(input("insert Y coordinate: "))
	if x_pos <= w and x_pos >= 0 and y_pos <= h and y_pos >= 0: 
		break
# Make the x and y coordinates be the middle of the ghost not the top left corner
x_pos = x_pos - wg_half
y_pos = y_pos - hg_half
# Check if each pixel is green on the image ghost
for y in range(hg):
	for x in range(wg):
		(r, g, b,_) = ghost_image.get_at( (x, y) )#r,g,b are the red blue pixels of the ghost
		#If the pixel is in range of the background image go through
		if x_pos + x >= 0 and y_pos + y >= 0 and y_pos + y < h and x_pos + x < w:
			#rb, bb, gb, the b is ment for background
			(rb, gb, bb,_) = background_image.get_at( (x + x_pos, y + y_pos) )
			if g != 255 and b != 0 and r != 0:#If not green then get transparency
				g = (g + gb) / 2
				r = (r + rb) / 2				
				b = (b + bb) / 2				
				ghost_image.set_at( (x, y), (r, g, b) )	
			else:#Replace the pixel cover of the green with the pixel of the background at the same location
				ghost_image.set_at( (x, y), (rb, gb, bb))
# Blit ghost image onto background image where x_pos and y_pos are	
display_background_image.blit(ghost_image, (x_pos, y_pos))
# Keep pygame alive
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()
