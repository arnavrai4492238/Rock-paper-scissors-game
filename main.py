"""
Module 3: Main Program
Rock-Paper-Scissors Project

This module connects Module 1 and Module 2 and controls
the complete game workflow.
"""

from module1_input import display_rules, get_user_choice, get_replay_choice
from module2_game_logic import play_round


def main():
    """Run the Rock-Paper-Scissors game."""
    display_rules()

    while True:
        user_choice = get_user_choice()

        # Restart the input step if the user enters non-numeric input.
        if user_choice is None:
            continue

        play_round(user_choice)

        ans = get_replay_choice()

        if ans == "n":
            break

        print()


if __name__ == "__main__":
    main()
