from app.state_controller.StateController import StateController
from app.state_controller.states.TitleState import TitleState

if __name__ == "__init__":
    title_state = TitleState()
    state_controller = StateController(title_state)
    
