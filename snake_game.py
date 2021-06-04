import arcade
import snake_class
import apple

SPRITE_SCALING = 0.5

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
SCREEN_TITLE = "Snake"

MOVEMENT_SPEED = 25


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title)
        super().set_update_rate(1 / 4)
        self.direction_list = [False, False, False, False]
        arcade.set_background_color(arcade.color.BANANA_MANIA)

    def setup(self):
        """ Set up the game and initialize the variables. """
        self.snake = snake_class.SnakeHead()
        #self.snake = snake_class.Snake()
        self.snake.center_x = SCREEN_WIDTH / 2
        self.snake.center_y = SCREEN_HEIGHT / 2
        self.apple = apple.Apple("myapple.png", SPRITE_SCALING)
        coord = self.apple.new_apple2(SCREEN_WIDTH, SCREEN_HEIGHT, MOVEMENT_SPEED)
        self.apple.center_x = coord[0]
        self.apple.center_y = coord[1]

    def on_draw(self):
        """
        Render the screen.
        """
        arcade.start_render()

        self.apple.draw()
        self.snake.draw()


    def on_update(self, delta_time):
        """ Movement and game logic """
        self.snake.change_x = 0
        self.snake.change_y = 0
        self.apple.new_apple(SCREEN_WIDTH, SCREEN_HEIGHT, MOVEMENT_SPEED, self.snake.center_x, self.snake.center_y)
        if self.direction_list[0]:
            self.snake.change_y = MOVEMENT_SPEED
        elif self.direction_list[1]:
            self.snake.change_y = -MOVEMENT_SPEED
        elif self.direction_list[2]:
            self.snake.change_x = -MOVEMENT_SPEED
        elif self.direction_list[3]:
            self.snake.change_x = MOVEMENT_SPEED

        self.snake.update()

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.direction_list = list(map(lambda x: False, self.direction_list))
            self.direction_list[0] = True
        elif key == arcade.key.DOWN:
            self.direction_list = list(map(lambda x: False, self.direction_list))
            self.direction_list[1] = True
        elif key == arcade.key.LEFT:
            self.direction_list = list(map(lambda x: False, self.direction_list))
            self.direction_list[2] = True
        elif key == arcade.key.RIGHT:
            self.direction_list = list(map(lambda x: False, self.direction_list))
            self.direction_list[3] = True


def main():
    """ Main method """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.schedule(window.on_update, 40)
    arcade.run()


if __name__ == "__main__":
    main()