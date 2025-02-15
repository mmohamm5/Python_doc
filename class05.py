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
