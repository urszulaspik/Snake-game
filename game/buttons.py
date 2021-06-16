import arcade
import arcade.gui
from game import level1
from game import menu
from game import level2
from game import result_view


class ExitButton(arcade.gui.UIFlatButton):
    """
    Class with exit button
    """

    def on_click(self):
        """ Called when user lets off button, close application"""
        arcade.close_window()


class LevelButton(arcade.gui.UIFlatButton):
    '''
    Class with button for level 1 and level 2
    '''

    def __init__(self, text: str, center_x: int, center_y: int, width: int, user: arcade.gui.UIInputBox, level: str):
        '''
        Create button
        :param text: (str) text on button
        :param center_x: (int) middle position of x
        :param center_y: (int) middle position of y
        :param width: (int) width of button
        :param user: (arcade.gui.UIInputBox) input with user name
        :param level: (str) level of game, can be "level1" or "level2"
        '''
        super().__init__(text=text, center_x=center_x, center_y=center_y, width=width)
        self.user = user
        self.level = level

    def on_click(self):
        '''Called when user lets off button, change view for level 1'''
        if self.level == "level1":
            view = level1.MyGame(self.user)
        else:
            view = level2.MyGame2(self.user)
        view.setup()
        view.window.show_view(view)


class AuthorButton(arcade.gui.UIFlatButton):
    '''
    Class with button for view with about author section
    '''

    def __init__(self, text: str, center_x: int, center_y: int, width: int, user: arcade.gui.UIInputBox = "User Name"):
        '''
        Create button
        :param text: (str) text on button
        :param center_x: (int) middle position of x
        :param center_y: (int) middle position of y
        :param width: (int) width of button
        :param user: (arcade.gui.UIInputBox) input with user name
        '''
        super().__init__(text=text, center_x=center_x, center_y=center_y, width=width)
        self.user = user

    def on_click(self):
        """ Called when user lets off button, change view for author view """
        view = menu.AuthorView(self.user)
        view.setup()
        view.window.show_view(view)


class RulesButton(arcade.gui.UIFlatButton):
    '''
    Class with button for view with section with rules
    '''

    def __init__(self, text: str, center_x: int, center_y: int, width: int, user: arcade.gui.UIInputBox = "User Name"):
        '''
        Create button
        :param text: (str) text on button
        :param center_x: (int) middle position of x
        :param center_y: (int) middle position of y
        :param width: (int) width of button
        :param user: (arcade.gui.UIInputBox) input with user name
        '''
        super().__init__(text=text, center_x=center_x, center_y=center_y, width=width)
        self.user = user

    def on_click(self):
        """ Called when user lets off button, change view for rules view """
        view = menu.RulesView(self.user)
        view.setup()
        view.window.show_view(view)


class ResultButton(arcade.gui.UIFlatButton):
    '''
    Class with button for view with section with result in level 1
    '''

    def __init__(self, text: str, center_x: int, center_y: int, width: int, user: arcade.gui.UIInputBox, level: str):
        '''
        Create button
        :param text: (str) text on button
        :param center_x: (int) middle position of x
        :param center_y: (int) middle position of y
        :param width: (int) width of button
        :param user: (arcade.gui.UIInputBox) input with user name
        :param level: (str) level of game, can be "level1" or "level2"
        '''
        super().__init__(text=text, center_x=center_x, center_y=center_y, width=width)
        self.user = user
        self.level = level

    def on_click(self):
        """ Called when user lets off button, change view for result level 1 view """
        view = result_view.ResultView(self.user, self.level)
        view.setup()
        view.window.show_view(view)


class MenuButton(arcade.gui.UIFlatButton):
    """
    Class with button with menu view
    """

    def __init__(self, text: str, center_x: int, center_y: int, width: int, user: arcade.gui.UIInputBox = "User Name"):
        '''
        Create button
        :param text: (str) text on button
        :param center_x: (int) middle position of x
        :param center_y: (int) middle position of y
        :param width: (int) width of button
        :param user: (arcade.gui.UIInputBox) input with user name
        '''
        super().__init__(text=text, center_x=center_x, center_y=center_y, width=width)
        self.user = user

    def on_click(self):
        """ Called when user lets off button, change view for menu view """
        view = menu.StartView(self.user)
        view.setup()
        view.window.show_view(view)


class Result2Button(arcade.gui.UIFlatButton):
    '''
    Class with button for view with section with result in level 2
    '''

    def __init__(self, text: str, center_x: int, center_y: int, width: int, user: arcade.gui.UIInputBox = "User Name"):
        '''
        Create button
        :param text: (str) text on button
        :param center_x: (int) middle position of x
        :param center_y: (int) middle position of y
        :param width: (int) width of button
        :param user: (arcade.gui.UIInputBox) input with user name
        '''
        super().__init__(text=text, center_x=center_x, center_y=center_y, width=width)
        self.user = user

    def on_click(self):
        """ Called when user lets off button, change view for result level 2 view  """
        view = result_view.ResultView2(self.user)
        view.setup()
        view.window.show_view(view)
