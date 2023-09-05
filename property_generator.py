import random as r
import attributes
import json
import ast


def generate_property(prop: str, properties: dict):
    if prop in attributes.property_dependency_map:
        return property_gen_map[prop](
            properties[attributes.property_dependency_map[prop]]
        )
    else:
        return property_gen_map[prop]()


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


def gen_skills(background) -> str:
    return attributes.backgrounds[background]


def gen_location() -> str:
    return r.choice(["Surviving the Wilds in ", "In an inn in "]) + r.choice(
        attributes.starting_locations
    )


def gen_name(race) -> str:
    raw_race_names = []
    for name_list in attributes.names_dict[race]:
        raw_race_names.append(ast.literal_eval(name_list))

    race_names = [item for sublist in raw_race_names for item in sublist]
    return r.choice(race_names)


def gen_stone(background) -> str:
    return r.choice(
        attributes.stones[r.choice(attributes.background_sign_map[background])]
    )


def gen_dawnguard(divine) -> str:
    if divine in attributes.divines:
        return "Dawnguard"
    return r.choice(["Dawnguard", "Vampires"])


def gen_alignment(divine) -> str:
    if divine in attributes.divines:
        return r.choice(["Lawful", "Neutral", "Chaotic"]) + r.choice(
            [" Good", " Neutral"]
        )
    if divine in attributes.daedra:
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
