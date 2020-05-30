import pygame

from gui.event import *
from gui.game_engine import GameEngine
from gui.event_manager import Listener, EventManager


class Keyboard(Listener):
    def __init__(self, event_manager: EventManager, game_engine: GameEngine):
        super().__init__(event_manager)
        self.game_engine = game_engine

        self.keydown_state_map = {
            States.MENU: self.keydown_menu,
            States.HELP: self.keydown_help,
            States.PLAY: self.keydown_play,
        }

    def notify(self, event: Event):
        # Controller event handling is only performed on TickEvents
        if not isinstance(event, TickEvent):
            return

        for event in pygame.event.get():
            # handle window manager closing the window (X-button click)
            if event.type == pygame.QUIT:
                self.event_manager.post(QuitEvent())

            # handle key presses
            elif event.type == pygame.KEYDOWN:
                self.handle_keydown(event)

    def handle_keydown(self, event: Event):
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

    def keydown_menu(self, event):
        """Handles menu key events."""

        # escape pops the menu
        if event.key == pygame.K_ESCAPE:
            self.event_manager.post(StateChangeEvent(States.POP))

        # space plays the game
        if event.key == pygame.K_SPACE:
            self.event_manager.post(StateChangeEvent(States.STATE_PLAY))

    def keydown_help(self, event):
        """Handles help key events"""
        # space, enter or escape pops the help
        if event.key in (pygame.K_ESCAPE, pygame.K_SPACE, pygame.K_RETURN):
            self.event_manager.post(StateChangeEvent(States.POP))

    def keydown_play(self, event):
        """Handles play key events"""
        if event.key == pygame.K_ESCAPE:
            # todo this should ask for confirmation before exitting the game
            self.event_manager.post(StateChangeEvent(States.POP))

        # F1 shows the help
        if event.key == pygame.K_F1:
            self.event_manager.post(StateChangeEvent(States.STATE_HELP))
        else:
            self.event_manager.post(KeyboardEvent(event.unicode))


if __name__ == "__main__":
    from unittest.mock import MagicMock

    mock_event_manager = MagicMock()
    mock_game_engine = MagicMock()

    keyboard = Keyboard(mock_event_manager, mock_game_engine)
    assert keyboard.game_engine is mock_game_engine
    assert keyboard.event_manager is mock_event_manager
