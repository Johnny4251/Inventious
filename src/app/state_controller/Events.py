from enum import Enum

class Event(Enum):
    train = 1
    create_dataset = 2
    select_model = 3
    view_board = 4
    leave_board = 5
    exit = 6