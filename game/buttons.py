import arcade
import arcade.gui
import snake_game
import menu
import level2
import result_view


class ExitButton(arcade.gui.UIFlatButton):
    """
    Class with exit button
    """

    def on_click(self):
        """ Called when user lets off button, close application"""
        arcade.close_window()


class Level1Button(arcade.gui.UIFlatButton):
    '''
    Class with button for level 1
    '''

    def __init__(self, text: str, center_x: int, center_y: int, width: int, user: arcade.gui.UIInputBox):
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
        '''Called when user lets off button, change view for level 1'''
        view = snake_game.MyGame(self.user)
        view.setup()
        view.window.show_view(view)


class Level2Button(arcade.gui.UIFlatButton):
    '''
    Class with button for level 2
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
        '''Called when user lets off button, change view for level 2'''
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
        """ Called when user lets off button, change view for result level 1 view """
        view = result_view.ResultView(self.user)
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