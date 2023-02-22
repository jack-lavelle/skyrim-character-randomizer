#Run from command-line with: "python -c 'import prototype as p; p.main()'"
#TODO: If divine == talos then stormcloak
#TODO: weapons specialization
#TODO: If alignment good then dawnguard
#TODO: home province
import random as r
import json
import ast

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

    backgroundStonesMap = {
        'Agent': r.sample([r.sample(thiefStones, 1), r.sample(warriorStones, 1)], 1)[0][0], 
        'Acrobat': r.sample([r.sample(thiefStones, 1), r.sample(warriorStones, 1)], 1)[0][0], 
        'Assassin': r.sample([r.sample(thiefStones, 1), r.sample(warriorStones, 1)], 1)[0][0], 
        'Barbarian': r.sample(warriorStones, 1)[0], 
        'Bard': r.sample(warriorStones, 1)[0], 
        'Battlemage': r.sample([r.sample(mageStones, 1), r.sample(warriorStones, 1)], 1)[0][0], 
        'Crusader': r.sample([r.sample(mageStones, 1), r.sample(warriorStones, 1)], 1)[0][0], 
        'Healer': r.sample(mageStones, 1)[0], 
        'Knight': r.sample([r.sample(mageStones, 1), r.sample(warriorStones, 1)], 1)[0][0], 
        'Monk': r.sample([r.sample(mageStones, 1), r.sample(warriorStones, 1), r.sample(thiefStones, 1)], 1)[0][0], 
        'Nightblade': r.sample([r.sample(mageStones, 1), r.sample(warriorStones, 1)], 1)[0][0], 
        'Pilgrim': r.sample(warriorStones, 1)[0], 
        'Scout': r.sample(warriorStones, 1)[0], 
        'Sorcerer': r.sample(mageStones, 1)[0], 
        'Spellsword': r.sample([r.sample(mageStones, 1), r.sample(warriorStones, 1)], 1)[0][0], 
        'Thief': r.sample(thiefStones, 1)[0], 
        'Warrior': r.sample(warriorStones, 1)[0], 
        'Witchhunter': r.sample([r.sample(mageStones, 1), r.sample(warriorStones, 1)], 1)[0][0]
    }
    
    moralities = ["Never", "Occasional", "Habitual"]
        
    def getName(self, race):
        #TODO: remove the need for this complicated name business
        with open("sample_names.json") as names_input:
            names = json.load(names_input)
        l = []
        for nameList in names[race]:
            l.append(ast.literal_eval(nameList))
            
        return l[r.randint(0, len(l) - 1)][r.randint(0, len(l) - 1)]
    
    def __init__(self, selector):
        def logical_build():
            randomint = r.randint(0, len(list(self.backgrounds.keys())) - 1)
            self.race = self.races[r.randint(0, len(self.races) - 1)]
            self.name = self.getName(self.race)
            self.sex = ''.join(r.sample(["Male", "Female"], 1))
            self.background = list(self.backgrounds.keys())[randomint]
            self.stone = self.backgroundStonesMap[self.background]
            self.location = str(self.startinglocations[r.randint(0, len(self.startinglocations) - 1)]) + ''.join(r.sample([" Surviving the Wilds", " in an Inn"], 1))
            self.divine = self.divines[r.randint(0, len(self.divines) - 1)]
            self.civilwar = self.civilwars[r.randint(0, len(self.civilwars) - 1)]
            self.dawnguard = self.dawnguards[r.randint(0, len(self.dawnguards) - 1)]
            self.alignment = ''.join([r.sample(["Lawful", "Neutral", "Chaotic"], 1)[0], " ", r.sample(["Good", "Neutral", "Evil"], 1)[0]])
            self.skills = self.backgrounds[list(self.backgrounds.keys())[randomint]]
                    

        def customized_build():
            #TODO
            pass

        d = {0 : logical_build, 1 : customized_build}
        d[selector]()

def characterGen():
    test = CharacterBuild(0)

    for x in test.__dict__:
        print(str(x) + ": " + str(test.__dict__[x]))
        
characterGen()