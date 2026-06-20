class Event:
    """
    Base class for events.

    Subclasses should represent relevant information as needed and
    override the text property.
    """

    @property
    def text(self) -> str:
        raise NotImplementedError("must be overriden by subclass")
