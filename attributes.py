import json

with open("sample_names.json") as names_input:
    names_dict = json.load(names_input)

property_keys = [
    "name",
    "sex",
    "race",
    "background",
    "stone",
    "skills",
    "location",
    "province",
    "dragonborn",
    "civilwar",
    "divine",
    "dawnguard",
    "alignment",
    "traits",
]


property_dependency_map = {
    "skills": "background",
    "name": "race",
    "stone": "background",
    "dawnguard": "divine",
    "alignment": "divine",
}


races = [
    "Altmer",
    "Argonian",
    "Bosmer",
    "Breton",
    "Dunmer",
    "Imperial",
    "Khajiit",
    "Nord",
    "Orc",
    "Redguard",
]
sexes = ["Male", "Female"]
starting_locations = [
    "Dawnstar",
    "Falkreath",
    "Markarth",
    "Riften",
    "Solitude",
    "Whiterun",
    "Windhelm",
    "Winterhold",
]
divines = [
    "Akatosh",
    "Arkay",
    "Dibella",
    "Julianos",
    "Kynareth",
    "Mara",
    "Stendarr",
    "Talos",
    "Zenithar",
    "Auriel",
]
daedra = ["Azura", "Boethiah", "Mephala", "Nocturnal"]

factions = [
    "College of Winterhold",
    "The Companions",
    "The Thieves Guild",
    "The Dark Brotherhood",
    "The Bard's College",
]
civilwars = ["Stormcloaks", "Imperial"]
dawnguards = ["Volkihar Clan", "Dawnguard"]

early_enemies = [
    "horkers",
    "skeevers",
    "mudcrabs",
    "slaughterfish",
    "bears",
    "witches",
    "wolves",
    "bandits",
    "human forsworn",
    "humanoid skeletons",
    "baby frostbite spiders",
]
midgame_enemies = [
    "guards",
    "soldiers",
    "draugr",
    "hagravens",
    "trolls",
    "icewraiths",
    "spiders",
    "mammoths",
    "fireatronachs",
    "frostatronachs",
]
endgame_enemies = [
    "giants",
    "vampires",
    "mages",
    "dragons",
    "falmer",
    "dwemer automatons",
    "werewolves",
    "dragonpriests",
    "daedra",
    "elitesoldiers",
]

moralities = ["Never", "Occasional", "Habitual"]

stones = {
    "Warrior": ["The Lady", "The Lord", "The Steed", "The Warrior"],
    "Mage": ["The Apprentice", "The Atronach", "The Mage", "The Ritual"],
    "Thief": ["The Lover", "The Shadow", "The Thief", "The Tower"],
    "The Serpent": "The Serpent",
}

skills_map = {
    "Offensive Skills": [
        "Marksman",
        "One Handed",
        "Two Handed",
        "Conjuration",
        "Destruction",
        "Restoration",
        "Illusion",
        "Alchemy",
        "Enchanting",
        "Sneak",
        "Smithing",
    ],
    "Defensive Skills": [
        "Block",
        "Evasion",
        "Heavy Armour",
        "Alchemy",
        "Enchanting",
        "Alteration",
        "Illusion",
        "Restoration",
        "Sneak",
        "Smithing",
    ],
    "Noncombat-Based Skills": [
        "Alchemy",
        "Enchanting",
        "Lockpicking",
        "Pickpocket",
        "Smithing",
        "Speech",
    ],
}

backgrounds = {
    "Agent": "Illusion, Lockpicking, Marksman, One-Handed, Sneak, Speechcraft",
    "Acrobat": "Lockpicking, Marksman, One-Handed, Pickpocket, Sneak, Speechcraft",
    "Assassin": "Alchemy, Evasion, Lockpicking, Marksman, One-Handed, Sneak",
    "Barbarian": "Block, Evasion, Marksman, One-Handed, Smithing, Two-Handed",
    "Bard": "Block, Enchanting, Illusion, Evasion, One-Handed, Speechcraft",
    "Battlemage": "Alteration, Conjuration, Destruction, Enchanting, Heavy Armor, Two-Handed",
    "Crusader": "Alchemy, Block, Destruction, Heavy Armor, One-Handed, Restoration",
    "Healer": "Alchemy, Alteration, Destruction, Illusion, Restoration, Speechcraft",
    "Knight": "Block, Enchanting, Heavy Armor, One-Handed, Restoration, Speechcraft",
    "Monk": "Alteration, Illusion, Lockpicking, Marksman, One-Handed, Sneak",
    "Nightblade": "Alteration, Destruction, Evasion, Lockpicking, One-Handed, Restoration",
    "Pilgrim": "Block, Illusion, Evasion, One-Handed, Smithing, Speechcraft",
    "Scout": "Alchemy, Evasion, Marksman, One-Handed, Smithing, Sneak",
    "Sorcerer": "Alteration, Conjuration, Destruction, Enchanting, Heavy Armor, Restoration",
    "Spellsword": "Alteration, Destruction, Heavy Armor, Illusion, One-Handed, Restoration",
    "Thief": "Alchemy, Evasion, Lockpicking, Pickpocket, Sneak, Speechcraft",
    "Warrior": "Block, Heavy Armor, Marksman, One-Handed, Smithing, Two-Handed",
    "Witchhunter": "Alchemy, Destruction, Lockpicking, Marksman, One-Handed, Sneak",
}

background_sign_map = {
    "Agent": ["Thief", "Warrior"],
    "Acrobat": ["Thief", "Warrior"],
    "Assassin": ["Thief", "Warrior"],
    "Barbarian": ["Warrior"],
    "Bard": ["Warrior"],
    "Battlemage": ["Mage", "Warrior"],
    "Crusader": ["Mage", "Warrior"],
    "Healer": ["Mage"],
    "Knight": ["Mage", "Warrior"],
    "Monk": ["Mage", "Warrior", "Thief"],
    "Nightblade": ["Mage", "Warrior"],
    "Pilgrim": ["Warrior"],
    "Scout": ["Warrior"],
    "Sorcerer": ["Mage"],
    "Spellsword": ["Mage", "Warrior"],
    "Thief": ["Thief"],
    "Warrior": ["Warrior"],
    "Witchhunter": ["Mage", "Warrior"],
}
