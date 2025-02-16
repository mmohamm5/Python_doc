# 1) Below we've provided a list of tuples, where each tuple contains details about an employee of a 
# shop: their name, the number of hours worked last week, and their hourly rate.
#  Print how much each employee is due to be paid at the end of the week in a nice, readable format.
employees = [
    ("Rolf Smith", 35, 8.75),
    ("Anne Pun", 30, 12.50),
    ("Charlie Lee", 50, 15.50),
    ("Bob Smith", 20, 7.00)
]
for employee_list in employees:
        due_amount = employee_list [1] * employee_list[2]
        print(f"{employee_list[0]} due amount is : {due_amount}")

#2) For the employees above, print out those who are earning an hourly wage above average.
total_amount = 0
hourly_total = 0
for employee_list in employees:
        hourly_total +=  employee_list[2]

        #print(f"{employee_list[0]} due amount is : {due_amount}")
        total_amount = total_amount +hourly_total

avarage = hourly_total/len(employees)
print(avarage)

for employee_list in employees:
        if employee_list[2] > avarage:
              print(f"{employee_list[0]} is getting hourly wage above avarage")