class MonsterClass:
    """A blueprint for handling the selection of a monster class.

    This class provides a method for a user to choose a valid monster class
    from a predefined list.
    """

    def __init__(self, character_class_list):
        """Initializes the MonsterClass object with a list of available classes.

        Args:
            character_class_list (list): A list of valid monster class names.
        """
        # We save the list of valid classes as an attribute so other
        # methods in the class can access it later.
        self.character_class_list = character_class_list
        # We start with an empty string to hold the player's choice.
        # This will be filled in by the player_choice() method.
        self.monster_class = ""

    def player_choice(self):
        """Prompts the user to choose a monster class and validates the input.

        The method will repeatedly ask for input until a valid choice is made.
        The final choice is stored in the `self.monster_class` attribute.
        """
        while True:
            # We create a clean string to show the user all the available options.
            # The .join() method puts the separator " / " between each item in the list.
            separator = " / "
            options_string = separator.join(self.character_class_list)

            # We get the user's input, capitalize the options for display, and convert the
            # input to lowercase for easier validation.
            self.monster_class = input(
                f"Choose your monster class.\n{options_string.title()}\n"
            ).lower()

            # We check if the user's input exists within our list of valid classes.
            if self.monster_class in self.character_class_list:
                print("--------------------------------------------------")
                print(f"You picked the '{self.monster_class.title()}' class")
                print("--------------------------------------------------")
                # The 'break' statement exits the loop once a valid choice is made.
                break
            else:
                # If the choice is invalid, we print an error and the loop continues.
                print("Invalid choice. Please choose from the list.")
