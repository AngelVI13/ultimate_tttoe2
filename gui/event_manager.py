"""
Module implements event manager class that handles communication
between model, view & controller. In addition a listener base class
is defined.
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from weakref import WeakKeyDictionary

from gui.event import Event, TickEvent


class EventManager:
    """Coordinates the communication between the Model,
    View and Controller.
    """

    def __init__(self):
        self.listeners = WeakKeyDictionary()

    def register_listener(self, listener: Listener):
        """Add listener to to `spam` list. It will rececive
        all posted events through its notify(event) call
        """
        self.listeners[listener] = 1

    def post(self, event: Event):
        """Forward event to all registered listeners."""

        if not isinstance(event, TickEvent):
            # print any non tick event
            print(str(event))  # todo remove

        for listener in self.listeners:
            listener.notify(event)


class Listener(ABC):
    """Base Listener class. Implements registering listeners and
    an abstract method for notifying subscribers.
    """

    def __init__(self, event_manager: EventManager):
        self.event_manager = event_manager
        self.event_manager.register_listener(self)

    @abstractmethod
    def notify(self, event: Event):
        pass


if __name__ == "__main__":
    event_manager = EventManager()

    try:
        listener = Listener()
    except Exception as err:
        assert isinstance(err, TypeError)
