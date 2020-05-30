import pygame

from gui.event import *
from gui.state import States
from gui.event_manager import Listener


class View(Listener):
    """Draws the model state onto the screen."""
    
    def __init__(self, event_manager, game_engine, window_size, window_title, fps):
        super().__init__(event_manager)
        self.game_engine = game_engine
        self.window_size = window_size
        self.window_title = window_title
        self.fps = fps

        self.initialized = False
        
        self.screen = None
        self.clock = None
        self.font_instance = None

        self.render_handler_map = {
            States.MENU: self.render_menu,
            States.HELP: self.render_help,
            States.PLAY: self.redner_play,
        }

    def notify(self, event: Event):
        """Receive events posted on the message queue."""
        if isinstance(event, InitializeEvent):
            self.initialize()

        elif isinstance(event, QuitEvent):
            self.initialized = False
            pygame.quit()

        elif isinstance(event, TickEvent):
            # drawing only on tick events and when initialized
            if not self.initialized:
                return

            current_state = self.game_engine.peek()
            handler = self.render_handler_map.get(current_state)
            if handler is None:
                raise Exception(f"Unsupported state: {current_state}. No render handler defined.")

            handler()  # draw on canvas
            pygame.display.flip()  # update canvas on screen
            
            # limit the redraw speed
            self.clock.tick(self.fps)
            
    def render_menu():
        self.screen.fill(pygame.Color("white"))
        text = self.font.render("Menu. (space to play, esc to exit)", True, pygame.Color("black"))
        self.screen.blit(text, (0, 0))

    def render_help():
        self.screen.fill(pygame.Color("white"))
        text = self.font.render("Help. (space, esc to return)", True, pygame.Color("black"))
        self.screen.blit(text, (0, 0))

    def render_play():
        self.screen.fill(pygame.Color("white"))
        text = self.font.render("Play (f1 for help, esc for menu)", True, pygame.Color("black"))
        self.screen.blit(text, (0, 0))

    def initialize(self):
        pygame.init()
        pygame.font.init()
        pygame.display.set_caption(self.window_title)
        self.clock = pygame.time.Clock()
        self.font_instance = pygame.font.Font(None, 30)  # todo what are these params
        self.initialized = True
