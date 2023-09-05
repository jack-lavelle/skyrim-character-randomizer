import unittest
from CharacterBuild import Character


class TestCharacterCreator(unittest.TestCase):
    def test_random_character(self):
        # The passed dictionary is the selected properties to hardcode. Empty -> random generation.
        character = Character({})

        self.assertTrue(all_values_not_none(character.properties))

    def test_semi_random_character(self):
        # The specific property is set and no value is `None`.
        test_properties = {"background": "Bard"}
        character = Character(test_properties)

        self.assertEqual(
            [True, "Bard"],
            [
                all_values_not_none(character.properties),
                character.properties["background"],
            ],
        )


def all_values_not_none(d: dict) -> bool:
    for key, val in d.items():
        if val == None:
            return False

    return True


if __name__ == "__main__":
    try:
        unittest.main()
    except SystemExit as e:
        pass
