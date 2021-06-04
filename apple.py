import arcade
import random

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

class Apple(arcade.Sprite):
    def new_apple2(self, screen_width, screen_hight, snake_thick):
        #if self.eating == True:
        x = round(random.randrange(0, screen_width - snake_thick) / snake_thick) * snake_thick #cos jest nie tak
        y = round(random.randrange(0, screen_hight - snake_thick) / snake_thick) * snake_thick #cos jest nie tak
        return (x, y)

    def update(self):
        self.center_x = self.new_apple[0]
        self.center_y = self.new_apple[1]

        '''if self.center_x + 25 < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH - 25:
            self.right = SCREEN_WIDTH - 25

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > SCREEN_HEIGHT - 25:
            self.top = SCREEN_HEIGHT - 25'''
    
    def eating(self, x, y):
        if self.center_x == x and self.center_y == y:
            return True
        else:
            return False

    def new_apple(self, screen_width, screen_hight, snake_thick, x, y):
        if self.eating(x, y) == True:
            self.center_x = round(random.randrange(0, screen_width - snake_thick) / snake_thick) * snake_thick #cos jest nie tak
            self.center_y = round(random.randrange(0, screen_hight - snake_thick) / snake_thick) * snake_thick #cos jest nie tak
            return True
        