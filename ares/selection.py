from typing import Iterable

from ares.option import Option


class Selection[Value]:
    """
    Represent a list of options that can be selected from.

    Selections are created by rules and represent a decision that needs
    to be made before the rule can continue executing.
    """

    def __init__(self, options: Iterable[Option[Value]]):
        """
        Initialise selection with options.

        Each option has a name and value. Names and values should (but
        need not be) unique. At least one option must be provided;
        ValueError is raised if this is not the case.
        """
        self.options = list(options)
        if not self.options:
            raise ValueError("options cannot be empty")
        self._choice: int | None = None

    @classmethod
    def initial(cls):
        """Return a dummy selection that is automatically resolved."""
        selection = Selection([Option("start", None)])
        selection.value = None
        return selection

    @property
    def resolved(self):
        """Whether an option has already been selected."""
        return self._choice is not None

    @property
    def option(self):
        """The selected option (None if not resolved)."""
        if self._choice is None:
            return None
        return self.options[self._choice]

    @option.setter
    def option(self, option: Option):
        if self.resolved:
            raise ValueError("selection is already resolved")
        if option not in self.options:
            raise ValueError("invalid choice")
        self._choice = self.options.index(option)

    @property
    def name(self):
        """The name of the selected option (None if not resolved)."""
        if self._choice is None:
            return None
        return self.options[self._choice].name

    @name.setter
    def name(self, name: str):
        if self.resolved:
            raise ValueError("selection is already resolved")
        names = [option.name for option in self.options]
        if name not in names:
            raise ValueError("invalid choice")
        self._choice = names.index(name)

    @property
    def value(self):
        """The value of the selected option (None if not resolved)."""
        if self._choice is None:
            return None
        return self.options[self._choice].value

    @value.setter
    def value(self, value: Value):
        if self.resolved:
            raise ValueError("selection is already resolved")
        values = [option.value for option in self.options]
        if value not in values:
            raise ValueError("invalid choice")
        self._choice = values.index(value)
