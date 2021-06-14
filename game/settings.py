import arcade

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 600
GAME_WIDTH = 500
GAME_HEIGHT = 500
SCREEN_TITLE = "Snake"
MOVEMENT_SPEED = 25
SOUNDS = {
    'eat': arcade.load_sound("game/asserts/sound/apple_eat.ogg"),
    "dead": arcade.load_sound("game/asserts/sound/game_over.ogg"),
    "heart": arcade.load_sound("game/asserts/sound/heart.ogg")
}
SNAKEBODY = {
    "body": "game/asserts/image/snake_body.png",
    "head_top": "game/asserts/image/snake_head_top.png",
    "head_bottom": "game/asserts/image/snake_head_bottom.png",
    "head_right": "game/asserts/image/snake_head_right.png",
    "head_left": "game/asserts/image/snake_head_left.png"
}

APPLE = {
    "good_apple": "game/asserts/image/myapple.png",
    "bad_apple": "game/asserts/image/black_apple.png",
    "rotten_apple": "game/asserts/image/brown_apple.png"
}

BACKGROUNDS = {
    "game": "game/asserts/image/background.png",
    "result1": "game/asserts/image/result1.png",
    "result2": "game/asserts/image/result2.png",
    "start": "game/asserts/image/start.png",
    "game_over": "game/asserts/image/game_over.png",
    "author": "game/asserts/image/author.png",
    "rules": "game/asserts/image/rules.png"

}

RESULTS = {
    "level1": "game/asserts/results/result_level1.csv",
    "level2": "game/asserts/results/result_level2.csv"
}

HEART = {
    "heart": "game/asserts/image/heart.png"
}