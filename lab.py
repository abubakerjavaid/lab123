class Person:
    def __init__(self, name, age, address):
      
        self._name = name
        self._age = age
        self._address = address

    # Getter and setter methods for the name attribute
    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    # Getter and setter methods for the age attribute
    def get_age(self):
        return self._age

    def set_age(self, age):
        self._age = age

    # Getter and setter methods for the address attribute
    def get_address(self):
        return self._address

    def set_address(self, address):
        self._address = address

# Example usage:
# Create an instance of the Person class
person = Person(name="ABUBAKER", age=23, address="18 j izmir town Main Stre ")

# Get information
print("Name:", person.get_name())
print("Age:", person.get_age())
print("Address:", person.get_address())

# Update information
person.set_name("abubaker")
person.set_age(23)
person.set_address("lahore")

# Display updated information
print("\nUpdated Information:")
print("Name:", person.get_name())
print("Age:", person.get_age())
print("Address:", person.get_address())

                
