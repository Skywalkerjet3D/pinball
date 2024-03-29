import pygame


WIDTH = 600
HEIGHT = 1000
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

fps = 120
timer = pygame.time.Clock()

# game variables
wall_thickness = 10

def draw_walls():
    MARGIN = HEIGHT/100

    # top = pygame.draw.line(screen, "white", (MARGIN, MARGIN),(WIDTH-MARGIN, MARGIN), wall_thickness)
    # bottom = pygame.draw.line(screen, "white", (MARGIN, HEIGHT-MARGIN),(WIDTH-MARGIN, HEIGHT-MARGIN), wall_thickness)
    # right = pygame.draw.line(screen, "white", (WIDTH-MARGIN, MARGIN),(WIDTH-MARGIN, HEIGHT-MARGIN), wall_thickness)
    # left = pygame.draw.line(screen, "white", (MARGIN, MARGIN),(MARGIN, HEIGHT-MARGIN), wall_thickness)

    top = pygame.draw.line(screen, "white", (0, 0),(WIDTH, 0), wall_thickness)
    bottom = pygame.draw.line(screen, "white", (0, HEIGHT),(WIDTH, HEIGHT), wall_thickness)
    right = pygame.draw.line(screen, "white", (WIDTH, 0),(WIDTH, HEIGHT), wall_thickness)
    left = pygame.draw.line(screen, "white", (0, 0),(0, HEIGHT), wall_thickness)

    wall_list = [top, bottom, right, left]
    return wall_list

# main game loop
run = True
while run:
    timer.tick(fps)
    screen.fill("black")

    box = draw_walls()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip
pygame.quit
