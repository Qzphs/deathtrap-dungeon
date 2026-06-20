from ares.event import Event
from ares.message import Message


class State:
    """
    Base class for states.

    The base class manages events, which are used to record text output.
    Subclasses are responsible for managing all other data.
    """

    def __init__(self):
        self.events: list[Event] = []

    def record(self, event: str | Event):
        """
        Apply an event to this stage.

        If event is str, it is automatically converted to a Message.
        """
        if isinstance(event, str):
            event = Message(event)
        self.events.append(event)
