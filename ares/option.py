class Option[Value]:
    """Represent an option within a selection."""

    def __init__(self, name: str, value: Value):
        """
        Initialise self with name and value.

        The name of an option is a string intended to be displayed to a
        user. The value of an option is any internal-facing value that
        is used by the enclosing selection or rule.
        """
        self.name = name
        self.value = value
