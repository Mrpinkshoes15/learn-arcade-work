import arcade
import random


# screen stuff
WIDTH = 1200
HEIGHT = 1200
arcade.open_window(WIDTH, HEIGHT, 'moving car')
arcade.set_background_color(arcade.csscolor.LIGHT_GREEN)
arcade.start_render()

#def square(center_x, center_y):
    #arcade.draw_rectangle_filled(center_x, center_y, 5, 5, arcade.csscolor.BLACK)

#for x in range(400, 640, 10):
    #for y in range(x + 100, 640, 10):
        #square(x, y)

def draw_section_6(center_x, center_y):
    arcade.draw_rectangle_filled(center_x, center_y, 5, 5, arcade.csscolor.BLACK)


for x in range(300):
    for y in range(200):
        draw_section_6(x, y)

arcade.finish_render()
arcade.run()