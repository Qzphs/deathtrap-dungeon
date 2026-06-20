from typing import Callable, Generator, Hashable

from ares.effect import Effect
from ares.selection import Selection
from ares.state import State

Invocation = Generator["Effect | Selection | None", None, None]


class Rule:
    """
    Wrapper class for rule functions.

    This class stores the effect type and tag of the rule in addition to
    its callback function, and validates the type and tag of incoming
    effects before resolving them.
    """

    def __init__(
        self,
        callback: Callable[[Effect, State], Invocation],
        effect_type: type[Effect],
        effect_tag: Hashable = None,
    ):
        self.callback = callback
        self.effect_type = effect_type
        self.effect_tag = effect_tag

    def resolve(self, effect: Effect, state: State):
        """
        Return an invocation used to resolve this effect.

        This is the same as validating the type and tag of the effect,
        then calling the callback function.

        If the type or tag of the effect do not match this rule, raise
        TypeError (this probably should not happen unless something is
        wrong with ares).

        This method is intended to be called by the ares system only.
        """
        if not isinstance(effect, self.effect_type):
            raise TypeError(f"effect does not match type {self.effect_type}")
        if effect.tag != self.effect_tag:
            raise TypeError(f"effect does not match tag {self.effect_tag}")
        return self.callback(effect, state)
