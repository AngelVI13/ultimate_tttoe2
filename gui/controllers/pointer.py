import pygame

from gui.event import *
from gui.view import View
from gui.views.menu import MenuActions
from gui.game_engine import GameEngine
from gui.event_manager import EventManager


class Pointer:
    # constants of pygame mouse button values
    LEFT_CLICK = 1
    RIGHT_CLICK = 3

    def __init__(self, event_manager: EventManager, game_engine: GameEngine, view: View):
        self.event_manager = event_manager
        self.game_engine = game_engine
        self.view = view

        self.mouseup_state_map = {
            States.MENU: self.mouseup_menu,
            States.HELP: self.mouseup_help,
            States.PLAY: self.mouseup_play,
        }

    def handle_mouseup(self, event: Event):
        if event.button != self.LEFT_CLICK:
            return

        current_state = self.game_engine.state.peek()

        handler = self.mouseup_state_map.get(current_state)
        if handler is None:
            raise Exception(
                f"Uknown state: {current_state}. No handling defined for state."
            )

        handler(event)


    def mouseup_menu(self, event):
        """Handles menu pointer events."""

        # get pointer to the view.
        # depending on the state -> check what was clicked on the screen
        # change state of model

        # escape pops the menu
        for button in self.view.menu_view.buttons:
            if button.box.collidepoint(event.pos):
                if button.action == MenuActions.QUIT:
                    self.event_manager.post(StateChangeEvent(States.POP))

    def mouseup_help(self, event):
        """Handles help key events"""
        # space, enter or escape pops the help
        pass

    def mouseup_play(self, event):
        """Handles play key events"""
        pass