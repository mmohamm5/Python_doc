# split, join, and Slices
numbers = [1, 2, 3, 4, 5]
numbers = str(numbers)
print(numbers)

project_authors = ["Mike", "Sofia", "Helen"]
project_authors = ", ".join(project_authors)

print(f"The people who worked on this project are: {project_authors}.")

#user_numbers = input("Please enter 5 numbers separated by commas: ") # 1, 2, 3, 4, 5
#user_numbers = user_numbers.split(",")

#numbers_list = []

#for number in user_numbers:
    #numbers_list.append(number.strip())

#print(numbers_list) # ['1', '2', '3', '4', '5']

sample_string = "Python"

print(list(sample_string)) # ['P', 'y', 't', 'h', 'o', 'n']
print(tuple(sample_string)) # ('P', 'y', 't', 'h', 'o', 'n')