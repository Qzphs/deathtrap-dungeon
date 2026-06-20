from typing import Hashable


class Effect:
    """
    Base class for ares effects.

    Subclasses should be used to represent different effect types.
    """

    @property
    def tag(self) -> Hashable:
        """
        Optionally return a hashable object used to classify effects.

        If multiple rules handle the same effect type, the rule with
        matching tag is selected to resolve the effect.
        """
        return None
