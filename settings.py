
from enum import Enum

# Drawing colors
BG_COLOR = (144, 201, 120)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Display screen
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.6)
SCROLL_THRESHOLD = SCREEN_WIDTH // 6
FPS = 60

# Gamemap tiles
ROWS = 16
COLS = 150
TILE_SIZE = SCREEN_HEIGHT // ROWS
TILE_TYPE_COUNT = 21
DIRT_TILE_FIRST = 0
DIRT_TILE_LAST = 8
WATER_TILE_FIRST = 9
WATER_TILE_LAST = 10
DECORATION_TILE_FIRST = 11
DECORATION_TILE_LAST = 14
PLAYER_TILE_ID = 15
ENEMY_TILE_ID = 16
AMMO_TILE_ID = 17
GRENADE_TILE_ID = 18
HEALTH_TILE_ID = 19
LEVEL_EXIT_TILE_ID = 20

# World physics values
GRAVITY = 0.75

# Soldier animations
class Action(Enum):
    IDLE = 0
    RUN = 1
    JUMP = 2
    DEATH = 3

class Direction(Enum):
    LEFT = -1
    RIGHT = 1
    IDLE = 0
    def reverse(self):
        return Direction(-self.value)
    def pause(self):
        return Direction(0)
    def __mul__(self, operand):
        if operand == -1:
            return Direction(-self.value)
        raise ValueError("Multiplication only support -1 to reverse direction")
