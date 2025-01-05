import random

"""
This code generates a quiz with math problems. The user can select the language and level of difficulty. 
The code provides feedback on the user's answers and displays their score at the end.
"""


def quiz():
    # List of possible operations
    operations = ["+", "-", "*", "/", "//", "^", "%"]

    # Dictionary mapping operation symbols to corresponding operations
    operation_functions = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y,
        "//": lambda x, y: x // y,
        "^": lambda x, y: x ** y,
        "%": lambda x, y: x % y
    }

    # Prompt the user to select a language
    lang = input("Choose a language (E/H)? : ")

    # Import the language
     if lang in ["E", "e"]:
        from english import welcome_msg, level, correct, incorrect
    elif lang in ["H", "h"]:
        from hebrew import welcome_msg, level, correct, incorrect
    else:
        print("Invalid language selection. Defaulting to English.")
        from english import welcome_msg, level, correct, incorrect

    # Prompt the user for the number of questions and the level of difficulty
    while True:
        try:
            questions_num = int(input(welcome_msg))
            if questions_num < 1:
                raise ValueError("Number of questions must be positive and at least 1.")
            break
        except ValueError as e:
            print(f"Error: {e}.")

    while True:
        try:
            quiz_level = int(input(level))
            if quiz_level < 1:
                raise ValueError("Difficulty level must be positive and at least 1.")
            break
        except ValueError as e:
            print(f"Error: {e}.")

    # Determine the range of numbers to use based on the selected level
    if level == 1:
        low = 2
        high = 10
    elif level == 2:
        low = 10
        high = 20
    else:
        low = 20
        high = 40

    # Generate and solve the requested number of math problems
    print()
    count_correct = 0

    for i in range(questions_num):
        operation = random.choice(operations)
        num1 = random.randint(low, high)
        num2 = random.randint(low, high)

        # Get the function corresponding to the chosen operation
        op_func = operation_functions[operation]

        # Perform the operation on the numbers
        result = float(op_func(num1, num2))

        # Print the problem and the result
        while True:
            try:
                user_answer = float(input(f"{i + 1}) {num1} {operation} {num2} = ?\n"))
                break
            except ValueError:
                print("Please enter a valid number.")

        if user_answer == result:
            print(random.choice(correct), "\n")
            count_correct += 1
        else:
            print(random.choice(incorrect), "\n")

    # Print the final score
    print(f"You answered {count_correct}/{questions_num} Questions Correctly.")


quiz()
