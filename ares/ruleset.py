from typing import Callable, Hashable

from ares.effect import Effect
from ares.rule import Invocation, Rule
from ares.state import State


class Ruleset:
    """Represent a collection of rules."""

    def __init__(self):
        """
        Initialise an empty ruleset.

        New rules should be added using either add() or the rule() decorator.
        """
        self.rules: dict[tuple[type[Effect], Hashable], Rule] = {}

    def add(self, rule: Rule):
        """
        Add a rule to this ruleset.

        The effect type and tag of the rule should match the effects
        that the rule resolves.
        """
        self.rules[rule.effect_type, rule.effect_tag] = rule

    def rule(self, effect_type: type[Effect], tag: Hashable = None):
        """
        Decorator for adding rules to the ruleset.

        The effect type and tag of the rule should match the effects
        that the rule resolves.
        """

        def decorator(func: Callable[[Effect, State], Invocation]):
            self.add(Rule(func, effect_type, tag))
            return func

        return decorator
