import pytest

from game.character import Character, Equipment, Gem, Knowledge, Potion, State


@pytest.fixture
def character():
    return Character()


def test_has_equipment(character: Character):
    assert not character.has(Equipment.BONE)
    character.equipment.append(Equipment.BONE)
    assert character.has(Equipment.BONE)


def test_has_gem(character: Character):
    assert not character.has(Gem.DIAMOND)
    character.gems.append(Gem.DIAMOND)
    assert character.has(Gem.DIAMOND)


def test_has_knowledge(character: Character):
    assert not character.has(Knowledge.BLOODBEAST)
    character.knowledge.append(Knowledge.BLOODBEAST)
    assert character.has(Knowledge.BLOODBEAST)


def test_has_potion(character: Character):
    assert not character.has(Potion.HEAT_RESISTANCE)
    character.potions.append(Potion.HEAT_RESISTANCE)
    assert character.has(Potion.HEAT_RESISTANCE)


def test_has_state(character: Character):
    assert not character.has(State.DRUNK_FROM_FAIRY_FOUNTAIN)
    character.states.append(State.DRUNK_FROM_FAIRY_FOUNTAIN)
    assert character.has(State.DRUNK_FROM_FAIRY_FOUNTAIN)


def test_has_rejects_invalid_type(character: Character):
    with pytest.raises(TypeError):
        character.has("Bloodbeast")
