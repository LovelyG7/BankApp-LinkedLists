import random

diamonds = ["AD","2D", "3D", "4D", "5D", "6D",
            "7D", "8D", "9D", "10D", "JD", "QD", "KD"]

hand = []

while diamonds: 
    play = input("Type 'P' to pick a card or 'Q' to quit: ")
    if play == "Q":
        break 
    elif play =="P": 
       card = random.choice(diamonds)
       hand.append(card) 

       print("Your hand: ",hand)
       diamonds.remove(card)
       print("Remaining cards", diamonds)
    else: 
        print(" Please choose 'P' or 'Q'")

if not diamonds: 
    print("There are no more cards to pick")