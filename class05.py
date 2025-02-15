#Conditionals and Booleans
movies = [
    ("Inside Out", 2015, True),
    ("Toy Story 4", 2019, False),
    ("Up", 2009, True)
]
print(bool(0))              # False
print(bool(6))              # True

print(bool("Caterpillar"))  # True
print(bool(""))             # False

print(bool([]))             # False
print(bool([0, 1, 2, 3]))   # True

print(bool(True))           # True
print(bool(False))          # False

a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # True
print(a is b)  # False

a = [1, 2, 3]
b = [1, 2, 3]

print(id(a))  # 139806639351360
print(id(b))  # 139806638418944

print(a == b)  # True
print(a is b)  # False

age = int(input("How old are you? "))

if age < 18:
      print("Sorry, we can't serve you.")
else:
      print("We ready to serve")

age = int(input("How old are you? "))

if age < 18:
      print("Sorry, we can't serve you.")
else:
    chosen_drink = input("What can I get for you? ")
