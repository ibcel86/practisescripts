import random
import os

# Game selections 
ROCK     = 'rock'
PAPER    = 'paper'
SCISSORS = 'scissors'
RESET    = 'reset'

# Randomiser for computer to select choice
def get_computer_rps():
    random_int = random.randint(1, 3)
    if random_int == 1:
        return ROCK
    if random_int == 2:
        return PAPER
    return SCISSORS

# User selection
def get_user_rps():
    selection = ''
    while selection not in [ROCK, PAPER, SCISSORS, RESET]:
        selection = input('Enter rock, paper, or scissors (or type "reset" to reset scores): ').lower()
    return selection

# Reset score function that saves files into current working directory 
def reset_scores():
    base_dir = os.path.join(os.getcwd(), "Scores")
    uscore_path = os.path.join(base_dir, "uscore.txt")
    cscore_path = os.path.join(base_dir, "cscore.txt")
    os.makedirs(base_dir, exist_ok=True)
    with open(uscore_path, "w") as uscore_file, open(cscore_path, "w") as cscore_file:
        uscore_file.write("0")
        cscore_file.write("0")
    print("Scores have been reset to 0.")

# Checks results and declares winner
def result_check(user, computer):
    base_dir = os.path.join(os.getcwd(), "Scores")
    uscore_path = os.path.join(base_dir, "uscore.txt")
    cscore_path = os.path.join(base_dir, "cscore.txt")
    os.makedirs(base_dir, exist_ok=True)
    if not os.path.exists(uscore_path):
        with open(uscore_path, "w") as uscore_file:
            uscore_file.write("0")
    if not os.path.exists(cscore_path):
        with open(cscore_path, "w") as cscore_file:
            cscore_file.write("0")

    if user == computer:
        print("It's a tie!")
        return None 
    elif (user == PAPER and computer == ROCK) or \
         (user == ROCK and computer == SCISSORS) or \
         (user == SCISSORS and computer == PAPER):
        with open(uscore_path, "r+") as uscore_file:
            user_score = int(uscore_file.read())
            user_score += 1
            uscore_file.seek(0)
            uscore_file.write(str(user_score))
        print("You win!")
        return "user"
    else:
        with open(cscore_path, "r+") as cscore_file:
            computer_score = int(cscore_file.read())
            computer_score += 1
            cscore_file.seek(0)
            cscore_file.write(str(computer_score))
        print("The computer wins!")
        return "computer"

# Function to display scores at the end of each round
def display_scores():
    base_dir = os.path.join(os.getcwd(), "Scores")
    uscore_path = os.path.join(base_dir, "uscore.txt")
    cscore_path = os.path.join(base_dir, "cscore.txt")
    with open(uscore_path, "r") as current_uscore, open(cscore_path, "r") as current_cscore:
        report_uscore = int(current_uscore.read())
        report_cscore = int(current_cscore.read())
        print(f"The current scores are user {report_uscore} point(s) and computer {report_cscore} point(s)")

# Iterates best of three so the code executes three times until either the computer or user wins
def main():
    reset_scores()
    user_wins = 0
    computer_wins = 0

    while user_wins < 2 and computer_wins < 2:
        for _ in range(3):
            user_choice = get_user_rps()

            if user_choice == RESET:
                reset_scores()
                return

            computer_choice = get_computer_rps()
            winner = result_check(user_choice, computer_choice)

            if winner == "user":
                user_wins += 1
            elif winner == "computer":
                computer_wins += 1

            display_scores()

            if user_wins == 2:
                print("User wins the best of three!")
                break
            elif computer_wins == 2:
                print("Computer wins the best of three!")
                break

        if user_wins == 2 or computer_wins == 2:
            break

    reset_scores()

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes" or play_again == "y":
        main()
    elif play_again == "no" or play_again == "n":
        print("Game has ended")
        reset_scores()

main()
    
