from __future__ import annotations
from abc import ABC, abstractmethod


class Command(ABC):
    """
    The Command interface declares a method for executing a command.
    """

    @abstractmethod
    def execute(self) -> None:
        pass


class TravelCommand(Command):

    def __init__(self, root_container, direction):
        self._root_container = root_container
        self._direction = direction

    def execute(self) -> None:
        print("executed")
        self._root_container.move_rooms(self._direction)

