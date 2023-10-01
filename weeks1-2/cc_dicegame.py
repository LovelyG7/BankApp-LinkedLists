import random

def dice_game():
    high_score = 0
 
#Option to roll dice menu

    while True: 
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        score = die1+die2
        
        print("1) Roll Dice!")
        print("2) Exit Game.")
        play = input("Select option 1 or 2: ")
    
        if play == "1": 
            print("You rolled a ...", die1)
            print("You rolled a ... ", die2)
            print("Your current score is",score)

#Update Score   
            if score >= high_score:
                high_score = score
                print("New high score!")
                print("Current High Score: "+ str(high_score))
            else: 
                print("Your highest score is", high_score, "try again?")
    
        elif play == "2":
            print("You have chosen to the leave the game. Good Bye!")
            break
        else:
            print("Please choose only 1 or 2")
dice_game()