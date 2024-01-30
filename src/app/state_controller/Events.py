from enum import Enum

class Event(Enum):
    TRAIN = 1
    CREATE_DATASET = 2
    SELECT_MODEL = 3
    VIEW_BOARD = 4
    LEAVE_BOARD = 5
    EXIT = 6
    TITLE = 7