import arcade
from arcade.gui import UIManager
from game import buttons
from game.settings import BACKGROUNDS, SCREEN_HEIGHT, SCREEN_WIDTH, SOUNDS, RESULTS
from game import results_read


class GameOverView(arcade.View):
    """ Class with view to show when game is over """

    def __init__(self, score: int, user: arcade.gui.UIInputBox, level: str):
        """
        Create view
        :param score: (int) points earned by the user in the game
        :param user: (arcade.gui.UIInputBox) input with user name
        :param level: (str) level of game, can be "level1" and "level2"
        """
        super().__init__()
        self.texture = arcade.load_texture(BACKGROUNDS["game_over"])
        self.ui_manager = UIManager()
        self.score = score
        self.user = user
        self.sound = None
        self.level = level

    def on_draw(self):
        """ Draw this view """
        arcade.start_render()
        self.texture.draw_sized(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                                SCREEN_WIDTH, SCREEN_HEIGHT)

    def sound_stop(self):
        """
        If sound exists, stop that sound
        """
        try:
            arcade.stop_sound(self.sound)
        except:
            pass

    def on_hide_view(self):
        """ Call when view is not shown anymore"""
        self.ui_manager.unregister_handlers()
        self.sound_stop()

    def on_show_view(self):
        """ Call when this view is shown """
        self.sound = arcade.play_sound(SOUNDS["dead"])
        self.setup()

    def setup(self):
        """ Set up this view, creat buttons. """
        self.ui_manager.purge_ui_elements()
        results_read.today_points_write(RESULTS[self.level], self.score, self.user.text)
        y_slot = self.window.height // 6

        button = buttons.ExitButton(
            'Exit',
            center_x=self.window.width // 2,
            center_y=y_slot * 1,
            width=250,
        )
        button.set_style_attrs(
            bg_color_hover=(135, 21, 25),
            bg_color_press=(122, 21, 24),
        )
        self.ui_manager.add_ui_element(button)

        button = buttons.MenuButton(
            'Menu',
            center_x=self.window.width // 2,
            center_y=y_slot * 2,
            width=250,
            user=self.user.text
        )
        button.set_style_attrs(
            bg_color_hover=(226, 99, 1),
            bg_color_press=(192, 85, 3),
        )
        self.ui_manager.add_ui_element(button)

        button = buttons.LevelButton("Play again",
                                      center_x=self.window.width // 2,
                                      center_y=y_slot * 3,
                                      width=250,
                                      user=self.user,
                                      level = self.level
                                      )
        button.set_style_attrs(
            bg_color_hover=(226, 99, 1),
            bg_color_press=(192, 85, 3),
        )
        self.ui_manager.add_ui_element(button)

        score_label = arcade.gui.UILabel(
            f'Your score: {self.score}',
            center_x=self.window.width // 2,
            center_y=y_slot * 4
        )
        score_label.set_style_attrs(
            font_color=(255, 204, 51),
            font_color_hover=(255, 228, 14)
        )
        self.ui_manager.add_ui_element(score_label)