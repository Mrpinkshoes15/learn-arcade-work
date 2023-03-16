import arcade

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
MOVEMENT_SPEED = 3


class Smile:
    def __init__(self, position_x, position_y, change_x, change_y, radius, color):

        # Take the parameters of the init function above,
        # and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color

    def draw_smile(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x, self.position_y - 60, self.radius, self.color)
        arcade.draw_arc_filled(self.position_x, self.position_y, 200, 100, arcade.csscolor.RED, 180, 360)
        arcade.draw_arc_filled(self.position_x, self.position_y - 5, 180, 80, arcade.csscolor.DARK_RED, 180, 360)
        arcade.draw_arc_filled(self.position_x, self.position_y - 30, 100, 200, arcade.csscolor.LIGHT_PINK, 180, 360)
        arcade.draw_arc_filled(self.position_x - 20, self.position_y - 30, 60, 20, arcade.csscolor.LIGHT_PINK, 0, 180)
        arcade.draw_arc_filled(self.position_x + 20, self.position_y - 30, 60, 20, arcade.csscolor.LIGHT_PINK, 0, 180)

    def update(self):
        # Move the ball
        self.position_y += self.change_y
        self.position_x += self.change_x

        # See if the ball hit the edge of the screen. If so, change direction
        if self.position_x < self.radius:
            self.position_x = self.radius

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.position_x = SCREEN_WIDTH - self.radius

        if self.position_y < self.radius:
            self.position_y = self.radius

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.position_y = SCREEN_HEIGHT - self.radius


class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.ASH_GREY)

        # Create our ball
        self.smile = Smile(50, 50, 0, 0, 30, arcade.color.AUBURN)

    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()
        self.smile.draw_smile()

    def update(self, delta_time):
        self.smile.update()

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT:
            self.smile.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.smile.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.smile.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.smile.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.smile.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.smile.change_y = 0


def main():
    window = MyGame(640, 480, "Drawing Example")
    arcade.run()


main()