#This is made to be completely self-contained despite breaking code organization norms. Until I have made a website proper, this will be copied and pasted into an online python 
#console.

#Simply copy and paste this into an online python console (https://www.programiz.com/python-programming/online-compiler/) and follow the prompts. More features
#will be added as time goes on.
import random as r

class CharacterBuild:
    races = ["Altmer", "Argonian", "Bosmer", "Breton", "Dunmer", "Imperial", "Khajiit", "Nord", "Orc", "Redguard"]
    startinglocations = ["Dawnstar", "Falkreath", "Markarth", "Riften", "Solitude", "Whiterun", "Windhelm", "Winterhold"]
    divines = ["Akatosh", "Arkay", "Dibella", "Julianos", "Kynareth", "Mara", "Stendarr", "Talos", "Zenithar", "Nocturnal", "Auriel"]

    factions = ["College of Winterhold", "The Companions", "The Thieves Guild", "The Dark Brotherhood", "The Bard's College"]
    civilwars = ["Stormcloaks", "Imperial"]
    dawnguards = ["Volkihar Clan", "Dawnguard"]

    warriorStones = ["The Lady", "The Lord", "The Steed", "The Warrior"]
    mageStones = ["The Apprentice", "The Atronach", "The Mage", "The Ritual"]
    thiefStones = ["The Lover", "The Shadow", "The Thief", "The Tower"]
    stones = [warriorStones, mageStones, thiefStones, "The Serpent"]

    warriorSkills = [["Marksman", "One Handed", "Two Handed"], ["Block"]]
    mageSkills = [["Conjuration", "Destruction"], ["Alteration", "Illusion", "Restoration"]]
    nonCombatSkills = ["Alchemy", "Enchanting", "Lockpicking + Pickpocket", "Smithing", "Speech"]
    combatSkills = [warriorSkills, mageSkills]
    armours = ["Evasion", "Heavy Armour", "Alteration + Illusion (mage armor + blur)"]
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

    moralities = ["Never", "Occasional", "Habitual"]
    
    def __init__(self, selector):
        def logical_build():
            self.race = self.races[r.randint(0, len(self.races) - 1)]
            self.startinglocation = self.startinglocations[r.randint(0, len(self.startinglocations) - 1)]
            self.divine = self.divines[r.randint(0, len(self.divines) - 1)]
            self.civilwar = self.civilwars[r.randint(0, len(self.civilwars) - 1)]
            self.dawnguard = self.dawnguards[r.randint(0, len(self.dawnguards) - 1)]
            self.murder = self.moralities[r.randint(0, len(self.moralities) - 1)]
            self.theft = self.moralities[r.randint(0, len(self.moralities) - 1)]

            randomint = r.randint(0, len(list(self.backgrounds.keys())) - 1)
            self.background = list(self.backgrounds.keys())[randomint]
            self.skills = self.backgrounds[list(self.backgrounds.keys())[randomint]]

        def customized_build():
            #TODO
            pass


        d = {0 : logical_build, 1 : customized_build}
        d[selector]()

test = CharacterBuild(0)

for x in test.__dict__:
    print(str(x) + ": " + str(test.__dict__[x]))