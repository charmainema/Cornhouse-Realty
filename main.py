# import modules
import pygame
import os
import sys
import random
import time

# initialize game
pygame.init()

# set game variables
CLOCK = pygame.time.Clock()
framerate = 60
# set window
WINDOW_WIDTH, WINDOW_HEIGHT = 1400, 700
SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Cornhouse Realty")

# filler variable
filler = None

# backgrounds
# intro background
# image dimensions
INTRO_BACKGROUND_WIDTH, INTRO_BACKGROUND_HEIGHT = 1200, 710
# background rect
OPENING_SCREEN_RECT = pygame.Rect(
    WINDOW_WIDTH / 2 - INTRO_BACKGROUND_WIDTH / 2, 
    WINDOW_HEIGHT / 2 - INTRO_BACKGROUND_HEIGHT / 2, 
    INTRO_BACKGROUND_WIDTH, 
    INTRO_BACKGROUND_HEIGHT)
# images
OPENING_SCREEN_BACKGROUND = pygame.image.load(os.path.join("assets", "backgrounds", "opening screen", "opening screen.png"))
OPENING_SCREEN_ANIM_BACKGROUND = pygame.image.load(os.path.join("assets", "backgrounds", "opening screen", "opening screen anim.png"))

# office floor
# image dimensions
OFFICE_FLOOR_WIDTH, OFFICE_FLOOR_HEIGHT = WINDOW_WIDTH, WINDOW_HEIGHT
# image scale
floor_scale = 4
# background rect
OFFICE_FLOOR_RECT = pygame.Rect(
    WINDOW_WIDTH / 2 - OFFICE_FLOOR_WIDTH / 2, 
    WINDOW_HEIGHT / 2 - OFFICE_FLOOR_HEIGHT / 2 - 650, 
    OFFICE_FLOOR_WIDTH * floor_scale, 
    OFFICE_FLOOR_HEIGHT * floor_scale)
# image
OFFICE_FLOOR_BACKGROUND = pygame.image.load(os.path.join("assets", "backgrounds", "floors", "office floor.png"))

# manager's office floor
# image
MANAGER_OFFICE_FLOOR_BACKGROUND = pygame.image.load(os.path.join("assets", "backgrounds", "floors", "manager's office floor.png"))
# image scale
MANAGER_OFFICE_FLOOR_SCALE = 1.5
# image dimensions
MANAGER_OFFICE_FLOOR_WIDTH, MANAGER_OFFICE_FLOOR_HEIGHT = MANAGER_OFFICE_FLOOR_BACKGROUND.get_width() * MANAGER_OFFICE_FLOOR_SCALE, \
    MANAGER_OFFICE_FLOOR_BACKGROUND.get_height() * MANAGER_OFFICE_FLOOR_SCALE
# background rect
MANAGER_OFFICE_FLOOR_RECT = pygame.Rect(
    -270, 
    200 - MANAGER_OFFICE_FLOOR_HEIGHT, 
    MANAGER_OFFICE_FLOOR_WIDTH, 
    MANAGER_OFFICE_FLOOR_HEIGHT)

# kitchen floor
KITCHEN_FLOOR_BACKGROUND = pygame.image.load(os.path.join("assets", "backgrounds", "floors", "kitchen floor.png"))
KITCHEN_FLOOR_SCALE = 2
KITCHEN_FLOOR_WIDTH, KITCHEN_FLOOR_HEIGHT = KITCHEN_FLOOR_BACKGROUND.get_width() * KITCHEN_FLOOR_SCALE, \
    KITCHEN_FLOOR_BACKGROUND.get_height() * KITCHEN_FLOOR_SCALE
KITCHEN_FLOOR_RECT = pygame.Rect(
    -250, 
    200 - KITCHEN_FLOOR_HEIGHT, 
    KITCHEN_FLOOR_WIDTH, 
    KITCHEN_FLOOR_HEIGHT)

# catch-a-corn opening screen
CATCH_A_CORN_OPENING_BACKGROUND_IMG = pygame.image.load(os.path.join("assets", "backgrounds", "catch-a-corn opening.png"))
CATCH_A_CORN_OPENING_SCALE = 5.5
CATCH_A_CORN_OPENING_WIDTH, CATCH_A_CORN_OPENING_HEIGHT = CATCH_A_CORN_OPENING_BACKGROUND_IMG.get_width() * CATCH_A_CORN_OPENING_SCALE, \
    CATCH_A_CORN_OPENING_BACKGROUND_IMG.get_height() * CATCH_A_CORN_OPENING_SCALE
CATCH_A_CORN_OPENING_BACKGROUND_RECT = pygame.Rect(
    WINDOW_WIDTH / 2 - CATCH_A_CORN_OPENING_WIDTH / 2, 
    WINDOW_HEIGHT / 2 - CATCH_A_CORN_OPENING_HEIGHT / 2, 
    CATCH_A_CORN_OPENING_WIDTH, 
    CATCH_A_CORN_OPENING_HEIGHT)

# catch-a-corn background
CATCH_A_CORN_BACKGROUND_IMG = pygame.image.load(os.path.join("assets", "backgrounds", "catch-a-corn background.png"))
CATCH_A_CORN_SCALE = 5.5
CATCH_A_CORN_WIDTH, CATCH_A_CORN_HEIGHT = CATCH_A_CORN_BACKGROUND_IMG.get_width() * CATCH_A_CORN_SCALE, \
    CATCH_A_CORN_BACKGROUND_IMG.get_height() * CATCH_A_CORN_SCALE
CATCH_A_CORN_BACKGROUND_RECT = pygame.Rect(
    WINDOW_WIDTH / 2 - CATCH_A_CORN_WIDTH / 2, 
    WINDOW_HEIGHT / 2 - CATCH_A_CORN_HEIGHT / 2, 
    CATCH_A_CORN_WIDTH, 
    CATCH_A_CORN_HEIGHT)

# lab hallway 1
# background
HALLWAY1_BACKGROUND_IMG = pygame.image.load(os.path.join("assets", "backgrounds", "hallway", "hallway.png"))
HALLWAY1_SCALE = 6
HALLWAY1_WIDTH, HALLWAY1_HEIGHT = HALLWAY1_BACKGROUND_IMG.get_width() * HALLWAY1_SCALE, \
    HALLWAY1_BACKGROUND_IMG.get_height() * HALLWAY1_SCALE
HALLWAY1_RECT = pygame.Rect(0, 90, HALLWAY1_WIDTH, HALLWAY1_HEIGHT)
# lighting
HALLWAY1_LIGHTING_IMG = pygame.image.load(os.path.join("assets", "backgrounds", "hallway", "door.png"))
HALLWAY1_LIGHTING_RECT = pygame.Rect(HALLWAY1_RECT.x, HALLWAY1_RECT.y, HALLWAY1_WIDTH, HALLWAY1_HEIGHT)

# lab hallway 2
# background
HALLWAY2_BACKGROUND_IMG = pygame.image.load(os.path.join("assets", "backgrounds", "hallway", "hallway pt.2.png"))
HALLWAY2_SCALE = 6
HALLWAY2_WIDTH, HALLWAY2_HEIGHT = HALLWAY2_BACKGROUND_IMG.get_width() * HALLWAY2_SCALE, \
    HALLWAY2_BACKGROUND_IMG.get_height() * HALLWAY2_SCALE
HALLWAY2_RECT = pygame.Rect(0, 90, HALLWAY2_WIDTH, HALLWAY2_HEIGHT)
# lighting
HALLWAY2_LIGHTING_IMG = pygame.image.load(os.path.join("assets", "backgrounds", "hallway", "door lighting 2.png"))
HALLWAY2_LIGHTING_RECT = pygame.Rect(HALLWAY2_RECT.x, HALLWAY2_RECT.y, HALLWAY2_WIDTH, HALLWAY2_HEIGHT)

# lab
# background
LAB_BACKGROUND_IMG = pygame.image.load(os.path.join("assets", "backgrounds", "lab", "lab.png"))
LAB_SCALE = 6
LAB_WIDTH, LAB_HEIGHT = LAB_BACKGROUND_IMG.get_width() * LAB_SCALE, LAB_BACKGROUND_IMG.get_height() * LAB_SCALE
LAB_RECT = pygame.Rect(0, 90, LAB_WIDTH, LAB_HEIGHT)
# lighting
LAB_LIGHTING_IMG = pygame.image.load(os.path.join("assets", "backgrounds", "lab", "lab lighting.png"))
LAB_LIGHTING_RECT = pygame.Rect(LAB_RECT.x, LAB_RECT.y, LAB_WIDTH, LAB_HEIGHT)

# objects
ROW_DISTANCE = 650
# egg face
EGG_FACE_SPRITE = pygame.image.load(os.path.join("assets", "objects", "egg-face.png"))

# cubicle
# generic cubicle (empty cubicle)
CUBICLE_SPRITE = pygame.image.load(os.path.join("assets", "objects", "cubicles", "cubicle.png"))
CUBICLE_WIDTH, CUBICLE_HEIGHT = CUBICLE_SPRITE.get_width() * 4, CUBICLE_SPRITE.get_height() * 4
CUBICLE_RECT = pygame.Rect(
    WINDOW_WIDTH / 2 - CUBICLE_WIDTH / 2, 
    WINDOW_HEIGHT / 2 - CUBICLE_HEIGHT / 2, 
    CUBICLE_WIDTH, CUBICLE_HEIGHT)

# cubicle sprites
BILL_CUBICLE_SPRITE = pygame.image.load(os.path.join("assets", "objects", "cubicles", "bill's cubicle.png"))
BOOK_CUBICLE_SPRITE = pygame.image.load(os.path.join("assets", "objects", "cubicles", "book cubicle.png"))
CORN_CUBICLE_SPRITE = pygame.image.load(os.path.join("assets", "objects", "cubicles", "corn cubicle.png"))
CUPCAKE_CUBICLE_SPRITE = pygame.image.load(os.path.join("assets", "objects", "cubicles", "cupcake cubicle.png"))
EGG_CUBICLE_SPRITE = pygame.image.load(os.path.join("assets", "objects", "cubicles", "egg cubicle.png"))
MESSY_CUBICLE_SPRITE = pygame.image.load(os.path.join("assets", "objects", "cubicles", "messy cubicle.png"))
NERD_CUBICLE_SPRITE = pygame.image.load(os.path.join("assets", "objects", "cubicles", "nerd cubicle.png"))
NORMAL_CUBICLE_SPRITE = pygame.image.load(os.path.join("assets", "objects", "cubicles", "normal cubicle.png"))
POSTER_CUBICLE_SPRITE = pygame.image.load(os.path.join("assets", "objects", "cubicles", "poster cubicle.png"))
SYMMETRICAL_CUBICLE_SPRITE = pygame.image.load(os.path.join("assets", "objects", "cubicles", "symmetrical cubicle.png"))

# layout of cubicle sprites (row by row from left to right)
CUBICLE_SPRITES = [
    [BILL_CUBICLE_SPRITE, EGG_CUBICLE_SPRITE, MESSY_CUBICLE_SPRITE, CUBICLE_SPRITE, BOOK_CUBICLE_SPRITE],
    [NORMAL_CUBICLE_SPRITE, SYMMETRICAL_CUBICLE_SPRITE, CUPCAKE_CUBICLE_SPRITE, CORN_CUBICLE_SPRITE, NERD_CUBICLE_SPRITE],
    [POSTER_CUBICLE_SPRITE, BOOK_CUBICLE_SPRITE, MESSY_CUBICLE_SPRITE, NORMAL_CUBICLE_SPRITE, POSTER_CUBICLE_SPRITE],
    [CORN_CUBICLE_SPRITE, NERD_CUBICLE_SPRITE, CUPCAKE_CUBICLE_SPRITE, SYMMETRICAL_CUBICLE_SPRITE, MESSY_CUBICLE_SPRITE],
    [BOOK_CUBICLE_SPRITE, BILL_CUBICLE_SPRITE, NORMAL_CUBICLE_SPRITE, BOOK_CUBICLE_SPRITE, CUBICLE_SPRITE],
    [CUPCAKE_CUBICLE_SPRITE, POSTER_CUBICLE_SPRITE, CUBICLE_SPRITE, NERD_CUBICLE_SPRITE, CORN_CUBICLE_SPRITE]]

# cubicle hitbox (constructed of 3 separate hitboxes)
# left hitbox
LEFT_CUBICLE_HITBOX = pygame.Rect(
    CUBICLE_RECT.left, 
    CUBICLE_RECT.top, 
    CUBICLE_RECT.width / 6.5, 
    CUBICLE_RECT.height - 100)
# right hitbox
RIGHT_CUBICLE_HITBOX = pygame.Rect(
    CUBICLE_RECT.left + CUBICLE_RECT.width - CUBICLE_RECT.width / 5, 
    CUBICLE_RECT.top, CUBICLE_RECT.width / 6.5, 
    LEFT_CUBICLE_HITBOX.height)
# middle hitbox
MIDDLE_CUBICLE_HITBOX_OFFSET = 60
MIDDLE_CUBICLE_HITBOX = pygame.Rect(
    CUBICLE_RECT.left, 
    CUBICLE_RECT.top + MIDDLE_CUBICLE_HITBOX_OFFSET, 
    CUBICLE_RECT.width, 
    CUBICLE_RECT.height * (1/9))

# list of all cubicles and cubicles colliders, used to draw and control collisions
all_cubicles = []
all_cubicle_colliders = []

# office plant
OFFICE_PLANT_SCALE = 3
OFFICE_PLANT_SPRITE = pygame.image.load(os.path.join("assets", "objects", "office plant.png"))
OFFICE_PLANT_WIDTH, OFFICE_PLANT_HEIGHT = OFFICE_PLANT_SPRITE.get_width() * OFFICE_PLANT_SCALE, OFFICE_PLANT_SPRITE.get_height() * OFFICE_PLANT_SCALE
OFFICE_PLANT_RECT = pygame.Rect(WINDOW_WIDTH / 2 - OFFICE_PLANT_WIDTH / 2, WINDOW_HEIGHT / 2 - OFFICE_PLANT_HEIGHT / 2, OFFICE_PLANT_WIDTH, OFFICE_PLANT_HEIGHT)
# all office plants and office plant colliders, used to draw and control collisions
all_office_plants = []
all_office_plant_colliders = []

# manager's office main desk
MANAGER_DESK_SPRITE = pygame.image.load(os.path.join("assets", "objects", "manager's office", "manager's office desk.png"))
MANAGER_DESK_SCALE = 3
MANAGER_DESK_WIDTH, MANAGER_DESK_HEIGHT = MANAGER_DESK_SPRITE.get_width() * MANAGER_DESK_SCALE, \
    MANAGER_DESK_SPRITE.get_height() * MANAGER_DESK_SCALE
MANAGER_DESK_RECT = pygame.Rect(
    MANAGER_OFFICE_FLOOR_RECT.x + MANAGER_OFFICE_FLOOR_BACKGROUND.get_width() / 2 + 100, 
    MANAGER_OFFICE_FLOOR_RECT.y + 400, 
    MANAGER_DESK_WIDTH, 
    MANAGER_DESK_HEIGHT)
MANAGER_DESK_HITBOX = pygame.Rect(MANAGER_DESK_RECT.x, MANAGER_DESK_RECT.y, MANAGER_DESK_WIDTH, MANAGER_DESK_HEIGHT - 200)

# manager's chair
MANAGER_CHAIR_SPRITE = pygame.image.load(os.path.join("assets", "objects", "manager's office", "manager's chair.png"))

# bookcase
BOOKCASE_COLLIDER_OFFSET = 145
# bookcase 1
BOOKCASE_SPRITE1 = pygame.image.load(os.path.join("assets", "objects", "bookcases", "bookcase.png"))
BOOKCASE_SCALE = 3
BOOKCASE_WIDTH, BOOKCASE_HEIGHT = BOOKCASE_SPRITE1.get_width() * BOOKCASE_SCALE, BOOKCASE_SPRITE1.get_height() * BOOKCASE_SCALE
BOOKCASE1_RECT = pygame.Rect(MANAGER_OFFICE_FLOOR_RECT.x + MANAGER_OFFICE_FLOOR_RECT.width / 2 - BOOKCASE_WIDTH * 4 / 2 - 150, MANAGER_OFFICE_FLOOR_RECT.y - 50, BOOKCASE_WIDTH, BOOKCASE_HEIGHT)
BOOKCASE1_COLLIDER = pygame.Rect(BOOKCASE1_RECT.x, BOOKCASE1_RECT.y, BOOKCASE_WIDTH, BOOKCASE_HEIGHT - BOOKCASE_COLLIDER_OFFSET)
# bookcase 2
BOOKCASE_SPRITE2 = pygame.image.load(os.path.join("assets", "objects", "bookcases", "bookcase 2.png"))
BOOKCASE2_RECT = pygame.Rect(BOOKCASE1_RECT.x + BOOKCASE_WIDTH, BOOKCASE1_RECT.y, BOOKCASE_WIDTH, BOOKCASE_HEIGHT)
BOOKCASE2_COLLIDER = pygame.Rect(BOOKCASE2_RECT.x, BOOKCASE2_RECT.y, BOOKCASE_WIDTH, BOOKCASE_HEIGHT - BOOKCASE_COLLIDER_OFFSET)
# bookcase 3
BOOKCASE_SPRITE3 = pygame.image.load(os.path.join("assets", "objects", "bookcases", "bookcase 3.png"))
BOOKCASE3_RECT = pygame.Rect(BOOKCASE1_RECT.x + BOOKCASE_WIDTH * 2, BOOKCASE1_RECT.y, BOOKCASE_WIDTH, BOOKCASE_HEIGHT)
BOOKCASE3_COLLIDER = pygame.Rect(BOOKCASE3_RECT.x, BOOKCASE3_RECT.y, BOOKCASE_WIDTH, BOOKCASE_HEIGHT - BOOKCASE_COLLIDER_OFFSET)
# bookcase 4
BOOKCASE_SPRITE4 = pygame.image.load(os.path.join("assets", "objects", "bookcases", "bookcase 4.png"))
BOOKCASE4_RECT = pygame.Rect(BOOKCASE1_RECT.x + BOOKCASE_WIDTH * 3, BOOKCASE1_RECT.y, BOOKCASE_WIDTH, BOOKCASE_HEIGHT)
BOOKCASE4_COLLIDER = pygame.Rect(BOOKCASE4_RECT.x, BOOKCASE4_RECT.y, BOOKCASE_WIDTH, BOOKCASE_HEIGHT - BOOKCASE_COLLIDER_OFFSET)
# bookcase toggle
BOOKCASE_TOGGLE_RECT = pygame.Rect(BOOKCASE1_RECT.x, BOOKCASE1_RECT.y, BOOKCASE1_RECT.width * 4, BOOKCASE1_RECT.height + 10)

# carpet
BLUE_CARPET_SCALE = 2
BLUE_CARPET_SPRITE = pygame.image.load(os.path.join("assets", "objects", "carpet.png"))
BLUE_CARPET_WIDTH, BLUE_CARPET_HEIGHT = BLUE_CARPET_SPRITE.get_width() * BLUE_CARPET_SCALE, BLUE_CARPET_SPRITE.get_height() * BLUE_CARPET_SCALE
BLUE_CARPET_RECT = pygame.Rect(
    MANAGER_DESK_RECT.x + MANAGER_DESK_RECT.width / 2 - BLUE_CARPET_WIDTH / 2, 
    MANAGER_DESK_RECT.y + MANAGER_DESK_RECT.height + 20, 
    BLUE_CARPET_WIDTH, 
    BLUE_CARPET_HEIGHT)

# kitchen counter
KITCHEN_COUNTER_SPRITE = pygame.image.load(os.path.join("assets", "objects", "kitchen counter", "kitchen counter.png"))
KITCHEN_COUNTER_SCALE = 4
KITCHEN_COUNTER_WIDTH, KITCHEN_COUNTER_HEIGHT = KITCHEN_COUNTER_SPRITE.get_width() * KITCHEN_COUNTER_SCALE, KITCHEN_COUNTER_SPRITE.get_height() * KITCHEN_COUNTER_SCALE
KITCHEN_COUNTER_RECT = pygame.Rect(
    KITCHEN_FLOOR_RECT.x + 5, 
    KITCHEN_FLOOR_RECT.y + 10, 
    KITCHEN_COUNTER_WIDTH, 
    KITCHEN_COUNTER_HEIGHT)
KITCHEN_COUNTER_COLLIDER = pygame.Rect(
    KITCHEN_COUNTER_RECT.x, 
    KITCHEN_COUNTER_RECT.y, 
    KITCHEN_COUNTER_WIDTH, 
    KITCHEN_COUNTER_HEIGHT - 130)

# fridge
FRIDGE_SPRITE = pygame.image.load(os.path.join("assets", "objects", "fridge.png"))
FRIDGE_SCALE = 4
FRIDGE_WIDTH, FRIDGE_HEIGHT = FRIDGE_SPRITE.get_width() * FRIDGE_SCALE, FRIDGE_SPRITE.get_height() * FRIDGE_SCALE
FRIDGE_RECT = pygame.Rect(
    KITCHEN_COUNTER_RECT.x + KITCHEN_COUNTER_WIDTH + 5, 
    KITCHEN_FLOOR_RECT.y - FRIDGE_HEIGHT / 2 + 35, 
    FRIDGE_WIDTH, 
    FRIDGE_HEIGHT)
FRIDGE_COLLIDER = pygame.Rect(
    FRIDGE_RECT.x, 
    FRIDGE_RECT.y, 
    FRIDGE_WIDTH, 
    FRIDGE_HEIGHT - 130)

# glass of cornmeal
CORNMEAL_SPRITE = pygame.image.load(os.path.join("assets", "objects", "glass of cornmeal.png"))
CORNMEAL_SCALE = 3
CORNMEAL_WIDTH, CORNMEAL_HEIGHT = CORNMEAL_SPRITE.get_width() * CORNMEAL_SCALE, CORNMEAL_SPRITE.get_height() * CORNMEAL_SCALE
CORNMEAL_RECT = pygame.Rect(
    KITCHEN_COUNTER_RECT.x + 400, 
    KITCHEN_COUNTER_RECT.y + 10, 
    CORNMEAL_WIDTH, 
    CORNMEAL_HEIGHT)

# corn
CORN_SPRITE = pygame.image.load(os.path.join("assets", "objects", "catch-a-corn", "corn.png"))
CORN_SCALE = 5.5
CORN_WIDTH, CORN_HEIGHT = CORN_SPRITE.get_width() * CORN_SCALE, CORN_SPRITE.get_height() * CORN_SCALE
CORN_RECT = pygame.Rect(WINDOW_WIDTH / 2, -100, CORN_WIDTH, CORN_HEIGHT)

# corn basket
CORN_BASKET_SPRITE = pygame.image.load(os.path.join("assets", "objects", "catch-a-corn", "corn basket.png"))
CORN_BASKET_SCALE = 5.5
CORN_BASKET_WIDTH, CORN_BASKET_HEIGHT = CORN_BASKET_SPRITE.get_width() * CORN_BASKET_SCALE, CORN_BASKET_SPRITE.get_height() * CORN_BASKET_SCALE
CORN_BASKET_RECT = pygame.Rect(WINDOW_WIDTH / 2, WINDOW_HEIGHT - 130, CORN_BASKET_WIDTH, CORN_BASKET_HEIGHT)
# mechanics
corn_basket_x_velocity = 8
corn_basket_y_velocity = 8

# egg
EGG_SPRITE = pygame.image.load(os.path.join("assets", "objects", "catch-a-corn", "egg.png"))
EGG_SCALE = 5.5
EGG_WIDTH, EGG_HEIGHT = EGG_SPRITE.get_width() * EGG_SCALE, EGG_SPRITE.get_height() * EGG_SCALE
EGG_RECT = pygame.Rect(CATCH_A_CORN_BACKGROUND_RECT.x + CATCH_A_CORN_BACKGROUND_RECT.width - 60, 20, EGG_WIDTH, EGG_HEIGHT)

# chicken img
CHICKEN_IMG = pygame.image.load(os.path.join("assets", "objects", "catch-a-corn", "chicken img.png"))
CHICKEN_IMG_SCALE = 4
CHICKEN_IMG_WIDTH, CHICKEN_IMG_HEIGHT = CHICKEN_IMG.get_width() * CHICKEN_IMG_SCALE, CHICKEN_IMG.get_height() * CHICKEN_IMG_SCALE
CHICKEN_IMG_RECT = pygame.Rect(CATCH_A_CORN_BACKGROUND_RECT.x + 10, 10, CHICKEN_IMG_WIDTH, CHICKEN_IMG_HEIGHT)

# health
HEALTH_SPRITE = pygame.image.load(os.path.join("assets", "objects", "catch-a-corn", "health.png"))
HEALTH_SCALE = 5
HEALTH_WIDTH, HEALTH_HEIGHT = HEALTH_SPRITE.get_width() * HEALTH_SCALE, HEALTH_SPRITE.get_height() * HEALTH_SCALE
HEALTH_RECT = pygame.Rect(CATCH_A_CORN_BACKGROUND_RECT.x + 10 + 100, 20, HEALTH_WIDTH, HEALTH_HEIGHT)
all_health = []

# players
# player1
PLAYER_SPRITE = pygame.image.load(os.path.join("assets", "player", "bill.png"))
PLAYER_ICON = pygame.image.load(os.path.join("assets", "player", "player icon.png"))
PLAYER_WIDTH, PLAYER_HEIGHT = PLAYER_SPRITE.get_width() * 3, PLAYER_SPRITE.get_height() * 3
PLAYER_SIZE = (PLAYER_WIDTH, PLAYER_HEIGHT)
PLAYER_HITBOX = pygame.Rect(
    WINDOW_WIDTH / 2 - PLAYER_WIDTH / 2 , 
    WINDOW_HEIGHT / 2 - PLAYER_HEIGHT / 2 + 5, 
    PLAYER_WIDTH, PLAYER_HEIGHT)
PLAYER_X_VELOCITY = 30
PLAYER_Y_VELOCITY = 30
walk_count = 0

# player run animation frames
# left
PLAYER_RUN_ANIMATION_LEFT_FRAME1 = pygame.transform.scale(
    pygame.image.load(os.path.join("assets", "player", "run animation", "left", "run frame 1.png")), PLAYER_SIZE)
PLAYER_RUN_ANIMATION_LEFT_FRAME2 = pygame.transform.scale(
    pygame.image.load(os.path.join("assets", "player", "run animation", "left", "run frame 2.png")), PLAYER_SIZE)
PLAYER_RUN_ANIMATION_LEFT_FRAME3 = pygame.transform.scale(
    pygame.image.load(os.path.join("assets", "player", "run animation", "left", "run frame 3.png")), PLAYER_SIZE)
# right
PLAYER_RUN_ANIMATION_RIGHT_FRAME1 = pygame.transform.scale(
    pygame.image.load(os.path.join("assets", "player", "run animation", "right", "run frame 1.png")), PLAYER_SIZE)
PLAYER_RUN_ANIMATION_RIGHT_FRAME2 = pygame.transform.scale(
    pygame.image.load(os.path.join("assets", "player", "run animation", "right", "run frame 2.png")), PLAYER_SIZE)
PLAYER_RUN_ANIMATION_RIGHT_FRAME3 = pygame.transform.scale(
    pygame.image.load(os.path.join("assets", "player", "run animation", "right", "run frame 3.png")), PLAYER_SIZE)

# character images and icons
# scale character image sizes
CHARACTER_SCALE = 4
# tommy
TOMMY_SPRITE = pygame.image.load(os.path.join("assets", "characters", "sprites", "tommy.png"))
CHARACTER_WIDTH, CHARACTER_HEIGHT = TOMMY_SPRITE.get_width() * CHARACTER_SCALE, TOMMY_SPRITE.get_height() * CHARACTER_SCALE
TOMMY_RECT = pygame.Rect(750, 140, CHARACTER_WIDTH, CHARACTER_HEIGHT)
TOMMY_ICON = pygame.image.load(os.path.join("assets", "characters", "character icons", "tommy-icon.png"))
# arnold
ARNOLD_SPRITE = pygame.image.load(os.path.join("assets", "characters", "sprites", "arnold.png"))
ARNOLD_RECT = pygame.Rect(900, 900, CHARACTER_WIDTH, CHARACTER_HEIGHT)
ARNOLD_ICON = pygame.image.load(os.path.join("assets", "characters", "character icons", "arnold-icon.png"))
# jacob
JACOB_SPRITE = pygame.image.load(os.path.join("assets", "characters", "sprites", "jacob.png"))
JACOB_RECT = pygame.Rect(2300, 800, CHARACTER_WIDTH, CHARACTER_HEIGHT)
JACOB_ICON = pygame.image.load(os.path.join("assets", "characters", "character icons", "jacob-icon.png"))
# jillian
JILLIAN_SPRITE = pygame.image.load(os.path.join("assets", "characters", "sprites", "jillian.png"))
JILLIAN_RECT = pygame.Rect(3200, 140, CHARACTER_WIDTH, CHARACTER_HEIGHT)
JILLIAN_ICON = pygame.image.load(os.path.join("assets", "characters", "character icons", "jillian-icon.png"))
# john
JOHN_SPRITE = pygame.image.load(os.path.join("assets", "characters", "sprites", "john.png"))
JOHN_RECT = pygame.Rect(3700, 1450, CHARACTER_WIDTH, CHARACTER_HEIGHT)
JOHN_ICON = pygame.image.load(os.path.join("assets", "characters", "character icons", "john-icon.png"))
# may
MAY_SPRITE = pygame.image.load(os.path.join("assets", "characters", "sprites", "may.png"))
MAY_RECT = pygame.Rect(4250, 800, CHARACTER_WIDTH, CHARACTER_HEIGHT)
MAY_ICON = pygame.image.load(os.path.join("assets", "characters", "character icons", "may-icon.png"))
# princess
PRINCESS_SPRITE = pygame.image.load(os.path.join("assets", "characters", "sprites", "princess.png"))
PRINCESS_RECT = pygame.Rect(4650, 800, CHARACTER_WIDTH, CHARACTER_HEIGHT)
PRINCESS_ICON = pygame.image.load(os.path.join("assets", "characters", "character icons", "princess-icon.png"))
# july
JULY_SPRITE = pygame.image.load(os.path.join("assets", "characters", "sprites", "july.png"))
JULY_RECT = pygame.Rect(2600, 1400, CHARACTER_WIDTH, CHARACTER_HEIGHT)
JULY_ICON = pygame.image.load(os.path.join("assets", "characters", "character icons", "july-icon.png"))
# thomas
THOMAS_SPRITE = pygame.image.load(os.path.join("assets", "characters", "sprites", "thomas.png"))
THOMAS_RECT = pygame.Rect(1300, 1450, CHARACTER_WIDTH, CHARACTER_HEIGHT)
THOMAS_ICON = pygame.image.load(os.path.join("assets", "characters", "character icons", "thomas-icon.png"))
# flower
FLOWER_SPRITE = pygame.image.load(os.path.join("assets", "characters", "sprites", "flower.png"))
FLOWER_RECT = pygame.Rect(3650, 140, CHARACTER_WIDTH, CHARACTER_HEIGHT)
FLOWER_ICON = pygame.image.load(os.path.join("assets", "characters", "character icons", "flower-icon.png"))
# pete
PETE_SPRITE = pygame.image.load(os.path.join("assets", "characters", "sprites", "pete.png"))
PETE_RECT = pygame.Rect(4650, 1450, CHARACTER_WIDTH, CHARACTER_HEIGHT)
PETE_ICON = pygame.image.load(os.path.join("assets", "characters", "character icons", "pete-icon.png"))
# manager
# human form
MANAGER_SPRITE =pygame.image.load(os.path.join("assets", "characters", "sprites", "manager.png"))
MANAGER_ICON = pygame.image.load(os.path.join("assets", "characters", "character icons", "manager-icon.png"))
# chicken form
CHICKEN_SPRITE = pygame.image.load(os.path.join("assets", "characters", "sprites", "chicken.png"))
CHICKEN_LEFT_SPRITE = pygame.image.load(os.path.join("assets", "characters", "sprites", "chicken (left).png"))
CHICKEN_ICON = pygame.image.load(os.path.join("assets", "characters", "character icons", "manager-real-icon.png"))
MANAGER_RECT = pygame.Rect(MANAGER_DESK_RECT.x + MANAGER_DESK_RECT.width / 2 - CHARACTER_WIDTH + 70, MANAGER_DESK_RECT.y - 90, CHARACTER_WIDTH, CHARACTER_HEIGHT)

# character-player dialogue, indexed in chronological order
character_dialogue = {
    "tommy": {
        "character": [
            [["Hi! I'm Tommy! :) You're the new employee, right?",
              "Your name's Bill, right?"],
             ["You live in the cubicle to the left, right?"],
             ["HI NEIGHBOUR!!!"]],

            [["In this office, I am (ominous voice) the keeper",
              "of eggs. Everyday I make my rounds and deliver",
              "the eggs to EVERY cubicle. NO EXCEPTIONS."]],

            [["Sometimes when I deliver my eggs to the others",
              "they get mad. They throw the eggs back at me.",
              "Maybe it's because I boiled them."],
             ["Maybe they don't like boiled eggs?"]],

            [["I'M TOMMY!!! I LIKE EGGS!!"]]],

        "player": ["Oh, uh, hi.",
                   "Eggs...?"]},
    
    "arnold": {
        "character": [
        [["So you're the new guy, huh? Figures. WE CAN TELL."],
         ["The way you walk. The way you talk. Everything",
          "about you SCREAMS newbie. *Scoff*"]],

        [["Get out of my sight before I report you to",
         "the manager."]]],
         
         "player": []},
    
    "jacob": {
        "character": [
        [["*Munch* *munch* *munch*. *Sniff*."],
         ["You got games on your phone?"]],
         [["Tommy and I live in our cubicles. No, I'm not",
           "lying. We really never leave this place. I mean,",
           "what's the point when everything I need is right",
           "here?"],
          ["I mean, there's no shower here so that's kind of",
           "a trade-off. This place's still better than my",
           "mom's, anyway."],
           ["What? Why are you looking at me like that?"]],
          [["What? Why are you looking at me like that?"]]],
         
        "player": []},
    
    "jillian": {
        "character": [["CORN"]],
        
        "player": []},
    
    "john": {
        "character": [[[":)"]]],
        
        "player": []},
    
    "may": {
        "character": [
        [["Today the company is holding a costume party.",
         "Too bad you joined the company too late to",
         "participate!"]]],
         
         "player": []},
    
    "princess": {
        "character": [
            [["Hi! Are you new here? My name's Princess!",
              "Don't listen to Pete. He doesn't know",
              "anything!"]],
            [["Pete's the guy just farther down, near",
              "John."]]],
        
        "player": []},
    
    "july": {
        "character": [
        [["Hey, new guy!"],
         ["It appears the manager is looking for you.",
          "Head down through the doorway below. It seems to",
          "be important."]],
        [["The manager doesn't like to wait, hehe."]]],
        
        "player": []},
    
    "thomas": {
        "character": [
            [["Did you see my brother Tommy over there?",
              "I hear you're the new guy! Bill, isn't it?"],
             ["Like Tommy I am the (ominous voice) keeper",
              "of muffins."],
             ["Huh? They look moldy? HOW DARE YOU SUGGEST",
              "THAT I, THE GREAT THOMAS, AM DELIVERING",
              "moLDy MUFFINS TO THE PEOPLE??? >:("],
             ["*Ahem*, well, I've only had them for a couple",
              "of months, so they shouldn't be moldy yet."]],
            [["You look a bit concerned. How 'bout you try a",
              "muffin for yourself?"]]],
        
        "player": [
            [["You take a muffin. It's clearly past",
              "its due date."],
             ["You bite into the muffin. Yup, that's",
              "definitely mold."]]]},
    
    "flower": {
        "character": [
        [["Yeah, I'm wearing this t-shirt again.",
         "You got a problem with that, bud?",],
        ["What do you mean, \"what t-shirt?\"",
          "You got eyes, bud???"]],
        [["What do you mean, \"what t-shirt?\"",
         "You got eyes, bud???"]]],
         
        "player": []},
    
    "pete": {
        "character": [
            [["Hey. New guy. You need to get out of here.",
             "It's.. It's not safe here."]],
            [["No, you really, REALLY need to get out of here.",
             "They- they- ..."],
             ["No, there's too many people around here.",
              "Come back after becoming more familiar with",
              "the company. You'll get it then."]],
            [["Come back after you've seen more."]]],
        
        "player": []}
}

character_dialogue_world2 = {
    "manager": {
        "character": [
            [["So, I've been waiting..."],
             ["Bill, isn't it? We've met before."],
             ["..."],
             ["So, how are you liking your new job",
              "here at Cornhouse Realty? Are your",
              "co-workers treating you well?"],
             ["..."],
             ["Well, I see there is no need for",
              "formal introductions..."],
             ["Let's just get to work then."],
             ["Your first task...."],
             ["Is to fetch me a glass of cornmeal.",
              "(Helpful hint: you can find it in the kitchen)"]],
             [["Well, get to work then, son!"]]],

        "player": []
    }
}

quest_complete_dialogue = {
    "manager": {
        "character": [
            [["Aha, you've brought me the cornmeal. I can",
              "see you are a diligent worker, son.",
              "Keep this way and you will be rewarded for your",
              "efforts accordingly."],
              ["Anyway, I think you have demonstrated your",
               "abilities very well. Now that you have proved",
               "your loyalty, I will assign your next task."],
              ["As you may (or may not) have known, we here at",
               "Cornouse Realty are focused mainly on the",
               "residential real estate market."],
              ["To be even more specific, we specialize in",
               "apartments and houses here in Corntown."],
              ["Recently, we've been working on a development",
               "project to re-zone a 30 acre cornfield into",
               "a bustling city center."],
               ["(Funded in part by our sister company,",
               "'Cornhouse Investments', of course.)"],
              ["I was so impressed by your enthusiasm that I",
               "would like to personally offer you a role in",
               "this grand project."],
              ["Your next task is to partake in the bid for the",
               "land we are considering to purchase for this",
               "project."],
              ["You will head to your cubicle (the one beside",
               "Tommy's at the very top left-hand corner),",
               "and use your computer to bid EGGS for the land."],
              ["The more eggs you bid, the more likely we are",
                "to secure the piece of land. We are predicting",
                "you will need at least 100 eggs to succeed."],
              ["Hop to it, now! The bid starts in the next 10",
               "minutes, so there is no time to waste! Head to",
               "your cubicle and begin."]],
              [["Well, get to work then, son!"]]],

        "player": []
    }
}

quest2_complete_dialogue = {
    "manager": {
        "character": [
            [["You've secured the land? Ahah! As expected",
              "of our best (and only) new employee!"],
             ["I see you've been working hard there, Bill.",
              "A real go-getter you are! As I said previously,",
              "good people are rewarded. And you deserve a",
              "reward!"],
             ["Go on and have yourself a break. You deserve it!"],
             ["How about having a chat with your new co-workers?",
              "I'm sure they would like to get to know you, too!"],
             ["Anyway, it's my break time, too. Leave me now.",
              "I have a reservation at the best pizza place in",
              "town!"]],
              [["Go ahead and have a break! THAT'S AN ORDER,",
                "HAHA!"]]],

        "player": []
    },

    "tommy": {
        "character": [
            [["HEY, BEST NEW BUDDY!"],
             ["Oooooh by now the entire office has heard about",
              "your success!"],
             ["The way you showed up the entire room of bidders",
              "with those 100 EGGS was amazing! You absolutely",
              "did not hold back with those EGGS!"],
             ["I was so impressed watching you from my cubicle.",
              "As expected from my best buddy!"],
             ["You really are a Cornhouse Realty employee now,",
              "with that go-getter attitude! Haha!"],
             ["You should come over to my place to hangout some",
              "time, best buddy! :)"]],
            [["You should come over to my place to hangout some",
              "time, best buddy! :)"]]]
    },

    "arnold": {
        "character": [
            [["So. I heard about the cornfield.",
              "Not bad for a first-timer, but don't get",
              "ahead of yourself now."],
             ["One time, there was a big bid for a 100 acre",
              "ranch, and I spear-headed the operation.",
              "The game was tight, and I..."],
             ["(You leave before he can finish)."]],
            [["AS I WAS SAYING BEFORE YOU SO RUDELY LEFT,",
              "the bid was tight and I ever so bravely-",
              "(you leave before he can finish)."]]
        ]
    },

    "thomas": {
        "character": [
            [["Congrats on your first bid, Bill!",
              "To celebrate, how 'bout you have a",
              "muffin! It's my treat!"],
             ["(You take a muffin and reluctantly bite",
              "into it)."],
             ["(It tastes like sweaty socks)."],
             ["So, how is it? Good, right? I told you! They're",
              "not moldy!"],
             ["(You feel like crying)."]],
            [["I make the best muffins in the world!!! :D"]]]
    },

    "july": {
        "character": [
            [["That guy over there... That guy beside John,",
              "Pete... He's kind of odd, isn't he? Hehe."],
             ["Look over there. He's looking at you. It looks",
              "like he has something to say to you. Maybe you",
              "should talk to him, hehe."]],
            [["You should talk to Pete, hehe."]]
        ]
    },

    "pete": {
        "character": [
            [["I hear you've made a name for yourself,",
              "haven't you? It feels good to be",
              "respected by the manager, right?"],
             ["I would know. I was in your shoes those",
              "years ago. But I regret everything. Bill, I'm",
              "telling you. There's something off."],
             ["I'm saying this for your own good. Please,",
             "Bill. You cannot let the manager get to your",
             "head."],
             ["No, if anything, you need to leave here as",
              "soon as you can. It's not safe for you here.",
              "I... I can't say why. They're listening."],
             ["They have eyes and ears everywhere. They're",
               "always listening. Leave while you have the",
               "chance, Bill. Please."],
             ["Do what I should have all those years ago.",
              "Find somewhere else to work. It's not safe",
              "here."],
             ["..."],
             ["......."],
             ["You aren't leaving... Why aren't you",
              "leaving..."],
             ["Do you... not believe me?"],
             ["PLEASE. BILL."],
             ["..."],
             ["Hah.... fine. If you don't believe me,",
              "go see it for yourself."],
             ["Behind the manager's bookshelf..."],
             ["...Go look behind the manager's bookshelf."]],
             [["If you don't believe me, go look behind",
               "the manager's bookshelf."]]
        ]
    }
}

final_character_dialogue = {
    "manager": {
        "character": [
            [["..."],
             ["....."],
             ["!!!"],
             ["Bill!! What are you doing here?"],
             ["..."],
             ["Who am I, you ask? You don't recognize",
              "me?"],
             ["..."],
             ["...Hahaha. Of course you don't. It's",
               "me, your manager! HAHAHA!"],
             ["..."],
             ["You're a bit early for the meeting.",
              "HAHAHAHAAHA."],
             ["..."],
             ["..You already know by now."],
             ["Your fate was decided the moment you",
              "stepped foot in this building."],
             ["You aren't supposed to be here, are",
              "you?"],
             ["..."],
             ["Control. All you want is control."],
             ["Of your life, of your role in this",
              "world, of your actions. Of yourself."],
             ["Did any of that ever matter, though?"],
             ["Where did control ever get you?",
              "To this company? HAHAHA!"],
             ["Stuck in this lab! As if your current",
              "position is much of a blessing!",
              "HAHAHA!"],
             ["..."],
             ["You had your life all set out for you,",
              "didn't you? You live a perfect,",
              "comfortable life. No hardships."],
             ["Straight to university. Straight",
              "to a job. Proud of yourself, aren't ",
              "you?"],
             ["..."],
             ["But you are a man without conviction.",
              "There is no place in this world for",
              "a man like you."],
             ["In fact, there is no place for",
              "PEOPLE in this world."],
             ["..."],
             ["There is no place for HUMANS."],
             ["All you do is consume."],
             ["Consume, consume, consume."],
             ["But you never produce."],
             ["I mean, look at this world. Ever since",
              "your kind discovered how to.."],
             ["..optimize your consumption through",
              "industrial practices.."],
             ["YOU HUMANS HAVE DESTROYED EVERYTHING."],
             ["..."],
             ["..And us chickens..."],
             ["Are what you consume. Without a thought."],
             ["And you know, all of us here at Cornhouse",
              "Realty are chickens. I bet you didn't",
              "even realize that, huh?"],
             ["All your co-workers."],
             ["..."],
             ["..But today..."],
             ["Today, your oh-so-happy life will be",
              "utterly destroyed by what you loved",
              "consuming so much. CHICKENS."],
             ["TODAY IS WHEN ALL OF THIS ENDS."],
             ["You see, when I press this big ol' red",
              "button over here,"],
             ["You humans will CEASE TO EXIST."],
             ["..."],
             ["So, Bill. Any last words?"],
             ["..."],
             ["corn."],
             ["Umm what-"],
             ["corn"],
             ["..."],
             ["......"],
             ["CORN."],
             ["...?"],
             ["........?"],
             ["CORN!!!!"]
             ],
            [[""]]
        ]
    }
}

# text box
TEXT_BOX = pygame.Rect(120, WINDOW_HEIGHT - 200, WINDOW_WIDTH - 240, 200)
DIALOGUE_TOGGLE_BOX = pygame.Rect(0, 0, 50, 50)
CHARACTER_ICON_RECT = pygame.Rect(155, WINDOW_HEIGHT - 140, 100, 100)

# pathways
PATHWAY_SPRITE = pygame.image.load(os.path.join("assets", "pathway", "pathway.png"))
PATHWAY_RECT_SIZE = 300
PATHWAY_COLLIDER_WIDTH, PATHWAY_COLLIDER_HEIGHT = 200, 50
# to manager's office
TO_MANAGER_OFFICE_COLLIDER = pygame.Rect(
    OFFICE_FLOOR_RECT.left + OFFICE_FLOOR_RECT.width / 2 - 100, 
    OFFICE_FLOOR_RECT.top + OFFICE_FLOOR_HEIGHT * floor_scale - 50, 
    PATHWAY_COLLIDER_WIDTH, 
    PATHWAY_COLLIDER_HEIGHT)

TO_MANAGER_OFFICE_RECT = pygame.Rect(TO_MANAGER_OFFICE_COLLIDER.x , TO_MANAGER_OFFICE_COLLIDER.y - 250, PATHWAY_RECT_SIZE, PATHWAY_RECT_SIZE)

# to main office
TO_OFFICE_COLLIDER = pygame.Rect(
    MANAGER_OFFICE_FLOOR_RECT.x + MANAGER_OFFICE_FLOOR_BACKGROUND.get_width() / 2 + 100, 
    150, 
    PATHWAY_COLLIDER_WIDTH, 
    PATHWAY_COLLIDER_HEIGHT)

TO_OFFICE_RECT = pygame.Rect(TO_OFFICE_COLLIDER.x , TO_OFFICE_COLLIDER.y - 250, PATHWAY_RECT_SIZE, PATHWAY_RECT_SIZE)

# to kitchen
TO_KITCHEN_COLLIDER = pygame.Rect(TO_MANAGER_OFFICE_RECT.x, OFFICE_FLOOR_RECT.y, PATHWAY_COLLIDER_WIDTH, PATHWAY_COLLIDER_HEIGHT) 
TO_KITCHEN_RECT = pygame.Rect(TO_KITCHEN_COLLIDER.x, TO_KITCHEN_COLLIDER.y, PATHWAY_RECT_SIZE, PATHWAY_RECT_SIZE) 

# to main office from kitchen
TO_MAIN_OFFICE_COLLIDER = pygame.Rect(
    KITCHEN_FLOOR_RECT.x + KITCHEN_FLOOR_RECT.width - 330, 
    KITCHEN_FLOOR_RECT.y + KITCHEN_FLOOR_RECT.height - 50, 
    PATHWAY_COLLIDER_WIDTH, 
    PATHWAY_COLLIDER_HEIGHT) 

TO_MAIN_OFFICE_RECT = pygame.Rect(
    TO_MAIN_OFFICE_COLLIDER.x - 20, 
    TO_MAIN_OFFICE_COLLIDER.y - 250, 
    PATHWAY_RECT_SIZE, 
    PATHWAY_RECT_SIZE) 

# to hallway1 
TO_HALLWAY1_COLLIDER = pygame.Rect(BOOKCASE1_RECT.x + BOOKCASE1_RECT.width * 4 / 2 - 100, BOOKCASE1_RECT.y, 200, 50)
TO_HALLWAY1_RECT = pygame.Rect(TO_HALLWAY1_COLLIDER.x -45, TO_HALLWAY1_COLLIDER.y, PATHWAY_RECT_SIZE, BOOKCASE_HEIGHT - 20)

# to manager's office from hallway
TO_MANAGER_FROM_OFFICE_COLLIDER = pygame.Rect(HALLWAY1_RECT.x, HALLWAY1_RECT.y, 220, HALLWAY1_RECT.height)

# to hallway2
TO_HALLWAY_2_COLLIDER = pygame.Rect(HALLWAY1_RECT.x + HALLWAY1_RECT.width - 60, HALLWAY1_RECT.y, 60, HALLWAY1_RECT.height)

# to lab
TO_HALLWAY1_FROM_HALLWAY2_COLLIDER = pygame.Rect(TO_MANAGER_FROM_OFFICE_COLLIDER.x, TO_HALLWAY_2_COLLIDER.y, 60, HALLWAY1_RECT.height)
TO_LAB_COLLIDER = pygame.Rect(HALLWAY2_RECT.x + HALLWAY2_RECT.width - 60, TO_HALLWAY_2_COLLIDER.y, 60, HALLWAY1_RECT.height)

# list of all pathways
office_pathways = [TO_MANAGER_OFFICE_COLLIDER, TO_KITCHEN_COLLIDER]
manager_office_pathways = [TO_OFFICE_COLLIDER, TO_HALLWAY1_COLLIDER]
kitchen_pathways = [TO_MAIN_OFFICE_COLLIDER]
hallway1_pathways = [TO_MANAGER_FROM_OFFICE_COLLIDER, TO_HALLWAY_2_COLLIDER]
hallway2_pathways = [TO_HALLWAY1_FROM_HALLWAY2_COLLIDER, TO_LAB_COLLIDER]

# quest goals
quest_goals = {
    "1": "Goal: fetch the manager a glass of cornmeal from the kitchen.",
    "2": "New goal: Head to your cubicle to bid 100 EGGS for a 30 acre cornfield.",
    "3": "New goal: Have a break and chat with your co-workers. That's an order!",
    "4": "Go to the manager's office and check behind the bookshelf."
}

QUEST_TOGGLE_BOX = pygame.Rect(0, 0, 50, 50)

# sounds
# music
OFFICE_MUSIC = pygame.mixer.Sound(os.path.join("assets", "sounds", "music", "thelounge.mp3"))
HALLWAY_MUSIC = pygame.mixer.Sound(os.path.join("assets", "sounds", "music", "caves-of-dawn-10376.mp3"))
LAB_MUSIC = pygame.mixer.Sound(os.path.join("assets", "sounds", "music", "dark-ambient-126122.mp3"))
CATCH_A_CORN_INTRO_MUSIC = pygame.mixer.Sound(os.path.join("assets", "sounds", "music", "ccs2-103546.mp3"))
CATCH_A_CORN_MUSIC = pygame.mixer.Sound(os.path.join("assets", "sounds", "music", "suits-you-69233.mp3"))
MANAGER_THEME = pygame.mixer.Sound(os.path.join("assets", "sounds", "music", "suits-you-69233.mp3"))
INTRO_THEME = pygame.mixer.Sound(os.path.join("assets", "sounds", "music", "bensound free music.mp3"))
END_THEME = pygame.mixer.Sound(os.path.join("assets", "sounds", "music", "a-small-miracle-132333.mp3"))
# sound effects
MOVE_BOOKCASE = pygame.mixer.Sound(os.path.join("assets", "sounds", "sfx", "earth-rumble-6953.mp3"))
DIALOGUE_TOGGLE_SOUND = pygame.mixer.Sound(os.path.join("assets", "sounds", "sfx", "medium-text-blip-14855.mp3"))
START_GAME_SOUND = pygame.mixer.Sound(os.path.join("assets", "sounds", "sfx", "game-start-6104.mp3"))
CATCH_A_CORN_WIN_SOUND = pygame.mixer.Sound(os.path.join("assets", "sounds", "sfx", "winsquare-6993.mp3"))
CATCH_A_CORN_LOSE_SOUND = pygame.mixer.Sound(os.path.join("assets", "sounds", "sfx", "8-bit-video-game-fail-version-2-145478.mp3"))
CATCH_A_CORN_LOSE_SOUND.set_volume(0.5)
CATCH_A_CORN_CATCH_CORN_SOUND = pygame.mixer.Sound(os.path.join("assets", "sounds", "sfx", "8-bit-video-game-points-version-1-145826.mp3"))
CATCH_A_CORN_LOSE_HEALTH_SOUND = pygame.mixer.Sound(os.path.join("assets", "sounds", "sfx", "lose health.mp3"))
CATCH_A_CORN_LOSE_HEALTH_SOUND.set_volume(0.5)
PICK_UP_OBJECT_SOUND = pygame.mixer.Sound(os.path.join("assets", "sounds", "sfx", "pick up object.mp3"))
QUEST_SOUND = pygame.mixer.Sound(os.path.join("assets", "sounds", "sfx", "quest.mp3"))
QUEST_COMPLETE_SOUND = pygame.mixer.Sound(os.path.join("assets", "sounds", "sfx", "confirm-38513.mp3"))
CORN_WHOOSH_SOUND = pygame.mixer.Sound(os.path.join("assets", "sounds", "sfx", "cartoony-whooshes-7114.mp3"))
MANAGER_HIT_SOUND = pygame.mixer.Sound(os.path.join("assets", "sounds", "sfx", "ding-idea-40142.mp3"))
END_SOUND = pygame.mixer.Sound(os.path.join("assets", "sounds", "sfx", "door-slam-sound-effect-21878.mp3"))

# colours
NAVY_BLUE = (30, 33, 36)
BLACK = "black"
WHITE = "white"
DARK_GREY = (31, 31, 31)
YELLOW = (255, 251, 0)
DARK_GREEN = (0, 117, 16)

# fonts
PRESS_START_2P_REGULAR = os.path.join("assets", "fonts", "PressStart2P-Regular", "PressStart2P-Regular.ttf")

class create:
    class background:
        def __init__(self, background_img, rect):
            self.background_img = background_img
            self.rect = rect
    
    class mechanics:
        class movement:
            def __init__(self, x_velocity, y_velocity, left_key, right_key, up_key, down_key, left_limit, right_limit, top_limit, bottom_limit, toggle_movement, toggle_y_velocity):
                self.x_velocity = x_velocity
                self.y_velocity = y_velocity
                self.left_key = left_key
                self.right_key = right_key
                self.up_key = up_key
                self.down_key = down_key
                self.left_limit = left_limit
                self.right_limit = right_limit
                self.top_limit = top_limit
                self.bottom_limit = bottom_limit
                self.toggle_movement = toggle_movement
                self.toggle_y_velocity = toggle_y_velocity
        
        class collider:
            class player:
                def __init__(self, hitbox):
                    self.hitbox = hitbox
                
        class dialogue:
            class text_box:
                def __init__(self, rect, character_name, character_icon, text, toggle, text_pos_top):
                    self.rect = rect
                    self.character_name = character_name
                    self.character_icon = character_icon
                    self.text = text
                    self.toggle = toggle
                    self.text_pos_top = text_pos_top

            class text_box_toggle:
                def __init__(self, toggle):
                    self.toggle = toggle

        class quest:
            def __init__(self, quest_num, goal, toggle_collect, has_item, text_color):
                self.quest_num = quest_num
                self.goal = goal
                self.toggle_collect = toggle_collect
                self.has_item = has_item
                self.text_color = text_color

            # create player quest settings
            class set_quest:
                def __init__(self, has_quest, quest):
                    self.has_quest = has_quest
                    self.quest = quest

    class player:
        def __init__(self, sprite, rect, movement, collider, dialogue_toggle, quest_set, can_play_minigame, can_move_bookcase, bookcase_moved, debug):
            self.sprite = sprite
            self.rect = rect
            self.movement = movement
            self.collider = collider
            self.dialogue_toggle = dialogue_toggle
            self.quest_set = quest_set
            self.can_play_minigame = can_play_minigame
            self.can_move_bookcase = can_move_bookcase
            self.bookcase_moved = bookcase_moved
            self.debug = debug

    class character:
        def __init__(self, name, sprite, rect, icon, dialogue, dialogue_index, dialogue_toggle_index, first_line, dialogue_end, final_dialogue):
            self.name = name
            self.sprite = sprite
            self.rect = rect
            self.icon = icon
            self.dialogue = dialogue
            self.dialogue_index = dialogue_index
            self.dialogue_toggle_index = dialogue_toggle_index
            self.first_line = first_line
            self.dialogue_end = dialogue_end
            self.final_dialogue = final_dialogue

    class object:
        def __init__(self, sprite, rect, collider):
            self.sprite = sprite
            self.rect = rect
            self.collider = collider

        # cubicles
        class cubicles:
            def cubicle_array(num_cubicles, cubicles, cubicle_colliders, left, top):
                for i in range(num_cubicles + 1):
                    cubicles.append(pygame.Rect(left, top, CUBICLE_RECT.width, CUBICLE_RECT.height))
                    cubicle_colliders.append([
                        pygame.Rect(left, top, LEFT_CUBICLE_HITBOX.width, LEFT_CUBICLE_HITBOX.height - 50),
                        pygame.Rect(left + CUBICLE_RECT.width - RIGHT_CUBICLE_HITBOX.width, top, RIGHT_CUBICLE_HITBOX.width, RIGHT_CUBICLE_HITBOX.height - 50),
                        pygame.Rect(
                            left + LEFT_CUBICLE_HITBOX.width, 
                            top + MIDDLE_CUBICLE_HITBOX_OFFSET, 
                            MIDDLE_CUBICLE_HITBOX.width, 
                            MIDDLE_CUBICLE_HITBOX.height)])
                    # shift cubicle right
                    left += CUBICLE_RECT.width
        
            def create_cubicles(num_cubicles, left, top):
                cubicles = []
                cubicle_colliders = []
                create.object.cubicles.cubicle_array(num_cubicles, cubicles, cubicle_colliders, left, top)
                all_cubicles.append(cubicles)
                all_cubicle_colliders.append(cubicle_colliders)
            
            def all_cubicles(ROW_DISTANCE):
                NUM_COLUMNS = 3

                # create left column
                left_column_top = -50
                left_column_left = 100
                num_cubicles_left_column = 4
                for i in range(NUM_COLUMNS):
                    create.object.cubicles.create_cubicles(num_cubicles_left_column, left_column_left, left_column_top)
                    left_column_top += ROW_DISTANCE
                
                # create right column
                right_column_top = -50
                right_column_left = CUBICLE_RECT.width * num_cubicles_left_column + CUBICLE_RECT.width * 2
                num_cubicles_right_column = 4
                for i in range(NUM_COLUMNS):
                    create.object.cubicles.create_cubicles(num_cubicles_right_column, right_column_left, right_column_top)
                    right_column_top += ROW_DISTANCE
        
        # office plants
        class office_plants:
            def office_plant_array(num_plants, plants, plant_colliders, left, top, ROW_DISTANCE):
                for i in range(num_plants):
                    plants.append(pygame.Rect(left, top, OFFICE_PLANT_RECT.width, OFFICE_PLANT_RECT.height))
                    plant_colliders.append(pygame.Rect(left, top, OFFICE_PLANT_RECT.width - 14, OFFICE_PLANT_RECT.height - 140))
                    top += ROW_DISTANCE

            def create_office_plants(num_plants, left, top, ROW_DISTANCE):
                office_plants = []
                office_plant_colliders = []
                create.object.office_plants.office_plant_array(num_plants, office_plants, office_plant_colliders, left, top, ROW_DISTANCE)
                all_office_plants.append(office_plants)
                all_office_plant_colliders.append(office_plant_colliders)
            
            def all_office_plants(ROW_DISTANCE):
                num_plants = 3

                # position plant at center of cubicle
                top = -50 + CUBICLE_RECT.height / 2 - OFFICE_PLANT_HEIGHT / 2
                left = CUBICLE_RECT.width * 5 + 105

                # create column 1
                create.object.office_plants.create_office_plants(num_plants, left, top, ROW_DISTANCE)
                
                # create column 2
                create.object.office_plants.create_office_plants(num_plants, left + CUBICLE_RECT.width - 170, top, ROW_DISTANCE)

        # health
        class health:
            def hearts(num_hearts):
                x = 0
                for i in range(num_hearts):
                    all_health.append(pygame.Rect(CATCH_A_CORN_BACKGROUND_RECT.x + 10 + 120 + x, 30, HEALTH_WIDTH, HEALTH_HEIGHT))
                    x += HEALTH_WIDTH + 1

    class pathway:
        def __init__(self, x, y, rect, location_text):
            self.x = x
            self.y = y
            self.rect = rect
            self.location_text = location_text

    class world:
        def __init__(self, world, background, objects, characters):
            self.world = world
            self.background = background
            self.objects = objects
            self.characters = characters

# create mechanics
# movement
# player
player_movement = create.mechanics.movement(
    PLAYER_X_VELOCITY,      # x velocity
    PLAYER_Y_VELOCITY,      # y velocity
    pygame.K_a,             # left key
    pygame.K_d,             # right key
    pygame.K_w,             # up key
    pygame.K_s,             # down key
    OFFICE_FLOOR_RECT.left + 700, # left limit
    -4900,                        # right limit
    400,                          # top limit
    -2400,                        # bottom limit
    True,
    True)             

# corn basket
corn_basket_movement = create.mechanics.movement(
    corn_basket_x_velocity, 
    corn_basket_y_velocity,
    pygame.K_a,
    pygame.K_d,
    filler,
    filler,
    CATCH_A_CORN_BACKGROUND_RECT.left + 12,
    CATCH_A_CORN_BACKGROUND_RECT.left + CATCH_A_CORN_BACKGROUND_RECT.width - CORN_BASKET_RECT.width - 5,
    filler,
    filler,
    True,
    True)

# create colliders
player_collider = create.mechanics.collider.player(PLAYER_HITBOX)

# create player quest settings
no_quest = create.mechanics.quest("0", None, False, False, WHITE)
player_quest = create.mechanics.quest.set_quest(False, no_quest)

# game graphics + mechanics
class game:
    def __init__(self, game_world, end):
        self.game_world = game_world
        self.end = end

    class background:
        # create backgrounds
        INTRO_BACKGROUND = create.background(OPENING_SCREEN_BACKGROUND, OPENING_SCREEN_RECT)
        OFFICE_FLOOR = create.background(OFFICE_FLOOR_BACKGROUND, OFFICE_FLOOR_RECT)
        MANAGER_OFFICE_FLOOR = create.background(MANAGER_OFFICE_FLOOR_BACKGROUND, MANAGER_OFFICE_FLOOR_RECT)
        KITCHEN_FLOOR = create.background(KITCHEN_FLOOR_BACKGROUND, KITCHEN_FLOOR_RECT)
        CATCH_A_CORN_BACKGROUND = create.background(CATCH_A_CORN_BACKGROUND_IMG, CATCH_A_CORN_BACKGROUND_RECT)
        CATCH_A_CORN_OPENING_BACKGROUND = create.background(CATCH_A_CORN_OPENING_BACKGROUND_IMG, CATCH_A_CORN_OPENING_BACKGROUND_RECT)
        # hallway 1
        HALLWAY1_BACKGROUND = create.background(HALLWAY1_BACKGROUND_IMG, HALLWAY1_RECT)
        HALLWAY1_LIGHTING = create.background(HALLWAY1_LIGHTING_IMG, HALLWAY1_LIGHTING_RECT)
        # hallway 2
        HALLWAY2_BACKGROUND = create.background(HALLWAY2_BACKGROUND_IMG, HALLWAY2_RECT)
        HALLWAY2_LIGHTING = create.background(HALLWAY2_LIGHTING_IMG, HALLWAY2_LIGHTING_RECT)
        # hallway 1
        LAB_BACKGROUND = create.background(LAB_BACKGROUND_IMG, LAB_RECT)
        LAB_LIGHTING = create.background(LAB_LIGHTING_IMG, LAB_LIGHTING_RECT)

    class object:
        # create objects
        # world 1
        # create cubicle rectangles and colliders
        create.object.cubicles.all_cubicles(ROW_DISTANCE)

        # create office plant rectangles and colliders
        create.object.office_plants.all_office_plants(ROW_DISTANCE)

        # compile list of all objects
        objects = [all_cubicles, all_cubicle_colliders, all_office_plants, all_office_plant_colliders]
        
        # world 2
        # manager's office desk
        MANAGER_DESK = create.object(MANAGER_DESK_SPRITE, MANAGER_DESK_RECT, MANAGER_DESK_HITBOX)

        MANAGER_OFFICE_CARPET = create.object(BLUE_CARPET_SPRITE, BLUE_CARPET_RECT, BLUE_CARPET_RECT)

        # create bookcases
        BOOKCASE_1 = create.object(BOOKCASE_SPRITE1, BOOKCASE1_RECT, BOOKCASE1_COLLIDER)
        BOOKCASE_2 = create.object(BOOKCASE_SPRITE2, BOOKCASE2_RECT, BOOKCASE2_COLLIDER)
        BOOKCASE_3 = create.object(BOOKCASE_SPRITE3, BOOKCASE3_RECT, BOOKCASE3_COLLIDER)
        BOOKCASE_4 = create.object(BOOKCASE_SPRITE4, BOOKCASE4_RECT, BOOKCASE4_COLLIDER)
        # list of all bookcases
        bookcases = [BOOKCASE_1, BOOKCASE_2, BOOKCASE_3, BOOKCASE_4]

        manager_office_objects = [MANAGER_DESK, bookcases]

        carpets = [MANAGER_OFFICE_CARPET]

        # world 3
        KITCHEN_COUNTER = create.object(KITCHEN_COUNTER_SPRITE, KITCHEN_COUNTER_RECT, KITCHEN_COUNTER_COLLIDER)
        FRIDGE = create.object(FRIDGE_SPRITE, FRIDGE_RECT, FRIDGE_COLLIDER)
        CORNMEAL = create.object(CORNMEAL_SPRITE, CORNMEAL_RECT, CORNMEAL_RECT)
        KITCHEN_OBJECTS = [KITCHEN_COUNTER, FRIDGE, CORNMEAL]

        # world 4
        CORN = create.object(CORN_SPRITE, CORN_RECT, CORN_RECT)
        EGG = create.object(EGG_SPRITE, EGG_RECT, EGG_RECT)
        CHICKEN = create.object(CHICKEN_IMG, CHICKEN_IMG_RECT, CHICKEN_IMG_RECT)
        create.object.health.hearts(5)
        all_health = all_health

    class quest:
        class quest1:
            quest1 = create.mechanics.quest("1", quest_goals["1"], False, False, WHITE)

            def quest1_complete():
                game.player.PLAYER.quest_set.quest.has_item = True
                game.player.PLAYER.quest_set.quest.goal = "Goal update: Cornmeal has been collected! Give cornmeal to manager."
                game.player.PLAYER.quest_set.quest.text_color = "yellow"
                game.character.MANAGER.dialogue = quest_complete_dialogue["manager"]["character"]
                game.character.MANAGER.dialogue_end = False
                game.character.MANAGER.dialogue_index = 0
                game.character.MANAGER.dialogue_toggle_index = 0 
                game.character.MANAGER.final_dialogue = False

        class quest2:
            quest2 = create.mechanics.quest("2", quest_goals["2"], False, False, WHITE)
            quest2_cubicle = pygame.Rect(
                all_cubicle_colliders[0][0][2].x, 
                all_cubicle_colliders[0][0][2].y, 
                all_cubicle_colliders[0][0][2].width, 
                all_cubicle_colliders[0][0][2].height + 200)
            
            def check_minigame_toggle():
                if game.player.PLAYER.can_play_minigame and game.player.PLAYER.collider.hitbox.colliderect(game.quest.quest2.quest2_cubicle):
                    return True

        class quest3:
            quest3 = create.mechanics.quest("3", quest_goals["3"], False, False, WHITE)

            def update_dialogue():
                # update character dialogue
                game.character.ARNOLD.dialogue = quest2_complete_dialogue["arnold"]["character"]
                game.character.ARNOLD.dialogue_toggle_index = 0
                game.character.ARNOLD.dialogue_index = 0
                game.character.ARNOLD.dialogue_end = False
                game.character.ARNOLD.final_dialogue = False
                game.character.THOMAS.dialogue = quest2_complete_dialogue["thomas"]["character"]
                game.character.THOMAS.dialogue_toggle_index = 0
                game.character.THOMAS.dialogue_index = 0
                game.character.THOMAS.dialogue_end = False
                game.character.THOMAS.final_dialogue = False
                game.character.TOMMY.dialogue = quest2_complete_dialogue["tommy"]["character"]
                game.character.TOMMY.dialogue_toggle_index = 0
                game.character.TOMMY.dialogue_index = 0
                game.character.TOMMY.dialogue_end = False
                game.character.TOMMY.final_dialogue = False
                game.character.JULY.dialogue = quest2_complete_dialogue["july"]["character"]
                game.character.JULY.dialogue_toggle_index = 0
                game.character.JULY.dialogue_index = 0
                game.character.JULY.dialogue_end = False
                game.character.JULY.final_dialogue = False
                game.character.PETE.dialogue = quest2_complete_dialogue["pete"]["character"]
                game.character.PETE.dialogue_toggle_index = 0
                game.character.PETE.dialogue_index = 0
                game.character.PETE.dialogue_end = False
                game.character.PETE.final_dialogue = False

        class quest4:
            quest4 = create.mechanics.quest("4", quest_goals["4"], False, False, "red")

            def check_bookcase_toggle():
                if game.player.PLAYER.collider.hitbox.colliderect(BOOKCASE_TOGGLE_RECT) and game.player.PLAYER.can_move_bookcase:
                    game.render.quest.draw_toggle(BOOKCASE2_RECT, 100, 100)
                    return True

    class player:
        # create player
        PLAYER = create.player(
            PLAYER_SPRITE,
            PLAYER_HITBOX,
            player_movement,
            player_collider,
            pygame.K_e,
            player_quest,
            False,
            False,
            False,
            0)

        CORN_BASKET = create.player(CORN_BASKET_SPRITE, CORN_BASKET_RECT, corn_basket_movement, CORN_BASKET_RECT, filler, filler, filler, filler, filler, filler)

    class character:
        # world 1 characters
        # create characters
        TOMMY = create.character("Tommy", TOMMY_SPRITE, TOMMY_RECT, TOMMY_ICON, character_dialogue["tommy"]["character"], 0, 0, True, False, False)
        ARNOLD = create.character("Arnold", ARNOLD_SPRITE, ARNOLD_RECT, ARNOLD_ICON, character_dialogue["arnold"]["character"], 0, 0, True, False, False)
        JACOB = create.character("Jacob", JACOB_SPRITE, JACOB_RECT, JACOB_ICON, character_dialogue["jacob"]["character"], 0, 0, True, False, False)
        JILLIAN = create.character("Jillian", JILLIAN_SPRITE, JILLIAN_RECT, JILLIAN_ICON, character_dialogue["jillian"]["character"], 0, 0, True, False, False)
        JOHN = create.character("John", JOHN_SPRITE, JOHN_RECT, JOHN_ICON, character_dialogue["john"]["character"], 0, 0, True, False, False)
        MAY = create.character("May", MAY_SPRITE, MAY_RECT, MAY_ICON, character_dialogue["may"]["character"], 0, 0, True, False, False)
        PRINCESS = create.character("Princess", PRINCESS_SPRITE, PRINCESS_RECT, PRINCESS_ICON, character_dialogue["princess"]["character"], 0, 0, True, False, False)
        JULY = create.character("July", JULY_SPRITE, JULY_RECT, JULY_ICON, character_dialogue["july"]["character"], 0, 0, True, False, False)
        THOMAS = create.character("Thomas", THOMAS_SPRITE, THOMAS_RECT, THOMAS_ICON, character_dialogue["thomas"]["character"], 0, 0, True, False, False)
        FLOWER = create.character("Flower", FLOWER_SPRITE, FLOWER_RECT, FLOWER_ICON, character_dialogue["flower"]["character"], 0, 0, True, False, False)
        PETE = create.character("Pete", PETE_SPRITE, PETE_RECT, PETE_ICON, character_dialogue["pete"]["character"], 0, 0, True, False, False)

        # compile list of all characters, used to draw all characters and control movement
        characters = [ARNOLD, TOMMY, JACOB, JILLIAN, JOHN, MAY, PRINCESS, JULY, THOMAS, FLOWER, PETE]

        # world 2 characters
        MANAGER = create.character("Manager", MANAGER_SPRITE, MANAGER_RECT, MANAGER_ICON, character_dialogue_world2["manager"]["character"], 0, 0, True, False, False)
        manager_office_characters = [MANAGER]

        # lab characters
        lab_characters = [MANAGER]

    class text_box:
        text_box = create.mechanics.dialogue.text_box(TEXT_BOX, "character name", "character icon", "text", False, 5)
        toggle = create.mechanics.dialogue.text_box_toggle(False)

    class pathway:
        # office pathways
        TO_MANAGER_OFFICE_PATHWAY = create.pathway(TO_MANAGER_OFFICE_COLLIDER.x - 50, TO_MANAGER_OFFICE_COLLIDER.y - 250, TO_MANAGER_OFFICE_RECT, "To manager's office")
        TO_KITCHEN_PATHWAY = create.pathway(TO_KITCHEN_RECT.x, TO_KITCHEN_RECT.y, TO_KITCHEN_RECT, "To kitchen ")
        render_office_pathways = [TO_MANAGER_OFFICE_PATHWAY, TO_KITCHEN_PATHWAY]

        # manager's office pathway
        TO_OFFICE_PATHWAY = create.pathway(TO_OFFICE_COLLIDER.x, TO_OFFICE_COLLIDER.y, TO_OFFICE_RECT, "To main office")
        TO_HALLWAY1_PATHWAY = create.pathway(TO_HALLWAY1_COLLIDER.x, TO_HALLWAY1_COLLIDER.y, TO_HALLWAY1_RECT, "To ??? ")
        render_manager_office_pathways = [TO_OFFICE_PATHWAY, TO_HALLWAY1_PATHWAY]

        # kitchen pathways
        TO_MAIN_OFFICE_PATHWAY = create.pathway(TO_MAIN_OFFICE_COLLIDER.x, TO_MAIN_OFFICE_COLLIDER.y, TO_MAIN_OFFICE_RECT, "To main office")
        render_kitchen_pathways = [TO_MAIN_OFFICE_PATHWAY]

    # handle graphics
    class render:
        class graphics:
            def sprites(object):
                size = (object.rect.width, object.rect.height)
                pygame.Surface.blit(SCREEN, pygame.transform.scale(object.sprite, size), object.rect)
            
            def all_characters(character_list):
                for character in character_list:
                    game.render.graphics.sprites(character)

            def cubicles(cubicles_list, cubicle_sprites):
                row_num = 0
                for row in cubicles_list:
                    cubicle_num = 0
                    for cubicle in row:
                        pygame.Surface.blit(SCREEN, 
                            pygame.transform.scale(cubicle_sprites[row_num][cubicle_num], (cubicle.width, cubicle.height)), 
                            cubicle)
                        cubicle_num += 1
                    row_num += 1
            
            # only used for cubicle hitbox debugging
            def cubicle_hitboxes(cubicle_colliders):
                for array in cubicle_colliders:
                    for cubicle in array:
                        for collider in cubicle:
                            pygame.draw.rect(SCREEN, "red", collider)
            
            def office_plants(office_plants):
                for column in office_plants:
                    for office_plant in column:
                        pygame.Surface.blit(SCREEN, 
                            pygame.transform.scale(OFFICE_PLANT_SPRITE, (OFFICE_PLANT_WIDTH, OFFICE_PLANT_HEIGHT)), 
                            office_plant)
        
            def bookcases(bookcases):
                for bookcase in bookcases:
                    game.render.graphics.sprites(bookcase)

            def all_hearts(health):
                for heart in health:
                    pygame.Surface.blit(SCREEN, pygame.transform.scale(HEALTH_SPRITE, (heart.width, heart.height)), heart)

            def border():
                # create game borders
                BORDER_WIDTH = 105
                BORDER_HEIGHT = 20
                LEFT_BORDER = pygame.Rect(0, 0, BORDER_WIDTH, WINDOW_HEIGHT)
                RIGHT_BORDER = pygame.Rect(WINDOW_WIDTH - BORDER_WIDTH, 0, BORDER_WIDTH, WINDOW_HEIGHT)
                TOP_BORDER = pygame.Rect(0, 0, WINDOW_WIDTH, BORDER_HEIGHT)
                BOTTOM_BORDER = pygame.Rect(0, WINDOW_HEIGHT - BORDER_HEIGHT, WINDOW_WIDTH, BORDER_HEIGHT)
                # draw game borders
                pygame.draw.rect(SCREEN, "black", LEFT_BORDER)
                pygame.draw.rect(SCREEN, "black", RIGHT_BORDER)
                #pygame.draw.rect(SCREEN, "black", TOP_BORDER)
                #pygame.draw.rect(SCREEN, "black", BOTTOM_BORDER)

            def background(background):
                size = (background.rect.width, background.rect.height)
                pygame.Surface.blit(SCREEN, pygame.transform.scale(background.background_img, size), background.rect) 

            def all_graphics(game_world):
                if game_world.world == "world1":
                    game.world.world1.graphics.render_all()
                elif game_world.world == "world2":
                    game.world.world2.graphics.render_all()
                elif game_world.world == "world3":
                    game.world.world3.graphics.render_all()
                elif game_world.world == "world4":
                    game.world.world4.graphics.render_all()
                elif game_world.world == "world5":
                    game.world.world5.graphics.render_all()
                elif game_world.world == "world6":
                    game.world.world6.graphics.render_all()
                elif game_world.world == "world7":
                    game.world.world7.graphics.render_all()

        class dialogue:
            def text_box_rect():
                pygame.draw.rect(SCREEN, DARK_GREY, TEXT_BOX)

            def text(text):
                font = pygame.font.Font(PRESS_START_2P_REGULAR, 20)
                # draw text
                render_text = pygame.font.Font.render(font, text, False, WHITE)
                pygame.Surface.blit(SCREEN, render_text, (TEXT_BOX.left + 160, TEXT_BOX.top + game.text_box.text_box.text_pos_top))
                # draw character name
                render_character_name = pygame.font.Font.render(font, game.text_box.text_box.character_name, False, YELLOW)
                pygame.Surface.blit(SCREEN, render_character_name, (TEXT_BOX.left + 35, TEXT_BOX.top + 25))
                # draw continue text
                continue_font = pygame.font.Font(PRESS_START_2P_REGULAR, 15)
                render_continue_text = pygame.font.Font.render(continue_font, "(press 'E' to continue)", False, WHITE)
                pygame.Surface.blit(SCREEN, render_continue_text, (TEXT_BOX.left + TEXT_BOX.width - 400, TEXT_BOX.top + TEXT_BOX.height - 30))

            def dialogue_toggle_button(player):
                # draw toggle box
                toggle_box = DIALOGUE_TOGGLE_BOX
                pygame.draw.rect(SCREEN, BLACK, toggle_box)
                # draw key
                key = "E"
                font = pygame.font.Font(PRESS_START_2P_REGULAR, 20)
                render_text = pygame.font.Font.render(font, key, False, WHITE)
                pygame.Surface.blit(SCREEN, render_text, (toggle_box.left + toggle_box.width / 2 - 10, toggle_box.top + toggle_box.height / 2 - 10))
                
            def text_box(text):
                game.text_box.text_box.text_pos_top = 60
                game.render.dialogue.text_box_rect()
                for line in text:
                    game.render.dialogue.text(line)
                    game.text_box.text_box.text_pos_top += 35
    
            def character_icon(textbox_icon):
                pygame.Surface.blit(SCREEN, pygame.transform.scale(textbox_icon, (CHARACTER_ICON_RECT.width, CHARACTER_ICON_RECT.height)), CHARACTER_ICON_RECT)

            def draw_textbox_mechanics():
                # draw text box toggle if near character
                if game.text_box.toggle.toggle == True:
                    game.render.dialogue.dialogue_toggle_button(game.player.PLAYER)
                # draw text box if toggled
                if game.text_box.text_box.toggle == True:
                    game.render.dialogue.text_box(game.text_box.text_box.text)
                    game.render.dialogue.character_icon(game.text_box.text_box.character_icon)
                else:
                    QUEST_SOUND.stop()

        class pathway:
            def pathways(pathways):
                for pathway in pathways:
                    rotation = 0
                    if pathway == game.pathway.TO_KITCHEN_PATHWAY or pathway == game.pathway.TO_HALLWAY1_PATHWAY:
                        rotation = 180
                    pygame.Surface.blit(SCREEN, pygame.transform.rotate(pygame.transform.scale(PATHWAY_SPRITE, (pathway.rect.width, pathway.rect.height)), rotation), pathway.rect)
            
            def pathway_text(pathways):
                for pathway in pathways:
                    if game.player.PLAYER.collider.hitbox.colliderect(pathway.rect):
                        if pathway == game.pathway.TO_HALLWAY1_PATHWAY and game.player.PLAYER.bookcase_moved == False:
                            continue
                        # draw background rect
                        background_rect = pygame.Rect(pathway.rect.x, pathway.rect.y, len(pathway.location_text) * 20 + 20, 60)
                        pygame.draw.rect(SCREEN, BLACK, background_rect)
                        # draw text
                        font = pygame.font.Font(PRESS_START_2P_REGULAR, 20)
                        render_font = pygame.font.Font.render(font, pathway.location_text, False, WHITE)
                        pygame.Surface.blit(SCREEN, render_font, (pathway.rect.x + 20, pathway.rect.y + 20))

        class quest:
            # draw quest.goal text when quest.goal is updated
            def quest_text(quest_goal):
                font_size = 18
                margin = 20
                text_length = len(quest_goal) * font_size
                # draw background rect
                background_rect = pygame.Rect(WINDOW_WIDTH / 2 - text_length / 2, 50, text_length + margin * 2, font_size + margin * 2)
                pygame.draw.rect(SCREEN, BLACK, background_rect)
                # draw text
                font = pygame.font.Font(PRESS_START_2P_REGULAR, font_size)
                render_font = pygame.font.Font.render(font, quest_goal, False, game.player.PLAYER.quest_set.quest.text_color)
                pygame.Surface.blit(SCREEN, render_font, (background_rect.x + margin, background_rect.y + margin))
            
            def draw_toggle(rect, x_offset, y_offset):
                # draw toggle box
                    toggle_box = QUEST_TOGGLE_BOX
                    QUEST_TOGGLE_BOX.x, QUEST_TOGGLE_BOX.y = rect.x - 100 + x_offset, rect.y + y_offset
                    pygame.draw.rect(SCREEN, BLACK, toggle_box)
                    # draw key
                    key = "E"
                    font = pygame.font.Font(PRESS_START_2P_REGULAR, 20)
                    render_text = pygame.font.Font.render(font, key, False, WHITE)
                    pygame.Surface.blit(SCREEN, render_text, (toggle_box.left + toggle_box.width / 2 - 10, toggle_box.top + toggle_box.height / 2 - 10))

            def draw_collect_item_toggle():
                if  game.player.PLAYER.quest_set.quest.toggle_collect and game.player.PLAYER.quest_set.quest.quest_num == "1":
                    game.render.quest.draw_toggle(game.object.CORNMEAL.rect, 0, 0)
                elif game.quest.quest2.check_minigame_toggle():
                    game.render.quest.draw_toggle(game.quest.quest2.quest2_cubicle, 150, 100)
                    
            def draw_quest():
                if game.player.PLAYER.quest_set.has_quest:
                    game.render.quest.quest_text(game.player.PLAYER.quest_set.quest.goal)

    # handle animations
    class animate:
        def intro():
            # initialize animation
            zoom_x = 4800
            zoom_y = 2840
            INTRO_BACKGROUND_ANIM_RECT = pygame.Rect(
                WINDOW_WIDTH / 2 - zoom_x / 2, WINDOW_HEIGHT / 2 - zoom_y / 2, zoom_x, zoom_y)
            INTRO_BACKGROUND_ANIM = create.background(OPENING_SCREEN_ANIM_BACKGROUND, INTRO_BACKGROUND_ANIM_RECT)

            # play zoom animation
            while zoom_x > 1200 and zoom_y > 710:
                pygame.Surface.fill(SCREEN, "white")
                # update width based on zoom ration
                INTRO_BACKGROUND_ANIM.rect = pygame.Rect(
                    WINDOW_WIDTH / 2 - zoom_x / 2, WINDOW_HEIGHT / 2 - zoom_y / 2, zoom_x, zoom_y)
                # draw background and border
                game.render.graphics.background(INTRO_BACKGROUND_ANIM)
                game.render.graphics.border()
                pygame.display.flip()
                pygame.time.delay(10)
                # update zoom ratio
                zoom_x *= 0.98
                zoom_y *= 0.98

            # draw title screen
            pygame.time.delay(500)
            game.render.graphics.background(game.background.INTRO_BACKGROUND)
            game.render.graphics.border()

            # play intro screen if space is pressed
            proceed = False
            INTRO_THEME.play(-1)
            while proceed == False:
                text = "Press SPACE to continue"
                font = pygame.font.Font(PRESS_START_2P_REGULAR, 25)
                render_font = pygame.font.Font.render(font, text, False, BLACK)
                render_font2 = pygame.font.Font.render(font, text, False, WHITE)
                pygame.Surface.blit(SCREEN, render_font2, (
                    WINDOW_WIDTH / 2 - render_font.get_width() / 2 - 3, WINDOW_HEIGHT / 2 + 63))
                pygame.Surface.blit(SCREEN, render_font, (WINDOW_WIDTH / 2 - render_font.get_width() / 2, WINDOW_HEIGHT / 2 + 60))
                pygame.display.flip()

                # exit game if window closed
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        START_GAME_SOUND.play()
                        pygame.time.delay(500)
                        proceed = True

            # play game if space is pressed
            to_game = False
            while to_game == False:
                # draw intro screen
                x = 70
                a = 40
                pygame.Surface.fill(SCREEN, BLACK)
                game.world.world4.graphics.render_opening_text("It feels like just yesterday when I graduated the University of Corn for Dummies...", WHITE, 15, x)
                game.world.world4.graphics.render_opening_text("(Although it's really been 8 years...)", WHITE, 15, x + a)
                game.world.world4.graphics.render_opening_text("All this time, I have been working my way up to achieve my dream of becoming a", WHITE, 15, x + 2*a)
                game.world.world4.graphics.render_opening_text("realtor here in Corntown. The corporate world isn't a forgiving one.", WHITE, 15, x + 3*a)
                game.world.world4.graphics.render_opening_text("Actually, I built my way up in the previous company I was employed at, and became the", WHITE, 15, x + 4*a)
                game.world.world4.graphics.render_opening_text("official corn peeler! ..And all of that led me to my first solid job at my first", WHITE, 15, x + 5*a)
                game.world.world4.graphics.render_opening_text("real estate company: Cornhouse Realty. Today, I begin my first day as an official", WHITE, 15, x + 6*a)
                game.world.world4.graphics.render_opening_text("Cornhouse Realty realtor. Mom, you always said that I would turn out a failure ever ", WHITE, 15, x + 7*a)
                game.world.world4.graphics.render_opening_text("since I was accepted at the University of Corn for Dummies. I know the degree turned", WHITE, 15, x + 8*a)
                game.world.world4.graphics.render_opening_text("out to be fake and the dean of the school was arrested for fraud.. ", WHITE, 15, x + 9*a)
                game.world.world4.graphics.render_opening_text("..But I'm a new man! Dreams do come true, mom!", WHITE, 15, x + 10*a)
                game.world.world4.graphics.render_opening_text("Anyway, I'm off to work now. Wish me luck!", WHITE, 15, x + 11*a)
                game.world.world4.graphics.render_opening_text("- With love, Bill", WHITE, 15, x + 12*a)
                game.world.world4.graphics.render_opening_text("(Press SPACE to continue)", YELLOW, 15, x + 13*a + 20)
                pygame.display.flip()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        INTRO_THEME.stop()
                        START_GAME_SOUND.play()
                        pygame.time.delay(1000)
                        to_game = True

        class movement:
            class player:
                # player run animation frames
                PLAYER_RUN_ANIMATION = {
                    "left": [
                        PLAYER_RUN_ANIMATION_LEFT_FRAME1,
                        PLAYER_RUN_ANIMATION_LEFT_FRAME2,
                        PLAYER_RUN_ANIMATION_LEFT_FRAME3,
                        PLAYER_RUN_ANIMATION_LEFT_FRAME2],
                    "right": [
                        PLAYER_RUN_ANIMATION_RIGHT_FRAME1,
                        PLAYER_RUN_ANIMATION_RIGHT_FRAME2,
                        PLAYER_RUN_ANIMATION_RIGHT_FRAME3,
                        PLAYER_RUN_ANIMATION_RIGHT_FRAME2],
                    "standing": [pygame.transform.scale(PLAYER_SPRITE, (PLAYER_HITBOX.width, PLAYER_HITBOX.height))]
                }

                # draw run animation, draw each run frame 2 times calculated based on run count (to slow down animation)
                def run(player, animation, direction, walk_count):
                    if game_settings.game_world.world == "world1":
                        num_frames = 3
                    else: 
                        num_frames = 5
                    try:
                        player.sprite = animation[direction][walk_count//num_frames]
                    except:
                        player.sprite = animation[direction][0]

            class objects:
                def move_cubicles(cubicles, cubicle_colliders, x_velocity, y_velocity):
                    array_num = 0
                    for array in cubicles:
                        cubicle_num = 0
                        for cubicle in array:
                            try:
                                # move drawing position
                                cubicle.x += x_velocity
                                cubicle.y += y_velocity
                                # update collider position
                                # y position
                                cubicle_colliders[array_num][cubicle_num][0].y = cubicle.y
                                cubicle_colliders[array_num][cubicle_num][1].y = cubicle.y
                                cubicle_colliders[array_num][cubicle_num][2].y = cubicle.y + MIDDLE_CUBICLE_HITBOX_OFFSET
                                # x position
                                cubicle_colliders[array_num][cubicle_num][0].x = cubicle.x
                                cubicle_colliders[array_num][cubicle_num][1].x = cubicle.x + cubicle.width - \
                                    cubicle_colliders[array_num][cubicle_num][1].width
                                cubicle_colliders[array_num][cubicle_num][2].x = cubicle.x
                            except:
                                print("line 339")
                                print(cubicle_num, len(cubicle_colliders[array_num]), len(array), array_num)
                            cubicle_num += 1
                        array_num += 1
                    
                def move_office_plants(office_plants, office_plant_colliders, x_velocity, y_velocity):
                    column_num = 0
                    for column in office_plants:
                        office_plant_num = 0
                        for office_plant in column:
                            # move office plants
                            office_plant.x += x_velocity
                            office_plant.y += y_velocity
                            # move office plant colliders
                            office_plant_colliders[column_num][office_plant_num].x = office_plant.x + 5
                            office_plant_colliders[column_num][office_plant_num].y = office_plant.y + 40
                            office_plant_num += 1
                        column_num += 1
            
                def move_manager_desk(x_velocity, y_velocity):
                    game.object.MANAGER_DESK.rect.x += x_velocity
                    game.object.MANAGER_DESK.rect.y += y_velocity
                    game.object.MANAGER_DESK.collider.x += x_velocity
                    game.object.MANAGER_DESK.collider.y += y_velocity

                def move_bookcases(bookcases, x_velocity, y_velocity):
                    for bookcase in bookcases:
                        bookcase.rect.x += x_velocity
                        bookcase.rect.y += y_velocity
                        bookcase.collider.x, bookcase.collider.y = bookcase.rect.x, bookcase.rect.y

                def move_carpets(carpets, x_velocity, y_velocity):
                    for carpet in carpets:
                        carpet.rect.x += x_velocity
                        carpet.rect.y += y_velocity

                def move_kitchen_objects(kitchen_objects, x_velocity, y_velocity):
                    for object in kitchen_objects:
                        object.rect.x += x_velocity
                        object.rect.y += y_velocity
                        object.collider.x, object.collider.y = object.rect.x, object.rect.y

                def move_quest_cubicle():
                    game.quest.quest2.quest2_cubicle.x = all_cubicle_colliders[0][0][2].x
                    game.quest.quest2.quest2_cubicle.y = all_cubicle_colliders[0][0][2].y

                def move_quest_bookcase(x_velocity, y_velocity):
                    BOOKCASE_TOGGLE_RECT.x += x_velocity
                    BOOKCASE_TOGGLE_RECT.y += y_velocity

            class background:
                def move_background(background, x_velocity, y_velocity):
                    background.rect.x += x_velocity
                    background.rect.y += y_velocity
            
            class characters:
                def move_characters(characters, x_velocity, y_velocity):
                    for character in characters:
                        character.rect.x += x_velocity
                        character.rect.y += y_velocity

            class pathways:
                def collider(pathways, x_velocity, y_velocity):
                    # move pathway collider
                    for pathway in pathways:
                        pathway.x += x_velocity
                        pathway.y += y_velocity

                def pathway(pathways, pathway_sprites, x_velocity, y_velocity):
                    game.animate.movement.pathways.collider(pathways, x_velocity, y_velocity)
                    # move pathway sprites
                    for pathway_sprite in pathway_sprites:
                        pathway_sprite.rect.x += x_velocity
                        pathway_sprite.rect.y += y_velocity

    # handle game mechanics
    class mechanics:
        class time:
            def timer(time_check, time_count):
                time_elapsed = time_check[-1] - time_check[0]
                if time_elapsed >= time_count:
                    return True
                else:
                    return False

        class collision:
            # check for collision with cubicles
            def check_collision_cubicles(player, cubicle_colliders):
                for column in cubicle_colliders:
                    for cubicle in column:
                        for collider in cubicle:
                            try:
                                if player.collider.hitbox.colliderect(collider):
                                    return True
                            except:
                                print("line 360")

            # check for collision with office plants    
            def check_collision_office_plants(player, office_plant_colliders):
                for column in office_plant_colliders:
                    for collider in column:
                        if player.collider.hitbox.colliderect(collider):
                            return True

            def check_collision_manager_desk(player):
                if player.collider.hitbox.colliderect(game.object.MANAGER_DESK.collider):
                    return True

            def check_collision_bookcase(player, bookcases):
                for bookcase in bookcases:
                    if player.collider.hitbox.colliderect(bookcase.collider):
                        return True

            def check_collision_kitchen_objects():
                for object in game.object.KITCHEN_OBJECTS:
                    if game.player.PLAYER.collider.hitbox.colliderect(object.collider):
                        if object == game.object.CORNMEAL:
                            game.player.PLAYER.quest_set.quest.toggle_collect = True
                            return False
                        return True

            # check for player limit
            def check_collision_player_limits(player):
                # check for limit x
                if game_settings.game_world.background.rect.x >= player.movement.left_limit \
                    or game_settings.game_world.background.rect.x <= player.movement.right_limit:
                    return True
                # check for limit y
                if game_settings.game_world.background.rect.y >= player.movement.top_limit \
                    or game_settings.game_world.background.rect.y <= player.movement.bottom_limit:
                    return True

            # check for collision with pathways
            def check_collision_pathways(pathways):
                for pathway in pathways:
                    if game.player.PLAYER.collider.hitbox.colliderect(pathway):
                        return pathway
            
            # teleport player based on pathway
            def teleport_pathway(pathways):
                teleport_offset = 300
                pathway = game.mechanics.collision.check_collision_pathways(pathways)
                if pathway == TO_MANAGER_OFFICE_COLLIDER:
                    pygame.time.delay(500)
                    # set game_world to manager's office
                    game_settings.game_world = MANAGER_OFFICE
                    # move elements backward so player does not continuously collide with pathway
                    game.mechanics.movement.move_all(game_settings.game_world, 0, teleport_offset)
                    game.world.world2.mechanics.set_mechanics()
                elif pathway == TO_OFFICE_COLLIDER:
                    pygame.time.delay(500)
                    game_settings.game_world = OFFICE
                    game.mechanics.movement.move_all(game_settings.game_world, 0, teleport_offset)
                    game.world.world1.mechanics.set_mechanics()
                elif pathway == TO_KITCHEN_COLLIDER:
                    pygame.time.delay(500)
                    game_settings.game_world = KITCHEN
                    game.mechanics.movement.move_all(game_settings.game_world, 0, teleport_offset)
                    game.world.world3.mechanics.set_mechanics()
                elif pathway == TO_MAIN_OFFICE_COLLIDER:
                    pygame.time.delay(500)
                    game_settings.game_world = OFFICE
                    game.mechanics.movement.move_all(game_settings.game_world, 0, -teleport_offset)
                    game.world.world1.mechanics.set_mechanics()
                elif pathway == TO_HALLWAY1_COLLIDER:
                    pygame.time.delay(500)
                    game_settings.game_world = HALLWAY1
                    game.mechanics.movement.move_all(game_settings.game_world, -200, 0)
                    game.world.world5.mechanics.set_mechanics()
                elif pathway == TO_MANAGER_FROM_OFFICE_COLLIDER:
                    pygame.time.delay(500)
                    HALLWAY_MUSIC.stop()
                    OFFICE_MUSIC.play(-1)
                    game_settings.game_world = MANAGER_OFFICE
                    game.mechanics.movement.move_all(game_settings.game_world, 0, -40)
                    game.world.world2.mechanics.set_mechanics()
                    game.player.PLAYER.rect.y = 278
                elif pathway == TO_HALLWAY_2_COLLIDER:
                    pygame.time.delay(500)
                    game_settings.game_world = HALLWAY2
                    game.mechanics.movement.move_all(game_settings.game_world, -50, 0)
                    game.world.world6.mechanics.set_mechanics()
                elif pathway == TO_HALLWAY1_FROM_HALLWAY2_COLLIDER:
                    pygame.time.delay(500)
                    game_settings.game_world = HALLWAY1
                    game.mechanics.movement.move_all(game_settings.game_world, 100, 0)
                    game.world.world5.mechanics.set_mechanics()
                elif pathway == TO_LAB_COLLIDER:
                    pygame.time.delay(500)
                    game_settings.game_world = LAB
                    game.mechanics.movement.move_all(game_settings.game_world, -50, 0)
                    game.world.world7.mechanics.set_mechanics()

            def handle_pathway(game_world):
                if game_world.world == "world1":
                    game.world.world1.mechanics.collisions.pathways.check_collision_pathways()
                elif game_world.world == "world2":
                    game.world.world2.mechanics.collisions.pathways.check_collision_pathways()
                elif game_world.world == "world3":
                    game.world.world3.mechanics.collisions.pathways.check_collision_pathways()
                elif game_world.world == "world5":
                    game.world.world5.mechanics.collisions.pathways.check_collision_pathways()
                elif game_world.world == "world6":
                    game.world.world6.mechanics.collisions.pathways.check_collision_pathways()

            # check for player collision, push player back if collision detected
            def check_collision(player):
                key_pressed = pygame.key.get_pressed()
                
                # control negative movement to push player back based on key_pressed
                if key_pressed[player.movement.left_key]:
                    game.mechanics.movement.move_all(game_settings.game_world, -player.movement.x_velocity, 0)
                elif key_pressed[player.movement.right_key]:
                    game.mechanics.movement.move_all(game_settings.game_world, -player.movement.x_velocity, 0)
                elif key_pressed[player.movement.up_key]:
                    game.mechanics.movement.move_all(game_settings.game_world, 0, -player.movement.y_velocity)
                elif key_pressed[player.movement.down_key]:
                    game.mechanics.movement.move_all(game_settings.game_world, 0, -player.movement.y_velocity)

            def handle_collision(game_world, player):
                if game_world.world == "world1":
                    game.world.world1.mechanics.movement.handle_all_hitboxes(player)
                elif game_world.world == "world2":
                    game.world.world2.mechanics.movement.handle_all_hitboxes(player)
                elif game_world.world == "world3":
                    game.world.world3.mechanics.movement.handle_all_hitboxes(player)
                elif game_world.world == "world7":
                    game.world.world7.mechanics.movement.handle_all_hitboxes(player)

        class movement:
            # move graphics positions based on player movement
            def move_all(game_world, x_velocity, y_velocity):
                if game_world.world == "world1":
                    game.world.world1.mechanics.movement.move_all(x_velocity, y_velocity)
                elif game_world.world == "world2":
                    game.world.world2.mechanics.movement.move_all(x_velocity, y_velocity)
                elif game_world.world == "world3":
                    game.world.world3.mechanics.movement.move_all(x_velocity, y_velocity)
                elif game_world.world == "world5":
                    game.world.world5.mechanics.movement.move_all(x_velocity, y_velocity)
                elif game_world.world == "world6":
                    game.world.world6.mechanics.movement.move_all(x_velocity, y_velocity)
                elif game_world.world == "world7":
                    game.world.world7.mechanics.movement.move_all(x_velocity, y_velocity)
                
            # handle player movement
            def handle_player_movement(game_world, player):
                global walk_count
                key_pressed = pygame.key.get_pressed()
                direction = "standing"
                if player.movement.toggle_movement == True:
                    if key_pressed[player.movement.left_key]:
                        player.movement.x_velocity = PLAYER_X_VELOCITY 
                        player.movement.y_velocity = 0
                        direction = "left"
                        walk_count += 1
                    elif key_pressed[player.movement.right_key]:
                        player.movement.x_velocity = -PLAYER_X_VELOCITY
                        player.movement.y_velocity = 0
                        direction = "right"
                        walk_count += 1
                    elif key_pressed[player.movement.up_key] and player.movement.toggle_y_velocity:
                        player.movement.y_velocity = PLAYER_Y_VELOCITY
                        player.movement.x_velocity = 0
                        direction = "right"
                        walk_count += 1
                    elif key_pressed[player.movement.down_key] and player.movement.toggle_y_velocity:
                        player.movement.y_velocity =  -PLAYER_Y_VELOCITY
                        player.movement.x_velocity = 0
                        direction = "left"
                        walk_count += 1
                    else:
                        player.movement.x_velocity = 0
                        player.movement.y_velocity = 0
                        direction = "standing"
                        walk_count = 0

                # reset animation to beginning (ensure list index does not go out of range for animation)
                if walk_count == 11 and game_settings.game_world.world == "world1":
                    walk_count = 1
                elif walk_count == 21:
                    walk_count = 1

                # move background to imitate player movement
                game.mechanics.movement.move_all(game_world, player.movement.x_velocity, player.movement.y_velocity)
                # animate player running
                game.animate.movement.player.run(player, game.animate.movement.player.PLAYER_RUN_ANIMATION, direction, \
                    walk_count)
                # check for player collision with object
                game.mechanics.collision.handle_collision(game_world, player)

        class dialogue:
            # update text_box.text (dialogue), character name and character icon
            def update_character_dialogue(player, character):
                # update dialogue toggle box position
                DIALOGUE_TOGGLE_BOX.x, DIALOGUE_TOGGLE_BOX.y = character.rect.x, character.rect.y
                # update text
                game.text_box.text_box.text = character.dialogue[character.dialogue_toggle_index][character.dialogue_index]
                game.mechanics.dialogue.toggle_dialogue(player, character)
                game.text_box.toggle.toggle = True
                # update character name
                game.text_box.text_box.character_name = character.name
                # update character icon
                game.text_box.text_box.character_icon = character.icon

            # if player collides with character, allow player to press 'e' to toggle dialogue
            def get_character_dialogue(player, characters):
                game.text_box.text_box.dialogue_index = 0
                for character in characters:
                    if player.collider.hitbox.colliderect(character.rect):
                        if character == game.character.MANAGER and game.player.PLAYER.can_move_bookcase:
                            continue
                        # update text
                        game.mechanics.dialogue.update_character_dialogue(player, character)
                        # check for mission from manager
                        game.mechanics.quest.assign_quest(character)
                
            def change_dialogue(character):
                # continue to replay last line if dialogue_toggle_index exceeds list index
                if character.dialogue_toggle_index == len(character.dialogue) - 1:
                    character.final_dialogue = True
                if character.final_dialogue:
                    character.dialogue_index = 0
                    character.dialogue_toggle_index = -1
                # update character's dialogue_toggle_index
                elif character.dialogue_end == True:
                    character.dialogue_toggle_index += 1
                    character.dialogue_end = False
                    character.dialogue_index = 0

            def change_line(character):
                DIALOGUE_TOGGLE_SOUND.play()
                if character.first_line == True:
                    character.first_line = False
                # add to dialogue index to continue text
                elif character.dialogue_index < len(character.dialogue[character.dialogue_toggle_index]) - 1:
                    character.dialogue_index += 1
                # end dialogue if dialogue_index exceeds list index
                else:
                    game.text_box.text_box.toggle = False
                    game.player.PLAYER.movement.toggle_movement = True
                    character.dialogue_end = True
                    character.first_line = True

            # toggle dialogue box 
            def toggle_dialogue(player, character):
                game.render.dialogue.dialogue_toggle_button(player)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        # toggle dialogue box if 'e' is pressed, make sure player has stopped moving before dialogue can be toggled
                        if event.key == pygame.K_e and player.movement.x_velocity == 0 and player.movement.y_velocity == 0:
                            game.text_box.text_box.toggle = True
                            player.movement.toggle_movement = False
                            game.mechanics.dialogue.change_dialogue(character)
                            game.mechanics.dialogue.change_line(character)
                            
            def handle_dialogue(player, characters):
                # reset dialogue toggle box when player walks away from character
                game.text_box.toggle.toggle = False
                # handle character's dialogue based on rect collision
                game.mechanics.dialogue.get_character_dialogue(player, characters)

        class quest:
            def assign_quest(character):
                if game.text_box.text_box.toggle:
                    if character.name == "Manager" and game.player.PLAYER.can_move_bookcase == False:
                        # assign quest 1
                        if character.dialogue == character_dialogue_world2["manager"]["character"] and character.dialogue_toggle_index == 0 and character.dialogue_index == len(character.dialogue[0]) - 1:
                            QUEST_SOUND.play()
                            game.player.PLAYER.quest_set.quest = game.quest.quest1.quest1
                            game.player.PLAYER.quest_set.has_quest = True
                        # assign quest 2
                        elif character.dialogue == quest_complete_dialogue["manager"]["character"] and character.dialogue_toggle_index == 0 and character.dialogue_index == len(character.dialogue[0]) - 1:
                            QUEST_SOUND.play()
                            game.player.PLAYER.quest_set.quest = game.quest.quest2.quest2
                            game.player.PLAYER.can_play_minigame = True
                            game.player.PLAYER.quest_set.has_quest = True
                        elif character.dialogue == quest2_complete_dialogue["manager"]["character"] and character.dialogue_toggle_index == 0 and character.dialogue_index == len(character.dialogue[0]) - 1:
                            QUEST_SOUND.play()
                            game.player.PLAYER.quest_set.quest = game.quest.quest3.quest3
                            game.player.PLAYER.quest_set.has_quest = True
                            game.quest.quest3.update_dialogue()
                    elif character.name == "Pete":
                        if character.dialogue == quest2_complete_dialogue["pete"]["character"] and character.dialogue_toggle_index == 0 and character.dialogue_index == len(character.dialogue[0]) - 1:
                            QUEST_SOUND.play()
                            game.player.PLAYER.quest_set.quest = game.quest.quest4.quest4
                            game.player.PLAYER.quest_set.has_quest = True
                            game.player.PLAYER.can_move_bookcase = True
                            game.character.MANAGER.sprite = MANAGER_CHAIR_SPRITE
                else: 
                    QUEST_SOUND.stop()

            def collect_item(event):
                if event.type == pygame.KEYDOWN and event.key == pygame.K_e and game.player.PLAYER.quest_set.quest.toggle_collect == True and game.player.PLAYER.quest_set.quest.quest_num == "1":
                    PICK_UP_OBJECT_SOUND.play()
                    game.quest.quest1.quest1_complete()

            def toggle_minigame(event):
                if event.type == pygame.KEYDOWN and event.key == pygame.K_e and game.quest.quest2.check_minigame_toggle():
                    game_settings.game_world = CATCH_A_CORN
                    game.world.world4.mechanics.set_mechanics()
                    game.world.world4.mechanics.opening_screen_toggle = True
                
            def toggle_bookcase(event):
                if event.type == pygame.KEYDOWN and event.key == pygame.K_e and game.player.PLAYER.can_move_bookcase and game.quest.quest4.check_bookcase_toggle():
                    timer = []
                    timer.append(int(time.time()))
                    TOTAL_DISTANCE = 5
                    TIME = 5
                    OFFICE_MUSIC.stop()
                    MOVE_BOOKCASE.play()
                    LAB_MUSIC.play(-1)
                    while game.mechanics.time.timer(timer, TIME) == False:
                        BOOKCASE1_RECT.x -= TOTAL_DISTANCE / TIME
                        BOOKCASE2_RECT.x -= TOTAL_DISTANCE / TIME
                        BOOKCASE3_RECT.x += TOTAL_DISTANCE / TIME
                        BOOKCASE4_RECT.x += TOTAL_DISTANCE / TIME
                        game.player.PLAYER.movement.toggle_movement = False
                        game.world.world2.graphics.render_all()
                        timer.append(int(time.time()))
                        game.player.PLAYER.can_move_bookcase = False
                    MOVE_BOOKCASE.stop()
                    LAB_MUSIC.stop()
                    OFFICE_MUSIC.play(-1)
                    timer = []
                    game.player.PLAYER.movement.toggle_movement = True
                    game.player.PLAYER.bookcase_moved = True

    # attributes and functions unique to each world
    class world:
        # office
        class world1:
            class graphics:
                def render_all():
                    # draw office graphics
                    pygame.Surface.fill(SCREEN, "black")
                    game.render.graphics.background(game.background.OFFICE_FLOOR)
                    #pygame.draw.rect(SCREEN, "white", TO_MANAGER_OFFICE)
                    game.render.graphics.cubicles(all_cubicles, CUBICLE_SPRITES)
                    game.render.graphics.office_plants(all_office_plants)
                    game.render.graphics.all_characters(game.character.characters)
                    game.render.pathway.pathways(game.pathway.render_office_pathways)
                    game.render.graphics.sprites(game.player.PLAYER)
                    game.render.dialogue.draw_textbox_mechanics()
                    # draw pathway text if true
                    game.render.pathway.pathway_text(game.pathway.render_office_pathways)
                    game.render.graphics.border()
                    # draw quest goal if player.quest_set.has_quest == True
                    game.render.quest.draw_quest()
                    # draw quest item activate toggle if user collides with quest object
                    game.render.quest.draw_collect_item_toggle()

                    # update display
                    pygame.display.flip()
            
            class mechanics:
                def set_mechanics():
                    global PLAYER_X_VELOCITY, PLAYER_Y_VELOCITY
                    PLAYER_X_VELOCITY, PLAYER_Y_VELOCITY = 30, 30
                    game.player.PLAYER.movement.left_limit = OFFICE_FLOOR_RECT.left + OFFICE_FLOOR_RECT.width / 2
                    game.player.PLAYER.movement.right_limit = -4900
                    game.player.PLAYER.movement.top_limit = 400
                    game.player.PLAYER.movement.bottom_limit = -2400
                    game.player.PLAYER.movement.toggle_movement = True

                class collisions:
                    class pathways:
                        def check_collision_pathways():
                            game.mechanics.collision.teleport_pathway(office_pathways)

                class movement:
                    def move_all(x_velocity, y_velocity):
                        # office
                        game.animate.movement.background.move_background(game.background.OFFICE_FLOOR, x_velocity, y_velocity)
                        game.animate.movement.objects.move_cubicles(all_cubicles, all_cubicle_colliders, x_velocity, y_velocity)
                        game.animate.movement.objects.move_office_plants(all_office_plants, all_office_plant_colliders, x_velocity, y_velocity)
                        game.animate.movement.characters.move_characters(game.character.characters, x_velocity, y_velocity)
                        game.animate.movement.pathways.pathway(office_pathways, game.pathway.render_office_pathways, x_velocity, y_velocity)
                        game.animate.movement.objects.move_quest_cubicle()

                    def handle_all_hitboxes(player):
                        game.player.PLAYER.quest_set.quest.toggle_collect = False
                        # check for player collisions
                        if game.mechanics.collision.check_collision_cubicles(player, all_cubicle_colliders) \
                            or game.mechanics.collision.check_collision_office_plants(player, all_office_plant_colliders) \
                            or game.mechanics.collision.check_collision_player_limits(player):
                            # move player based on collision
                            game.mechanics.collision.check_collision(player)

        # manager's office
        class world2:
            class graphics:
                def render_all():
                    # draw manager's office graphics
                    pygame.Surface.fill(SCREEN, "black")
                    game.render.graphics.background(game.background.MANAGER_OFFICE_FLOOR)
                    game.render.graphics.sprites(game.object.MANAGER_OFFICE_CARPET)
                    game.render.graphics.all_characters(game.character.manager_office_characters)
                    game.render.graphics.sprites(game.object.MANAGER_DESK)
                    game.render.pathway.pathways(game.pathway.render_manager_office_pathways)
                    #pygame.draw.rect(SCREEN, WHITE, TO_HALLWAY1_COLLIDER)
                    game.render.graphics.bookcases(game.object.bookcases)
                    game.render.graphics.sprites(game.player.PLAYER)
                    game.render.pathway.pathway_text(game.pathway.render_manager_office_pathways)
                    game.render.dialogue.draw_textbox_mechanics()
                    game.render.graphics.border()
                    # draw quest goal if player.quest_set.has_quest == True
                    game.render.quest.draw_quest()
                    # draw bookcase toggle if player.can_move_bookcase
                    game.quest.quest4.check_bookcase_toggle()

                    # update display
                    pygame.display.flip()
            
            class mechanics:
                def set_mechanics():
                    global PLAYER_X_VELOCITY, PLAYER_Y_VELOCITY
                    PLAYER_X_VELOCITY, PLAYER_Y_VELOCITY = 20, 20
                    game.player.PLAYER.movement.left_limit = 680
                    game.player.PLAYER.movement.right_limit = -1470
                    game.player.PLAYER.movement.top_limit = 349
                    game.player.PLAYER.movement.bottom_limit = -1301
                    game.player.PLAYER.movement.toggle_movement = True
                    game.player.PLAYER.movement.toggle_y_velocity = True

                class collisions:
                    class pathways:
                        def check_collision_pathways():
                            game.mechanics.collision.teleport_pathway(manager_office_pathways)

                class movement:
                    def move_all(x_velocity, y_velocity):
                        # manager's office
                        game.animate.movement.objects.move_manager_desk(x_velocity, y_velocity)
                        game.animate.movement.background.move_background(game.background.MANAGER_OFFICE_FLOOR, x_velocity, y_velocity)
                        game.animate.movement.characters.move_characters(game.character.manager_office_characters, x_velocity, y_velocity)
                        game.animate.movement.pathways.pathway(manager_office_pathways, game.pathway.render_manager_office_pathways, x_velocity, y_velocity)
                        game.animate.movement.objects.move_bookcases(game.object.bookcases, x_velocity, y_velocity)
                        game.animate.movement.objects.move_carpets(game.object.carpets, x_velocity, y_velocity)
                        game.animate.movement.objects.move_quest_bookcase(x_velocity, y_velocity)

                    def handle_all_hitboxes(player):
                        if game.mechanics.collision.check_collision_manager_desk(player) \
                            or game.mechanics.collision.check_collision_player_limits(player) \
                            or game.mechanics.collision.check_collision_bookcase(player, game.object.bookcases):
                            # move player based on collision
                            game.mechanics.collision.check_collision(player)

        # kitchen
        class world3:
            class graphics:
                def render_all():
                    pygame.Surface.fill(SCREEN, "black")
                    game.render.graphics.background(game.background.KITCHEN_FLOOR)
                    game.render.pathway.pathways(game.pathway.render_kitchen_pathways)
                    game.render.pathway.pathway_text(game.pathway.render_kitchen_pathways)
                    game.render.graphics.sprites(game.object.KITCHEN_COUNTER)
                    game.render.graphics.sprites(game.object.FRIDGE)
                    game.render.graphics.sprites(game.object.CORNMEAL)
                    game.render.graphics.sprites(game.player.PLAYER)
                    game.render.quest.draw_collect_item_toggle()
                    # draw quest goal if player.quest_set.has_quest == True
                    game.render.quest.draw_quest()

                    pygame.display.flip()
                
            class mechanics:
                def set_mechanics():
                    global PLAYER_X_VELOCITY, PLAYER_Y_VELOCITY
                    PLAYER_X_VELOCITY, PLAYER_Y_VELOCITY = 10, 10
                    game.player.PLAYER.movement.left_limit = 670
                    game.player.PLAYER.movement.right_limit = -370
                    game.player.PLAYER.movement.top_limit = 306
                    game.player.PLAYER.movement.bottom_limit = -474
                    game.player.PLAYER.movement.toggle_movement = True
                
                class collisions:
                    class pathways:
                        def check_collision_pathways():
                            game.mechanics.collision.teleport_pathway(kitchen_pathways)

                class movement:
                    def move_all(x_velocity, y_velocity):
                        game.animate.movement.background.move_background(game.background.KITCHEN_FLOOR, x_velocity, y_velocity)
                        game.animate.movement.pathways.pathway(kitchen_pathways, game.pathway.render_kitchen_pathways, x_velocity, y_velocity)
                        game.animate.movement.objects.move_kitchen_objects(game.object.KITCHEN_OBJECTS, x_velocity, y_velocity)

                    def handle_all_hitboxes(player):
                        game.player.PLAYER.quest_set.quest.toggle_collect = False
                        if game.mechanics.collision.check_collision_player_limits(player) \
                            or game.mechanics.collision.check_collision_kitchen_objects():
                            game.mechanics.collision.check_collision(player)

        # catch-a-corn
        class world4:
            class graphics:
                def render_opening_text(text, color, font_size, y):
                    font = pygame.font.Font(PRESS_START_2P_REGULAR, font_size)
                    text_width = len(text) * font_size
                    render_text = pygame.font.Font.render(font, text, False, color)
                    pygame.Surface.blit(SCREEN, render_text, (CATCH_A_CORN_BACKGROUND_RECT.x + CATCH_A_CORN_BACKGROUND_RECT.width / 2 - text_width / 2, y))

                def render_opening_screen():
                    if game.world.world4.mechanics.enter_count == 0:
                        game.render.graphics.background(game.background.CATCH_A_CORN_OPENING_BACKGROUND)
                        game.world.world4.graphics.render_opening_text("PRESS SPACE TO CONTINUE", BLACK, 20, CATCH_A_CORN_BACKGROUND_RECT.y + CATCH_A_CORN_BACKGROUND_RECT.width - 140)
                    elif game.world.world4.mechanics.enter_count == 1:
                        game.world.world4.graphics.render_opening_text("CATCH-A-CORN:", "yellow", 25, 100)
                        game.world.world4.graphics.render_opening_text("Catch corn to earn EGGS by using 'A' and 'D' to move the egg basket.", WHITE, 20, 180)
                        game.world.world4.graphics.render_opening_text("If you miss a corn, you will lose a life. You have 5 lives.", WHITE, 20, 230)
                        game.world.world4.graphics.render_opening_text("To win the bid, you must earn 100 EGGS by catching 100 corn.", WHITE, 20, 280)
                        game.world.world4.graphics.render_opening_text("Good luck!", WHITE, 20, 330)
                        game.world.world4.graphics.render_opening_text("Press SPACE to continue", WHITE, 20, 470)

                def render_corn():
                    for corn in game.world.world4.mechanics.all_corn:
                        pygame.Surface.blit(SCREEN, pygame.transform.scale(CORN_SPRITE, (corn.width, corn.height)), corn)

                def render_egg_count():
                    font_size = 20
                    font = pygame.font.Font(PRESS_START_2P_REGULAR, font_size)
                    text = f"{game.world.world4.mechanics.egg_count} x "
                    text_width = len(text) * font_size
                    render_text = pygame.font.Font.render(font, text, False, WHITE)
                    pygame.Surface.blit(SCREEN, render_text, (CATCH_A_CORN_BACKGROUND_RECT.x + CATCH_A_CORN_BACKGROUND_RECT.width - 60 - text_width, 40))

                def render_win_loss(text, color):
                    CATCH_A_CORN_MUSIC.stop()
                    timer = []
                    timer.append(int(time.time()))
                    timer.append(int(time.time()))
                    while game.mechanics.time.timer(timer, 5) == False:
                        game.world.world4.graphics.render_opening_text(text, color, 50, 290)
                        pygame.display.flip()
                        timer.append(int(time.time()))
                    game_settings.game_world = OFFICE
                    game.world.world1.mechanics.set_mechanics()
                    if game.world.world4.mechanics.win and game.player.PLAYER.quest_set.quest.quest_num == "2":
                        QUEST_COMPLETE_SOUND.play()
                    # reset game settings
                    game.world.world4.mechanics.egg_count = 0
                    game.world.world4.mechanics.all_corn = []
                    game.world.world4.mechanics.time = []
                    game.world.world4.mechanics.opening_screen_toggle = True
                    game.world.world4.mechanics.enter_count = 0
                    game.world.world4.mechanics.win_loss_toggle = False
                    game.world.world4.mechanics.win = False
                    game.world.world4.mechanics.loss = False
                    game.world.world4.mechanics.speed_multiplier = 1
                    create.object.health.hearts(5)
                    OFFICE_MUSIC.play(-1)

                def render_all():
                    pygame.Surface.fill(SCREEN, "black")
                    # draw opening screen background
                    if game.world.world4.mechanics.opening_screen_toggle == True:
                        game.world.world4.graphics.render_opening_screen()
                    # draw game
                    elif game.world.world4.mechanics.opening_screen_toggle == False and game.world.world4.mechanics.win_loss_toggle == False:
                        game.render.graphics.background(game.background.CATCH_A_CORN_BACKGROUND)
                        game.world.world4.graphics.render_corn()
                        game.render.graphics.sprites(game.player.CORN_BASKET)
                        game.render.graphics.sprites(game.object.EGG)
                        game.render.graphics.sprites(game.object.CHICKEN)
                        game.render.graphics.all_hearts(game.object.all_health)
                        game.world.world4.graphics.render_egg_count()
                    elif game.world.world4.mechanics.win_loss_toggle == True and game.world.world4.mechanics.loss == True:
                        game.render.graphics.background(game.background.CATCH_A_CORN_BACKGROUND)
                        game.world.world4.graphics.render_win_loss("YOU LOSE.", "red")
                    elif game.world.world4.mechanics.win_loss_toggle == True and game.world.world4.mechanics.win == True:
                        game.render.graphics.background(game.background.CATCH_A_CORN_BACKGROUND)
                        game.world.world4.graphics.render_win_loss("YOU WIN!", DARK_GREEN)
                    # refresh display
                    pygame.display.flip()
                
            class mechanics:
                egg_count = 0
                all_corn = []
                time = []
                time2 = []
                opening_screen_toggle = True
                enter_count = 0
                win_loss_toggle = False
                win = False
                loss = False
                speed_multiplier = 1

                def set_mechanics():
                    game.player.PLAYER.movement.toggle_movement = False
                    CATCH_A_CORN_INTRO_MUSIC.play(-1)
                    OFFICE_MUSIC.stop()

                class proceed:
                    def opening_screen(event):
                        if game_settings.game_world == CATCH_A_CORN and event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and game.world.world4.mechanics.enter_count < 2:
                            game.world.world4.mechanics.enter_count += 1
                            START_GAME_SOUND.play()
                            if game.world.world4.mechanics.enter_count == 2:
                                game.world.world4.mechanics.opening_screen_toggle = False
                                CATCH_A_CORN_INTRO_MUSIC.stop()
                                START_GAME_SOUND.play()
                                pygame.time.delay(1000)
                                CATCH_A_CORN_MUSIC.play(-1)

                class win_loss:
                    def handle_win():
                        CATCH_A_CORN_WIN_SOUND.play()
                        game.world.world4.mechanics.win_loss_toggle = True
                        game.world.world4.mechanics.win = True
                        game.player.PLAYER.quest_set.quest.has_item = True
                        if game.player.PLAYER.quest_set.quest.quest_num == "2":
                            game.player.PLAYER.quest_set.quest.text_color = YELLOW
                            game.player.PLAYER.quest_set.quest.goal = "Goal update: Cornfield has been secured! Tell the manager this good news."
                            # update manager dialogue
                            game.character.MANAGER.dialogue = quest2_complete_dialogue["manager"]["character"]
                            game.character.MANAGER.dialogue_toggle_index = 0
                            game.character.MANAGER.dialogue_index = 0
                            game.character.MANAGER.dialogue_end = False
                            game.character.MANAGER.first_line = True
                            game.character.MANAGER.final_dialogue = False
                        
                    def handle_loss():
                        CATCH_A_CORN_LOSE_SOUND.play()
                        game.world.world4.mechanics.win_loss_toggle = True
                        game.world.world4.mechanics.loss = True

                    def handle_win_loss():
                        if game.world.world4.mechanics.egg_count == 100:
                            game.world.world4.mechanics.win_loss.handle_win()
                        elif len(game.object.all_health) == 0:
                            game.world.world4.mechanics.win_loss.handle_loss()

                class corn:
                    def spawn_corn():
                        if game.mechanics.time.timer(game.world.world4.mechanics.time, 1):
                            x_pos = random.choice(range(int(CATCH_A_CORN_BACKGROUND_RECT.x), int(CATCH_A_CORN_BACKGROUND_RECT.x + CATCH_A_CORN_BACKGROUND_RECT.width - CORN_WIDTH)))
                            game.world.world4.mechanics.all_corn.append(pygame.Rect(x_pos, -100, CORN_WIDTH, CORN_HEIGHT))
                            game.world.world4.mechanics.time = []

                class health:
                    def handle_health():
                        if len(game.object.all_health) > 0:
                            game.object.all_health.remove(game.object.all_health[-1])
                            CATCH_A_CORN_LOSE_HEALTH_SOUND.play()

                class collision:
                    def check_collision_corn(corn_list, player):
                        for corn in corn_list:
                            if player.collider.colliderect(corn):
                                CATCH_A_CORN_CATCH_CORN_SOUND.play()
                                game.world.world4.mechanics.egg_count += 1
                                game.world.world4.mechanics.all_corn.remove(corn)

                class movement():
                    def handle_basket_movement(player):
                        key_pressed = pygame.key.get_pressed()
                        # handle movement
                        if key_pressed[player.movement.left_key] and player.rect.x >= player.movement.left_limit:
                            player.rect.x -= player.movement.x_velocity
                        if key_pressed[player.movement.right_key] and player.rect.x <= player.movement.right_limit:
                            player.rect.x += player.movement.x_velocity
                        
                        player.collider.x = player.rect.x
            
                    def handle_corn_movement():
                        game.world.world4.mechanics.time2.append(int(time.time()))
                        corn_velocity = game.world.world4.mechanics.speed_multiplier
                        for corn in game.world.world4.mechanics.all_corn:
                            corn.y += corn_velocity
                            if corn.y > WINDOW_HEIGHT:
                                game.world.world4.mechanics.all_corn.remove(corn)
                                game.world.world4.mechanics.health.handle_health()

                        game.world.world4.mechanics.time2.append(int(time.time()))
                        if game.mechanics.time.timer(game.world.world4.mechanics.time2, 2):
                            game.world.world4.mechanics.speed_multiplier += 0.3
                            game.world.world4.mechanics.time2 = []

            def handle_catch_a_corn():
                if game_settings.game_world.world == "world4" and game.world.world4.mechanics.opening_screen_toggle == False and game.world.world4.mechanics.win_loss_toggle == False:
                    # initialize minigame
                    game.world.world4.mechanics.time.append(int(time.time()))
                    player = game.player.CORN_BASKET
                    game.world.world4.mechanics.corn.spawn_corn()
                    game.world.world4.mechanics.movement.handle_corn_movement()
                    game.world.world4.mechanics.movement.handle_basket_movement(player)
                    game.world.world4.mechanics.collision.check_collision_corn(game.world.world4.mechanics.all_corn, player)
                    game.world.world4.mechanics.win_loss.handle_win_loss()

        # hallway
        class world5:
            class graphics:
                def render_all():
                    pygame.Surface.fill(SCREEN, "black")
                    game.render.graphics.background(game.background.HALLWAY1_BACKGROUND)
                    game.render.graphics.sprites(game.player.PLAYER)
                    game.render.graphics.background(game.background.HALLWAY1_LIGHTING)
                    pygame.display.flip()
            
            class mechanics:
                def set_mechanics():
                    global PLAYER_X_VELOCITY
                    PLAYER_X_VELOCITY = 10
                    game.player.PLAYER.movement.toggle_y_velocity = False
                    game.player.PLAYER.rect.y = 428
                    OFFICE_MUSIC.stop()
                    HALLWAY_MUSIC.play(-1)
                    
                class collisions:
                    class pathways:
                        def check_collision_pathways():
                            game.mechanics.collision.teleport_pathway(hallway1_pathways)

                class movement:
                    def move_all(x_velocity, y_velocity):
                        game.animate.movement.background.move_background(game.background.HALLWAY1_BACKGROUND, x_velocity, y_velocity)
                        game.animate.movement.background.move_background(game.background.HALLWAY1_LIGHTING, x_velocity, y_velocity)
                        game.animate.movement.pathways.collider(hallway1_pathways, x_velocity, y_velocity)

        # hallway 2
        class world6:
            class graphics:
                def render_all():
                    pygame.Surface.fill(SCREEN, "black")
                    game.render.graphics.background(game.background.HALLWAY2_BACKGROUND)
                    game.render.graphics.sprites(game.player.PLAYER)
                    game.render.graphics.background(game.background.HALLWAY2_LIGHTING)
                    pygame.display.flip()

            class mechanics:
                def set_mechanics():
                    game.world.world5.mechanics.set_mechanics()

                class collisions:
                    class pathways:
                        def check_collision_pathways():
                            game.mechanics.collision.teleport_pathway(hallway2_pathways)
                    
                class movement:
                    def move_all(x_velocity, y_velocity):
                        game.animate.movement.background.move_background(game.background.HALLWAY2_BACKGROUND, x_velocity, y_velocity)
                        game.animate.movement.background.move_background(game.background.HALLWAY2_LIGHTING, x_velocity, y_velocity)
                        game.animate.movement.pathways.collider(hallway2_pathways, x_velocity, y_velocity)

        # lab
        class world7:
            class graphics:
                def render_all():
                    pygame.Surface.fill(SCREEN, "black")
                    game.render.graphics.background(game.background.LAB_BACKGROUND)
                    game.render.graphics.sprites(game.player.PLAYER)
                    game.render.graphics.all_characters(game.character.lab_characters)
                    game.render.graphics.background(game.background.LAB_LIGHTING)
                    game.render.dialogue.draw_textbox_mechanics()
                    pygame.display.flip()
                    
            class mechanics:
                def set_mechanics():
                    game.player.PLAYER.movement.right_limit = -3310
                    game.player.PLAYER.movement.left_limit = 650
                    HALLWAY_MUSIC.stop()
                    LAB_MUSIC.play(-1)
                    game.character.MANAGER.dialogue_end = False
                    game.character.MANAGER.dialogue_index = 0
                    game.character.MANAGER.dialogue_toggle_index = 0
                    game.character.MANAGER.dialogue = final_character_dialogue["manager"]["character"]
                    game.character.MANAGER.sprite = CHICKEN_SPRITE
                    game.character.MANAGER.rect.x = LAB_RECT.x + LAB_RECT.width - 500
                    game.character.MANAGER.rect.y = 428
                    game.character.MANAGER.first_line = True

                class movement:
                    def move_all(x_velocity, y_velocity):
                        game.animate.movement.background.move_background(game.background.LAB_BACKGROUND, x_velocity, y_velocity)
                        game.animate.movement.background.move_background(game.background.LAB_LIGHTING, x_velocity, y_velocity)
                        game.animate.movement.characters.move_characters(game.character.lab_characters, x_velocity, y_velocity)
                    
                    def handle_all_hitboxes(player):
                        if game.mechanics.collision.check_collision_player_limits(player):
                            game.mechanics.collision.check_collision(player)
                
                class quest:
                    def end_game():
                        while game_settings.end:
                            # draw end screen
                            pygame.Surface.fill(SCREEN, "black")
                            END_SOUND.play()
                            pygame.time.delay(1000)
                            END_SOUND.stop()
                            END_THEME.play()
                            while True:
                                game.world.world4.graphics.render_opening_text(" THE END.", YELLOW, 70, 200)
                                game.world.world4.graphics.render_opening_text("..And the sun rises once more.", WHITE, 20, 300)
                                game.world.world4.graphics.render_opening_text("(You saved the world!)", WHITE, 20, 350)
                                game.world.world4.graphics.render_opening_text("(Press SPACE to end game.)", WHITE, 15, 450)
                                pygame.display.flip()
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        sys.exit()
                                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                                        START_GAME_SOUND.play()
                                        pygame.time.delay(500)
                                        sys.exit()

                    def animate_corn():
                        game.player.PLAYER.dialogue_toggle = False
                        # corn movement
                        degree = 0
                        x = 0
                        y = 100
                        while x <= WINDOW_WIDTH + 100:
                            CORN_WHOOSH_SOUND.play()
                            degree += 10
                            x += 20
                            y += 8
                            pygame.Surface.fill(SCREEN, "black")
                            game.render.graphics.background(game.background.LAB_BACKGROUND)
                            game.render.graphics.sprites(game.player.PLAYER)
                            # move manager
                            if x >= game.character.MANAGER.rect.x:
                                game.character.MANAGER.rect.x = WINDOW_WIDTH + 500
                            if game.character.MANAGER.rect.x == WINDOW_WIDTH + 500:
                                MANAGER_HIT_SOUND.play()
                            game.render.graphics.all_characters(game.character.lab_characters)
                            game.render.graphics.background(game.background.LAB_LIGHTING)
                            pygame.Surface.blit(SCREEN, pygame.transform.rotate(pygame.transform.scale(CORN_SPRITE, (CORN_WIDTH, CORN_HEIGHT)), (degree)), (x, y))
                            pygame.display.flip()
                        CORN_WHOOSH_SOUND.stop()

                        # draw win text
                        pygame.time.delay(500)
                        timer = []
                        timer.append(int(time.time()))
                        CATCH_A_CORN_WIN_SOUND.play()
                        while game.mechanics.time.timer(timer, 5) == False:
                            game.world.world4.graphics.render_opening_text("YOU WIN!", WHITE, 50, 290)
                            pygame.display.flip()
                            timer.append(int(time.time()))
                        game_settings.end = True

                    def dialogue_event():
                        if game.character.MANAGER.dialogue_index == 2:
                            game.character.MANAGER.sprite = CHICKEN_LEFT_SPRITE
                        elif game.character.MANAGER.dialogue_index == 7:
                            game.text_box.text_box.character_name = "Manager"
                        elif game.character.MANAGER.dialogue_index == 48 or game.character.MANAGER.dialogue_index == 50 or \
                             game.character.MANAGER.dialogue_index == 53 or game.character.MANAGER.dialogue_index == 56:
                            game.text_box.text_box.character_name = "Bill"
                            game.text_box.text_box.character_icon = PLAYER_ICON
                            # animate corn collision
                            if game.character.MANAGER.dialogue_index == 56:
                                game.world.world7.mechanics.quest.animate_corn()
                        elif game.character.MANAGER.dialogue_index == 49 or game.character.MANAGER.dialogue_index == 47 or game.character.MANAGER.dialogue_index == 52 \
                            or game.character.MANAGER.dialogue_index == 55:
                            game.text_box.text_box.character_name = "Manager"
                            game.text_box.text_box.character_icon = CHICKEN_ICON

                    def toggle_final_dialogue(event):
                        if LAB_RECT.x <= -2830:
                            if game.character.MANAGER.first_line:
                                game.character.MANAGER.first_line = False
                                game.character.MANAGER.final_dialogue = False
                                LAB_MUSIC.stop()
                                game.text_box.text_box.toggle = True
                                game.player.PLAYER.movement.x_velocity = 0
                                game.player.PLAYER.movement.toggle_movement = False
                                game.text_box.text_box.text = game.character.MANAGER.dialogue[0][0]
                                game.text_box.text_box.character_icon = CHICKEN_ICON
                                game.text_box.text_box.character_name = "???"
                                TEXT_BOX.y = LAB_RECT.y
                                CHARACTER_ICON_RECT.y = game.text_box.text_box.rect.y + 60
                            if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                                game.mechanics.dialogue.change_dialogue(game.character.MANAGER)
                                game.mechanics.dialogue.change_line(game.character.MANAGER)
                                game.text_box.text_box.text = game.character.MANAGER.dialogue[game.character.MANAGER.dialogue_toggle_index][game.character.MANAGER.dialogue_index]
                                game.world.world7.mechanics.quest.dialogue_event()

# create worlds (different rooms loaded when user steps on pathway)
# world 1
OFFICE = create.world(
    "world1",
    game.background.OFFICE_FLOOR, 
    game.object.objects, 
    game.character.characters)
# world 2
MANAGER_OFFICE = create.world( 
    "world2",
    game.background.MANAGER_OFFICE_FLOOR, 
    game.object.manager_office_objects, 
    game.character.manager_office_characters)
# world 3
KITCHEN = create.world("world3", game.background.KITCHEN_FLOOR, [], [])
# world 4
CATCH_A_CORN = create.world("world4", game.background.CATCH_A_CORN_BACKGROUND, [], [])
# world 5
HALLWAY1 = create.world("world5", game.background.HALLWAY1_BACKGROUND, [], [])
# world 6
HALLWAY2 = create.world("world6", game.background.HALLWAY2_BACKGROUND, [], [])
# world 7
LAB = create.world("world7", game.background.LAB_BACKGROUND, [], [])

# set game settings (ex. game world)
game_settings = game(OFFICE, False)

# game
def main():
    CLOCK.tick(framerate)
    # title screen + animation
    game.animate.intro()
    OFFICE_MUSIC.play(-1)
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # handle quest toggles
            game.mechanics.quest.collect_item(event)
            game.mechanics.quest.toggle_minigame(event)
            game.mechanics.quest.toggle_bookcase(event)
            # handle catch-a-corn opening screen
            game.world.world4.mechanics.proceed.opening_screen(event)
            # toggle final game dialogue
            game.world.world7.mechanics.quest.toggle_final_dialogue(event)

        # handle player movement and collisions based on assigned game_settings.game_world.world
        game.mechanics.movement.handle_player_movement(game_settings.game_world, game.player.PLAYER)
        
        # teleport player to new world when pathway is stepped on
        game.mechanics.collision.handle_pathway(game_settings.game_world)

        # render game graphics based on assigned game_world.world
        game.render.graphics.all_graphics(game_settings.game_world)
        
        # handle dialogue with world-specific characters
        game.mechanics.dialogue.handle_dialogue(game.player.PLAYER, game_settings.game_world.characters)

        # run catch-a-corn if minigame active
        game.world.world4.handle_catch_a_corn()

        # display game end screen if game_settings.end == True
        game.world.world7.mechanics.quest.end_game()

# run game
main()