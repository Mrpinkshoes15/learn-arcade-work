import random
import arcade

SPRITE_SCALING = 0.5

DEFAULT_SCREEN_WIDTH = 800
DEFAULT_SCREEN_HEIGHT = 500
SCREEN_TITLE = "flappy Plane"

class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title, resizable=True)

        # Sprite lists
        self.player_list = None
        self.ostical_list = None

        self.all_sprites_list = None

        # list for wall blocks
        self.multiples_of_64_list = [320, 384, 448, 512]
        self.score = 0
        # Set up the player
        self.player_sprite = None

        # Physics engine so we don't run into walls.
        self.physics_engine = None

        # Track the current state of what key is pressed
        self.space_pressed = False


        # Create the cameras. One for the GUI, one for the sprites.

        # We scroll the 'sprite world' but not the GUI.


    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.ostical_list = arcade.SpriteList()
        self.all_sprites_list = arcade.SpriteList()

        # Set up the player
        self.player_sprite = arcade.Sprite("piderman.png",
                                           scale=0.04)
        self.player_sprite.center_x = 40
        self.player_sprite.center_y = 40
        self.player_list.append(self.player_sprite)

        ### Set up walls with random empty spaces
        for y in range(136, 1650, 128):
            for x in range(0, 2560, 64):
                # Randomly skip a box so the player can find a way through
                if random.randrange(5) > 0:
                    wall = arcade.Sprite(":resources:images/tiles/brickGrey.png", SPRITE_SCALING)
                    wall.center_x = x
                    wall.center_y = y
                    self.ostical_list.append(wall)
        # makes random choice based on a list
        # creates random path blockers
        c = random.choice(self.multiples_of_64_list)
        for y in range(200, 1650, c):
            for x in range(192, 2560, c):
                wall = arcade.Sprite(":resources:images/tiles/brickTextureWhite.png", SPRITE_SCALING)
                wall.center_x = x
                wall.center_y = y
                self.ostical_list.append(wall)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.ostical_list)

        ### left and right boarders
        for side_boarders_y in range(8, 1694, 64):
            for side_position_x in range(-64, 2528, 2560):
                side_boarder = arcade.Sprite("kekw.png", 0.1)
                side_boarder.center_x = side_position_x
                side_boarder.center_y = side_boarders_y
                self.ostical_list.append(side_boarder)

        ## top and bottom boarders
        for top_boarders_x in range(0, 2560, 64):
            for top_position_y in range(8, 1694, 1664):
                top_boarder = arcade.Sprite("kekw.png", 0.1)
                top_boarder.center_x = top_boarders_x
                top_boarder.center_y = top_position_y
                self.ostical_list.append(top_boarder)


        arcade.set_background_color(arcade.color.BLACK_BEAN)

    def on_draw(self):
        """ Render the screen. """

        # This command has to happen before we start drawing
        self.clear()

        # Select the camera we'll use to draw all our sprites

        self.camera_sprites.use()

        # Draw all the sprites.
        self.ostical_list.draw()
        self.player_list.draw()
        self.coin_list.draw()

        # Select the (unscrolled) camera for our GUI

        self.camera_gui.use()

        # Draw the GUI
        # arcade.draw_rectangle_filled(self.width // 2,
        #                              20,
        #                              self.width,
        #                              40,
        #                              arcade.color.ALMOND)
        # text = f"Scroll value: ({self.camera_sprites.position[0]:5.1f}, " \
        #        f"{self.camera_sprites.position[1]:5.1f})"
        # arcade.draw_text(text, 10, 10, arcade.color.BLACK_BEAN, 20)
        output = f"Score: {self.score}"
        arcade.draw_text(output, 400, 270, arcade.color.WHITE, 18)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.SPACE:
            self.up_pressed = True

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.SPACE:
            self.up_pressed = False

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Calculate speed based on the keys pressed
        self.player_sprite.change_x = 0
        self.player_sprite.change_y = 0


        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.physics_engine.update()

        ### scoring
        coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                              self.coin_list)

        # Loop through each colliding sprite, remove it, and add to the score.
        for coin in coins_hit_list:
            coin.remove_from_sprite_lists()
            self.score += 10



    def main():
        """ Main function """
        window = MyGame(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT, SCREEN_TITLE)
        window.setup()
        arcade.run()

    if __name__ == "__main__":
        main()