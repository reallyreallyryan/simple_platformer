# Initial setup for a platformer game
# First time working with sprites/image movements

import pygame
import spritesheet

pygame.init()

# Global Variables
size = width, height = 600, 600
FPS = 60
background_color = (150, 250, 250)

# Player Speed
VEL = 5
clock = pygame.time.Clock()

# Player Starting Coordinates 
x = 50
y = 450

rectX = 50
rectY = 65

# Make Screen / Load Images
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Test Game!")
bg = pygame.image.load("assets/background.jpg")

#Floor Image
floor_image = pygame.image.load("assets/floor.png")
floor_image = pygame.transform.scale(floor_image, (width, 100) )

# Player Image
walkRight =[pygame.image.load("assets/run1.png"), pygame.image.load("assets/run2.png"), pygame.image.load("assets/run3.png"), pygame.image.load("assets/run4.png")]
walkLeft = [pygame.image.load("assets/left_run1.png"), pygame.image.load("assets/left_run2.png"), pygame.image.load("assets/left_run3.png"), pygame.image.load("assets/left_run4.png")]
jump = pygame.image.load("assets/jump1.png")

player_image = pygame.image.load("assets/lady.png")


isJump = False
jumpCount = 7 
left = False
right = False
walkCount = 0


def redrawGameWindow():
    global walkCount
    screen.blit(bg, (0, 0))
    screen.blit(floor_image, (0, 500))

    if walkCount + 1 >= 9:
        walkCount = 0

    if left:
        screen.blit(walkLeft[walkCount//3], (x,y))
        walkCount += 1
    elif right:
        screen.blit(walkRight[walkCount//3], (x,y))
        walkCount += 1
    elif isJump:
        screen.blit(jump, (x,y))
    else:
        screen.blit(player_image, (x, y))

    pygame.display.update()


# Main Game Loop
run = True
while run == True:
    clock.tick(FPS)
    # Paint Images on Screen



    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            run = False

    # Keeping Player on Screen
    #if y < 450:
        #y += VEL
    if x < 0:
        x = 0
    if x >= width - rectX:
        x = width - rectX

    # Move Character
    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        x += VEL
        right = True
        left = False
    elif keys[pygame.K_LEFT]:
        x -= VEL
        left = True
        right = False
    else:
        right = False
        left = False
        walkCount = 0 

    # Jump Physics
    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
            right = False
            left = False
            walkCount =  0

    else: 
        if jumpCount >= -7:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) /2 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 7
    redrawGameWindow()

pygame.quit()
