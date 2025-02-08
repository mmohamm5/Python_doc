######## LIST  ##########
names = ["John", "Alice", "Sarah", "George"]
print(type(names))
#add iteams
names.append ("Hea")
names = names +["Modon"]
#value add with position
names.insert(1,"Kobita") # add in the specific place.

## removing iteam
names.remove("Alice")
#delete the positions.
print(f"Alice will be remove from the list:{names}")
del names[0]

print(f"Position 0 will be remove from the list:{names}")
##pop means it will delete from last. if we mention positions then it will follow this.

names.pop ()
print(f"Remove from the last:{names}")
pop_iteam = names.pop(1)
print (pop_iteam)
##clear all iteams from list
name =names.clear()
print(f"The list will be empty:{name}")

print(names)

#movie list
movie_titles = [
    "Eternal Sunshine of the Spotless Mind",
    "Memento",
    "Requiem for a Dream"
]
print(movie_titles)

###### Tupple  #####
names = ("John", "Sarah", "Alice")
tokies = [
    ("Eternal Sunshine of the Spotless Mind", 2004),
    ("Memento", 2000),
    ("Requiem for a Dream", 2000)
]                   #list er vitor tupple nichi
print(tokies[0])

jak = "Shawon"
print(type(jak))
