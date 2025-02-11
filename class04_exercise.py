#1. Create a movies list containing a single tuple. The tuple should contain a movie title, the director’s name,
#  the release year of the movie, and the movie’s budget.
movies = [
    ("movie title is theree idiods", "Raju hirani", "2003", "100 cr")
]
#gprint (movies)

#2.Use the input function to gather information about another movie. 
# You need a title, director’s name, release year, and budget.
title = input("Title:")
director = input("Directors name:")
release = input("Release year:")
budget = input("Budget:")
#print(title")

#3.Create a new tuple from the values you gathered using input. 
# Make sure they’re in the same order as the tuple you wrote in the movies list.
new_movies =(title, director, release, budget)
#print (new_movies)

# 4 Use an f-string to print the movie name and release year by accessing your new movie tuple.
print(f"{new_movies[0]} ({new_movies[2]})")

# 5. Add the new movie tuple to the movies collection using append.
movies.append (new_movies)
print(movies[0])
print(movies[1])