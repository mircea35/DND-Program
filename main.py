import random
from array import *
import os

cache = 0
AnimalHandling = 0

#This is the function defining the main menu
def Menu():
    print("D&D Sheet Builder\n 1 - Character creation\n 2 - Party Creation\n 3 - GM Viewer\n 4 - Quit\n")
    index = int(input("Enter the value: "))
    if index == 1:
        CharacterCreation()
    if index == 4:
        quit()
    else:
        print("Incorrect answer. Try again")
        Menu()

#This is the class defining the character template
class Character:

    def __init__(self, name, race, Class, level, strength, dexterity, constitution, wisdom, intelligence, charisma, Athletics, Acrobatics, SleightOfHand, Stealth, Arcana, History, Investigation):
        self.name = name
        self.race = race
        self.Class = Class
        self.level = level
        self.Strength = strength
        self.Dexterity = dexterity
        self.Constitution = constitution
        self.Wisdom = wisdom
        self.Intelligence = intelligence
        self.Charisma = charisma
        self.Athletics = Athletics
        self.Acrobatics = Acrobatics
        self.SleightOfHand = SleightOfHand
        self.Stealth = Stealth
        self.Arcana = Arcana
        self.History = History
        self.Investigation = Investigation


#This is the function defines the different races and converts the user input to the race

def raceTranslation():
    global race
    global temp_r

    global temp_str2
    global temp_dex2
    global temp_const2
    global temp_wis2
    global temp_intelli2
    global temp_charisma2

    if temp_r == 1:
        race = "Dragonborn"
        temp_str2 = 2
        temp_dex2 = 0
        temp_const2 = 0
        temp_wis2 = 0
        temp_intelli2 = 0
        temp_charisma2 = 1

    elif temp_r == 2:
        race = "Dwarf"
        temp_str2 = 0
        temp_dex2 = 0
        temp_const2 = 2
        temp_wis2 = 0
        temp_intelli2 = 0
        temp_charisma2 = 0

    elif temp_r == 3:
        race = "Elf"
        temp_str2 = 0
        temp_dex2 = 2
        temp_const2 = 0
        temp_wis2 = 0
        temp_intelli2 = 0
        temp_charisma2 = 0

    elif temp_r == 4:
        race = "Gnome"
        temp_str2 = 0
        temp_dex2 = 0
        temp_const2 = 0
        temp_wis2 = 0
        temp_intelli2 = 2
        temp_charisma2 = 0

    elif temp_r == 5:
        race = "Half-Elf"
        temp_str2 = 0
        temp_dex2 = 0
        temp_const2 = 0
        temp_wis2 = 0
        temp_intelli2 = 0
        temp_charisma2 = 2

        for i in range(2):
            print("Because you've chosen Half-Elf, you can increase 2 ability scores by 1.\n 1 for Strength\n 2 for Dexterity\n 3 for Constitution\n 4 for Wisdom\n 5 for Intelligence\n")
            option = int(input("Type your answer: "))
            if option == 0:
                print("")
            elif option == 1:
                temp_str2 += 1
            elif option == 2:
                temp_dex2 += 1
            elif option == 3:
                temp_const2 += 1
            elif option == 4:
                temp_wis2 += 1
            elif option == 5:
                temp_intelli2 += 1
            else:
                print("Error: Something went wrong - 2")

    elif temp_r == 6:
        race = "Halfling"
        temp_str2 = 0
        temp_dex2 = 2
        temp_const2 = 0
        temp_wis2 = 0
        temp_intelli2 = 0
        temp_charisma2 = 0

    elif temp_r == 7:
        race = "Half-Orc"
        temp_str2 = 2
        temp_dex2 = 0
        temp_const2 = 1
        temp_wis2 = 0
        temp_intelli2 = 0
        temp_charisma2 = 0

    elif temp_r == 8:
        race = "Human"
        temp_str2 = 1
        temp_dex2 = 1
        temp_const2 = 1
        temp_wis2 = 1
        temp_intelli2 = 1
        temp_charisma2 = 1

    elif temp_r == 9:
        race = "Tiefling"
        temp_str2 = 0
        temp_dex2 = 0
        temp_const2 = 0
        temp_wis2 = 0
        temp_intelli2 = 1
        temp_charisma2 = 2

    else:
        print("Something went wrong.")

#This is the function defines the different classes and converts the user input to a class
def classTranslation():
    #The vriable temp_c is the temporary value which helps determine the class
    #The varibale cache is used to cache the bonus for the skills
    global Class
    global temp_c
    global cache

    global AnimalHandling
    global Athletics
    global Intimidation

    if temp_c == 1:
        Class = "Barbarian"
        print(AnimalHandling , " " , cache)
        for i in range(2):
            print("Because you've chosen Barbarian, you gain Proficency two of these skills.\n 1 for Animal Handling\n 2 for Athletics\n 3 for Intimidation\n 4 for Nature\n 5 for Perception\n 6 for Survival\n")
            option = int(input("Type your answer: "))
            if option == 0:
                print("Option is 0")
            elif option == 1:
                AnimalHandling += cache
            elif option == 2:
                Athletics += cache
            elif option == 3:
                Intimidation += cache
            elif option == 4:
                Nature += cache
            elif option == 5:
                Perception += cache
            elif option == 6:
                Survival += cache
            else:
                print("Error: Something went wrong")

    elif temp_c == 2:
        Class = "Bard"
        for i in range(3):
               print("Because you've chosen Bard, You gain proficency in three skills of your choice. \n 1 for Athletics\n 2 for Acrobatics\n 3 for Sleight of Hand\n 4 for Stealth\n 5 for Arcana\n 6 for History\n 7 for Investigation\n 8 for Nature\n 9 for Religion\n 10 for Animal Handling\n 11 for Insight\n 12 for Medicine\n 13 for Perception\n 14 for Survival\n 15 for Deception\n 16 for Intimidation\n 17 for Performance\n 18 for Persuasion\n")
               option = int(input("Type your answer: "))
               if option == 1:
                   Athletics += cache
               elif option == 2:
                   Acrobatics += cache
               elif option == 3:
                   SleightOfHand += cache
               elif option == 4:
                   Stealth += cache
               elif option == 5:
                   Arcana += cache
               elif option == 6:
                   History += cache
               elif option == 7:
                   Investigation += cache
               elif option == 8:
                   Nature += cache
               elif option == 9:
                   Religion += cache
               elif option == 10:
                   AnimalHandling += cache
               elif option == 11:
                   Insight += cache
               elif option == 12:
                   Medicine += cache
               elif option == 13:
                   Perception += cache
               elif option == 14:
                   Survival += cache
               elif option == 15:
                   Deception += cache
               elif option == 16:
                   Intimidation += cache
               elif option == 17:
                   Performance += cache
               elif option == 18:
                   Persuasion += cache
               else:
                   print("Error: Somethng went wrong")

    elif temp_c == 3:
        Class = "Cleric"
        for i in range(2):
            #edit the line below
            print("Because you've chosen Cleric, you gain proficency in two of these skills.\n 1 for History\n 2 for Insight\n 3 for Medicine\n 4 for Persuasion\n 5 for Religion\n")
            option = int(input("Type your answer: "))
            if option == 1:
                History += cache
            elif option == 2:
                Insight += cache
            elif option == 3:
                Medicine += cache
            elif option == 4:
                Persuasion += cache
            elif option == 5:
                Religion += cache
            else:
                print("Error: Something went wrong")
    elif temp_c == 4:
        Class = "Druid"
        for i in range(2):
            #edit the line below
            print("Because you've chosen Druid, you gain proficency in two of these skills.\n 1 for Arcana\n 2 for Animal Handling\n 3 for Insight\n 4 for Medicine\n 5 for Nature\n 6 for Perception\n 7 for Religion\n 8 for Survival\n")
            option = int(input("Type your answer: "))
            if option == 1:
                Arcana += cache
            elif option == 2:
                AnimalHandling += cache
            elif option == 3:
                Insight += cache
            elif option == 4:
                Medicine += cache
            elif option == 5:
                Nature += cache
            elif option == 6:
                Perception += cache
            elif option == 7:
                Religion += cache
            elif option == 8:
                Survival += cache
            else:
                print("Error: Something went wrong")

    elif temp_c == 5:
            Class = "Fighter"
            #not finished
            print("Because you've chosen Fighter, you gain proficeny in two of these skills.\n 1 for Acrobatics\n 2 for Animal Handling\n 3 for Athletics\n 4 for History\n 5 for Insight\n 6 for Intimidation\n 7 for Perception\n 8 for Survival\n")
            option = int(input("Type your answer: "))
            if option == 1:
                Arcana += cache
            elif option == 2:
                AnimalHandling += cache
            elif option == 3:
                Insight += cache
            elif option == 4:
                Medicine += cache
            elif option == 5:
                Nature += cache
            elif option == 6:
                Perception += cache
            elif option == 7:
                Religion += cache
            elif option == 8:
                Survival += cache
            else:
                print("Error: Something went wrong")

    elif temp_c == 6:
            Class = "Monk"
            #not finished
            print("Because you've chosen Druid, you can increase 2 ability scores by 1.\n 1 for Animal Handling\n 2 for Athletics\n 3 for Intimidation\n 4 for Nature\n 5 for Perception\n 6 for Survival\n")
            option = int(input("Type your answer: "))
            if option == 1:
                Arcana += cache
            elif option == 2:
                AnimalHandling += cache
            elif option == 3:
                Insight += cache
            elif option == 4:
                Medicine += cache
            elif option == 5:
                Nature += cache
            elif option == 6:
                Perception += cache
            elif option == 7:
                Religion += cache
            elif option == 8:
                Survival += cache
            else:
                print("Error: Something went wrong")


    elif temp_c == 7:
        Class = "Paladin"
    elif temp_c == 8:
        Class = "Ranger"
    elif temp_c == 9:
        Class = "Rogue"
    elif temp_c == 10:
        Class = "Sorcerer"
    elif temp_c == 11:
        Class = "Warlock"
    elif temp_c == 12:
        Class = "Wizard"
    else:
        print("Something went wrong.")


#This function generate a random number (would roll a dice) in order to get the ability scores
def rollDice():
    
    numArray = array ('i',[])

    for i in range(4): 
        num = random.randint(1,6)
        numArray.append(num)

    numArray = sorted(numArray)
    highest_sum = numArray[1] + numArray[2] + numArray[3] 
    return highest_sum

#This function would save the character in the characters.txt
def saveChar():
    file = open("characters.txt", "a")
    save = str(char.name) + " , " + str(char.race) + " , " + str(char.Class) + " , " + str(char.level) + " , " + str(char.Strength) + " , " + str(char.Dexterity) + " , " + str(char.Constitution) + " , " + str(char.Wisdom) + " , " + str(char.Intelligence) + " , " + str(char.Charisma) + "\n"
    file.write(save)


def StrengthConversion():
    
    if strength == 1:
        Athletics = -5

    elif strength == 2 or strength == 3:
        Athletics = -4

    elif strength == 4 or strength == 5:
        Athletics = -3

    elif strength == 6 or strength == 7:
        Athletics = -2

    elif strength == 8 or strength == 9:
        Athletics = -1

    elif strength == 10 or strength == 11:
        Athletics = 0

    elif strength == 12 or strength == 13:
        Athletics = 1

    elif strength == 14 or strength == 15:
        Athletics = 2

    elif strength == 16 or strength == 17:
        Athletics = 3

    elif strength == 18 or strength == 19:
        Athletics = 4

    elif strength >= 20:
         Athletics = 5

def DexterityConversion():
    if dexterity == 1:
        Acrobatics  = -5
        SleightOfHand = -5
        Stealth = -5

    elif dexterity == 2 or dexterity == 3:
        Acrobatics = -4
        SleightOfHand = -4
        Stealth = -4

    elif dexterity == 4 or dexterity == 5:
        Acrobatics = -3
        SleightOfHand = -3
        Stealth = -3

    elif dexterity == 6 or dexterity == 7:
        Acrobatics = -2
        SleightOfHand = -2
        Stealth = -2

    elif dexterity == 8 or dexterity == 9:
        Acrobatics = -1
        SleightOfHand = -1
        Stealth = -1

    elif dexterity == 10 or dexterity == 11:
        Acrobatics = 0
        SleightOfHand = 0
        Stealth = 0

    elif dexterity == 12 or dexterity == 13:
        Acrobatics = 1
        SleightOfHand = 1
        Stealth = 1

    elif dexterity == 14 or dexterity == 15:
        Acrobatics = 2
        SleightOfHand = 2
        Stealth = 2

    elif dexterity == 16 or dexterity == 17:
        Acrobatics = 3
        SleightOfHand = 3
        Stealth = 3

    elif dexterity == 18 or dexterity == 19:
        Acrobatics = 4
        SleightOfHand = 4
        Stealth = 4

    elif dexterity >= 20:
        Acrobatics = 5
        SleightOfHand = 5
        Stealth = 5
        
def IntelligenceConversion():
    if intelligence == 1:
        Arcana = -5
        History = -5
        Investigation = -5
        Nature = -5
        Religion = -5

    elif intelligence == 2 or intelligence == 3:
        Arcana = -4
        History = -4
        Investigation = -4
        Nature = -4
        Religion = -4

    elif intelligence == 4 or intelligence == 5:
        Arcana = -3
        History = -3
        Investigation = -3
        Nature = -3
        Religion = -3

    elif intelligence == 6 or intelligence == 7:
        Arcana = -2
        History = -2
        Investigation = -2
        Nature = -2
        Religion = -2

    elif intelligence == 8 or intelligence == 9:
        Arcana = -1
        History = -1
        Investigation = -1
        Nature = -1
        Religion = -1

    elif intelligence == 10 or intelligence == 11:
        Arcana = 0
        History = 0
        Investigation = 0
        Nature = 0
        Religion = 0

    elif intelligence == 12 or intelligence == 13:
        Arcana = 1
        History = 1
        Investigation = 1
        Nature = 1
        Religion = 1

    elif intelligence == 14 or intelligence == 15:
        Arcana = 2
        History = 2
        Investigation = 2
        Nature = 2
        Religion = 2

    elif intelligence == 16 or intelligence == 17:
        Arcana = 3
        History = 3
        Investigation = 3
        Nature = 3
        Religion = 3

    elif intelligence == 18 or intelligence == 19:
        Arcana = 4
        History = 4
        Investigation = 4
        Nature = 4
        Religion = 4

    elif intelligence >= 20:
        Arcana = 5
        History = 5
        Investigation = 5
        Nature = 5
        Religion = 5

def WisdomConversion():
    if wisdom == 1:
        AnimalHandling = -5
        Insight = -5
        Medicine = -5
        Perception = -5
        Survival = -5

    elif wisdom == 2 or wisdom == 3:
        AnimalHandling = -4
        Insight = -4
        Medicine = -4
        Perception = -4
        Survival = -4

    elif wisdom == 4 or wisdom == 5:
        AnimalHandling = -3
        Insight = -3
        Medicine = -3
        Perception = -3
        Survival = -3

    elif wisdom == 6 or wisdom == 7:
        AnimalHandling = -2
        Insight = -2
        Medicine = -2
        Perception = -2
        Survival = -2

    elif wisdom == 8 or wisdom == 9:
        AnimalHandling = -1
        Insight = -1
        Medicine = -1
        Perception = -1
        Survival = -1

    elif wisdom == 10 or wisdom == 11:
        AnimalHandling = 0
        Insight = 0
        Medicine = 0
        Perception = 0
        Survival = 0

    elif wisdom == 12 or wisdom == 13:
        AnimalHandling = 1
        Insight = 1
        Medicine = 1
        Perception = 1
        Survival = 1

    elif wisdom == 14 or wisdom == 15:
        AnimalHandling = 2
        Insight = 2
        Medicine = 2
        Perception = 2
        Survival = 2

    elif wisdom == 16 or wisdom == 17:
        AnimalHandling = 3
        Insight = 3
        Medicine = 3
        Perception = 3
        Survival = 3

    elif wisdom == 18 or wisdom == 19:
        AnimalHandling = 4
        Insight = 4
        Medicine = 4
        Perception = 4
        Survival = 4

    elif wisdom >= 20:
        AnimalHandling = 5
        Insight = 5
        Medicine = 5
        Perception = 5
        Survival = 5

def CharismaConversion():
    if charisma == 1:
        Deception = -5
        Intimidation = -5
        Performance = -5
        Persuasion = -5


    elif charisma == 2 or charisma == 3:
        Deception = -4
        Intimidation = -4
        Performance = -4
        Persuasion = -4


    elif charisma == 4 or charisma == 5:
        Deception = -3
        Intimidation = -3
        Performance = -3
        Persuasion = -3


    elif charisma == 6 or charisma == 7:
        Deception = -2
        Intimidation = -2
        Performance = -2
        Persuasion = -2


    elif charisma == 8 or charisma == 9:
        Deception = -1
        Intimidation = -1
        Performance = -1
        Persuasion = -1


    elif charisma == 10 or charisma == 11:
        Deception = 0
        Intimidation = 0
        Performance = 0
        Persuasion = 0


    elif charisma == 12 or charisma == 13:
        Deception = 1
        Intimidation = 1
        Performance = 1
        Persuasion = 1


    elif charisma == 14 or charisma == 15:
        Deception = 2
        Intimidation = 2
        Performance = 2
        Persuasion = 2


    elif charisma == 16 or charisma == 17:
        Deception = 3
        Intimidation = 3
        Performance = 3
        Persuasion = 3


    elif charisma == 18 or charisma == 19:
        Deception = 4
        Intimidation = 4
        Performance = 4
        Persuasion = 4

    elif charisma >= 20:
        Deception = 5
        Intimidation = 5
        Performance = 5
        Persuasion = 5

def LevelConversion():
    global cache
    global lvl

    if lvl == 1:
        cache = 2

    elif lvl == 2:
        cache = 2

    elif lvl == 3:
        cache = 2

    elif lvl == 4:
        cache = 2

    elif lvl == 5:
        cache = 3

    elif lvl == 6:
        cache = 3

    elif lvl == 7:
        cache = 3

    elif lvl == 8:
        cache = 3

    elif lvl == 9:
        cache = 4

    elif lvl == 10:
        cache = 4

    elif lvl == 11:
        cache = 4

    elif lvl == 12:
        cache = 4

    elif lvl == 13:
        cache = 5

    elif lvl == 14:
        cache = 5

    elif lvl == 15:
        cache = 5

    elif lvl == 16:
        cache = 5

    elif lvl == 17:
        cache = 6

    elif lvl == 18:
        cache = 6

    elif lvl == 19:
        cache = 6

    elif lvl == 20:
        cache = 6

    else:
        Error()

def Error():
    print("There was an unknown error. Please try again")
    quit()


def CharacterCreation():
    global temp_r
    global temp_c
    global char
    global temp_str2
    global temp_dex2
    global temp_const2
    global temp_wis2
    global temp_intelli2
    global temp_charisma2
    global lvl

    name = str(input("Character name: "))
    temp_r = int(input("\nChoose a race\n 1 - Dragonborn\n 2 - Dwarf\n 3 - Elf\n 4 - Gnome\n 5 - Half-Elf\n 6 - Halfling\n 7 - Half-Orc\n 8 - Human\n 9 - Tiefling\n Type your answer: "))
    temp_c = int(input("\nChoose a class\n 1 - Barbarian\n 2 - Bard\n 3 - Cleric\n 4 - Druid\n 5 - Fighter\n 6 - Monk\n 7 - Paladin\n 8 - Ranger\n 9 - Rogue\n 10 - Sorcerer\n 11 - Warlock\n 12 - Wizard\n Type your answer: "))
    lvl = int(input("Set the level: "))

    raceTranslation()

    temp_strength = rollDice()
    strength = temp_strength + temp_str2

    temp_dexterity = rollDice()
    dexterity = temp_dexterity + temp_dex2

    temp_constitution = rollDice()
    constitution = temp_constitution + temp_const2

    temp_wisdom = rollDice()
    wisdom = temp_wisdom + temp_wis2

    temp_intelligence = rollDice()
    intelligence = temp_intelligence + temp_intelli2

    temp_charisma = rollDice()
    charisma = temp_charisma + temp_charisma2

    LevelConversion()

    classTranslation()

    char = Character(name, race, Class, lvl, strength, dexterity, constitution, wisdom, intelligence, charisma)

    saveChar()


Menu()

