"""
Module that defines all game related events.
"""
from gui.state import States


class Event():
    """A superclass for any events that might be generated
    by an object and sent to the EventManager
    """
    def __repr__(self):
        return f"{self.__class__.__name__}"


class QuitEvent(Event):
    """Event emitted when user entered input with 
    intention of quitting the game
    """
    pass


class TickEvent(Event):
    """Event signalizing the start of a `timeslice`"""
    pass


class KeyboardEvent(Event):
    """Event emmited on key press"""
    def __init__(self, unicode_char):
        self.char = unicode_char

    def __repr__(self):
        return f"{self.__class__.__name__}(unicode_char='{self.char}')"


class MouseEvent(Event):
    """Event emmited on mouse click"""
    def __init__(self, click_pos):
        self.click_pos = click_pos

    def __repr__(self):
        return f"{self.__class__.__name__}(click_pos='{self.click_pos}')"


class InitializeEvent(Event):
    """Tells all event listeners to initialize themselves.
    This includes loading libraries and resources.
    """
    pass


class StateChangeEvent(Event):
    """Event used to change the model's state machine."""
    def __init__(self, state: States):
        self.state = state

    def __repr__(self):
        return f"{self.__class__.__name__}(state='{self.state}')"


if __name__ == "__main__":
    event = Event()
    print(event)