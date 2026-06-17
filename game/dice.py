import random


def roll_dice(n: int):
    """Return the sum of n independent dice rolls."""
    return sum(random.randint(1, 6) for _ in range(n))
