class UI:
    def display_gauges(self, hunger, thirst, energy):
        print(f"Hunger: {hunger}/100")
        print(f"Thirst: {thirst}/100")
        print(f"Energy: {energy}/100")

    def display_message(self, message):
        print(message)

    def display_actions(self, actions):
        print("Choose an action:")
        for index, action in enumerate(actions, start=1):
            print(f"{index}. {action}")

    def get_user_choice(self, num_actions):
        choice = input(f"Enter the number of your choice (1-{num_actions}): ")
        return int(choice) if choice.isdigit() and 1 <= int(choice) <= num_actions else None

    def display_game_over(self):
        print("Game Over! You have not survived.") 

    def display_victory(self):
        print("Congratulations! You have survived the challenge!")