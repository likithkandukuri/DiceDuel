import random
import time

def roll_dice():
    return random.randint(1, 6)

def pause():
    time.sleep(1)

player_score = 0
computer_score = 0
WIN_SCORE = 100

print("Welcome to Dice Duel.")
print("First to 100 points wins.")
print("On your turn, roll or hold.")
print("If you roll a 1, you lose your round points.")
input("\nPress Enter to start the game...")

while player_score < WIN_SCORE and computer_score < WIN_SCORE:

    print("\n----------------------------------")
    print("Your total score:", player_score)
    print("Computer total score:", computer_score)

    round_score = 0
    turn_over = False

    while not turn_over:
        choice = input("\nRoll or hold? (r/h): ").lower()

        if choice == "r":
            roll = roll_dice()
            print("You rolled:", roll)
            pause()

            if roll == 1:
                print("You lose the points for this round.")
                round_score = 0
                turn_over = True
            else:
                round_score += roll
                print("Current round score:", round_score)

        elif choice == "h":
            player_score += round_score
            print("You decide to hold.")
            print("Your new total score:", player_score)
            turn_over = True
        else:
            print("Please type r or h.")

    if player_score >= WIN_SCORE:
        break

    print("\nComputer's turn.")
    pause()

    round_score = 0
    risk_limit = random.randint(12, 20)

    while True:
        roll = roll_dice()
        print("Computer rolled:", roll)
        pause()

        if roll == 1:
            print("Computer loses the round points.")
            round_score = 0
            break
        else:
            round_score += roll

        if round_score >= risk_limit:
            print("Computer decides to hold.")
            break

    computer_score += round_score
    print("Computer total score:", computer_score)

print("\n==================================")
print("Game Over")

if player_score >= WIN_SCORE:
    print("You win. That was a solid game.")
else:
    print("Computer wins. It played smart this time.")
