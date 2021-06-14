from settings import SCREEN_HEIGHT, SCREEN_WIDTH, SCREEN_TITLE
import menu
import arcade


def main():
    """ Main method """
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    start = menu.StartView()
    window.set_update_rate(1 / 10)
    window.show_view(start)

    arcade.run()


if __name__ == "__main__":
    main()
