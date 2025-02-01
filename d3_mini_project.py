name = input("Enter the employee name:").strip().title()
wage = input("Enter hourly wages:")
working_hour = input("Enter the working hour:")
total_amount = float(wage)*float(working_hour)

print(f"{name} earned ${total_amount} this week.")