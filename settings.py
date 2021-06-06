import arcade

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 600
GAME_WIDTH = 500
GAME_HEIGHT = 500
SCREEN_TITLE = "Snake"
MOVEMENT_SPEED = 25
SOUNDS = {
    'eat': arcade.load_sound("asserts/sound/apple_eat.ogg"),
    "dead": arcade.load_sound("asserts/sound/game_over.ogg"),
    "heart": arcade.load_sound("asserts/sound/heart.ogg")
}