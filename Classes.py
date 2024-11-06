# Step 1: Create the Person class
class Person:
   def __init__(self, name, age, country):
       self.name = name
       self.age = age
       self.country = country
       self.friends = []


   def add_friend(self, friend):
       self.friends.append(friend)


# Step 2: Make 5 Person objects
person1 = Person("Nate", 14, "USA")
person2 = Person("Ernesto", 99, "USA")
person3 = Person("Owen", 14, "USA")
person4 = Person("Noah", 13, "USA")
person5 = Person("Drew", 12, "USA")


# Step 3: Instantiate a sixth person and add the other 5 as friends
person6 = Person("Emanuel", 29, "DR")
person6.add_friend(person1)
person6.add_friend(person2)
person6.add_friend(person3)
person6.add_friend(person4)
person6.add_friend(person5)


# Step 4: Save the list of friends to friends.txt with ID numbers
with open("friends.txt", "w") as file:
   for idx, friend in enumerate(person6.friends, 1):
       file.write(f"{idx}. Name: {friend.name}, Age: {friend.age}, Country: {friend.country}\n")


with open("friends.txt", "r") as file:
    lines = file.readlines()


z = input("Enter the name of the person to be deleted: ")


with open("friends.txt", "w") as file:
    for line in lines:
        if z not in line:
            file.write(line)
