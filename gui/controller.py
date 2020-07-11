import pygame

from gui.event import *
from gui.game_engine import GameEngine
from gui.event_manager import Listener, EventManager
from gui.view import View
from gui.controllers.keyboard import Keyboard
from gui.controllers.pointer import Pointer


class Controller(Listener):
    def __init__(self, event_manager: EventManager, game_engine: GameEngine, view: View):
        super().__init__(event_manager)
        self.game_engine = game_engine

        self.keyboard = Keyboard(event_manager, game_engine, view)
        self.pointer = Pointer(event_manager, game_engine, view)

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
                self.keyboard.handle_keydown(event)

            # handle mouse clicks
            elif event.type == pygame.MOUSEBUTTONUP:
                self.pointer.handle_mouseup(event)
