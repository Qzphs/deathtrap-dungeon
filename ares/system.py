from typing import Generic, TypeVar

from ares.effect import Effect
from ares.rule import Invocation
from ares.ruleset import Ruleset
from ares.selection import Selection
from ares.state import State

S = TypeVar("S", bound=State)


class System(Generic[S]):
    """Manage rules, effects, and state."""

    def __init__(self, ruleset: Ruleset, state: S):
        self._invocations: list[Invocation] = []
        self._ruleset = ruleset
        self.selection = Selection.initial()
        self.state = state

    def resolve(self, effect: Effect):
        """Continue resolving effects, starting with this one."""
        self._add_invocation(effect)
        self._resolve_all()

    def select(self, option: str):
        """
        Select an option for the currently pending selection.

        The system will continue resolving effects once the selection is
        resolved.
        """
        self.selection.option = option
        self._resolve_all()

    def _add_invocation(self, effect: Effect):
        if (type(effect), effect.tag) not in self._ruleset.rules:
            raise ValueError(f"no rule handles {effect}")
        rule = self._ruleset.rules[type(effect), effect.tag]
        invocation = rule.resolve(effect, self.state)
        self._invocations.append(invocation)

    def _resolve_all(self):
        while self._invocations and self.selection.resolved:
            self._resolve_one(self._invocations[-1])

    def _resolve_one(self, invocation: Invocation):
        try:
            result = next(invocation)
            if isinstance(result, Effect):
                self._add_invocation(result)
            if isinstance(result, Selection):
                self.selection = result
        except StopIteration:
            self._invocations.pop()
