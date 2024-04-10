# Lab 1 Hamid Rezaian 
import random

def play_rock_paper_scissors():
    # de möjliga valen
    choices = ["sten", "sax", "påse"]

    # användarens val
    user_choice = input("Välj sten, sax eller påse: ").lower()

    # Validera användarens val
    if user_choice not in choices:
        print("Ogiltigt val. Vänligen välj sten, sax eller påse.")
        return

    # datorns val
    computer_choice = random.choice(choices)

    # vem är vinnaren
    if user_choice == computer_choice:
        print(f"Det blev oavgjort! Både du och datorn valde {user_choice}.")
    elif (user_choice == "sten" and computer_choice == "sax") or \
         (user_choice == "sax" and computer_choice == "påse") or \
         (user_choice == "påse" and computer_choice == "sten"):
        print(f"Du vann! Du valde {user_choice} och datorn valde {computer_choice}.")
    else:
        print(f"Datorn vann! Du valde {user_choice} och datorn valde {computer_choice}.")

# Spela spelet
play_rock_paper_scissors()