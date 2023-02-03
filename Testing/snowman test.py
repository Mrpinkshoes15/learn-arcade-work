import arcade
import math


# screen stuff
WIDTH = 1000
HEIGHT = 800
arcade.open_window(WIDTH, HEIGHT, 'moving car')
arcade.set_background_color(arcade.csscolor.LIGHT_GREEN)
x_start = 500
y_start = 400
arcade.start_render()

#colors
road = arcade.csscolor.DARK_SLATE_GRAY


#road
arcade.draw_polygon_filled([(500, 0), (600, 0), (550, 200), (450, 200)], road)
arcade.draw_polygon_filled([(450, 200), (550, 200), (700, 350), (600, 350)], road)
arcade.draw_polygon_filled([(600, 350), (700, 350)], road)

arcade.finish_render()
arcade.run()