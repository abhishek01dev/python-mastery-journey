# Day 01 – Syntax, Indentation & PEP8

## 📌 What I Learned Today

Today marks the beginning of my Python journey! I learned that Python's syntax is designed to be readable and clean. Unlike other languages, Python uses **indentation** (whitespace) to define code blocks instead of curly braces. I also discovered **PEP 8** — the official style guide that keeps Python code consistent across the community.

## 🧠 Key Concepts

- **Python Syntax**: Python reads like English. Statements end at the newline (no semicolons needed).
- **Indentation**: Python uses 4 spaces (not tabs!) to define blocks of code. Wrong indentation = `IndentationError`.
- **Comments**: Use `#` for single-line and `'''` or `"""` for multi-line/docstrings.
- **PEP 8**: The official style guide — covers naming conventions, line length (79 chars), spacing, and more.
- **print()**: The built-in function for outputting text to the console.

## 💻 Code Example

```python
# This is a comment — Python ignores it

# print() outputs text to the console
print("Hello, Python!")       # My very first Python line!

# Variables follow snake_case naming (PEP 8)
my_name = "Abhishek"
my_age = 25

# Indentation matters — this is how Python knows what's inside the if block
if my_age >= 18:
    print(f"{my_name} is an adult")    # 4 spaces = 1 level of indentation
    print("Welcome to Python!")         # Same level = same block
else:
    print("Keep learning!")

# Docstrings describe what a function does
def greet(name):
    """This function greets the user by name."""
    print(f"Hello, {name}! Welcome to the Python Mastery Journey 🐍")

greet("World")
```

## ⚠️ Common Mistakes / Gotchas

- **Mixing tabs and spaces**: Always use 4 spaces. Never mix tabs and spaces — it causes `IndentationError`.
- **Forgetting the colon `:` after `if`, `for`, `def`**: Python expects a colon before an indented block.
- **Using `Print()` instead of `print()`**: Python is case-sensitive! Built-in functions are lowercase.
- **Ignoring PEP 8**: Your code works without it, but following PEP 8 makes it readable for everyone.

## 📊 Quick Reference Table

| Topic | Rule | Example |
|:------|:-----|:--------|
| Indentation | 4 spaces per level | `if x:\n    print(x)` |
| Naming | snake_case for variables/functions | `my_variable = 10` |
| Naming | PascalCase for classes | `class MyClass:` |
| Line Length | Max 79 characters | Keep lines short |
| Comments | Use `#` with a space after | `# This is good` |
| Docstrings | Triple quotes for functions | `"""Describes the function"""` |

## 🔗 Resources

- [Official Python Docs](https://docs.python.org/3/tutorial/)
- [PEP 8 — Style Guide](https://peps.python.org/pep-0008/)
- [Python.org — Getting Started](https://www.python.org/about/gettingstarted/)

## ✅ Status: Completed on 25-03-2026
