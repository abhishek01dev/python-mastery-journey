# 🤝 Contributing to Python Mastery Journey

First off, **thank you** for considering contributing! This project thrives because of community support.

---

## 📋 Table of Contents

- [How Can You Contribute?](#-how-can-you-contribute)
- [Getting Started](#-getting-started)
- [Contribution Guidelines](#-contribution-guidelines)
- [Commit Message Convention](#-commit-message-convention)
- [Code Style](#-code-style)
- [Reporting Issues](#-reporting-issues)
- [Suggesting New Topics](#-suggesting-new-topics)
- [Code of Conduct](#-code-of-conduct)

---

## 💡 How Can You Contribute?

| Type | Description |
|:-----|:------------|
| 🐛 **Bug Fix** | Found a typo, broken link, or code error? Fix it! |
| 📝 **Content Improvement** | Better explanations, more examples, clearer notes |
| 🆕 **New Topics** | Suggest or add topics not yet covered |
| 🎨 **Design** | Improve README formatting, badges, or visuals |
| 📖 **Documentation** | Improve repo-level docs or add guides |
| 💻 **Code Examples** | Add alternative solutions or better examples |

---

## 🚀 Getting Started

1. **Fork** this repository
2. **Clone** your fork locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/python-mastery-journey.git
   cd python-mastery-journey
   ```
3. **Create a new branch** for your changes:
   ```bash
   git checkout -b feature/your-improvement
   ```
4. **Make your changes** following the guidelines below
5. **Commit** with a meaningful message (see convention below)
6. **Push** to your fork:
   ```bash
   git push origin feature/your-improvement
   ```
7. **Open a Pull Request** against the `main` branch

---

## 📏 Contribution Guidelines

### For Notes (`notes.md`)
- Follow the existing template structure exactly
- Write in a student-friendly tone — explain like you're teaching a friend
- Include at least one code example
- Mention common mistakes/gotchas
- Add relevant resource links

### For Code Files (`.py`)
- Add comments explaining important lines
- Keep code simple and focused on the topic
- Use meaningful variable/function names
- Include example output as comments at the bottom

### For Phase READMEs
- List all days covered with links
- Include learning outcomes
- Keep the format consistent with existing phase READMEs

---

## 💬 Commit Message Convention

Use this format for commit messages:

```
<emoji> <type>: <short description>

Examples:
✅ Day XX: Variables & Data Types — added notes and code
🐛 fix: corrected typo in day_05 notes.md
📝 docs: improved README badges section
🆕 add: new project — password generator
🎨 style: reformatted day_10 code examples
```

### Emoji Guide

| Emoji | Type | Usage |
|:-----:|:-----|:------|
| ✅ | day | New daily topic content |
| 🐛 | fix | Bug fixes, typo corrections |
| 📝 | docs | Documentation improvements |
| 🆕 | add | New content or features |
| 🎨 | style | Formatting, no code change |
| ♻️ | refactor | Code restructuring |
| 🗑️ | remove | Removing files or content |

---

## 🎨 Code Style

- **Python version:** 3.8+
- **Indentation:** 4 spaces (no tabs)
- **Naming:** snake_case for variables/functions, PascalCase for classes
- **Docstrings:** Use triple-quoted strings for function documentation
- **Line length:** Keep lines under 80 characters where possible
- Follow [PEP 8](https://peps.python.org/pep-0008/) guidelines

```python
# ✅ Good
def calculate_area(length, width):
    """Calculate the area of a rectangle."""
    return length * width

# ❌ Bad
def calcArea(l, w):
    return l*w
```

---

## 🐛 Reporting Issues

Found a problem? [Open an issue](https://github.com/abhishek01dev/python-mastery-journey/issues/new) with:

1. **Title:** Clear, concise description
2. **Description:** What's wrong and where (include file path)
3. **Expected:** What it should be
4. **Actual:** What it currently is
5. **Screenshot** (if applicable)

---

## 💡 Suggesting New Topics

Have an idea for a topic not covered? Open an issue with:

- **Title:** `[Topic Suggestion] Your Topic Name`
- **Description:** What the topic covers and why it's valuable
- **Level:** Beginner / Intermediate / Advanced
- **Phase:** Where it fits in the roadmap

---

## 📜 Code of Conduct

- Be **respectful** and **constructive** in all interactions
- Welcome **beginners** — everyone starts somewhere
- Focus on **learning** and **helping** others
- No spam, self-promotion, or off-topic content
- Follow GitHub's [Community Guidelines](https://docs.github.com/en/site-policy/github-terms/github-community-guidelines)

---

<p align="center">
  <strong>Every contribution, no matter how small, makes this resource better for everyone. 🙏</strong>
</p>
