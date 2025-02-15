# (1) Try to approximate the behaviour of the is operator using == Remember we have the id 
# function for finding the memory address for a given value, and we can compare memory addresses to 
# check for identity.
list1 = [1,2,3]
list2 = [1,2,3]
if (id(list1) == id(list2)):
    print(True)
else:
    print(False)
#2) Try to use the is operator or the id function to investigate the difference between this:
numbers = [1, 2, 3, 4]
new_numbers = numbers + [5]
print(numbers is new_numbers)
print(id(numbers) == id(new_numbers))

numbers = [1, 2, 3, 4]
numbers.append(5)
print(numbers)
print(id(numbers))
print(numbers is numbers)
#3) Ask the user to enter a number. Tell the user whether the number is positive, negative, or zero.
user_number = int(input("Enter the number:"))
if (user_number > 0):
    print("The number is positive")
elif(user_number < 0):
    print("The number is negative")
else:
    print("The number is zero")
# (4) Write a program to determine whether an employee is owed any overtime.
#  You should ask the user how many hours the employee worked this week,
#  as well as the hourly wage for this employee.
#If the employee worked more than 40 hours, you should print a message which says the employee is due 
# some additional pay, as well as the amount due. The additional amount owed is 10% of the employees 
# hourly wage for each hour worked over the 40 hours. In effect, the employees get paid 110% of their 
# hourly wage for any overtime.
weekly_hours = int(input("How many hours you did?"))
hourly_wage = float(input("How much for hourly wage?"))
if weekly_hours > 40:
    
    overtime_hours = weekly_hours - 40  # Calculate overtime hours
    overtime_rate = hourly_wage * 1.10  # 110% of the hourly wage
    overtime_pay = overtime_hours * overtime_rate  # Calculate overtime pay

    print(f"The employee is due additional pay: ${overtime_pay:.2f}")
else:
    print("The employee is not owed any overtime pay.")                   