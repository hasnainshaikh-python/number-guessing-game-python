
# 🎯 Interactive Number Guessing Game (CLI)

A lightweight, terminal-based number guessing game built in Python. The game generates a random target number, provides real-time directional feedback, validates user inputs against runtime errors, and persistently tracks the best (lowest) attempt score across sessions.

---

## 🚀 Features

* **Dynamic Number Generation:** Generates a pseudo-random integer between 1 and 100 using Python's built-in `random` module.
* **Persistent High Score Tracking:** Reads and updates the best attempt record using local file handling (`history.txt`) with `os.path.exists()` safety checks.
* **Robust Exception Handling:** Uses `try/except ValueError` blocks to catch invalid non-integer inputs without terminating the game loop.
* **Clean Terminal Feedback:** Provides immediate higher/lower guidance to help narrow down the target value efficiently.

---

## 🛠️ Tech Stack

* **Language:** Python 3.x
* **Modules Used:** `random`, `os`
* **Interface:** Command Line Interface (CLI)

---

## 📂 Project Structure

```text
THE NUMBER GUESSING GAME/
│
├── MAIN.py          # Game logic, input validation, and high-score handling
├── history.txt      # Persistent high-score storage file
└── README.md        # Project documentation