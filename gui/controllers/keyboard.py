import pygame

from gui.event import *
from gui.game_engine import GameEngine
from gui.event_manager import EventManager


class Keyboard:
    def __init__(self, event_manager: EventManager, game_engine: GameEngine):
        self.event_manager = event_manager
        self.game_engine = game_engine

        self.keydown_state_map = {
            States.MENU: self.keyup_menu,
            States.HELP: self.keyup_help,
            States.PLAY: self.keyup_play,
        }

    def handle_keyup(self, event: Event):
        if event.key == pygame.K_ESCAPE:
            self.event_manager.post(StateChangeEvent(States.POP))
            return

        current_state = self.game_engine.state.peek()

        handler = self.keydown_state_map.get(current_state)
        if handler is None:
            raise Exception(
                f"Uknown state: {current_state}. No handling defined for state."
            )

        handler(event)

    def keyup_menu(self, event):
        """Handles menu key events."""

        # escape pops the menu
        if event.key == pygame.K_ESCAPE:
            self.event_manager.post(StateChangeEvent(States.POP))

        # space plays the game
        if event.key == pygame.K_SPACE:
            self.event_manager.post(StateChangeEvent(States.PLAY))

    def keyup_help(self, event):
        """Handles help key events"""
        # space, enter or escape pops the help
        if event.key in (pygame.K_ESCAPE, pygame.K_SPACE, pygame.K_RETURN):
            self.event_manager.post(StateChangeEvent(States.POP))

    def keyup_play(self, event):
        """Handles play key events"""
        if event.key == pygame.K_ESCAPE:
            # todo this should ask for confirmation before exitting the game
            self.event_manager.post(StateChangeEvent(States.POP))

        # F1 shows the help
        if event.key == pygame.K_F1:
            self.event_manager.post(StateChangeEvent(States.HELP))
        else:
            self.event_manager.post(KeyboardEvent(event.unicode))


if __name__ == "__main__":
    from unittest.mock import MagicMock

    mock_event_manager = MagicMock()
    mock_game_engine = MagicMock()

    keyboard = Keyboard(mock_event_manager, mock_game_engine)
    assert keyboard.game_engine is mock_game_engine
    assert keyboard.event_manager is mock_event_manager
