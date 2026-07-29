# Rules:

# Ask age.
# If age is 21 or above:
# Ask salary.
# If salary is 30000 or more:
# Print "Loan Approved"
# Else:
# Print "Salary is too low"
# Else:
# Print "Age is not eligible"

# Don't ask for salary unless the age is at least 21.

age = int(input("Enter age: "))
    
if age >= 21:
  salary = int(input("Enter Salary: "))
  if salary >= 30000:
    print("Loan Approved")

  else: 
    print("Salary is less then our criteria")  
else:
    print("Age is not Eligible for the Loan")

