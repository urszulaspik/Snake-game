import arcade
import arcade.gui
import snake_game
import menu
import level2
import result_view

class ExitButton(arcade.gui.UIFlatButton):
    """
    To capture a button click, subclass the button and override on_click.
    """
    def on_click(self):
        """ Called when user lets off button """
        arcade.close_window()

class Level1Button(arcade.gui.UIFlatButton):
    def __init__(self, text, center_x, center_y, width, user):
        super().__init__(text=text, center_x=center_x, center_y=center_y, width=width)
        self.user = user
    def on_click(self):
        view = snake_game.MyGame(self.user)
        view.setup()
        view.window.show_view(view)

class Level2Button(arcade.gui.UIFlatButton):
    def __init__(self, text, center_x, center_y, width, user):
        super().__init__(text=text, center_x=center_x, center_y=center_y, width=width)
        self.user = user
    def on_click(self):
        view = level2.MyGame2(self.user)
        view.setup()
        view.window.show_view(view)

class AuthorButton(arcade.gui.UIFlatButton):
    """
    To capture a button click, subclass the button and override on_click.
    """
    def __init__(self, text, center_x, center_y, width, user="User Name"):
        super().__init__(text=text, center_x=center_x, center_y=center_y, width=width)
        self.user = user
    def on_click(self):
        """ Called when user lets off button """
        view = menu.AuthorView(self.user)
        view.setup()
        view.window.show_view(view)

class RulesButton(arcade.gui.UIFlatButton):
    """
    To capture a button click, subclass the button and override on_click.
    """
    def __init__(self, text, center_x, center_y, width, user="User Name"):
        super().__init__(text=text, center_x=center_x, center_y=center_y, width=width)
        self.user = user
    def on_click(self):
        """ Called when user lets off button """
        view = menu.RulesView(self.user)
        view.setup()
        view.window.show_view(view)

class ResultButton(arcade.gui.UIFlatButton):
    """
    To capture a button click, subclass the button and override on_click.
    """
    def __init__(self, text, center_x, center_y, width, user="User Name"):
        super().__init__(text=text, center_x=center_x, center_y=center_y, width=width)
        self.user = user
    def on_click(self):
        """ Called when user lets off button """
        view = result_view.ResultView(self.user)
        view.setup()
        view.window.show_view(view)

class MenuButton(arcade.gui.UIFlatButton):
    """
    To capture a button click, subclass the button and override on_click.
    """
    def __init__(self, text, center_x, center_y, width, user="User Name"):
        super().__init__(text=text, center_x=center_x, center_y=center_y, width=width)
        self.user = user
    def on_click(self):
        """ Called when user lets off button """
        view = menu.StartView(self.user)
        view.setup()
        view.window.show_view(view)

class Result2Button(arcade.gui.UIFlatButton):
    """
    To capture a button click, subclass the button and override on_click.
    """
    def __init__(self, text, center_x, center_y, width, user="User Name"):
        super().__init__(text=text, center_x=center_x, center_y=center_y, width=width)
        self.user = user
    def on_click(self):
        """ Called when user lets off button """
        view = result_view.ResultView2(self.user)
        view.setup()
        view.window.show_view(view)

