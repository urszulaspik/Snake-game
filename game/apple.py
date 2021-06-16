import arcade
import random


class Apple(arcade.Sprite):
    """Class with apple - snake's food"""

    def new_apple(self, screen_width: int, screen_hight: int, snake_thick: int, coord: arcade.SpriteList,
                  coord2: arcade.SpriteList = arcade.SpriteList()):
        '''
        Find new coordinates for apple, that do not collide with any other sprite
        :param screen_width: (int) width of screen with game
        :param screen_hight: (int) hight of screen with game
        :param snake_thick: (int) size of the snake's break
        :param coord: (arcade.SpriteList) list of opposits spirits
        :param coord2: (arcade.SpriteList) second list of opposits spirits 
        '''
        self.center_x = round(random.randrange(0, screen_width - snake_thick) / snake_thick) * snake_thick
        self.center_y = round(random.randrange(0, screen_hight - snake_thick) / snake_thick) * snake_thick
        while (arcade.check_for_collision_with_list(self, coord) != []) or (arcade.check_for_collision_with_list(self, coord2) != []) or self.center_x in (0, 500) or self.center_y in (0, 500):
            self.center_x = round(random.randrange(0, screen_width - snake_thick) / snake_thick) * snake_thick
            self.center_y = round(random.randrange(0, screen_hight - snake_thick) / snake_thick) * snake_thick

    def eating(self, x: float, y: float):
        '''
        Check if apple will be eaten
        :param x: (float) first coordinate of snake's head
        :param y: (float) second coordinate of snake's head
        :return: (bool) True - yes, False - no
        '''
        if self.center_x == x and self.center_y == y:
            return True
        else:
            return False

    def new_apple_ate(self, screen_width: float, screen_hight: float, snake_thick: int, x: float, y: float,
                      coord: arcade.SpriteList, coord2: arcade.SpriteList = arcade.SpriteList()):
        '''
        If apple will be eaten, find apple's new coorinates, that do not collide with any other sprite
        :param screen_width: (float) width of screen with game
        :param screen_hight: (float) hight of screen with game
        :param snake_thick: (int) size of the snake's break
        :param x: (float) first coordinate of snake's head
        :param y: (float) second coordinate of snake's head
        :param coord: (arcade.SpriteList) list of opposits spirits
        :param coord2: (arcade.SpriteList) second list of opposits spirits
        :return: (bool) True - yes, False - no
        '''
        if self.eating(x, y) == True:
            self.new_apple(screen_width, screen_hight, snake_thick, coord, coord2)
            return True
        return False
