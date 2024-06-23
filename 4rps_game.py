import random

def main():
    """
    This function runs the rock paper scissors game against the computer.
    """
    print("Welcome to the Rock-Paper-Scissors!")
    choices = {
        "0": "Rock",
        "1": "Paper",
        "2": "Scissors"
    }
    while True:  # creates an infinite loop till user decides to quit
        while True:
            user_input = input("Enter your choice (0 for Rock, 1 for Paper, 2 for Scissors): ")
            if user_input in choices:
                break
            else:
                print("Invalid input. Please enter '0', '1', or '2'")
        user_choice = choices[user_input]
        computer_input = str(random.randint(0, 2))  # this generates random integer between 0 to 2 for computer's choice
        computer_choice = choices[computer_input]

        win_conditions = {
            "Rock": "Scissors",
            "Paper": "Rock",
            "Scissors": "Paper"
        }

        if win_conditions[user_choice] == computer_choice:
            print(f"You win! {user_choice} beats {computer_choice}")
        elif user_choice == computer_choice:
            print(f"It's a tie! Both chose {user_choice}")
        else:
            print(f"Computer wins! {computer_choice} beats {user_choice}")

        play_again = input("Play again? (Y/N): ").lower()
        if play_again != "y" and play_again != "n":
            print("Invalid input. Please enter 'Y' or 'N'.")
        elif play_again != "y":
            print("Thank you for playing!")
            break

if __name__ == "__main__":
    main()
