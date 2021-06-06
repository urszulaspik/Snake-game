import arcade
from arcade.gui import UIManager
import buttons
from settings import *
import snake_game
import results_read

class StartView(arcade.View):
    """ View to show when game is over """

    def __init__(self):
        """ This is run once when we switch to this view """
        super().__init__()
        self.texture = arcade.load_texture("asserts/image/start.png")
        self.ui_manager = UIManager()

    def on_draw(self):
        """ Draw this view """
        arcade.start_render()
        self.texture.draw_sized(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                                SCREEN_WIDTH, SCREEN_HEIGHT)

    def on_hide_view(self):
        self.ui_manager.unregister_handlers()
    
    def on_show_view(self):
        self.setup()

    def setup(self):
        """ Set up this view. """
        self.ui_manager.purge_ui_elements()
        y_slot = self.window.height // 12

        button = buttons.ExitButton(
            'Exit',
            center_x=self.window.width // 2,
            center_y=y_slot * 1,
            width=250,
        )
        self.ui_manager.add_ui_element(button)

        button = buttons.AuthorButton( "Author",
            center_x=self.window.width // 2,
            center_y=y_slot * 2,
            width=250
        )
        self.ui_manager.add_ui_element(button)

        button = buttons.ResultButton( "Results",
            center_x=self.window.width // 2,
            center_y=y_slot * 3,
            width=250
        )
        self.ui_manager.add_ui_element(button)

        button = buttons.RulesButton( "Rules",
            center_x=self.window.width // 2,
            center_y=y_slot * 4,
            width=250
        )
        self.ui_manager.add_ui_element(button)

        button = buttons.Level2Button( "Play level 2",
            center_x=self.window.width // 2,
            center_y=y_slot * 5,
            width=250
        )
        self.ui_manager.add_ui_element(button)

        button = buttons.Level1Button( "Play level 1",
            center_x=self.window.width // 2,
            center_y=y_slot * 6,
            width=250
        )
        self.ui_manager.add_ui_element(button)


class GameOverView(arcade.View):
    """ View to show when game is over """

    def __init__(self, score):
        """ This is run once when we switch to this view """
        super().__init__()
        self.texture = arcade.load_texture("asserts/image/game_over.png")
        self.ui_manager = UIManager()
        self.score = score

    def on_draw(self):
        """ Draw this view """
        arcade.start_render()
        self.texture.draw_sized(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                                SCREEN_WIDTH, SCREEN_HEIGHT)

    def on_hide_view(self):
        self.ui_manager.unregister_handlers()
    
    def on_show_view(self):
        self.setup()


    def setup(self):
        """ Set up this view. """
        self.ui_manager.purge_ui_elements()
        results_read.today_points_write("result_level1.csv", self.score)
        y_slot = self.window.height // 8

        button = buttons.ExitButton(
            'Exit',
            center_x=self.window.width // 2,
            center_y=y_slot * 1,
            width=250,
        )
        self.ui_manager.add_ui_element(button)

        button = buttons.MenuButton(
            'Menu',
            center_x=self.window.width // 2,
            center_y=y_slot * 2,
            width=250,
        )
        self.ui_manager.add_ui_element(button)

        button = buttons.Level1Button( "Play again",
            center_x=self.window.width // 2,
            center_y=y_slot * 3,
            width=250
        )
        self.ui_manager.add_ui_element(button)

        ui_input_box = arcade.gui.UIInputBox(
            center_x = self.window.width // 2,
            center_y = y_slot*4,
            width = 250
        )
        ui_input_box.text = "User Name"
        ui_input_box.cursor_index = len(ui_input_box.text) #?
        self.ui_manager.add_ui_element(ui_input_box)

        self.ui_manager.add_ui_element(arcade.gui.UILabel(
            f'Your score: {self.score}',
            center_x=self.window.width // 2,
            center_y=y_slot * 5,
        ))

class AuthorView(arcade.View):
    """ View to show when game is over """

    def __init__(self):
        """ This is run once when we switch to this view """
        super().__init__()
        self.texture = arcade.load_texture("asserts/image/author.png")
        self.ui_manager = UIManager()

    def on_draw(self):
        """ Draw this view """
        arcade.start_render()
        self.texture.draw_sized(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                                SCREEN_WIDTH, SCREEN_HEIGHT)

    def on_hide_view(self):
        self.ui_manager.unregister_handlers()
    
    def on_show_view(self):
        self.setup()

    def setup(self):
        """ Set up this view. """
        self.ui_manager.purge_ui_elements()


        button = buttons.MenuButton(
            'Menu',
            center_x=self.window.width // 2,
            center_y=self.window.height // 6,
            width=200,
        )
        self.ui_manager.add_ui_element(button)


class RulesView(arcade.View):
    """ View to show when game is over """

    def __init__(self):
        """ This is run once when we switch to this view """
        super().__init__()
        self.texture = arcade.load_texture("asserts/image/rules.png")
        self.ui_manager = UIManager()

    def on_draw(self):
        """ Draw this view """
        arcade.start_render()
        self.texture.draw_sized(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                                SCREEN_WIDTH, SCREEN_HEIGHT)

    def on_hide_view(self):
        self.ui_manager.unregister_handlers()
    
    def on_show_view(self):
        self.setup()

    def setup(self):
        """ Set up this view. """
        self.ui_manager.purge_ui_elements()


        button = buttons.MenuButton(
            'Menu',
            center_x=self.window.width // 2,
            center_y=self.window.height // 6,
            width=200,
        )
        self.ui_manager.add_ui_element(button)

class GameOverView2(arcade.View):
    """ View to show when game is over """

    def __init__(self, score):
        """ This is run once when we switch to this view """
        super().__init__()
        self.texture = arcade.load_texture("asserts/image/game_over.png")
        self.ui_manager = UIManager()
        self.score = score

    def on_draw(self):
        """ Draw this view """
        arcade.start_render()
        self.texture.draw_sized(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                                SCREEN_WIDTH, SCREEN_HEIGHT)

    def on_hide_view(self):
        self.ui_manager.unregister_handlers()
        results_read.today_points_write("result_level2.csv", self.score)
    
    def on_show_view(self):
        self.setup()

    def setup(self):
        """ Set up this view. """
        self.ui_manager.purge_ui_elements()
        results_read.today_points_write("result_level2.csv", self.score)
        y_slot = self.window.height // 6
        button = buttons.ExitButton(
            'Exit',
            center_x=self.window.width // 2,
            center_y=y_slot * 1,
            width=250,
        )
        self.ui_manager.add_ui_element(button)

        button = buttons.MenuButton(
            'Menu',
            center_x=self.window.width // 2,
            center_y=y_slot * 2,
            width=250,
        )
        self.ui_manager.add_ui_element(button)

        button = buttons.Level2Button( "Play again",
            center_x=self.window.width // 2,
            center_y=y_slot * 3,
            width=250
        )
        self.ui_manager.add_ui_element(button)

        self.ui_manager.add_ui_element(arcade.gui.UILabel(
            f'Your score: {self.score}',
            center_x=self.window.width // 2,
            center_y=y_slot * 4,
        ))