import arcade
import random


class Apple(arcade.Sprite):
    def new_apple(self, screen_width, screen_hight, snake_thick, coord):
        x = round(random.randrange(0, screen_width - snake_thick) / snake_thick) * snake_thick
        y = round(random.randrange(0, screen_hight - snake_thick) / snake_thick) * snake_thick
        while (x, y) in coord or x in (0, 500) or y in (0, 500):
            x = round(random.randrange(0, screen_width - snake_thick) / snake_thick) * snake_thick
            y = round(random.randrange(0, screen_hight - snake_thick) / snake_thick) * snake_thick
        self.center_x = x
        self.center_y = y

    def update(self):
        self.center_x = self.new_apple[0]
        self.center_y = self.new_apple[1]
    
    def eating(self, x, y):
        if self.center_x == x and self.center_y == y:
            return True
        else:
            return False

    def new_apple_ate(self, screen_width, screen_hight, snake_thick, x, y, coord):
        if self.eating(x, y) == True:
            self.new_apple(screen_width, screen_hight, snake_thick, coord)
            return True
        