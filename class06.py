#Day 6: For Loops
movies = [
    (
        "Eternal Sunshine of the Spotless Mind",
        "Michel Gondry",
        2004
    ),
    (
        "Memento",
        "Christopher Nolan",
        2000
    ),
    (
        "Requiem for a Dream",
        "Darren Aronofsky",
        2000
    )
]
movie = movies[0]
print(f"{movie[0]} ({movie[2]}), by {movie[1]}")

movie = movies[1]
print(f"{movie[0]} ({movie[2]}), by {movie[1]}")

movie = movies[2]
print(f"{movie[0]} ({movie[2]}), by {movie[1]}")

## for loops

movies = [
    (
        "Eternal Sunshine of the Spotless Mind",
        "Michel Gondry",
        2004
    ),
    (
        "Memento",
        "Christopher Nolan",
        2000
    ),
    (
        "Requiem for a Dream",
        "Darren Aronofsky",
        2000
    )
]


for movie in movies:
    # Check the title of the current movie is Memento
    if movie[1] == "Memento":
        # If the title is Memento, inform the user that the movie exists and break the loop
        print("Memento is in the movie library!")
        break
#print(f"{movie[0]} ({movie[2]}), by {movie[1]}")

#Range
A =list(range(10))   #1............3
B = tuple(range(3,10)) #3.....9
range(0,10,2),4,6
range(0,10,3) #3,6,9
print(A) 
print(B) 
for number in range(10):
    print(number)

for number in range(10):
    print("Hello!")
for _ in range(10):
    print(_)
