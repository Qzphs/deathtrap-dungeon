import enum

import ares
from game.dice import roll_dice


class Character(ares.State):
    """Same as Character from Java implementation."""

    # Looks safe to inherit from ares.State as the Java implementation
    # seems to store minimal data outside the character.

    # TODO: introduce dedicated class if this assumption is wrong

    def __init__(self):
        super().__init__()

        self.base_skill = roll_dice(1) + 6
        self.base_stamina = roll_dice(2) + 12
        self.base_luck = roll_dice(1) + 6

        self.skill = self.base_skill
        self.stamina = self.base_stamina
        self.luck = self.base_luck
        self.food = 10
        self.gold = 0

        self.equipment = [
            Equipment.SWORD,
            Equipment.SHIELD,
            Equipment.LEATHER_ARMOUR,
        ]
        self.gems: list[Gem] = []
        self.knowledge: list[Knowledge] = []
        self.potions: list[Potion] = []
        self.states: list[State] = []

        self.page = 0

        self.has_eaten = False

    def has(self, thing: "Equipment | Gem | Knowledge | Potion | State"):
        """
        Check whether character has something.

        This is a convenience method and can be used with equipment,
        gems, knowledge, potions, or states.
        """
        if isinstance(thing, Equipment):
            return thing in self.equipment
        if isinstance(thing, Gem):
            return thing in self.gems
        if isinstance(thing, Knowledge):
            return thing in self.knowledge
        if isinstance(thing, Potion):
            return thing in self.potions
        if isinstance(thing, State):
            return thing in self.states
        raise TypeError(f"has() does not handle {thing.__class__.__name__}")


class Equipment(enum.Enum):

    # TODO: Equipment seems non-unique.
    # If it is, note this using a docstring.

    BRASS_BELL = "Brass Bell"
    BONE = "Bone"
    DAGGER = "Dagger"
    DOPPELGANGER_POTION = "Doppelganger Potion"
    DWARF_ARMOUR = "Dwarf Armour"
    GRAPPLING_IRON = "Grappling Iron"
    HOLLOW_WOODEN_TUBE = "Hollow Wooden Tube"
    IRON_HELMET = "Iron Helmet"
    IRON_SHIELD = "Iron Shield"
    IRON_SPIKES = "Iron Spikes"
    IRON_KEY = "Iron Key"
    JUG_OF_ACID = "Jug of Acid"
    LEATHER_ARMOUR = "Leather Armour"
    LEATHER_POUCH = "Leather Pouch"
    LONG_KNIFE = "Long Knife"
    MIRROR = "Mirror"
    MONKEY_BONE_CHARM = "Monkey Bone Charm"
    OPAL_DAGGER = "Opal Dagger"
    RING_OF_WISHES = "Ring of Wishes"
    ROPE = "Rope"
    SHIELD = "Shield"
    STILTS = "Stilts"
    SWORD = "Sword"
    WOODEN_BALL = "Wooden Ball"
    WOODEN_MALLET = "Wooden Mallet"


class Gem(enum.Enum):

    DIAMOND = "Diamond"
    EMERALD = "Emerald"
    GARNET = "Garnet"
    PEARL = "Pearl"
    RUBY = "Ruby"
    SAPPHIRE = "Sapphire"
    TOPAZ = "Topaz"


class Knowledge(enum.Enum):

    BLOODBEAST = "Bloodbeast"
    DOPPELGANGER = "Doppelganger"
    MANTICORE = "Manticore"
    SPIRIT_GIRL = "Spirit Girl"


class Potion(enum.Enum):

    HEAT_RESISTANCE = "Heat Resistance"
    TRAP_DETECTION = "Trap Detection"


class State(enum.Enum):

    DRUNK_FROM_FAIRY_FOUNTAIN = enum.auto()
    DRUNK_FROM_HAG_FOUNTAIN = enum.auto()
    EATEN_RICE = enum.auto()
    EXAMINED_ALCOVE = enum.auto()
    EXAMINED_BARBARIAN = enum.auto()
    OPENED_BLACK_BOOK = enum.auto()
    RUBBED_OINTMENT = enum.auto()
