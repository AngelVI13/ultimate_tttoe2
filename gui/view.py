import pygame
from event_manager import Listener


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

    def initialize(self):
        pygame.init()
        pygame.font.init()
        pygame.display.set_caption(self.window_title)
        self.clock = pygame.time.Clock()
        self.font_instance = pygame.font.Font(None, 30)  # todo what are these params
        self.initialized = True
