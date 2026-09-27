"""
Module 1: Input and Game Setup
Rock-Paper-Scissors Project

This module handles:
- Game rules
- Available choices
- User input validation
- Play-again input validation
"""

CHOICES = ["Rock", "Paper", "Scissors"]


def display_rules():
    """Display the rules of Rock-Paper-Scissors."""
    print("Welcome to Rock-Paper-Scissors!\n")
    print("Winning Rules:")
    print("Rock vs Paper -> Paper wins")
    print("Rock vs Scissors -> Rock wins")
    print("Paper vs Scissors -> Scissors wins\n")


def get_user_choice():
    """Get and validate the user's choice."""
    print("Choose an option:")
    print("1 - Rock")
    print("2 - Paper")
    print("3 - Scissors")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid number.\n")
        return None

    while choice < 1 or choice > 3:
        try:
            choice = int(input("Please enter a valid choice (1-3): "))
        except ValueError:
            print("Please enter a valid number.")
            continue

    return choice


def get_replay_choice():
    """Ask the user whether they want to play another round."""
    while True:
        ans = input("\nDo you want to play again? (Y/N): ").lower()

        if ans in ["y", "n"]:
            return ans

        print("Please enter Y or N.")
