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
SNAKEBODY = {
    "body": "asserts/image/snake_body.png",
    "head_top": "asserts/image/snake_head_top.png",
    "head_bottom": "asserts/image/snake_head_bottom.png",
    "head_right": "asserts/image/snake_head_right.png",
    "head_left": "asserts/image/snake_head_left.png"
}

APPLE = {
    "good_apple": "asserts/image/myapple.png",
    "bad_apple": "asserts/image/black_apple.png",
    "rotten_apple": "asserts/image/brown_apple.png"
}

BACKGROUNDS = {
    "game": "asserts/image/background.png",
    "result1": "asserts/image/result1.png",
    "result2": "asserts/image/result2.png",
    "start": "asserts/image/start.png",
    "game_over": "asserts/image/game_over.png",
    "author": "asserts/image/author.png",
    "rules": "asserts/image/rules.png"

}

RESULTS = {
    "level1": "result_level1.csv",
    "level2": "result_level2.csv"
}

HEART = {
    "heart": "asserts/image/heart.png"
}