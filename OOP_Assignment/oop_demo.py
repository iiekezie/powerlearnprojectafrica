# Activity 1: Design Your Own Class
class Device:
    """Base class for electronic devices"""
    def __init__(self, brand, model, power_source):
        self.brand = brand
        self.model = model
        self.power_source = power_source
        self.is_on = False

    def power_on(self):
        if not self.is_on:
            self.is_on = True
            return f"{self.brand} {self.model} is now ON"
        return f"{self.brand} {self.model} is already ON"

    def power_off(self):
        if self.is_on:
            self.is_on = False
            return f"{self.brand} {self.model} is now OFF"
        return f"{self.brand} {self.model} is already OFF"

    def __str__(self):
        return f"{self.brand} {self.model} ({self.power_source})"


class Smartphone(Device):
    """Smartphone class inheriting from Device"""
    def __init__(self, brand, model, os, storage_gb, battery_mah):
        super().__init__(brand, model, "Battery")
        self.os = os
        self.storage_gb = storage_gb
        self.battery_mah = battery_mah
        self.apps = []
        self.current_storage = 0

    def install_app(self, app_name, size_gb):
        if self.current_storage + size_gb > self.storage_gb:
            return f"Cannot install {app_name}. Not enough storage."
        
        self.apps.append(app_name)
        self.current_storage += size_gb
        return f"{app_name} installed successfully."

    def uninstall_app(self, app_name):
        if app_name not in self.apps:
            return f"{app_name} not found."
        
        self.apps.remove(app_name)
        # For simplicity, we'll assume each app takes 1GB
        self.current_storage -= 1
        return f"{app_name} uninstalled successfully."

    def get_storage_info(self):
        free_space = self.storage_gb - self.current_storage
        return f"Storage: {self.current_storage}GB used, {free_space}GB free"

    def __str__(self):
        return (f"{super().__str__()}\n"
                f"OS: {self.os}\n"
                f"Storage: {self.storage_gb}GB\n"
                f"Battery: {self.battery_mah}mAh\n"
                f"Installed Apps: {', '.join(self.apps) if self.apps else 'None'}")


# Activity 2: Polymorphism Challenge
class Animal:
    def __init__(self, name):
        self.name = name

    def move(self):
        raise NotImplementedError("Subclasses must implement this method")


class Dog(Animal):
    def move(self):
        return f"{self.name} the dog is running 🐕"


class Fish(Animal):
    def move(self):
        return f"{self.name} the fish is swimming 🐟"


class Bird(Animal):
    def move(self):
        return f"{self.name} the bird is flying 🦅"


class Snake(Animal):
    def move(self):
        return f"{self.name} the snake is slithering 🐍"


def demonstrate_polymorphism():
    """Demonstrates polymorphism with different animal movements"""
    animals = [
        Dog("Buddy"),
        Fish("Nemo"),
        Bird("Sky"),
        Snake("Viper")
    ]

    for animal in animals:
        print(animal.move())


def main():
    print("OOP Assignment")
    print("=============\n")

    # Activity 1 Demonstration
    print("Activity 1: Smartphone Class Demonstration")
    print("-----------------------------------------")
    my_phone = Smartphone("Apple", "iPhone 15", "iOS", 128, 4000)
    print(my_phone.power_on())
    print(my_phone.install_app("WhatsApp", 1))
    print(my_phone.install_app("Instagram", 2))
    print(my_phone.get_storage_info())
    print("\nSmartphone Details:")
    print(my_phone)
    print(my_phone.power_off())

    # Activity 2 Demonstration
    print("\nActivity 2: Polymorphism Challenge")
    print("--------------------------------")
    demonstrate_polymorphism()


if __name__ == "__main__":
    main()
