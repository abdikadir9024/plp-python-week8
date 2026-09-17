"""
Final Project: Personal Mini-Toolkit
Description: A menu-driven program providing a calculator, dynamic to-do list, 
             and a number guessing game.
Author: PLP Student
Repository: plp-python-week8
"""

import random

# ==============================================================================
# TOOL IMPLEMENTATIONS
# ==============================================================================

def run_calculator():
    """
    Tool 1: Simple Calculator
    Performs basic arithmetic operations using user input and conditionals.
    """
    print("\n--- [Tool 1: Simple Calculator] ---")
    
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print(" Error: Invalid number entered. Returning to main menu.")
        return

    print("\nChoose Operation:")
    print("  + : Addition")
    print("  - : Subtraction")
    print("  * : Multiplication")
    print("  / : Division")
    operation = input("Enter choice (+, -, *, /): ").strip()

    # Make decisions using conditionals
    if operation == "+":
        result = num1 + num2
        print(f"\nResult: {num1} + {num2} = {result}")
    elif operation == "-":
        result = num1 - num2
        print(f"\nResult: {num1} - {num2} = {result}")
    elif operation == "*":
        result = num1 * num2
        print(f"\nResult: {num1} * {num2} = {result}")
    elif operation == "/":
        if num2 == 0:
            print("\n Error: Division by zero is not allowed.")
        else:
            result = num1 / num2
            print(f"\nResult: {num1} / {num2} = {result}")
    else:
        print(f"\n Error: '{operation}' is not a valid operation.")


def run_todo_list():
    """
    Tool 2: To-Do List Manager
    Uses a dynamic list and a loop to allow users to add, view, and remove tasks.
    """
    tasks = []  # List that changes while the program runs
    
    print("\n--- [Tool 2: To-Do List Manager] ---")
    
    # Sub-menu loop
    while True:
        print("\nTo-Do Menu:")
        print("  1. View Tasks")
        print("  2. Add Task")
        print("  3. Remove Task")
        print("  4. Return to Main Menu")
        
        choice = input("Select an option (1-4): ").strip()

        if choice == "1":
            if not tasks:
                print("\nYour to-do list is currently empty!")
            else:
                print("\nYour Current Tasks:")
                for index, task in enumerate(tasks, start=1):
                    print(f"  {index}. {task}")

        elif choice == "2":
            new_task = input("\nEnter new task: ").strip()
            if new_task:
                tasks.append(new_task)
                print(f" Success: Task '{new_task}' added!")
            else:
                print(" Error: Task cannot be empty.")

        elif choice == "3":
            if not tasks:
                print("\nNo tasks available to remove.")
            else:
                print("\nYour Current Tasks:")
                for index, task in enumerate(tasks, start=1):
                    print(f"  {index}. {task}")
                
                try:
                    task_num = int(input("\nEnter task number to remove: "))
                    if 1 <= task_num <= len(tasks):
                        removed = tasks.pop(task_num - 1)
                        print(f" Success: Task '{removed}' removed!")
                    else:
                        print(" Error: Task number out of range.")
                except ValueError:
                    print(" Error: Please enter a valid number.")

        elif choice == "4":
            print("Returning to main menu...")
            break
        else:
            print(" Error: Invalid sub-menu choice. Please enter 1, 2, 3, or 4.")


def run_guessing_game():
    """
    Tool 3: Number Guessing Game
    Uses a while loop and conditionals to guide the user to guess a secret number.
    """
    secret_number = random.randint(1, 20)
    attempts = 0
    
    print("\n--- [Tool 3: Number Guessing Game] ---")
    print("I have selected a secret number between 1 and 20.")
    print("Can you guess what it is?")

    # Loop until the correct number is guessed
    while True:
        try:
            guess = int(input("\nEnter your guess (1-20): "))
            attempts += 1

            if guess < 1 or guess > 20:
                print(" Please stay within the range of 1 to 20.")
                continue

            # Conditionals to evaluate the guess
            if guess < secret_number:
                print(f" Too low! Attempt #{attempts}. Try again.")
            elif guess > secret_number:
                print(f" Too high! Attempt #{attempts}. Try again.")
            else:
                print(f"\n Congratulations! You found the number {secret_number} in {attempts} attempts!")
                break
        except ValueError:
            print(" Error: Please enter a whole number.")


# ==============================================================================
# MAIN MENU LOOP ROUTINE
# ==============================================================================

def main():
    # Welcoming start message
    print("==================================================")
    print("  WELCOME TO YOUR PERSONAL MINI-TOOLKIT ")
    print("==================================================")
    
    # Loop that runs until the user quits
    while True:
        print("\nMAIN MENU:")
        print("  1. Simple Calculator")
        print("  2. To-Do List Manager")
        print("  3. Number Guessing Game")
        print("  4. Quit")
        
        choice = input("\nPlease choose an option (1-4): ").strip()

        # Routing choices with if / elif / else
        if choice == "1":
            run_calculator()
        elif choice == "2":
            run_todo_list()
        elif choice == "3":
            run_guessing_game()
        elif choice == "4":
            # Friendly goodbye message
            print("\n==================================================")
            print(" Thank you for using the Personal Mini-Toolkit!")
            print(" Goodbye!")
            print("==================================================")
            break
        else:
            # Handling invalid inputs gracefully
            print(f"\n Error: '{choice}' is not a valid menu option.")
            print("Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()