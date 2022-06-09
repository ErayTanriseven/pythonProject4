import pygame

pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 640
LOWER_MARGIN = 100
SIDE_MARGIN = 300

screen = pygame.display.set_mode((SCREEN_WIDTH + SIDE_MARGIN, SCREEN_HEIGHT + LOWER_MARGIN))
pygame.display.set_caption("Level Editor")
ROWS = 16
MAX_COLS = 150
TILE_SIZE = SCREEN_HEIGHT // ROWS


world_data = []
for row in range(ROWS):
    r = [-1] * MAX_COLS
    world_data.append(r)

for tile in range(0,MAX_COLS):
    world_data[ROWS - 1][tile] = 0

for tile in range(2, 8):
    world_data[ROWS - 4][tile] = 0

for tile in range(19, 25):
    world_data[ROWS - 4][tile] = 0

for tile in range(10, 17):
    world_data[ROWS - 7][tile] = 0


pine1_img = pygame.image.load("img/Background/pine1.png").convert_alpha()
pine2_img = pygame.image.load("img/Background/pine2.png").convert_alpha()
mountain_img = pygame.image.load("img/Background/mountain2.png").convert_alpha()
sky_img = pygame.image.load("img/Background/sky_cloud.png").convert_alpha()

BROWN =(40, 27, 13)

img_list = []
for x in range(3):
    img = pygame.image.load((f"img/sayi/{x}.png"))
    img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
    img_list.append(img)

def draw_bg():
    screen.fill(BROWN)
    width = sky_img.get_width()
    for x in range(3):
        screen.blit(sky_img, ((x * width), 0))
        screen.blit(mountain_img, ((x * width), SCREEN_HEIGHT - mountain_img.get_height()-370))
        screen.blit(pine1_img, ((x * width), SCREEN_HEIGHT - pine1_img.get_height()-290))
        screen.blit(pine2_img, ((x * width), SCREEN_HEIGHT - pine2_img.get_height()-200))
        screen.blit(pine2_img, ((x * width), SCREEN_HEIGHT - pine2_img.get_height()-100))
        screen.blit(pine2_img, ((x * width), SCREEN_HEIGHT - pine2_img.get_height()-40))

def draw_world():
    for y, row in enumerate(world_data):
        for x, tile in enumerate(row):
            if tile >= 0:
                screen.blit(img_list[0], (x * TILE_SIZE, y * TILE_SIZE))



run = True
while run:

    draw_bg()
    draw_world()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()