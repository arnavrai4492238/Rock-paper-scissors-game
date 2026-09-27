# Rock-Paper-Scissors Game

## 1. Project Overview

Rock-Paper-Scissors is a simple command-line game developed using Python.

In this game, the user plays against the computer. The user selects one of three options:

1. Rock
2. Paper
3. Scissors

The computer randomly selects one option, and the program compares both choices to determine whether the user wins, the computer wins, or the result is a tie.

The project is implemented using a modular structure with three Python files.

---

## 2. Problem Statement

Develop a Python-based Rock-Paper-Scissors game that allows a user to play against a computer.

The system should:

- Accept the user's choice.
- Generate the computer's choice randomly.
- Compare the two choices.
- Determine the winner.
- Handle invalid input.
- Allow the user to play multiple rounds.
- Provide a clear command-line interface.

---

## 3. Objectives

The main objectives of this project are:

- To develop an interactive Python-based game.
- To understand and implement conditional statements.
- To use loops for repeated gameplay.
- To use the `random` module.
- To implement input validation and error handling.
- To understand modular programming in Python.
- To divide the program into separate functional modules.

---

## 4. Features

### Game Features

- Rock, Paper, and Scissors choices.
- Random computer choice.
- Automatic winner determination.
- Tie detection.
- Multiple rounds.
- Play-again option.
- Invalid input handling.
- User-friendly command-line interface.

### Programming Features

- Modular Python structure.
- Functions for individual tasks.
- `random` module for computer selection.
- `try-except` for handling invalid numeric input.
- Conditional statements for game logic.
- `while` loops for repeated gameplay.

---

## 5. Technologies Used

| Technology | Purpose |
|---|---|
| Python 3 | Main programming language |
| Random Module | Generates the computer's choice |
| Command Line | User interface |
| Git & GitHub | Version control and project submission |

---

## 6. Project Modules

The project is divided into three major modules.

### Module 1: Input and Game Setup

**File:** `module1_input.py`

This module handles:

- Displaying game rules.
- Storing Rock, Paper, and Scissors.
- Taking the user's choice.
- Validating the user's input.
- Asking whether the user wants to play again.

Main functions:

```python
display_rules()
get_user_choice()
get_replay_choice()
