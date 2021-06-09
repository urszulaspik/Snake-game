import arcade
from arcade.gui import UIManager
import buttons
from settings import *


class StartView(arcade.View):
    """ Class with start view """

    def __init__(self, name: str = "User Name"):
        """
        Create view
        :param name: (str) user name
        """
        super().__init__()
        self.texture = arcade.load_texture(BACKGROUNDS["start"])
        self.ui_manager = UIManager()
        self.name = name

    def on_draw(self):
        """ Draw this view """
        arcade.start_render()
        self.texture.draw_sized(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                                SCREEN_WIDTH, SCREEN_HEIGHT)

    def on_hide_view(self):
        """Called when this view is not shown anymore"""
        self.ui_manager.unregister_handlers()

    def on_show_view(self):
        """Called when this view is shown"""
        self.setup()

    def setup(self):
        """ Set up this view, create buttons """
        self.ui_manager.purge_ui_elements()
        y_slot = self.window.height // 12

        ui_input_box = arcade.gui.UIInputBox(
            center_x=self.window.width // 2,
            center_y=y_slot * 7,
            width=250
        )
        ui_input_box.set_style_attrs(
            bg_color=(66, 179, 208),
            bg_color_hover=(112, 212, 238),
            bg_color_focus=(255, 228, 14)
        )
        ui_input_box.text = self.name
        ui_input_box.cursor_index = len(ui_input_box.text)
        self.ui_manager.add_ui_element(ui_input_box)

        button = buttons.ExitButton(
            'Exit',
            center_x=self.window.width // 2,
            center_y=y_slot * 1,
            width=250
        )
        button.set_style_attrs(
            bg_color=(51, 139, 57),
            bg_color_hover=(135, 21, 25),
            bg_color_press=(122, 21, 24),
        )
        self.ui_manager.add_ui_element(button)

        button = buttons.AuthorButton("Author",
                                      center_x=self.window.width // 2,
                                      center_y=y_slot * 2,
                                      width=250,
                                      user=ui_input_box
                                      )
        button.set_style_attrs(
            bg_color=(51, 139, 57),
            bg_color_hover=(88, 196, 96),
            bg_color_press=(28, 71, 32),
        )
        self.ui_manager.add_ui_element(button)

        button = buttons.ResultButton("Results",
                                      center_x=self.window.width // 2,
                                      center_y=y_slot * 3,
                                      width=250,
                                      user=ui_input_box
                                      )
        button.set_style_attrs(
            bg_color=(51, 139, 57),
            bg_color_hover=(88, 196, 96),
            bg_color_press=(28, 71, 32),
        )
        self.ui_manager.add_ui_element(button)

        button = buttons.RulesButton("Rules",
                                     center_x=self.window.width // 2,
                                     center_y=y_slot * 4,
                                     width=250,
                                     user=ui_input_box
                                     )
        button.set_style_attrs(
            bg_color=(51, 139, 57),
            bg_color_hover=(88, 196, 96),
            bg_color_press=(28, 71, 32),
        )
        self.ui_manager.add_ui_element(button)

        button = buttons.Level1Button("Play level 1",
                                      center_x=self.window.width // 2,
                                      center_y=y_slot * 6,
                                      width=250,
                                      user=ui_input_box
                                      )
        button.set_style_attrs(
            bg_color=(51, 139, 57),
            bg_color_hover=(88, 196, 96),
            bg_color_press=(28, 71, 32),
        )
        self.ui_manager.add_ui_element(button)

        button = buttons.Level2Button("Play level 2",
                                      center_x=self.window.width // 2,
                                      center_y=y_slot * 5,
                                      width=250,
                                      user=ui_input_box
                                      )
        button.set_style_attrs(
            bg_color=(51, 139, 57),
            bg_color_hover=(88, 196, 96),
            bg_color_press=(28, 71, 32),
        )
        self.ui_manager.add_ui_element(button)


class AuthorView(arcade.View):
    """ Class with about author view """

    def __init__(self, user: arcade.gui.UIInputBox):
        """
        Create view
        :param user: (arcade.gui.UIInputBox) input with user name
        """
        super().__init__()
        self.texture = arcade.load_texture(BACKGROUNDS["author"])
        self.ui_manager = UIManager()
        self.user = user

    def on_draw(self):
        """ Draw this view """
        arcade.start_render()
        self.texture.draw_sized(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                                SCREEN_WIDTH, SCREEN_HEIGHT)

    def on_hide_view(self):
        """Called when this view is not shown anymore"""
        self.ui_manager.unregister_handlers()

    def on_show_view(self):
        """Called when this view is shown"""
        self.setup()

    def setup(self):
        """ Set up this view, create buttons"""
        self.ui_manager.purge_ui_elements()

        button = buttons.MenuButton(
            'Menu',
            center_x=self.window.width // 2,
            center_y=self.window.height // 6,
            width=200,
            user=self.user.text
        )
        button.set_style_attrs(
            bg_color=(255, 153, 204),
            bg_color_hover=(255, 102, 178),
            bg_color_press=(204, 0, 102),
        )
        self.ui_manager.add_ui_element(button)


class RulesView(arcade.View):
    """ Class with rules view """

    def __init__(self, user: arcade.gui.UIInputBox):
        """
        Create view
        :param user: (arcade.gui.UIInputBox) input with user name
        """
        super().__init__()
        self.texture = arcade.load_texture(BACKGROUNDS["rules"])
        self.ui_manager = UIManager()
        self.user = user

    def on_draw(self):
        """ Draw this view """
        arcade.start_render()
        self.texture.draw_sized(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                                SCREEN_WIDTH, SCREEN_HEIGHT)

    def on_hide_view(self):
        """Called when this view is not shown anymore"""
        self.ui_manager.unregister_handlers()

    def on_show_view(self):
        """Called when this view is shown"""
        self.setup()

    def setup(self):
        """ Set up this view, create buttons """
        self.ui_manager.purge_ui_elements()

        button = buttons.MenuButton(
            'Menu',
            center_x=self.window.width // 2,
            center_y=self.window.height // 9,
            width=200,
            user=self.user.text
        )
        button.set_style_attrs(
            bg_color_hover=(159, 255, 233),
            bg_color_press=(51, 201, 166),
        )
        self.ui_manager.add_ui_element(button)
