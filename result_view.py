import arcade
from arcade.gui import UIManager
import buttons
from settings import *
#import snake_game
import results_read
import pandas as pd

class ResultView(arcade.View):
    """ View to show when game is over """

    def __init__(self):
        """ This is run once when we switch to this view """
        super().__init__()
        self.texture = arcade.load_texture("asserts/image/result1.png")
        self.ui_manager = UIManager()

    def on_draw(self):
        """ Draw this view """
        arcade.start_render()
        self.texture.draw_sized(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                                SCREEN_WIDTH, SCREEN_HEIGHT)
        arcade.draw_rectangle_outline(SCREEN_WIDTH/2, SCREEN_HEIGHT/2-25, SCREEN_WIDTH-50, 3*SCREEN_HEIGHT/5, arcade.color.BLACK)
        arcade.draw_line(175, 95, 175, 455, arcade.color.BLACK)
        #for count, i in enumerate(results_read.reading("result_level1.csv")):
        #results_read.exist_result("result_level1.csv")
        for index, row in pd.read_csv("result_level1.csv").iterrows():
            arcade.draw_text(f"{index+1}.", 50, 437-index*36, arcade.color.BLACK, 18, anchor_x="center", anchor_y="center", align="center")
            arcade.draw_text(str(row["points"]), 125, 437-index*36, arcade.color.BLACK, 18, anchor_x="center", anchor_y="center", align="center")
            arcade.draw_text(str(row["user"]), 175, 437-index*36, arcade.color.BLACK, 18, width= 150, anchor_x="left", anchor_y="center", align="center")
            arcade.draw_text(str(row["date"]), 325, 437-index*36, arcade.color.BLACK, 18, width= 150, anchor_x="left", anchor_y="center", align="center")
        
        arcade.draw_line(75, 95, 75, 455, arcade.color.BLACK)
        arcade.draw_line(325, 95, 325, 455, arcade.color.BLACK)
        for i in range(10):
            arcade.draw_line(25, 419-i*36, 475, 419-i*36, arcade.color.BLACK)

    def on_hide_view(self):
        self.ui_manager.unregister_handlers()
    
    def on_show_view(self):
        self.setup()

    def setup(self):
        """ Set up this view. """
        self.ui_manager.purge_ui_elements()
        y_slot = self.window.height // 12
        results_read.exist_result("result_level1.csv")
        button = buttons.MenuButton(
            'Menu',
            center_x=self.window.width // 4,
            center_y=y_slot * 1,
            width=200,
        )
        self.ui_manager.add_ui_element(button)

        button = buttons.Result2Button(
            'Level 2',
            center_x=3*self.window.width // 4,
            center_y=y_slot * 1,
            width=200,
        )
        self.ui_manager.add_ui_element(button)

class ResultView2(arcade.View):
    """ View to show when game is over """

    def __init__(self):
        """ This is run once when we switch to this view """
        super().__init__()
        self.texture = arcade.load_texture("asserts/image/result2.png")
        self.ui_manager = UIManager()

    def on_draw(self):
        """ Draw this view """
        arcade.start_render()
        self.texture.draw_sized(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                                SCREEN_WIDTH, SCREEN_HEIGHT)
        arcade.draw_rectangle_outline(SCREEN_WIDTH/2, SCREEN_HEIGHT/2-25, SCREEN_WIDTH-50, 3*SCREEN_HEIGHT/5, arcade.color.BLACK)
        arcade.draw_line(175, 95, 175, 455, arcade.color.BLACK)
        for index, row in pd.read_csv("result_level2.csv").iterrows():
            arcade.draw_text(f"{index+1}.", 50, 437-index*36, arcade.color.BLACK, 18, anchor_x="center", anchor_y="center", align="center")
            arcade.draw_text(str(row["points"]), 125, 437-index*36, arcade.color.BLACK, 18, anchor_x="center", anchor_y="center", align="center")
            arcade.draw_text(str(row["user"]), 175, 437-index*36, arcade.color.BLACK, 18, width= 150, anchor_x="left", anchor_y="center", align="center")
            arcade.draw_text(str(row["date"]), 325, 437-index*36, arcade.color.BLACK, 18, width= 150, anchor_x="left", anchor_y="center", align="center")
        
        arcade.draw_line(75, 95, 75, 455, arcade.color.BLACK)
        arcade.draw_line(325, 95, 325, 455, arcade.color.BLACK)
        for i in range(10):
            arcade.draw_line(25, 419-i*36, 475, 419-i*36, arcade.color.BLACK)

    def on_hide_view(self):
        self.ui_manager.unregister_handlers()
    
    def on_show_view(self):
        self.setup()

    def setup(self):
        """ Set up this view. """
        self.ui_manager.purge_ui_elements()
        y_slot = self.window.height // 12
        results_read.exist_result("result_level2.csv")
        button = buttons.MenuButton(
            'Menu',
            center_x=self.window.width // 4,
            center_y=y_slot * 1,
            width=200,
        )
        self.ui_manager.add_ui_element(button)

        button = buttons.ResultButton(
            'Level 1',
            center_x=3*self.window.width // 4,
            center_y=y_slot * 1,
            width=200,
        )
        self.ui_manager.add_ui_element(button)