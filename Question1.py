def calculate_weekly_salary(hours_worked):
  """
  This function calculates the weekly salary for an employee based on the provided hours worked.

  Args:
      hours_worked: The number of hours worked by the employee (float).

  Returns:
      The weekly salary of the employee (float).
  """

  # Set the regular pay rate and regular working hours
  regular_pay_rate = 12.5
  regular_working_hours = 30

  # Calculate regular pay for 30 hours
  regular_pay = regular_pay_rate * regular_working_hours

  # Check for overtime hours
  if hours_worked > regular_working_hours:
    overtime_hours = hours_worked - regular_working_hours
    overtime_pay_rate = regular_pay_rate * 1.5  # Time and a half rate
    overtime_pay = overtime_hours * overtime_pay_rate
  else:
    overtime_hours = 0
    overtime_pay = 0

  # Calculate total salary (regular pay + overtime pay)
  total_salary = regular_pay + overtime_pay

  return total_salary

# Get the number of hours worked from the user
hours_worked = float(input("Enter the number of hours worked: "))

# Calculate the weekly salary
weekly_salary = calculate_weekly_salary(hours_worked)

# Print the weekly salary with two decimal places
print(f"The weekly salary is k{weekly_salary:.2f}")
