# Run from command-line with: "python -c 'import prototype as p; p.main()'"
# TODO: weapons specialization?
# TODO: religion and alignment
# TODO: DiD-ify skills (meaning make them viable for each run)
# TODO: look over Reddit post for ideas / refinements
# TODO: reference openAI chat for good backstory ... include query.
# TODO: revamp character generation when manually selecting skills
# TODO: mid-game character changes
# TODO: non-random builds
import random as r
import json
import ast
from typing import Any


class Character:
    def __init__(self):
        self.province = None
        self.race = None
        self.sex = None
        self.name = None
        self.dragonborn = None
        self.civilwar = None
        self.background = None
        self.skills = None
        self.stone = None
        self.location = None
        self.divine = None
        self.dawnguard = None
        self.alignment = None
        self.traits = None

        def random_build():
            self.province = r.choice(["Black Marsh", "Cyrodiil", "Elsweyr", "Hammerfell",
                                     "High Rock", "Morrowind", "Skyrim", "Summerset Isles",
                                      "Valenwood"])
            self.race = r.choice(races)
            self.sex = r.choice(sexes)
            self.name = gen_name(self.race)
            self.dragonborn = r.choice(["Dragonborn", "Not Dragonborn"])
            self.civilwar = r.choice(["Stormcloaks", "Imperials"])
            self.background = r.choice(list(backgrounds.keys()))
            self.skills = backgrounds[self.background]
            self.stone = gen_stone(self.background)
            self.location = r.choice(
                ["Surviving the Wilds in ", "In an inn in "]) + r.choice(startinglocations)
            self.divine = gen_divine()
            self.dawnguard = gen_dawnguard(self.divine)
            self.alignment = gen_alignment(self.divine)
            self.traits = gen_traits()

        def gen_name(race: str) -> str:
            raw_race_names = []
            for name_list in namesDict[race]:
                raw_race_names.append(ast.literal_eval(name_list))

            race_names = [
                item for sublist in raw_race_names for item in sublist]
            return r.choice(race_names)

        def gen_stone(background: str) -> str:
            return r.choice(stones[r.choice(backgroundSignMap[background])])

        def gen_dawnguard(divine: str) -> str:
            if divine in divines:
                return "Dawnguard"
            return r.choice(["Dawnguard", "Vampires"])

        def gen_alignment(divine: str) -> str:
            if divine in divines:
                return r.choice(["Lawful", "Neutral", "Chaotic"]) + r.choice([" Good", " Neutral"])
            if divine in daedra:
                return r.choice(["Lawful", "Neutral", "Chaotic"]) + " Evil"
            return r.choice(["Lawful", "Neutral", "Chaotic"]) + r.choice([" Good", " Neutral",
                                                                          " Evil"])

        def gen_traits():
            traits = []
            with open("traits.json") as json_data:
                traits_list = json.load(json_data)["traits"]

            for i in range(3):
                traits.append(r.choice(traits_list))

            return ', '.join(traits) + ", and " + r.choice(traits_list)

        def gen_divine():
            total_divines = divines + daedra
            return r.choice(total_divines)

        random_build()

    def get_character_dict(self):
        return self.__dict__


with open("sample_names.json") as names_input:
    namesDict = json.load(names_input)

races = ["Altmer", "Argonian", "Bosmer", "Breton", "Dunmer",
         "Imperial", "Khajiit", "Nord", "Orc", "Redguard"]
sexes = ["Male", "Female"]
startinglocations = ["Dawnstar", "Falkreath", "Markarth",
                     "Riften", "Solitude", "Whiterun", "Windhelm", "Winterhold"]
divines = ["Akatosh", "Arkay", "Dibella", "Julianos", "Kynareth",
           "Mara", "Stendarr", "Talos", "Zenithar", "Auriel"]
daedra = ["Azura", "Boethiah", "Mephala", "Nocturnal"]

factions = ["College of Winterhold", "The Companions",
            "The Thieves Guild", "The Dark Brotherhood", "The Bard's College"]
civilwars = ["Stormcloaks", "Imperial"]
dawnguards = ["Volkihar Clan", "Dawnguard"]

earlyEnemies = ['horkers', 'skeevers', 'mudcrabs', 'slaughterfish', 'bears', 'witches',
                'wolves', 'bandits', 'human forsworn', 'humanoid skeletons',
                'baby frostbite spiders']
midgameEnemies = ['guards', 'soldiers', 'draugr', 'hagravens', 'trolls',
                  'icewraiths', 'spiders', 'mammoths', 'fireatronachs', 'frostatronachs']
endgameEnemies = ['giants', 'vampires', 'mages', 'dragons', 'falmer',
                  'dwemer automatons', 'werewolves', 'dragonpriests', 'daedra', 'elitesoldiers']

moralities = ["Never", "Occasional", "Habitual"]

stones = {
    "Warrior": ["The Lady", "The Lord", "The Steed", "The Warrior"],
    "Mage": ["The Apprentice", "The Atronach", "The Mage", "The Ritual"],
    "Thief": ["The Lover", "The Shadow", "The Thief", "The Tower"],
    "The Serpent": "The Serpent"
}

skills = {
    "Offensive Skills": ["Marksman", "One Handed", "Two Handed", "Conjuration", "Destruction",
                         "Restoration", "Illusion", "Alchemy", "Enchanting", "Sneak", "Smithing"],
    "Defensive Skills": ["Block", "Evasion", "Heavy Armour", "Alchemy", "Enchanting", "Alteration",
                         "Illusion", "Restoration", "Sneak", "Smithing"],
    "Noncombat-Based Skills": ["Alchemy", "Enchanting", "Lockpicking", "Pickpocket", "Smithing",
                               "Speech"]
}

backgrounds = {
    'Agent': 'Illusion, Lockpicking, Marksman, One-Handed, Sneak, Speechcraft',
    'Acrobat': 'Lockpicking, Marksman, One-Handed, Pickpocket, Sneak, Speechcraft',
    'Assassin': 'Alchemy, Evasion, Lockpicking, Marksman, One-Handed, Sneak',
    'Barbarian': 'Block, Evasion, Marksman, One-Handed, Smithing, Two-Handed',
    'Bard': 'Block, Enchanting, Illusion, Evasion, One-Handed, Speechcraft',
    'Battlemage': 'Alteration, Conjuration, Destruction, Enchanting, Heavy Armor, Two-Handed',
    'Crusader': 'Alchemy, Block, Destruction, Heavy Armor, One-Handed, Restoration',
    'Healer': 'Alchemy, Alteration, Destruction, Illusion, Restoration, Speechcraft',
    'Knight': 'Block, Enchanting, Heavy Armor, One-Handed, Restoration, Speechcraft',
    'Monk': 'Alteration, Illusion, Lockpicking, Marksman, One-Handed, Sneak',
    'Nightblade': 'Alteration, Destruction, Evasion, Lockpicking, One-Handed, Restoration',
    'Pilgrim': 'Block, Illusion, Evasion, One-Handed, Smithing, Speechcraft',
    'Scout': 'Alchemy, Evasion, Marksman, One-Handed, Smithing, Sneak',
    'Sorcerer': 'Alteration, Conjuration, Destruction, Enchanting, Heavy Armor, Restoration',
    'Spellsword': 'Alteration, Destruction, Heavy Armor, Illusion, One-Handed, Restoration',
    'Thief': 'Alchemy, Evasion, Lockpicking, Pickpocket, Sneak, Speechcraft',
    'Warrior': 'Block, Heavy Armor, Marksman, One-Handed, Smithing, Two-Handed',
    'Witchhunter': 'Alchemy, Destruction, Lockpicking, Marksman, One-Handed, Sneak'
}

backgroundSignMap = {
    'Agent': ["Thief", "Warrior"],
    'Acrobat': ["Thief", "Warrior"],
    'Assassin': ["Thief", "Warrior"],
    'Barbarian': ["Warrior"],
    'Bard': ["Warrior"],
    'Battlemage': ["Mage", "Warrior"],
    'Crusader': ["Mage", "Warrior"],
    'Healer': ["Mage"],
    'Knight': ["Mage", "Warrior"],
    'Monk': ["Mage", "Warrior", "Thief"],
    'Nightblade': ["Mage", "Warrior"],
    'Pilgrim': ["Warrior"],
    'Scout': ["Warrior"],
    'Sorcerer': ["Mage"],
    'Spellsword': ["Mage", "Warrior"],
    'Thief': ["Thief"],
    'Warrior': ["Warrior"],
    'Witchhunter': ["Mage", "Warrior"]
}


def character_test():
    character = Character()
    print(json.dumps(character.get_character_dict(), indent=4))


character_test()
