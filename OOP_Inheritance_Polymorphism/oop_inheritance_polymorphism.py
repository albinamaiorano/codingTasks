class Animal:
    def speak(self):
        # Define an abstract method to be implemented by subclasses
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
    def speak(self):
        # Implement the speak method for the Dog subclass
        return "Woof!"

class Cat(Animal):
    def speak(self):
        # Implement the speak method for the Cat subclass
        return "Meow!"

def main():
    # Create a list of Dog and Cat objects
    animals = [Dog(), Cat()]
    # Iterate over each animal object in the list
    for animal in animals:
        # Print the name of the animal class and the result of its speak method
        print(f"{animal.__class__.__name__}: {animal.speak()}")

if __name__ == "__main__":
    # Call the main function when the script is executed
    main()
