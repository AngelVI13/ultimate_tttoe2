from gui.event_manager import EventManager
from gui.game_engine import GameEngine
from gui.controller.keyboard import Keyboard
from gui.view import View
from gui.settings import DISPLAY_WIDTH, DISPLAY_HEIGHT


def main():
    event_manager = EventManager()
    game_engine = GameEngine(event_manager)
    _keyboard = Keyboard(event_manager, game_engine)
    _view = View(
        event_manager,
        game_engine,
        window_size=(DISPLAY_WIDTH, DISPLAY_HEIGHT),
        window_title="Ultimate Tic Tac Toe",
        fps=30,
    )
    game_engine.run()


if __name__ == "__main__":
    main()
