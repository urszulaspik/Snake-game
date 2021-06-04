import arcade

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

class SnakeHead(arcade.Sprite):

    def __init__(self):
        super().__init__()

        self.scale = 0.5
        self.textures = []
        texture = arcade.load_texture("snake_head_top.png")
        self.textures.append(texture)
        texture = arcade.load_texture("snake_head_bottom.png")
        self.textures.append(texture)
        texture = arcade.load_texture("snake_head_right.png")
        self.textures.append(texture)
        texture = arcade.load_texture("snake_head_left.png")
        self.textures.append(texture)
        self.texture = texture

    def update(self):
        if self.change_y > 0:
            self.texture = self.textures[0]
        elif self.change_y < 0:
            self.texture = self.textures[1]
        elif self.change_x > 0:
            self.texture = self.textures[2]
        elif self.change_x <= 0:
            self.texture = self.textures[3]

        '''if self.center_x + 25 < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH - 25:
            self.right = SCREEN_WIDTH - 25

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > SCREEN_HEIGHT - 25:
            self.top = SCREEN_HEIGHT - 25'''

class SnakeBody(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.scale = 0.5
        self.texture = arcade.load_texture("snake_body.png")

class Snake:
    def __init__(self, screen_width, screen_hight):
        self.center_x = screen_width / 2
        self.center_y = screen_hight / 2
        self.change_x = 0
        self.change_y = 0
        self.next = False
        self.length_snake = 1
        self.coord_list = [(screen_width / 2, screen_hight / 2)]
        self.head_posx = 0
        self.head_posy = 0
        self.dead = False

    def update(self):
        """ Move the player """
        self.center_x += self.change_x
        self.center_y += self.change_y
        self.head_posx = self.change_x
        self.head_posy = self.change_y
        self.coord_list.append((self.center_x, self.center_y))
        if len(self.coord_list) > self.length_snake:
            del self.coord_list[0]
        if self.next == True:
            self.length_snake += 1
        if self.coord_list[-1] in self.coord_list[:-1]:
            self.dead = True

        # Check for out-of-bounds
        #if self.center_x + 25 < 0:
        #    self.left = 0
        #elif self.right > SCREEN_WIDTH - 1:
        #    self.right = SCREEN_WIDTH - 1

        #if self.bottom < 0:
        #    self.bottom = 0
        #elif self.top > SCREEN_HEIGHT - 1:
        #    self.top = SCREEN_HEIGHT - 1
    
    def snake_body(self):
        full_snake = arcade.SpriteList()
        head = SnakeHead()
        head.center_x = self.coord_list[-1][0]
        head.center_y = self.coord_list[-1][1]
        head.change_x = self.head_posx
        head.change_y = self.head_posy
        head.update()
        full_snake.append(head)
        for i in self.coord_list[0:-1]:
            body = SnakeBody()
            body.center_x = i[0]
            body.center_y = i[1]
            full_snake.append(body)
        return full_snake
