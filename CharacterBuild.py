# Run from command-line with: "python -c 'import prototype as p; p.main()'"
# TODO: weapons specialization?
# TODO: religion and alignment
# TODO: DiD-ify skills (meaning make them viable for each run)
# TODO: look over Reddit post for ideas / refinements
# TODO: reference openAI chat for good backstory ... include query.
# TODO: revamp character generation when manually selecting skills
# TODO: mid-game character changes
# TODO: non-random builds

# TODO: rewrite this entire file using the Factory Method pattern.
import random as r
import json
import ast
import attributes


class Character:
    previously_checked_properties = []

    def __init__(self, build_type: str, properties: dict):
        # TODO: WHY DOES THE CONSTRUCTOR HAVE THIS MUCH SHIT???
        self.name = None
        self.sex = None
        self.race = None
        self.background = None
        self.stone = None
        self.skills = None
        self.location = None
        self.province = None
        self.dragonborn = None
        self.civilwar = None
        self.divine = None
        self.dawnguard = None
        self.alignment = None
        self.traits = None

        def gen_province() -> str:
            return r.choice(
                [
                    "Black Marsh",
                    "Cyrodiil",
                    "Elsweyr",
                    "Hammerfell",
                    "High Rock",
                    "Morrowind",
                    "Skyrim",
                    "Summerset Isles",
                    "Valenwood",
                ]
            )

        def gen_race() -> str:
            return r.choice(attributes.races)

        def gen_sex() -> str:
            return r.choice(attributes.sexes)

        def gen_dragonborn() -> str:
            return r.choice(["Dragonborn", "Not Dragonborn"])

        def gen_civilwar() -> str:
            return r.choice(["Stormcloaks", "Imperials"])

        def gen_background() -> str:
            return r.choice(list(attributes.backgrounds.keys()))

        def gen_skills() -> str:
            return attributes.backgrounds[self.background]

        def gen_location() -> str:
            return r.choice(["Surviving the Wilds in ", "In an inn in "]) + r.choice(
                attributes.starting_locations
            )

        def gen_name() -> str:
            raw_race_names = []
            for name_list in attributes.names_dict[self.race]:
                raw_race_names.append(ast.literal_eval(name_list))

            race_names = [item for sublist in raw_race_names for item in sublist]
            return r.choice(race_names)

        def gen_stone() -> str:
            return r.choice(
                attributes.stones[
                    r.choice(attributes.background_sign_map[self.background])
                ]
            )

        def gen_dawnguard() -> str:
            if self.divine in attributes.divines:
                return "Dawnguard"
            return r.choice(["Dawnguard", "Vampires"])

        def gen_alignment() -> str:
            if self.divine in attributes.divines:
                return r.choice(["Lawful", "Neutral", "Chaotic"]) + r.choice(
                    [" Good", " Neutral"]
                )
            if self.divine in attributes.daedra:
                return r.choice(["Lawful", "Neutral", "Chaotic"]) + " Evil"
            return r.choice(["Lawful", "Neutral", "Chaotic"]) + r.choice(
                [" Good", " Neutral", " Evil"]
            )

        def gen_traits():
            traits = []
            with open("traits.json") as json_data:
                traits_list = json.load(json_data)["traits"]

            for i in range(3):
                traits.append(r.choice(traits_list))

            return ", ".join(traits) + ", and " + r.choice(traits_list)

        def gen_divine():
            total_divines = attributes.divines + attributes.daedra
            return r.choice(total_divines)

        def random_build():
            self.province = gen_province()
            self.race = gen_race()
            self.sex = gen_sex()
            self.dragonborn = gen_dragonborn()
            self.civilwar = gen_civilwar()
            self.background = gen_background()
            self.skills = gen_skills()
            self.location = gen_location()
            self.name = gen_name()
            self.stone = gen_stone()
            self.divine = gen_divine()
            self.dawnguard = gen_dawnguard()
            self.alignment = gen_alignment()
            self.traits = gen_traits()

        if build_type == "random":
            random_build()
            return

        def set_name(name: str):
            self.name = name

        def set_sex(sex: str):
            self.sex = sex

        def set_race(race: str):
            self.race = race

        def set_stone(stone: str):
            self.stone = stone

        def set_background(background: str):
            self.background = background

        def set_skills(skills: str):
            self.skills = skills

        def set_location(location: str):
            self.location = location

        def set_province(province: str):
            self.province = province

        def set_dragonborn(dragonborn: str):
            self.dragonborn = dragonborn

        def set_civilwar(civilwar: str):
            self.civilwar = civilwar

        def set_divine(divine: str):
            self.divine = divine

        def set_dawnguard(dawnguard: str):
            self.dawnguard = dawnguard

        def set_alignment(alignment: str):
            self.alignment = alignment

        def set_traits(traits: str):
            self.traits = traits

        property_set_map = {
            "race": set_race,
            "name": set_name,
            "sex": set_sex,
            "stone": set_stone,
            "background": set_background,
            "skills": set_skills,
            "location": set_location,
            "province": set_province,
            "dragonborn": set_dragonborn,
            "civilwar": set_civilwar,
            "divine": set_divine,
            "dawnguard": set_dawnguard,
            "alignment": set_alignment,
            "traits": set_traits,
        }

        property_gen_map = {
            "province": gen_province,
            "race": gen_race,
            "sex": gen_sex,
            "dragonborn": gen_dragonborn,
            "civilwar": gen_civilwar,
            "background": gen_background,
            "skills": gen_skills,
            "location": gen_location,
            "divine": gen_divine,
            "traits": gen_traits,
            "name": gen_name,
            "stone": gen_stone,
            "dawnguard": gen_dawnguard,
            "alignment": gen_alignment,
        }

        # TODO: I don't like how I am using side-effects like this ... it can be hard to track down
        # where self.previously_checked_properties changes ... this should be overhauled to be more
        # clear and concise, function oriented.

        # TODO: This class needs rethinking ... it has too much going on when it should only
        # contain information about a Character.
        def semi_random_build(checked_properties: dict):
            for field, value in property_gen_map.items():
                if field in checked_properties:
                    self.previously_checked_properties.append(field)
                    property_set_map[field](checked_properties[field])
                else:
                    property_set_map[field](value())

        semi_random_build(properties)

    def get_character_dict(self):
        return self.__dict__

    def get_character_string_list(self):
        strings = []
        for x, y in self.__dict__.items():
            strings.append(x.capitalize() + " : " + y)

        return strings

    def get_character_string_dictionary_list(self):
        strings_keyvalues = []
        for x, y in self.__dict__.items():
            checked_bool = False
            if x in self.previously_checked_properties:
                checked_bool = True
            strings_keyvalues.append((x.capitalize() + " : " + y, {x: y}, checked_bool))

        return strings_keyvalues


# TODO: place these tests in a proper unittest file
def random_character_test():
    character = Character("random", None)
    print(json.dumps(character.get_character_string_list(), indent=4))


test_dict = {"background": "Bard"}


def semi_random_character_test(testDict):
    character = Character("semi-random", testDict)
    print(json.dumps(character.get_character_dict(), indent=4))
