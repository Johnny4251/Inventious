import sys
from app.state_controller.Events import Event
from app.state_controller.states.TitleState import TitleState
import Utils

class StateController:
    def __init__(self, curr_state):
        self.curr_state = curr_state

    def transition(self, event):
        if Utils.DEBUG_MODE: print("Transitioning to ", event)

        if event == Event.TITLE: self.__req_title()
        elif event == Event.EXIT:self.__exit()
        else: raise ValueError("Invalid Event:" + str(event))

        if Utils.DEBUG_MODE: print("Transitioned to ", event)

    def __req_title(self):
        title_state = TitleState()
        title_state.render()
        self.curr_state = title_state

    def __exit(self):
        print("exiting...")
        sys.exit()