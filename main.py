import pygame


WIDTH = 1200
HEIGHT = 2000
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

fps = 120
timer = pygame.time.Clock()

# game variables
wall_thickness = 10
MARGIN = HEIGHT/50
gravity = 0.15
bounce_stop = 1


def draw_walls():
    top = pygame.draw.line(screen, "white", (MARGIN, MARGIN),(WIDTH-MARGIN, MARGIN), wall_thickness)
    bottom = pygame.draw.line(screen, "white", (MARGIN, HEIGHT-MARGIN),(WIDTH-MARGIN, HEIGHT-MARGIN), wall_thickness)
    right = pygame.draw.line(screen, "white", (WIDTH-MARGIN, MARGIN),(WIDTH-MARGIN, HEIGHT-MARGIN), wall_thickness)
    left = pygame.draw.line(screen, "white", (MARGIN, MARGIN),(MARGIN, HEIGHT-MARGIN), wall_thickness)

    # top = pygame.draw.line(screen, 'white', (0, 0), (WIDTH, 0), wall_thickness)
    # bottom = pygame.draw.line(screen, 'white', (0, HEIGHT), (WIDTH, HEIGHT), wall_thickness)
    # right = pygame.draw.line(screen, 'white', (WIDTH, 0), (WIDTH, HEIGHT), wall_thickness)
    # left = pygame.draw.line(screen, 'white', (0, 0), (0, HEIGHT), wall_thickness)

    wall_list = [top, bottom, right, left]
    return wall_list

class Ball:
    def __init__(self, x_pos, y_pos, radius, color, mass, retention, y_speed, x_speed, id):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.radius = radius
        self.color = color
        self.mass = mass
        self.retention = retention
        self.y_speed = y_speed
        self.x_speed = x_speed
        self.id = id
        self.circle = ""

    def draw(self):
        self.circle = pygame.draw.circle(screen, self.color, (self.x_pos, self.y_pos), self.radius)


    def check_gravity(self):
        if self.y_pos < HEIGHT - MARGIN - self.radius - (wall_thickness/2):
            self.y_speed += gravity
        else:
            if self.y_speed > bounce_stop:
                self.y_speed = self.y_speed * -1 * self.retention
            else:
                if abs(self.y_speed) <= bounce_stop:
                    self.y_speed = 0
        return self.y_speed

    def collision(self):
        if self.y_pos and self.x_pos = wand:
            einfallswinkel = ausfallswinkel

    def update_pos(self):
        self.y_pos += self.y_speed
        self.x_pos += self.x_speed

ball1 =  Ball(WIDTH/2, 3*MARGIN, HEIGHT/100, "white", 100, .7, 0, 0, 1)
# main game loop
run = True
while run:
    timer.tick(fps)
    screen.fill("black")

    box = draw_walls()
    ball1.draw()

    ball1.update_pos()

    ball1.yspeed = ball1.check_gravity()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
pygame.quit
