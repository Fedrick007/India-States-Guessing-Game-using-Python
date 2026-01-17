# 🇮🇳 India States Guessing Game (Python Turtle)

An interactive **India States Guessing Game** built using **Python Turtle Graphics** and **Pandas**.  
Players guess Indian state names, and correct answers are displayed on the map in real time.

---

## 🎮 Game Features

- Interactive India map using Turtle graphics
- User input popup for guessing states
- Correct guesses appear at exact map coordinates
- Tracks total correct guesses
- Generates a CSV file of states to learn when exiting
- Beginner-friendly and educational

---

## 🛠️ Technologies Used

- Python 3
- Turtle Graphics
- Pandas
- CSV file handling

---

## 📂 Project Structure

```
india-states-game/
│
├── main.py                # Game logic and loop
├── india_states.txt       # States data with x & y coordinates
├── india_map.gif          # India map image
├── States_to_learn.csv    # Generated file for missed states
└── README.md
```

---

## ▶️ How to Run the Game

1. Install Python 3  
2. Install Pandas (if not installed):
   ```
   pip install pandas
   ```
3. Ensure these files are in the same folder:
   - `main.py`
   - `india_states.txt`
   - `india_map.gif`
4. Run the game:
   ```
   python main.py
   ```

---

## 🧠 How the Game Works

- The game displays an outline map of India
- A dialog box asks the player to guess a state name
- If the guess is correct:
  - The state name appears at the correct position on the map
- Type **Exit** anytime to:
  - End the game
  - Generate a `States_to_learn.csv` file containing missed states

---

## 🧠 Learning Outcomes

- Reading and processing CSV files using Pandas
- Working with Turtle screen, shapes, and coordinates
- Handling user input dynamically
- Using lists and condition checks effectively
- Creating educational games with Python

---

## 🚀 Future Improvements

- Add Union Territories
- Timer-based gameplay
- Scoreboard with accuracy percentage
- Hint system
- Sound effects

---

## 📜 License

This project is open-source and created for educational and learning purposes.

---

## 🙌 Author

Developed by **Fedrick Samuel W**  
An educational Python project to learn geography and programming together 🎯
