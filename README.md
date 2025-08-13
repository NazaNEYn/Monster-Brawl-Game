
# 📜 Description
Monster Brawl is a simple, turn-based combat game written in Python. You play as a powerful monster, fighting against an enemy to prove you are the new king. Choose your class, manage your health, and use a unique one-time superpower to defeat your foe!
<hr>

# ✨ Features
* **Character Selection**: Choose between a "Boss Class" with high health or a "Normal Class" with balanced stats.

* **Turn-Based Combat**: Engage in a battle of attrition where you and your enemy take turns attacking.

* **One-Time Superpower**: Unleash a special attack that deals double damage, but can only be used once per game.

* **Conditional Enemy**: The enemy enters a frenzied state when its health drops below 50%, increasing its aggression.

* **Simple Command** Interface: The game is controlled entirely through command-line input.
<hr>

# 🎮 How to Play
1. **Clone the repository:**<br>
   ```
   git clone [repository-url]
   ```
3. **Navigate to the project directory:**<br>
   ```
   cd [project-name]
   ```
5. **Run the game from your terminal:**
   ```
   python main.py
   ```
7. **Follow the on-screen prompts** to select your monster class and engage in combat.
<hr>

# 📁 Code Structure
* `main.py`: The main script that runs the game. It contains the game loop, user input handling, and combat flow.

* `fighter.py`: Defines the `Fighter` class, which serves as the blueprint for all characters (both the player and the enemy).

* `character_class.py`: Handles the logic for character selection and class attributes.

* `character_class_list.py`: Stores the data for the different monster classes available.

* `ascii.py`: Contains the ASCII art used for the game's visuals.
<hr>

# 🛠️ Requirements
* Python 3.x
<hr>

## OR
You can simply check out **[this link](https://programiz.pro/ide/python/GQSXQ8LPQ7?utm_medium=playground&utm_source=python-shared-project-link)**, log in and just run the game

## OR

Build with docker and run it.
```bash
docker build --tag=monsterbrawlgame . ; docker run -it monsterbrawlgame
```








