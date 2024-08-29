class Dog:
    def __init__(self, name, breed, age, color, weight, gender, owner_name, daily_food_amount):
        self.name = name
        self.breed = breed
        self.age = age
        self.color = color
        self.weight = weight
        self.gender = gender
        self.owner_name = owner_name
        self.daily_food_amount = daily_food_amount

    def is_white(self):
        return self.color.lower() in ["білий", "біла"]

    def print_name_and_breed(self):
        print(f"Ім'я: {self.name}, Порода: {self.breed}")

    def is_old(self):
        return self.age > 10

# Створення екземплярів класу Собака
dogs = [
    Dog("Бім", "Лабрадор", 5, "Білий", 25.0, "Чоловіча", "Олександр", 3.5),
    Dog("Леді", "Пудель", 3, "Біла", 12.0, "Жіноча", "Марія", 0.3),
    Dog("Рекс", "Німецька вівчарка", 12, "Чорний", 30.0, "Чоловіча", "Іван", 4.0),
    Dog("Белла", "Хаскі", 8, "Біло-сірий", 20.0, "Жіноча", "Анна", 3.8)
]

# Виведення імен білих собак, які не є старими
print("Імена білих собак, які не є старими:")
for dog in dogs:
    if dog.is_white() and not dog.is_old():
        print(dog.name)

# Виведення імен і породи собак жіночої статі
print("\nІмена та порода собак жіночої статі:")
for dog in dogs:
    if dog.gender.lower() == "жіноча":
        dog.print_name_and_breed()

# Виведення імен і породи тих собак, які потребують більше 3 кг їжі на добу
print("\nСобаки, які потребують більше 3 кг їжі на добу:")
for dog in dogs:
    if dog.daily_food_amount > 3:
        dog.print_name_and_breed()

# Визначення найстарішої собаки
oldest_dog = max(dogs, key=lambda d: d.age)
print(f"\nНайстаріша собака: Ім'я: {oldest_dog.name}, Порода: {oldest_dog.breed}, Вік: {oldest_dog.age} років")
