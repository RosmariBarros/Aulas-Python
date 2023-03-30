number = int(input("Enter the employee ID: "))
worked_hours = int(input("Enter the number of hours worked: "))
value_per_hour = float(input("Enter the amount per hour worked: "))

salary = float(worked_hours * value_per_hour) 

print("NUMBER =", number)
print(f"SALARY = U$ {salary:.2f}")


