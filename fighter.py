class Fighter:
    """
    Represents a character in the game, either the player's monster or an enemy.

    A Fighter has core attributes like health and attack power, as well as special
    flags for unique abilities.
    """

    def __init__(self, name, health, attack_power):
        """
        Initializes a new Fighter instance.

        Args:
            name (str): The name of the fighter.
            health (int): The starting health points of the fighter.
            attack_power (int): The base damage the fighter deals per attack.
        """
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  # Used to track the initial health value
        self.is_attacking = False  # Flag for the enemy's conditional attack
        self.used_super_power = False  # Flag for the player's one-time super attack

    def lose_health(self, damage_amount):
        """
        Decreases the fighter's health by a specified damage amount.

        Args:
            damage_amount (int): The amount of health to subtract.
        """
        self.health -= damage_amount
        # Ensures health doesn't drop below 0
        if self.health < 0:
            self.health = 0
        print(f"{self.name} took {damage_amount} damage!")
        print(f"{self.name}'s health is now: {self.health}")

    def attack(self, target):
        """
        Performs a normal attack on a target.

        Args:
            target (Fighter): The Fighter object to attack.
        """

        # Your attack() method takes a target as a parameter.

        # Inside the method, you tell the target to lose health.

        # The amount of health the target loses should be the attacker's self.attack_power.

        damage_dealt = self.attack_power
        print("--------------------------------------------------")
        print(f"{self.name} attacked {target.name} for {damage_dealt} damage!")
        print("--------------------------------------------------")

        target.lose_health(damage_dealt)

    def super_power(self, target):
        """
        Unleashes a one-time super attack on a target.

        This method checks if the superpower has been used and, if not,
        doubles the attack damage and sets the 'used_super_power' flag to True.

        Args:
            target (Fighter): The Fighter object to attack.
        """
        # Check if the superpower is still available

        if not self.used_super_power:
            print(f"{self.name} unleashes its super power 💣💥!")

            # Calculate the new damage, which is double the normal attack power
            damage_dealt = self.attack_power * 2

            # Make the target lose health with the super attack damage
            target.lose_health(damage_dealt)

            # Set the flag to True so it cannot be used again
            self.used_super_power = True

        else:
            print(f"The power has already been used.")
