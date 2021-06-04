import arcade
import snake_game
from arcade.gui import UIManager
import buttons
from settings import *


class GameOverView2(arcade.View):
    """ View to show when game is over """

    def __init__(self):
        """ This is run once when we switch to this view """
        super().__init__()
        self.texture = arcade.load_texture("asserts/image/game_over.png")

        # Reset the viewport, necessary if we have a scrolling game and we need
        # to reset the viewport back to the start so we can see what we draw.
        #arcade.set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)

    def on_draw(self):
        """ Draw this view """
        arcade.start_render()
        self.texture.draw_sized(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                                SCREEN_WIDTH, SCREEN_HEIGHT)

    def on_key_press(self, key, modifiers):
        """ If the user presses the mouse button, re-start the game. """
        if key == arcade.key.C:
            game_view = snake_game.MyGame()
            game_view.setup()
            self.window.show_view(game_view)
        if key == arcade.key.M:
            pass

class StartView2(arcade.View):
    """ View to show when game is over """

    def __init__(self):
        """ This is run once when we switch to this view """
        super().__init__()
        self.texture = arcade.load_texture("asserts/image/game_over.png")

        # Reset the viewport, necessary if we have a scrolling game and we need
        # to reset the viewport back to the start so we can see what we draw.
        #arcade.set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)

    def on_draw(self):
        """ Draw this view """
        arcade.start_render()
        self.texture.draw_sized(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                                SCREEN_WIDTH, SCREEN_HEIGHT)

    def on_key_press(self, key, modifiers):
        """ If the user presses the mouse button, re-start the game. """
        if key == arcade.key.C:
            game_view = snake_game.MyGame()
            game_view.setup()
            self.window.show_view(game_view)
        if key == arcade.key.M:
            pass


class StartView(arcade.View):
    """ View to show when game is over """

    def __init__(self):
        """ This is run once when we switch to this view """
        super().__init__()
        self.texture = arcade.load_texture("asserts/image/start.png")
        self.ui_manager = UIManager()
        

        # Reset the viewport, necessary if we have a scrolling game and we need
        # to reset the viewport back to the start so we can see what we draw.
        #arcade.set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)

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

        y_slot = self.window.height // 10

       # right side elements
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

        button = buttons.PlayButton( "Play",
            center_x=self.window.width // 2,
            center_y=y_slot * 5,
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
        

        # Reset the viewport, necessary if we have a scrolling game and we need
        # to reset the viewport back to the start so we can see what we draw.
        #arcade.set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)

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

        y_slot = self.window.height // 6

       # right side elements
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

        button = buttons.PlayButton( "Play again",
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
