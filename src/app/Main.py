import path_setup
import sys
from app.state_controller.StateController import StateController
from state_controller.states.TitleState import TitleState
from app.state_controller.Events import Event

if __name__ == "__main__":
    print("running...")
    title_state = TitleState()
    state_controller = StateController(title_state)
    state_controller.transition(Event.TITLE)
    sys.exit(state_controller.transition(Event.EXIT))