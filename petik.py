import random

class Pet:
    def __init__(self, name):
        self.name = name
        self.age = random.randint(1, 15)            # Випадковий вік від 1 до 15 років
        self.species = "котик"                      # Припустимо, що ми створюємо котика
        self.energy = random.randint(0, 100)        # Випадковий рівень енергії
        self.hunger = random.randint(0, 100)        # Випадковий рівень голоду
        self.happiness = random.randint(0, 100)     # Випадковий рівень настрою
        self.is_asleep = False
        print(f"Ви створили {self.species} на ім'я {self.name}!")

    def eat(self, food_amount):
        if self.is_asleep:
            print(f"{self.name} зараз спить і не може їсти.")
            return
        self.hunger = max(0, self.hunger - food_amount)
        self.energy = min(100, self.energy + food_amount // 2)
        print(f"{self.name} поїв(ла) і тепер голод на рівні {self.hunger}, а енергія — {self.energy}.")

    def sleep(self, hours):
        if self.is_asleep:
            print(f"{self.name} вже спить.")
            return
        self.is_asleep = True
        self.energy = min(100, self.energy + hours * 10)
        self.hunger = min(100, self.hunger + hours * 5)
        print(f"{self.name} спить... Енергія збільшується.")

    def wake_up(self):
        if not self.is_asleep:
            print(f"{self.name} вже прокинувся.")
            return
        self.is_asleep = False
        print(f"{self.name} прокинувся і готовий до гри!")

    def play(self):
        if self.is_asleep:
            print(f"{self.name} спить і не може грати.")
            return
        if self.energy <= 10:
            print(f"{self.name} надто втомився для гри.")
            return
        if self.hunger >= 80:
            print(f"{self.name} занадто голодний для гри.")
            return
        self.energy = max(0, self.energy - 20)
        self.hunger = min(100, self.hunger + 15)
        self.happiness = min(100, self.happiness + 20)
        print(f"{self.name} грається і тепер енергія на рівні {self.energy}, голод — {self.hunger}, а настрій — {self.happiness}.")

    def get_status(self):
        state = "спить" if self.is_asleep else "не спить"
        print(f"Ім'я: {self.name}, Вік: {self.age}, Вид: {self.species}")
        print(f"Енергія: {self.energy}, Голод: {self.hunger}, Настрій: {self.happiness}, Стан: {state}")

# Введення імені котика користувачем
name = input("Введіть ім'я котика: ")
my_pet = Pet(name)
my_pet.get_status()
