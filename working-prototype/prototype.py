#This is made to be completely independent despite breaking code organization norms. This will be copied and pasted into an online python console where it will
#function as intended.
import random as r

class CharacterBuild:
    def __init__(self, compRan):
        if compRan == "1":
            self.startingLocation = startingLocations[r.randrange(0, len(startingLocations), 1)]
            self.race = races[r.randrange(0, len(races), 1)]
            self.armour = armours[r.randrange(0, len(armours), 1)]

            stoneNum = r.randrange(0, len(stones), 1)
            if stoneNum == 3:
                self.stone = stones[3]
            else:
                self.stone = stones[stoneNum][r.randrange(0, len(stones[stoneNum]), 1)]
            
            self.civilwar = civilwar[r.randrange(0, len(civilwar), 1)]
            self.dawnguard = dawnguard[r.randrange(0, len(dawnguard), 1)]
            self.murder = morality[r.randrange(0, len(morality), 1)]
            self.theft = morality[r.randrange(0, len(morality), 1)]

            self.skills = set()
            while len(self.skills) < 6:
                skillSelect = r.randrange(0, 2, 1)
                if skillSelect == 1:
                    self.skills.add(skills[skillSelect][r.randrange(0, len(skills[skillSelect]), 1)])
                else:
                    randomSkillList = skills[skillSelect][r.randrange(0, len(skills[skillSelect]), 1)]
                    self.skills.add(randomSkillList[r.randrange(0, len(randomSkillList), 1)])

        else:
            print("not yet implemented.")

races = ["Altmer", "Argonian", "Bosmer", "Breton", "Dunmer", "Imperial", "Khajiit", "Nord", "Orc", "Redguard"]
startingLocations = ["Dawnstar", "Falkreath", "Markarth", "Riften", "Solitude", "Whiterun", "Windhelm", "Winterhold"]

armours = ["Evasion", "Heavy Armour", "Alteration + Illusion (mage armor + blur)"]

warriorStones = ["The Lady", "The Lord", "The Steed", "The Warrior"]
warriorCombatSkills = ["Marksman", "Block", "One Handed", "Two Handed"]

mageSkills = ["Alteration", "Conjuration", "Destruction", "Illusion", "Restoration"]
mageStones = ["The Apprentice", "The Atronach", "The Mage", "The Ritual"]

nonCombatSkills = ["Alchemy", "Enchanting", "Lockpicking", "Pickpocket", "Smithing", "Speech"]
thiefStones = ["The Lover", "The Shadow", "The Thief", "The Tower"]

combatSkills = [warriorCombatSkills, mageSkills]
skills = [combatSkills, nonCombatSkills]

stones = [warriorStones, mageStones, thiefStones, "The Serpent"]
factions = ["College of Winterhold", "The Companions", "The Thieves Guild", "The Dark Brotherhood", "The Bard's College"]
civilwar = ["Stormcloaks", "Imperial"]
dawnguard = ["Volkihar Clan", "Dawnguard"]
morality = ["Never", "Occasional", "Habitual"] #don't forget to do this twice (for theft and murder)

completelyRandom = input("0 if you want a more logical build or 1 for completely random build.\n")

myBuild = CharacterBuild(completelyRandom)
for attribute in vars(myBuild):
    print(attribute + " : " + str(vars(myBuild)[attribute]))