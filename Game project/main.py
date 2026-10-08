"""Hunt for the Gold"""

#Add link for education.
#Here my game summary will store.
SCORE_FILE = "scores.txt"

""" ---------------------------------------------------------------------- """
# class Player
#This class stores palyers name and age, game points also collected items.
class Player:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.game_point = 0
        self.inventory = []

    def add_item(self, item):
        self.inventory.append(item)

    def add_game_point(self, points):
        self.game_point += points
# This method prints game summary and player status.
    def show_status(self):
        print(f"\n--- {self.name}'s Status ---")
        print(f"Age: {self.age}")
        print(f"Game points: {self.game_point}")
        if self.inventory:
            print(f"Inventory: {', '.join(self.inventory)}")
        else:
            print("Inventory: empty")
        print("-------------------------\n")

""" ---------------------------------------------------------------------- """
#  Inventory check 
#Give the player option to check thier inventory in every point of the game.
def show_inventory(player):
    if player.inventory:
        print(f"\nYour inventory: {', '.join(player.inventory)}\n")
    else:
        print("\nYour inventory is empty.\n")
#The input for checking the inventroy in the game.
def get_input(player, prompt):
    while True:
        answer = input(prompt)
        if answer.strip().lower() == "i":
            show_inventory(player)
        else:
            return answer

""" ---------------------------------------------------------------------- """
# Game story text 

INTRO_TEXT = """
Welcome, explorer!

Long ago, a great treasure was hidden deep within Green Valley,
a wild place full of rivers, forests and caves.

But Green Valley is in danger. Pollution, illegal logging and
careless visitors threaten the animals and plants that live there.

Your goal: find the treasure AND protect Green Valley along the way.
"""

""" ---------------------------------------------------------------------- """
# This is the river path which has three challenges and max 4 game points. 

#challeng No.1: Clean up plastic waste or igonre
def handle_river_otters(player):
    print("\n The river is clogged with plastic waste.")
    print("A family of otters looks at you, hungry and confused.")
    print("1. Stop and clean up the plastic waste")
    print("2. Ignore it and keep walking")
    choice = get_input(player, "What do you do? (1-2, or 'i' for inventory): ")
    if choice == "1":
        print("You clean the river. The otters thank you!")
        player.add_game_point(2)
        player.add_item("silver key")
        print("You recived a silver key")
    else:
        print("You keep walking, feeling a bit guilty.")
        player.add_game_point(-1)

#challeng No.2: sovling a reddle 
def handle_river_bridge(player):
    print("\n An old stone bridge shows a riddle:")
    print('  "I have a bed but never sleep,')
    print('   I have a mouth but never eat. What am I?"')
    answer = get_input(player, "Your answer (or 'i' for inventory): ").strip().lower()
    if answer == "river":
        print("Correct! The bridge holds firm.")
        player.add_game_point(1)
    else:
        print("Wrong answer! The bridge wobbles, but you make it across.")
        player.add_game_point(-1)

#challeng No.3: Warm a fisherman about the harmfull net. explsin also to the player why it is harmfull
def handle_river_fisherman(player):
    print("\n A fisherman is about to use a harmful wide-mesh net.")
    print("1. Explain why it harms young fish")
    print("2. Say nothing")
    choice = get_input(player, "What do you do? (1-2, or 'i' for inventory): ")
    if choice == "1":
        print("The fisherman switches to a safer net.")
        player.add_game_point(1)
    else:
        print("The fisherman uses the harmful net anyway.")
        player.add_game_point(-1)

#This funtion arrange my challenges order.
def handle_river_path(player):
    print("\n--- THE RIVER PATH ---")
    handle_river_otters(player)
    handle_river_bridge(player)
    handle_river_fisherman(player)

""" ---------------------------------------------------------------------- """
# This is the forest path which has three challenges and max 4 game points. 

#challeng No.1: Reporst illegal loggeres.
def handle_forest_loggers(player):
    print("\n You catch loggers cutting down protected trees.")
    print("1. Report them and plant a new tree")
    print("2. Sneak past")
    choice = get_input(player, "What do you do? (1-2, or 'i' for inventory): ")
    if choice == "1":
        print("Rangers arrive quickly. The forest is safe for now.")
        print("You recived an old map")
        player.add_game_point(2)
        player.add_item("old map")
    else:
        print("You avoid trouble, but the logging continues.")
        player.add_game_point(-1)

#challeng No.2: Put out an abandoned campfire.
def handle_forest_campfire(player):
    print("\n A campfire was left burning, close to dry leaves.")
    print("1. Put the fire out properly")
    print("2. Assume it will burn out on its own")
    choice = get_input(player, "What do you do? (1-2, or 'i' for inventory): ")
    if choice == "1":
        print("You put the fire out. A wildfire is avoided.")
        player.add_game_point(1)
    else:
        print("You walk on, hoping for the best.")
        player.add_game_point(-1)

#challeng No.3: Free a trap fawm
def handle_forest_fawn(player):
    print("\n A baby deer is tangled in old plastic litter.")
    print("1. Carefully free the fawn")
    print("2. Take a photo and move on")
    choice = get_input(player, "What do you do? (1-2, or 'i' for inventory): ")
    if choice == "1":
        print("The fawn scampers off safely to find its mother.")
        player.add_game_point(1)
    else:
        print("The fawn stays stuck and afraid.")
        player.add_game_point(-1)

#This funtion arrange my challenges order.
def handle_forest_path(player):
    print("\n--- THE FOREST PATH ---")
    handle_forest_loggers(player)
    handle_forest_campfire(player)
    handle_forest_fawn(player)

""" ---------------------------------------------------------------------- """
# This is the mountain path which has three challenges and max 4 game points. 

#challeng No.1: Climb quietly.
def handle_mountain_eagle(player):
    print("\n You spot a golden eagle's nest with eggs.")
    print("1. Climb around quietly, keeping distance")
    print("2. Take the fast route right past the nest")
    choice = get_input(player, "What do you do? (1-2, or 'i' for inventory): ")
    if choice == "1":
        print("The eagle stays calm on her nest.")
        print("You recived a lantern")
        player.add_game_point(2)
        player.add_item("lantern")
    else:
        print("The eagle flies off, leaving the eggs exposed.")
        player.add_game_point(-1)

#challeng No.2: Packing the letters
def handle_mountain_litter(player):
    print("\n Earlier climbers left litter at a viewpoint.")
    print("1. Pack it out with you")
    print("2. Leave it")
    choice = get_input(player, "What do you do? (1-2, or 'i' for inventory): ")
    if choice == "1":
        print("You carry the extra weight, but the view is clean again.")
        player.add_game_point(1)
    else:
        print("You leave the litter behind.")
        player.add_game_point(-1)

#challeng No.3: Take the longer trail to protect seedling.
def handle_mountain_shortcut(player):
    print("\n A shortcut cuts through fragile new seedlings.")
    print("1. Take the longer trail around them")
    print("2. Take the shortcut")
    choice = get_input(player, "What do you do? (1-2, or 'i' for inventory): ")
    if choice == "1":
        print("It takes longer, but the seedlings survive.")
        player.add_game_point(1)
    else:
        print("You save time, but crush the fragile new growth.")
        player.add_game_point(-1)

#This funtion arrange my challenges order.
def handle_mountain_path(player):
    print("\n--- THE MOUNTAIN PATH ---")
    handle_mountain_eagle(player)
    handle_mountain_litter(player)
    handle_mountain_shortcut(player)

""" ---------------------------------------------------------------------- """
# All my three paths leads here to this cave 

def handle_cave_first_key(player):
    print("\n A ledge lit by glowing mushrooms crosses a chasm.")
    print("1. Step carefully around the mushrooms")
    print("2. Step straight over them to save time")
    choice = get_input(player, "What do you do? (1-2, or 'i' for inventory): ")
    if choice == "1":
        print("You cross safely and find an IRON KEY in an alcove.")
        print("You recived a iron key")
        player.add_game_point(1)
        player.add_item("iron key")
    else:
        print("You crush the mushrooms and miss the alcove. No key this time.")
        player.add_game_point(-1)

def handle_cave_second_key(player):
    print("Hint: What happens to each number when you move to the next?")
    print("\n A stone panel shows a sequence: 2  4  8  16  ?")
    answer = get_input(player, "What number comes next? (or 'i' for inventory): ").strip()
    if answer == "32":
        print("Correct! A hidden panel opens, revealing a GOLDEN KEY.")
        print("You recived a golden key")
        player.add_game_point(2)
        player.add_item("golden key")
    else:
        print("Wrong. The panel stays sealed shut.")
        player.add_game_point(-1)


def enter_cave(player):
    print("\n--- THE SHARED CAVE ---")
    print("All paths meet here, at the mouth of a dark cave.")
    if "lantern" in player.inventory:
        print("Your lantern lights the way perfectly.")
        player.add_game_point(1)
    else:
        print("Without a lantern, you feel your way through the dark.")
    handle_cave_first_key(player)
    handle_cave_second_key(player)


def enter_treasure_room(player):
    print("\n--- THE TREASURE ROOM ---")
    if player.inventory:
        print(f"Items you collected: {', '.join(player.inventory)}")
    else:
        print("You arrive with empty pockets.")

    has_iron_key = "iron key" in player.inventory
    has_golden_key = "golden key" in player.inventory

    if not (has_iron_key and has_golden_key):
        print("The chest has two locks, but you are missing a key.")
        print("LOCKED ENDING.")
        return "Locked ending"

    print("Both keys click into place, and the chest opens.")
    if player.game_point >= 3:
        print("Green Valley thanks you for protecting it. GOOD ENDING!")
        return "Good ending"
    elif player.game_point >= 0:
        print("You find the treasure, but the valley still feels wounded. NEUTRAL ENDING.")
        return "Neutral ending"
    else:
        print("The treasure inside looks tarnished. BAD ENDING.")
        return "Bad ending"

""" ---------------------------------------------------------------------- """
# File saving/loading 

def save_score(player, ending):
    with open(SCORE_FILE, "a") as file:
        file.write(f"{player.name},{player.age},{player.game_point},{ending}\n")


def load_scores():
    scores = []
    try:
        with open(SCORE_FILE, "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    scores.append(line.split(","))
    except FileNotFoundError:
        pass
    return scores

def show_scores():
    scores = load_scores()
    if not scores:
        print("\nNo scores saved yet.\n")
        return
    print("\n--- Explorer Records ---")
    for name, age, game, ending in scores:
        print(f"{name} (age {age}) - Game point: {game} - {ending}")
    print("------------------------\n")

""" ---------------------------------------------------------------------- """
# Menu and main loop 
#Asks for the player's name and age, then returns a new Player object
def ask_player_info():
    name = input("What is your name, explorer? ")
    while True:
        age_text = input("How old are you? ")
        if age_text.isdigit():
            age = int(age_text)
            break
        print("Please enter your age using numbers only.")
    return Player(name, age)

# Prints the main menu and returns the player's raw choice.
def show_main_menu():
    print("\n=== HUNT FOR THE GOLD ===")
    print("1. Start new game")
    print("2. Show explorer records")
    print("3. Quit")
    return input("Choose an option (1-3): ")

# Lets the player pick a path, then sends them through the cave and treasure room.
def choose_path(player):
    print("\nThree paths lie ahead:")
    print("1. Follow the river")
    print("2. Walk through the forest")
    print("3. Climb the mountain trail")
    choice = get_input(player, "Which path do you choose? (1-3): ")

    if choice == "1":
        handle_river_path(player)
    elif choice == "2":
        handle_forest_path(player)
    elif choice == "3":
        handle_mountain_path(player)
    else:
        print("Choose again!")
        return choose_path(player)

    enter_cave(player)
    return enter_treasure_room(player)


def start_game():
    print(INTRO_TEXT)
    player = ask_player_info()
    ending = choose_path(player)
    player.show_status()
    save_score(player, ending)
    print(f"Thank you for playing, {player.name}!")

# Main loop: keeps showing the menu until the player quits.
def main():
    while True:
        choice = show_main_menu()
        if choice == "1":
            start_game()
        elif choice == "2":
            show_scores()
        elif choice == "3":
            print("Goodbye, explorer!")
            break
        else:
            print("Please choose 1, 2 or 3.")


if __name__ == "__main__":
    main()