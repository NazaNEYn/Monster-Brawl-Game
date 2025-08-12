"""
This is the main script that runs the monster class selection game.

It imports the MonsterClass blueprint and the lists of available classes
to create different types of monster selectors for the player.
"""

# Import necessary modules and classes
import time
from character_class_list import boss_class, character_class
from character_class import MonsterClass
from fighter import Fighter
from ascii import monster_ascii

# --- GAME INTRODUCTION ---

print("-----------------------------")
print("👹 The Monster's Munchies 👹")
print("-----------------------------")
print("Roar! You're hungry for a fight... and a snack!")
print("Time to show those enemies who the real top monster is.")

print(monster_ascii)
time.sleep(1)
input("Press ENTER to unleash your fury...")
print("-----------------------------")

# Initialize game flags
Invalid_choice = False
game_over = False

# --- MONSTER SELECTION LOOP ---

while not game_over:
    # Prompt user to choose a monster class
    user_monster_class_choice = input(
        "Pick one, 'Boss Class 👹' or 'Normal Class 🧝'?\n"
    ).lower()
    time.sleep(1)

    # Check for valid monster class selection
    if user_monster_class_choice == "boss class":
        # Create a Boss Class monster
        boss = MonsterClass(boss_class)
        boss.player_choice()
        monster = Fighter("Big Boss", 500, 100)

    elif user_monster_class_choice == "normal class":
        # Create a Normal Class monster
        boss = MonsterClass(character_class)
        boss.player_choice()
        monster = Fighter("Monster", 360, 100)

    else:
        # Handle invalid input and restart the selection loop
        print("Invalid command. Try again!")
        continue

    # Note: The 'Invalid_choice' flag is not being used in this loop.
    # It can be safely removed or refactored if needed.

    # --- GAME START AND ENEMY SETUP ---

    time.sleep(1)
    print("------------------------")
    print("An enemy is approaching ")
    print("         ( -_•)╦̵̵̿╤─      ")
    print("------------------------")
    time.sleep(2)

    # Create the enemy fighter
    enemy = Fighter("Goblin", 1000, 10)

    print("--------------------------------------------------")
    print(f"You are the {monster.name} with {monster.health} HP.")
    print(f"A {enemy.name} with {enemy.health} HP appears!")
    print("--------------------------------------------------")
    time.sleep(2)

    # Explain the superpower to the player
    print("--------------------------------------------------")
    print(
        "Psssst, your monster has a super power.\nIt doubles the damage amount and you can use it 'whenever' you want.\nBUT the catch is that you can only use it ONCE."
    )
    print("--------------------------------------------------")
    time.sleep(2)

    # --- MAIN COMBAT LOOP ---

    while not game_over:
        # Prompt user for their turn command
        user_input = input("Type 'attack'🗡️, or 'super attack'💥\n").lower()

        # Handle player commands
        if user_input == "attack":
            monster.attack(enemy)
        elif user_input == "super attack":
            # The super_power method handles its own one-time use logic
            monster.super_power(enemy)
        else:
            print("Invalid command. Try again!")
            continue  # Added continue to skip to the next turn on invalid input

        # --- WIN/LOSS AND ENEMY TURN LOGIC ---

        # Check if the enemy is defeated
        if enemy.health <= 0:
            print("You defeated the enemy! WOOOHOOOO 🥳🥳!!")
            game_over = True
            continue  # Ends the inner loop

        # Check if the player is defeated
        if monster.health <= 0:
            print("You have been defeated! Game over.")
            game_over = True
            continue  # Ends the inner loop

        # Enemy's conditional attack
        if (
            not game_over
            and enemy.health < (enemy.max_health / 2)
            and not enemy.is_attacking
        ):
            enemy.attack(monster)
            print("----------------------------")
            print(f"{enemy.name} has attacked the {monster.name}")
            print("----------------------------")
            enemy
