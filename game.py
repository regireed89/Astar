# Import a library of functions called 'pygame'
# import pygame
# import drawablenode
# from drawablenode import *
from Astar import astar
# from Astar import set_gscore
# from Astar import manhattan
# from Astar import retrace
import pathfinding


def main():
    failcount = 0
    passcount = 0
    for _ in range(100):
        res = pathfinding.testfunc(astar)
        if res:
            passcount += 1
        else:
            failcount += 1
    print str.format('fails {0}, passes {1}', failcount, passcount)


if __name__ == '__main__':
    main()
# # Initialize the game engine
# pygame.init()

# # Define the colors we will use in RGB format
# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)
# BLUE = (0, 0, 255)
# GREEN = (0, 255, 0)
# RED = (255, 0, 0)
# PAD = (5, 5)
# ROWS = 10
# COLS = 10
# WIDTH = 50
# HEIGHT = 50
# SCREEN_WIDTH = COLS * (PAD[0] + WIDTH) + PAD[1]
# SCREEN_HEIGHT = ROWS * (PAD[0] + HEIGHT) + PAD[1]
# # Set the height and width of the SCREEN

# SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# NODES = []
# count = 0
# for i in range(0, ROWS):
#     for j in range(0, COLS):
#         node = DrawableNode([i, j], count)
#         NODES.append(node)
#         count += 1


# pygame.display.set_caption("Example code for the draw module")

# # Loop until the user clicks the close button.
# DONE = False
# CLOCK = pygame.time.Clock()

# pygame.font.init()
# font1 = pygame.font.Font(None, 14)
# font2 = pygame.font.Font(None, 28)
# #create walls
# walls = [NODES[42], NODES[43], NODES[44], NODES[45], NODES[46]]
# for i in walls:
#     i.color = BLACK
#     i.walkable = False

# for i in NODES:
#     i.get_neighbors(NODES)

# # node to start from
# start = NODES[0]
# start.color = GREEN
# # node to go to
# end = NODES[99]
# end.color = RED
# # start astar
# astar(start, end)
# # color the path
# p = retrace(start, end)
# for i in p:
#     i.color = BLACK

# while not DONE:
#     # This limits the while loop to a max of 10 times per second.
#     # Leave this out and we will use all CPU we can.
#     CLOCK.tick(10)

#     for event in pygame.event.get():  # User did something
#         if event.type == pygame.QUIT:  # If user clicked close
#             DONE = True  # Flag that we are DONE so we exit this loop

#     # All drawing code happens after the for loop and but
#     # inside the main while DONE==False loop.

#     # Clear the SCREEN and set the SCREEN background
#     SCREEN.fill(WHITE)
#     # Draw a circle
#     for i in NODES:
#         i.draw(SCREEN, font1)

#     # Go ahead and update the SCREEN with what we've drawn.
#     # This MUST happen after all the other drawing commands.
#     bg = pygame.Surface((SCREEN.get_size()[0] / 3, SCREEN.get_size()[1] / 3))
#     bg.fill(BLACK)
#     textrect = bg.get_rect()
#     pygame.display.flip()


# # Be IDLE friendly
# pygame.quit()
