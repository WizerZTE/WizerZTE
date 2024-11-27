class Animal:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species

    def speak(self):
        return "Тварина видає звук."

    def info(self):
        return f"Ім'я: {self.name}, Вік: {self.age}, Вид: {self.species}"


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age, "Собака")
        self.breed = breed

    def speak(self):
        return "Гав-гав!"

    def info(self):
        base_info = super().info()
        return f"{base_info}, Порода: {self.breed}"


class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age, "Кіт")
        self.color = color

    def speak(self):
        return "Мяу!"

    def info(self):
        base_info = super().info()
        return f"{base_info}, Колір: {self.color}"

if __name__ == "__main__":
    dog = Dog("Барсик", 3, "Лабрадор")
    cat = Cat("Мурчик", 2, "Сірий")

    print(dog.info())
    print(dog.speak())

    print(cat.info())
    print(cat.speak())