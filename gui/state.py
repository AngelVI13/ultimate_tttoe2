"""
Module that defines & implements logic related to game state handling.
"""
from enum import Enum, auto
from typing import Optional, List


class States(Enum):
    """State machine constants to represent current game state."""

    POP = auto()  # indicates when state stack should be poped
    MENU = auto()
    HELP = auto()
    PLAY = auto()


class StateMachine:
    """Stack-based state machine implementation.
    Supports - peek(), pop() & push().
    Peeking and popping an empty stack returns None
    """

    def __init__(self):
        self.state_stack: List[States] = []

    def peek(self) -> Optional[States]:
        """Returns the current state without altering the stack.
        Returns None if stack is empty.
        """
        if not self.state_stack:
            return None

        return self.state_stack[-1]

    def pop(self) -> Optional[States]:
        """Remove and return the current state from the stack.
        Return None if the stack is empty.
        """
        if not self.state_stack:
            return None

        return self.state_stack.pop()

    def push(self, state: States):
        """Push the new state onto the stack"""
        self.state_stack.append(state)


if __name__ == "__main__":
    state_machine = StateMachine()
    assert state_machine.pop() is None
    assert state_machine.peek() is None

    state_machine.push(States.MENU)
    assert state_machine.peek() == States.MENU
    assert state_machine.pop() == States.MENU
    assert state_machine.peek() is None
