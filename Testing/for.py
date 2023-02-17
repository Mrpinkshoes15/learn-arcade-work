#imports
import arcade
import random
from pyglet.window import key
from pyglet.window import Window

# screen stuff
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
SCALE = 1

# L_Paddle
l_paddle_x = 20
l_paddle_y = 400
l_paddle_size = 100
l_paddle_uplimit = 800
l_paddle_downlimit = 0
up = False
down = False


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, 'Pingk Pongk')
    arcade.set_background_color(arcade.csscolor.BLACK)
    arcade.run()

main()