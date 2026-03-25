# =============================================
# Day 01: Syntax, Indentation & PEP8
# Python Mastery Journey
# =============================================

# --- 1. Your First Python Program ---
# print() is a built-in function that outputs text to the console
print("Hello, Python!")                # Output: Hello, Python!
print("Welcome to the Python Mastery Journey! 🐍")

# --- 2. Comments ---
# Single-line comments start with #
# They are ignored by Python and are for humans reading the code

"""
This is a multi-line comment (actually a string literal).
It's often used as a docstring to document functions and classes.
Python ignores it if it's not assigned to a variable.
"""

# --- 3. Variables (snake_case naming — PEP 8) ---
my_name = "Abhishek"       # str  — text data
my_age = 25                # int  — whole number
my_height = 5.9            # float — decimal number
is_learning = True         # bool — True or False

print(f"Name: {my_name}")
print(f"Age: {my_age}")
print(f"Height: {my_height} ft")
print(f"Currently learning Python: {is_learning}")

# --- 4. Indentation (4 spaces = 1 level) ---
# Indentation defines code blocks in Python
# Wrong indentation causes IndentationError!

if my_age >= 18:
    print(f"{my_name} is an adult")     # This is INSIDE the if block
    print("Can vote and drive! 🚗")     # Same indentation = same block
else:
    print("Still a minor")              # This is INSIDE the else block

# This line is OUTSIDE the if/else — no indentation
print("Moving on...")

# --- 5. PEP 8 Best Practices Demo ---

# ✅ Good: snake_case for variables and functions
user_email = "abhishek@example.com"
total_score = 100


def calculate_average(scores: list[float]):
    """Calculate the average of a list of scores."""  # ← Docstring
    return sum(scores) / len(scores)


# ❌ Bad (avoid these):
# UserEmail = "..."          # PascalCase is for classes, not variables
# totalScore = 100           # camelCase is not Pythonic
# def CalculateAverage():    # Functions should be snake_case

# --- 6. PascalCase for Classes (PEP 8) ---
class StudentProfile:
    """A simple class to demonstrate PascalCase naming."""
    pass


# --- 7. Line Length (max 79 characters recommended) ---
# If a line is too long, break it using parentheses or backslash

long_message = (
    "This is a very long message that would exceed 79 characters, "
    "so we split it across multiple lines using parentheses."
)
print(long_message)

# --- 8. Putting It All Together ---
def greet_user(name, day_number):
    """
    Greet the user and show which day of the journey they are on.
    
    Args:
        name (str): The user's name
        day_number (int): Current day in the journey
    """
    print(f"\n{'='*50}")
    print(f"  Hello, {name}! 👋")
    print(f"  You are on Day {day_number} of Python Mastery Journey")
    print(f"  Keep going — consistency is key! 🔥")
    print(f"{'='*50}\n")


# Call the function
greet_user("Learner", 1)

# --- Output ---
# Hello, Python!
# Welcome to the Python Mastery Journey! 🐍
# Name: Abhishek
# Age: 25
# Height: 5.9 ft
# Currently learning Python: True
# Abhishek is an adult
# Can vote and drive! 🚗
# Moving on...
# ==================================================
#   Hello, Learner! 👋
#   You are on Day 1 of Python Mastery Journey
#   Keep going — consistency is key! 🔥
# ==================================================
