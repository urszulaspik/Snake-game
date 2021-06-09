import arcade
from settings import *


class SnakeHead(arcade.Sprite):
    """Class with head of snake"""

    def __init__(self):
        super().__init__()

        self.scale = 0.5
        self.textures = []
        texture = arcade.load_texture(SNAKEBODY["head_top"])
        self.textures.append(texture)
        texture = arcade.load_texture(SNAKEBODY["head_bottom"])
        self.textures.append(texture)
        texture = arcade.load_texture(SNAKEBODY["head_right"])
        self.textures.append(texture)
        texture = arcade.load_texture(SNAKEBODY["head_left"])
        self.textures.append(texture)
        self.texture = texture

    def update(self):
        """Update the sprite."""
        if self.change_y > 0:
            self.texture = self.textures[0]
        elif self.change_y < 0:
            self.texture = self.textures[1]
        elif self.change_x > 0:
            self.texture = self.textures[2]
        elif self.change_x <= 0:
            self.texture = self.textures[3]


class Snake:
    """Class with full snake with head and body"""

    def __init__(self, screen_width, screen_hight):
        """
        Create snake
        :param screen_width: (float) width of screen with game
        :param screen_hight:(float) hight of screen with game
        """
        self.center_x = screen_width / 2
        self.center_y = screen_hight / 2
        self.change_x = 0
        self.change_y = 0
        self.length_snake = 1
        self.coord_list = [(screen_width / 2, screen_hight / 2)]
        self.head_posx = 0
        self.head_posy = 0
        self.score = 0
        self.dead = False
        self.next = False
        self.bad_direction = False

    def dead_check(self):
        '''Check if snake is dead'''
        if self.coord_list[-1] in self.coord_list[:-2]:
            self.dead = True
        if self.coord_list[-1][0] in (0, 500) or self.coord_list[-1][1] in (0, 500):
            self.dead = True

    def direction_check(self):
        """Check if direction is correct"""
        if self.length_snake != 1 and self.coord_list[-1] == self.coord_list[-3]:
            self.bad_direction = True
            del self.coord_list[-1]
            self.center_x -= self.change_x
            self.center_y -= self.change_y
        else:
            self.head_posx = self.change_x
            self.head_posy = self.change_y

    def eat_check(self):
        """Check if snake ate red apple"""
        if self.next:
            self.length_snake += 1
            self.score += 1

    def update(self):
        """ Move the snake """
        self.center_x += self.change_x
        self.center_y += self.change_y
        self.coord_list.append((self.center_x, self.center_y))
        self.direction_check()
        self.eat_check()
        if len(self.coord_list) > self.length_snake:
            del self.coord_list[0]
        self.dead_check()

    def snake_body(self):
        """
        Create snake full body
        :return: (arcade.SpriteList) list with body elements
        """
        full_snake = arcade.SpriteList()
        head = SnakeHead()
        head.center_x = self.coord_list[-1][0]
        head.center_y = self.coord_list[-1][1]
        head.change_x = self.head_posx
        head.change_y = self.head_posy
        head.update()
        full_snake.append(head)
        for i in self.coord_list[:-1]:
            body = arcade.Sprite(SNAKEBODY["body"], head.scale)
            body.center_x = i[0]
            body.center_y = i[1]
            full_snake.append(body)
        return full_snake
