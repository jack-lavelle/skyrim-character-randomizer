import random as r, attributes as a

#logically -> skills contained within warrior / mage / thief

randomChoice = input("0 for warrior build, 1 for mage build, 2 for thief build, 3 for random build.\n")
#cb = character build


if randomChoice == 3:
    choice = r.randrange(0, 3, 1)
