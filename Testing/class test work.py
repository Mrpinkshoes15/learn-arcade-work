#imports
import arcade

# screen stuff
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 750
x = 500
y = 375
def draw_smile():
    arcade.draw_arc_filled(500, 375, 200, 100, arcade.csscolor.RED, 180, 360)
    arcade.draw_arc_filled(500, 375 - 5, 180, 80, arcade.csscolor.DARK_RED, 180, 360)
    arcade.draw_arc_filled(500, 375 - 30, 100, 200, arcade.csscolor.LIGHT_PINK, 180, 360)
    arcade.draw_arc_filled(500 - 20, 375 - 30, 60, 20, arcade.csscolor.LIGHT_PINK, 0, 180)
    arcade.draw_arc_filled(500 + 20, 375 - 30, 60, 20, arcade.csscolor.LIGHT_PINK, 0, 180)
    arcade.draw_line(500, 350, 500, 290, arcade.csscolor.PINK, 2)

def draw_lines(x, y):
    arcade.draw_rectangle_filled(x, y + 50, 125, 15, arcade.csscolor.SLATE_GREY, 0)
    arcade.draw_rectangle_filled(x + 250, y + 50, 125, 15, arcade.csscolor.SLATE_GREY, 0)
    arcade.draw_rectangle_filled(x - 250, y + 50, 125, 15, arcade.csscolor.SLATE_GREY, 0)
    arcade.draw_rectangle_filled(x + 500, y + 50, 125, 15, arcade.csscolor.SLATE_GREY, 0)
    arcade.draw_rectangle_filled(x - 500, y + 50, 125, 15, arcade.csscolor.SLATE_GREY, 0)
    arcade.draw_rectangle_filled(x + 750, y + 50, 125, 15, arcade.csscolor.SLATE_GREY, 0)
    arcade.draw_rectangle_filled(x - 750, y + 50, 125, 15, arcade.csscolor.SLATE_GREY, 0)
    arcade.draw_rectangle_filled(x - 1000, y + 50, 125, 15, arcade.csscolor.SLATE_GREY, 0)
    arcade.draw_circle_filled(x - 200, y + 400, 70, arcade.csscolor.WHITE_SMOKE, 0)
    arcade.draw_circle_filled(x - 125, y + 380, 50, arcade.csscolor.WHITE_SMOKE, 0)

def draw_road():
    # road
    arcade.draw_rectangle_filled(500, 150, 999, 300, arcade.csscolor.SLATE_GREY)
    arcade.draw_rectangle_filled(500, 300, 999, 15, arcade.csscolor.YELLOW)

def on_draw(delta_time):
    arcade.start_render()
    draw_road()
    draw_lines(on_draw.lines_x, 250)
    draw_smile()
    on_draw.lines_x += 10
    if on_draw.lines_x == 1200:
        on_draw.lines_x = 0
on_draw.lines_x = 0
def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, 'Ferrari F-40')
    arcade.set_background_color(arcade.csscolor.LIGHT_SKY_BLUE)
    arcade.schedule(on_draw, 1/60)
    arcade.run()

main()

