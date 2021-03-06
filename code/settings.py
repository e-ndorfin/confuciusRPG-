import player

# game setup
WIDTH = 1280
HEIGTH = 720
FPS = 60
TILESIZE = 64

# x = barrier, p = player, ' ' = air, t = tree, tr = trigger

WORLD_MAP = [
    ['t', 't', 't', 't', 't', 't', 't', 't', 'tr', 'tr',
        'tr', 'tr', 't', 't', 't', 't', 't', 't', 't', 't'],
    ['t', 't', 't', 't', 't', 't', 't', 't', ' ', ' ',
        ' ', ' ', 't', 't', 't', 't', 't', 't', 't', 't'],
    ['t', 't', 't', 't', 't', 't', 't', 't', ' ', ' ',
        ' ', ' ', 't', 't', 't', 't', 't', 't', 't', 't'],
    ['t', 't', 't', 't', 't', 't', 't', 't', ' ', ' ',
        ' ', ' ', 't', 't', 't', 't', 't', 't', 't', 't'],
    ['t', 't', 't', 't', 't', 't', 't', 't', ' ', ' ',
        ' ', ' ', 't', 't', 't', 't', 't', 't', 't', 't'],
    ['t', 't', 't', 't', 't', 't', 't', 't', ' ', ' ',
        ' ', ' ', 't', 't', 't', 't', 't', 't', 't', 't'],
    ['t', 't', 't', 't', 't', 't', 't', 't', ' ', 'p',
        ' ', ' ', 't', 't', 't', 't', 't', 't', 't', 't'],
    ['t', 't', 't', 't', 't', 't', 't', 't', 't', 't',
        't', 't', 't', 't', 't', 't', 't', 't', 't', 't'],
    ['t', 't', 't', 't', 't', 't', 't', 't', 't', 't',
        't', 't', 't', 't', 't', 't', 't', 't', 't', 't'],
    ['t', 't', 't', 't', 't', 't', 't', 't', 't', 't',
        't', 't', 't', 't', 't', 't', 't', 't', 't', 't'],
    ['t', 't', 't', 't', 't', 't', 't', 't', 't', 't',
        't', 't', 't', 't', 't', 't', 't', 't', 't', 't'],
]

# WORLD_MAP = [
# ['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x'],
# ['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
# ['x',' ','p',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
# ['x',' ',' ','x',' ',' ',' ',' ',' ','x','x','x','x','x',' ',' ',' ',' ',' ','x'],
# ['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ','x'],
# ['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ','x'],
# ['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ','x'],
# ['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ','x'],
# ['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ','x'],
# ['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ','x'],
# ['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ','x'],
# ['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x','x','x',' ',' ',' ','x'],
# ['x',' ',' ',' ',' ',' ',' ','x',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
# ['x',' ',' ',' ',' ',' ','x','x','x','x','x',' ',' ',' ',' ',' ',' ',' ',' ','x'],
# ['x',' ',' ',' ',' ',' ',' ','x','x','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
# ['x',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
# ['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
# ['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
# ['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
# ['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x'],
# ]
