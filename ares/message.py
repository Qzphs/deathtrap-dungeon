from ares.event import Event


class Message(Event):
    """Pre-defined event subclass that records text as-is."""

    def __init__(self, text: str):
        self._text = text

    @property
    def text(self):
        return self._text
