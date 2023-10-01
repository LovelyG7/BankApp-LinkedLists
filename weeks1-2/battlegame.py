#TASK 1
#indices of character stats list
name_i = 0
hp_i = 1
damage_i = 2

#name variables
Wizard ="Wizard"
Elf = "Elf"
Human = "Human"
Dragon = "Dragon"

#health variables
wizard_hp = 70
elf_hp = 100
human_hp = 150
dragon_hp = 300

#damage variables
wizard_damage = 150
elf_damage = 100
human_damage = 20
dragon_damage = 50 

#creating character stats lists
wizard_stats = [Wizard, wizard_hp, wizard_damage]
elf_stats = [Elf, elf_hp, elf_damage]
human_stats = [Human, human_hp, human_damage]
dragon_stats = [Dragon, dragon_hp, dragon_damage]


#TASK 2 & 3
# user input of character choice
print("1)" + Wizard)
print("2)" + Elf)
print("3)"+ Human)
character_chosen = input("Choose your you character:")

if character_chosen == "1":
    character_stats = wizard_stats
elif character_chosen == "2": 
    character_stats = elf_stats
elif character_chosen == "3":
    character_stats = human_stats
else: 
    print("Unknown character")
print("You have chosen:" + character_stats[name_i])
print("Health: "+ str(character_stats[hp_i]))
print("Damage: "+ str(character_stats[damage_i]))

#TASK 4
#character attacks dragon
while True:
    dragon_stats[hp_i] = dragon_stats[hp_i] - character_stats[damage_i]
    print("The ", character_stats[name_i], "damaged the Dragon!")
    print("The Dragon's hitpoints are now: ", str(dragon_stats[hp_i]))
 
    #Check dragon points
    if dragon_stats[hp_i] <= 0:
        print("The Dragon has lost the battle!")
        break 
    #dragon attacks character
    character_stats[hp_i]= character_stats[hp_i] - dragon_stats[damage_i]
    print("The ", dragon_stats[name_i], "strikes back at the ", character_stats[name_i])
    print("The ", character_stats[name_i], "'s hitpoints are now: ", str(character_stats[hp_i]))

#Check the character points
    if character_stats[hp_i] <= 0:
        print("The ", character_stats[name_i], "has fallen!")
        break

#After completing the task, Deondre mentioned we could have used a dictionary instead of lists
#We would need to change the indices the rest of the code to use it, but it would be cleaner. 
'''
wizard_dict = {
    "Name":"Wizard"
    "hp": 70,
    "damage": 150 }

elf_dict = {
    "Name": "Elf",
    "hp": 100,
    "damage": 100}

human_dict = {
    "Name": "Human",
    "hp": 150,
    "damage": 20}

dragon_dict = {
    "Name": "Dragon"
    "hp": 300, 
    "damage": 50}
'''