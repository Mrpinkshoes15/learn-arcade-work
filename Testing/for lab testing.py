""" Sprite Sample Program """

import random
import arcade

# --- Constants ---
SPRITE_SCALING_WALLS = .5
MOVEMENT_SPEED = 3

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 512


class Walls(arcade.Sprite):

    def update(self):
        """ Move the walls """
        # Move walls.
        # Remove these lines if physics engine is moving walls.
        self.center_x += self.change_x
        self.center_y += self.center_y


class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")

        # Variables that will hold sprite lists
        self.walls_list = None

        # Set up the walls info
        self.walls_sprite = None

        # Don't show the mouse cursor
        self.set_mouse_visible(True)

        self.space_pressed = False

        self.game_started = False

        arcade.set_background_color(arcade.color.LIGHT_SKY_BLUE)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.walls_list = arcade.SpriteList()
        # self.walls_sprite = arcade.Sprite(":resources:images/tiles/brickGrey.png", SPRITE_SCALING_WALLS)
        # self.walls_sprite.center_x = 800
        # self.walls_sprite.center_y = 300
        # self.walls_list.append(self.walls_sprite)

        for y in range(32, 512, 64):
            self.walls_sprite = arcade.Sprite(":resources:images/tiles/brickGrey.png", SPRITE_SCALING_WALLS)
            self.walls_sprite.center_x += self.walls_sprite.change_x
            self.walls_sprite.center_y = y
            self.walls_list.append(self.walls_sprite)

    def update_walls_speed(self):

        if self.space_pressed:
            print("Walls updated!")
            # Calculate speed based on the keys pressed
            ##self.walls_sprite.change_x += 100
            if self.space_pressed:
                self.walls_sprite.change_x += -MOVEMENT_SPEED
                self.space_pressed = False

    def on_draw(self):
        """ Draw everything """
        arcade.start_render()
        self.walls_list.draw()

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        if key == arcade.key.SPACE:
            self.game_started = True
            self.space_pressed = True
            print("pressed!")

    def update(self, delta_time):
        if self.game_started:
            """ Movement and game logic """
            # moving the walls
            self.walls_list.update()


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
