"""
Module 2: Game Logic
Rock-Paper-Scissors Project

This module handles:
- Computer's random choice
- Winner determination
- Playing one complete round
"""

import random
from module1_input import CHOICES


def get_computer_choice():
    """Generate a random computer choice."""
    comp_choice = random.randint(1, 3)
    return comp_choice


def determine_winner(user_choice, comp_choice):
    """
    Determine the winner.

    Returns:
        "Tie"              if both choices are the same.
        "User Wins"        if the user wins.
        "Computer Wins"    if the computer wins.
    """
    if user_choice == comp_choice:
        return "Tie"

    user_wins = (
        (user_choice == 1 and comp_choice == 3) or
        (user_choice == 2 and comp_choice == 1) or
        (user_choice == 3 and comp_choice == 2)
    )

    if user_wins:
        return "User Wins"

    return "Computer Wins"


def play_round(user_choice):
    """Play one round and display the result."""
    comp_choice = get_computer_choice()

    user_choice_name = CHOICES[user_choice - 1]
    computer_choice_name = CHOICES[comp_choice - 1]

    print("\nUser choice is:", user_choice_name)
    print("Now it's Computer's Turn...")
    print("Computer choice is:", computer_choice_name)
    print(user_choice_name, "vs", computer_choice_name)

    result = determine_winner(user_choice, comp_choice)

    if result == "Tie":
        print("<== It's a Tie! ==>")
    elif result == "User Wins":
        print("<== User Wins! ==>")
    else:
        print("<== Computer Wins! ==>")

    return result
