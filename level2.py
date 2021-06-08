import arcade
import snake_class
import apple
import game_over
from settings import *

class MyGame2(arcade.View):
    """
    Main application class.
    """

    def __init__(self, user):
        """
        Initializer
        """
        super().__init__()
        self.direction_list = [False, False, False, False]
        self.background = None
        self.live = 3
        self.user = user
        self.all = arcade.SpriteList()

    def setup(self):
        """ Set up the game and initialize the variables. """
        self.snake = snake_class.Snake(GAME_WIDTH / 2, GAME_HEIGHT / 2)
        self.apple = apple.Apple(APPLE["good_apple"], 0.5)
        self.apple.new_apple(GAME_WIDTH, GAME_HEIGHT, MOVEMENT_SPEED, self.snake.snake_body())
        self.all.append(self.apple)
        self.black_apple = apple.Apple(APPLE["bad_apple"], 0.5)
        self.black_apple.new_apple(GAME_WIDTH, GAME_HEIGHT, MOVEMENT_SPEED, self.snake.snake_body(), self.all)
        self.all.append(self.black_apple)
        self.background = arcade.load_texture(BACKGROUNDS["game"])
        self.heart_list = arcade.SpriteList()
        for i in range(self.live):
            heart = arcade.Sprite(HEART["heart"], 1)
            heart.center_x = 465 -i*60
            heart.center_y = 550
            self.heart_list.append(heart)
        self.rotten_list = arcade.SpriteList()
        for i in range(5):
            rotten = apple.Apple(APPLE["rotten_apple"], 0.5)
            rotten.new_apple(GAME_WIDTH, GAME_HEIGHT, MOVEMENT_SPEED, self.snake.snake_body(), self.all)
            self.all.append(rotten)
            self.rotten_list.append(rotten)

    def on_draw(self):
        """
        Render the screen.
        """
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0,
                                           SCREEN_WIDTH, SCREEN_HEIGHT,
                                           self.background)

        self.apple.draw()
        self.black_apple.draw()
        self.rotten_list.draw()
        self.snake.snake_body().draw()
        arcade.draw_rectangle_outline(GAME_WIDTH/2, GAME_HEIGHT/2, GAME_WIDTH-25, GAME_HEIGHT-25, arcade.color.BLACK)

        output = f"Score: {self.snake.score}"
        arcade.draw_text(output, 16, 540, arcade.color.BLACK, 25)
        self.heart_list.draw()

    def rotten_check(self):
        for i in self.rotten_list:
            if self.snake.center_x == i.center_x and self.snake.center_y == i.center_y:
                i.remove_from_sprite_lists()
                return True
        return False

    def heart_lose(self):
        if self.live > 1:
            self.heart_list.pop()
            self.live -= 1
            arcade.play_sound(SOUNDS["heart"])
        else: 
            self.snake.dead = True

    def on_update(self, delta_time):
        """ Movement and game logic """
        self.snake.change_x = 0
        self.snake.change_y = 0
        if self.apple.new_apple_ate(GAME_WIDTH, GAME_HEIGHT, MOVEMENT_SPEED, self.snake.center_x, self.snake.center_y, self.snake.snake_body(), self.all):
            arcade.play_sound(SOUNDS["eat"])
            self.black_apple.new_apple(GAME_WIDTH, GAME_HEIGHT, MOVEMENT_SPEED, self.snake.snake_body(), self.all)
            self.snake.next = True
        if self.black_apple.new_apple_ate(GAME_WIDTH, GAME_HEIGHT, MOVEMENT_SPEED, self.snake.center_x, self.snake.center_y, self.snake.snake_body(), self.all):
            self.heart_lose()
        if self.rotten_check():
            self.heart_lose()
        if self.direction_list[0]:
            self.snake.change_y = MOVEMENT_SPEED
        elif self.direction_list[1]:
            self.snake.change_y = -MOVEMENT_SPEED
        elif self.direction_list[2]:
            self.snake.change_x = -MOVEMENT_SPEED
        elif self.direction_list[3]:
            self.snake.change_x = MOVEMENT_SPEED

        self.snake.update()
        #self.all.update()
        self.snake.next = False
        if self.snake.dead == True:
            arcade.play_sound(SOUNDS["dead"])
            view = game_over.GameOverView2(self.snake.score, self.user)
            self.window.show_view(view)
        if self.snake.bad_direction == True:
            self.before_direction()
            self.snake.bad_direction = False

    def before_direction(self):
        index = self.direction_list.index(True)
        self.direction_list[index] = False
        if index == 0:
            self.direction_list[1] = True
        elif index == 1:
            self.direction_list[0] = True
        elif index == 2:
            self.direction_list[3] = True       
        elif index == 3:
            self.direction_list[2] = True 

    def direction_changer(self, index):
        self.direction_list = list(map(lambda x: False, self.direction_list))
        self.direction_list[index] = True

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.direction_changer(0)
        elif key == arcade.key.DOWN:
            self.direction_changer(1)
        elif key == arcade.key.LEFT:
            self.direction_changer(2)
        elif key == arcade.key.RIGHT:
            self.direction_changer(3)