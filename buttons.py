import arcade
import arcade.gui
import sys
import snake_game
import menu

class ExitButton(arcade.gui.UIFlatButton):
    """
    To capture a button click, subclass the button and override on_click.
    """
    def on_click(self):
        """ Called when user lets off button """
        #sys.exit()
        sys.exit()

class PlayButton(arcade.gui.UIFlatButton):
    def on_click(self):
        view = snake_game.MyGame()
        view.setup()
        view.window.show_view(view)

class AuthorButton(arcade.gui.UIFlatButton):
    """
    To capture a button click, subclass the button and override on_click.
    """
    def on_click(self):
        """ Called when user lets off button """
        #sys.exit()
        sys.exit()

class AuthorButton(arcade.gui.UIFlatButton):
    """
    To capture a button click, subclass the button and override on_click.
    """
    def on_click(self):
        """ Called when user lets off button """
        #sys.exit()
        sys.exit()

class RulesButton(arcade.gui.UIFlatButton):
    """
    To capture a button click, subclass the button and override on_click.
    """
    def on_click(self):
        """ Called when user lets off button """
        #sys.exit()
        sys.exit()

class ResultButton(arcade.gui.UIFlatButton):
    """
    To capture a button click, subclass the button and override on_click.
    """
    def on_click(self):
        """ Called when user lets off button """
        #sys.exit()
        sys.exit()

class RulesButton(arcade.gui.UIFlatButton):
    """
    To capture a button click, subclass the button and override on_click.
    """
    def on_click(self):
        """ Called when user lets off button """
        #sys.exit()
        sys.exit()

class MenuButton(arcade.gui.UIFlatButton):
    """
    To capture a button click, subclass the button and override on_click.
    """
    def on_click(self):
        """ Called when user lets off button """
        view = menu.StartView()
        view.setup()
        view.window.show_view(view)


