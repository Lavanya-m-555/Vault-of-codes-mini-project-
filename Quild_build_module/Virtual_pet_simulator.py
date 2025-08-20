import time
import random

class VirtualPet:
    def __init__(self, name="Fluffy"):
        self.name = name
        self.happiness = 50
        self.hunger = 50

    def feed(self):
        if self.hunger > 0:
            self.hunger -= 10
            self.happiness -= 2
            print(f"{self.name} has been fed! Hunger decreased, but happiness slightly decreased.")
        else:
            print(f"{self.name} is not hungry right now.")

    def play(self):
        if self.happiness < 100:
            self.happiness += 10
            self.hunger += 5
            print(f"{self.name} enjoyed playing! Happiness increased, but hunger slightly increased.")
        else:
            print(f"{self.name} is already very happy!")

    def check_status(self):
        print(f"\n--- {self.name}'s Status ---")
        print(f"Happiness: {self.happiness}")
        print(f"Hunger: {self.hunger}")
        print("--------------------------\n")

    def auto_change(self):
        self.hunger += 2
        self.happiness -= 1

    def is_game_over(self):
        if self.hunger >= 100:
            print(f"\n⚠️ {self.name} got too hungry! Game Over.")
            return True
        if self.happiness <= 0:
            print(f"\n⚠️ {self.name} became too sad! Game Over.")
            return True
        return False


def main():
    pet_name = input("Enter a name for your pet: ")
    pet = VirtualPet(pet_name)

    while True:
        print("\nWhat would you like to do?")
        print("1. Feed the pet")
        print("2. Play with the pet")
        print("3. Check pet's status")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            pet.feed()
        elif choice == "2":
            pet.play()
        elif choice == "3":
            pet.check_status()
        elif choice == "4":
            print(f"Thanks for playing with {pet.name}! Goodbye 👋")
            break
        else:
            print("Invalid choice, please try again.")

        # automatic changes after every action
        pet.auto_change()

        # bonus random event
        if random.randint(1, 5) == 3:
            event = random.choice(["snack", "sick"])
            if event == "snack":
                pet.hunger -= 5
                print(f"🍪 {pet.name} found a snack! Hunger decreased.")
            else:
                pet.happiness -= 5
                print(f"🤒 Oh no! {pet.name} feels sick. Happiness decreased.")

        if pet.is_game_over():
            break


if __name__ == "__main__":
    main()
