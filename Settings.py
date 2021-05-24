TITLE = "Chicken The Survivor"

#initialise the windows size
WIDTH = 1280
HEIGHT = 800
FPS = 60

# Player properties
PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.12
PLAYER_GRAV = 0.8

#starting platforms
PLATFORMS_LIST = [(100 , HEIGHT - 200 ,WIDTH - 150, 30 ),
                ( 700 , HEIGHT * 1/2 , 150 , 20),
                ( WIDTH / 3 - 50 , HEIGHT * 1/2 , 100 , 20),
                ( WIDTH / 4 - 50 , HEIGHT * 0.2 , 120 , 20)]

#initialise the color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
