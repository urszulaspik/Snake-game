import arcade
from arcade.gui import UIManager
import buttons
from settings import *
import results_read
import pandas as pd


class ResultView(arcade.View):
    """ Class with result level 1 view """

    def __init__(self, user):
        """
        Create view
        :param user: (arcade.gui.UIInputBox) input with user name
        """
        super().__init__()
        self.texture = arcade.load_texture(BACKGROUNDS["result1"])
        self.ui_manager = UIManager()
        self.user = user

    def on_draw(self):
        """ Draw this view """
        arcade.start_render()
        self.texture.draw_sized(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                                SCREEN_WIDTH, SCREEN_HEIGHT)
        arcade.draw_rectangle_outline(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 25, SCREEN_WIDTH - 50,
                                      3 * SCREEN_HEIGHT / 5, arcade.color.BLACK)
        arcade.draw_line(175, 95, 175, 455, arcade.color.BLACK)
        arcade.draw_text("Lp.", 50, 435, arcade.color.BLACK, 20, anchor_x="center", anchor_y="center", align="center")
        arcade.draw_text("Points", 125, 435, arcade.color.BLACK, 20, anchor_x="center", anchor_y="center",
                         align="center")
        arcade.draw_text("Name", 250, 435, arcade.color.BLACK, 20, anchor_x="center", anchor_y="center", align="center")
        arcade.draw_text("Date", 400, 435, arcade.color.BLACK, 20, anchor_x="center", anchor_y="center", align="center")
        for index, row in pd.read_csv(RESULTS["level1"]).iterrows():
            arcade.draw_text(f"{index + 1}.", 50, 399 - index * 32, arcade.color.BLACK, 18, anchor_x="center",
                             anchor_y="center", align="center")
            arcade.draw_text(str(row["points"]), 125, 399 - index * 32, arcade.color.BLACK, 18, anchor_x="center",
                             anchor_y="center", align="center")
            arcade.draw_text(str(row["user"]), 250, 399 - index * 32, arcade.color.BLACK, 18, width=145,
                             anchor_x="center", anchor_y="center", align="center")
            arcade.draw_text(str(row["date"]), 400, 399 - index * 32, arcade.color.BLACK, 18, width=145,
                             anchor_x="center", anchor_y="center", align="center")

        arcade.draw_line(75, 95, 75, 455, arcade.color.BLACK)
        arcade.draw_line(325, 95, 325, 455, arcade.color.BLACK)
        for i in range(10):
            arcade.draw_line(25, 415 - i * 32, 475, 415 - i * 32, arcade.color.BLACK)

    def on_hide_view(self):
        """Called when this view is not shown anymore"""
        self.ui_manager.unregister_handlers()

    def on_show_view(self):
        """Called when this view is shown"""
        self.setup()

    def setup(self):
        """ Set up this view. """
        self.ui_manager.purge_ui_elements()
        y_slot = self.window.height // 12
        results_read.exist_result(RESULTS["level1"])
        button = buttons.MenuButton(
            'Menu',
            center_x=self.window.width // 4,
            center_y=y_slot * 1,
            width=200,
            user=self.user.text
        )
        button.set_style_attrs(
            bg_color=(173, 213, 79),
            bg_color_hover=(186, 229, 85),
            bg_color_press=(149, 182, 73),
        )
        self.ui_manager.add_ui_element(button)

        button = buttons.Result2Button(
            'Level 2',
            center_x=3 * self.window.width // 4,
            center_y=y_slot * 1,
            width=200,
            user=self.user
        )
        button.set_style_attrs(
            bg_color=(173, 213, 79),
            bg_color_hover=(186, 229, 85),
            bg_color_press=(149, 182, 73),
        )
        self.ui_manager.add_ui_element(button)


class ResultView2(arcade.View):
    """ Class with result level 2 view """

    def __init__(self, user):
        """
        Create view
        :param user: (arcade.gui.UIInputBox) input with user name
        """
        super().__init__()
        self.texture = arcade.load_texture(BACKGROUNDS["result2"])
        self.ui_manager = UIManager()
        self.user = user

    def on_draw(self):
        """ Draw this view """
        arcade.start_render()
        self.texture.draw_sized(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                                SCREEN_WIDTH, SCREEN_HEIGHT)
        arcade.draw_rectangle_outline(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 25, SCREEN_WIDTH - 50,
                                      3 * SCREEN_HEIGHT / 5, arcade.color.BLACK)
        arcade.draw_line(175, 95, 175, 455, arcade.color.BLACK)
        arcade.draw_text("Lp.", 50, 435, arcade.color.BLACK, 20, anchor_x="center", anchor_y="center", align="center")
        arcade.draw_text("Points", 125, 435, arcade.color.BLACK, 20, anchor_x="center", anchor_y="center",
                         align="center")
        arcade.draw_text("Name", 250, 435, arcade.color.BLACK, 20, anchor_x="center", anchor_y="center", align="center")
        arcade.draw_text("Date", 400, 435, arcade.color.BLACK, 20, anchor_x="center", anchor_y="center", align="center")
        for index, row in pd.read_csv(RESULTS["level2"]).iterrows():
            arcade.draw_text(f"{index + 1}.", 50, 399 - index * 32, arcade.color.BLACK, 18, anchor_x="center",
                             anchor_y="center", align="center")
            arcade.draw_text(str(row["points"]), 125, 399 - index * 32, arcade.color.BLACK, 18, anchor_x="center",
                             anchor_y="center", align="center")
            arcade.draw_text(str(row["user"]), 250, 399 - index * 32, arcade.color.BLACK, 18, width=145,
                             anchor_x="center", anchor_y="center", align="center")
            arcade.draw_text(str(row["date"]), 400, 399 - index * 32, arcade.color.BLACK, 18, width=145,
                             anchor_x="center", anchor_y="center", align="center")

        arcade.draw_line(75, 95, 75, 455, arcade.color.BLACK)
        arcade.draw_line(325, 95, 325, 455, arcade.color.BLACK)
        for i in range(10):
            arcade.draw_line(25, 415 - i * 32, 475, 415 - i * 32, arcade.color.BLACK)

    def on_hide_view(self):
        """Called when this view is not shown anymore"""
        self.ui_manager.unregister_handlers()

    def on_show_view(self):
        """Called when this view is shown"""
        self.setup()

    def setup(self):
        """ Set up this view. """
        self.ui_manager.purge_ui_elements()
        y_slot = self.window.height // 12
        results_read.exist_result(RESULTS["level2"])
        button = buttons.MenuButton(
            'Menu',
            center_x=self.window.width // 4,
            center_y=y_slot * 1,
            width=200,
            user=self.user.text
        )
        button.set_style_attrs(
            bg_color=(173, 213, 79),
            bg_color_hover=(186, 229, 85),
            bg_color_press=(149, 182, 73),
        )
        self.ui_manager.add_ui_element(button)

        button = buttons.ResultButton(
            'Level 1',
            center_x=3 * self.window.width // 4,
            center_y=y_slot * 1,
            width=200,
            user=self.user
        )
        button.set_style_attrs(
            bg_color=(173, 213, 79),
            bg_color_hover=(186, 229, 85),
            bg_color_press=(149, 182, 73),
        )
        self.ui_manager.add_ui_element(button)
