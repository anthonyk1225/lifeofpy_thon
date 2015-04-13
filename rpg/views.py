class View:
    pass

    def battle(self):
        print("""
        Choose your opponent:
        Press 1 for Goblin (difficulty: Easy)
        Press 2 for Orc (difficulty: Medium)
        Press 3 for Ogre (difficulty: Hard)""")

    def start(self):
        print("Prepare for battle!")

    def turn(self):
        return input("""
        Choose an action:
        1 for attack
        2 for dodge
        3 for block""")
