# TASK 1

# Deondre realized this was better than a list :)
wizard_dict = {
    "Name": "Wizard",
    "hp": 70,
    "damage": 150}
elf_dict = {
    "Name": "Elf",
    "hp": 100,
    "damage": 100}
human_dict = {
    "Name": "Human",
    "hp": 150,
    "damage": 20}
dragon_dict = {
    "Name": "Dragon",
    "hp": 300,
    "damage": 50}
​
# Our previous idea
# wizard_stats = [wizard, wizard_hp, wizard_damage]
# elf_stats = [elf, elf_hp, elf_damage]
# human_stats = [human, human_hp, human_damage]
# dragon_stats = [dragon, dragon_hp, dragon_damage]
​
# TASK 2 & 3
# user input of character choice
while True:
    print("1) ", wizard_dict["Name"])
    print("2) ", elf_dict["Name"])
    print("3) ", human_dict["Name"])
    character_chosen = input("Choose the number of your character: ")
​
    if character_chosen == "1":
        character_dict = wizard_dict
        break
    elif character_chosen == "2":
        character_dict = elf_dict
        break
    elif character_chosen == "3":
        character_dict = human_dict
        break
    else:
        print("Unknown character")
print("You have chosen: " + character_dict["Name"])
print("Health: " + str(character_dict["hp"]))
print("Damage: " + str(character_dict["damage"]))
​
# TASK 4
# character attacks dragon
while True:
    # character attacks dragon
    dragon_dict["hp"] = dragon_dict["hp"] - character_dict["damage"]
    print("The ", character_dict["Name"],
          " damaged the ", dragon_dict["Name"], "!")
    print("The Dragon's hitpoints are now: ", str(dragon_dict["hp"]))
​
    # check dragon points
    if dragon_dict["hp"] <= 0:
        print("The Dragon has lost the battle!")
        break
​
    # dragon attacks character
    character_dict["hp"] = character_dict["hp"] - dragon_dict["damage"]
    print("The ", dragon_dict["Name"],
          "strikes back at the ", character_dict["Name"])
    print("The ", character_dict["Name"], " hitpoints are now: ", str(
        character_dict["hp"]))
​
    # check character points
    if character_dict["hp"] <= 0:
        print("The ", character_dict["Name"], " has fallen!")
        break