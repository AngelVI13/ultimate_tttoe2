import pygame

from gui.event import *
from gui.game_engine import GameEngine
from gui.event_manager import EventManager


class Pointer:
    LEFT_CLICK = 1
    RIGHT_CLICK = 3

    def __init__(self, event_manager: EventManager, game_engine: GameEngine):
        self.event_manager = event_manager
        self.game_engine = game_engine

    def handle_mouseup(self, event: Event):
        if event.button != self.LEFT_CLICK:
            return

        # get pointer to the view.
        # depending on the state -> check what was clicked on the screen
        # change state of model

        # too much view logic in controller ?
        # though it will not be related to showing things on screen
        # it will only be interacting with view objects like buttons etc.
        print(event, dir(event), event.__dict__)

        # current_state = self.game_engine.state.peek()

        # handler = self.keydown_state_map.get(current_state)
        # if handler is None:
        #     raise Exception(
        #         f"Uknown state: {current_state}. No handling defined for state."
        #     )

        # handler(event)
