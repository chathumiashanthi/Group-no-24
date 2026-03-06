# monthly_budget.py

# Ask for total monthly budget
budget = float(input("Enter your total monthly budget: "))

# Ask for 3 expenses
expense1 = float(input("Enter expense 1: "))
expense2 = float(input("Enter expense 2: "))
expense3 = float(input("Enter expense 3: "))

# Calculate total expenses
total_expenses = expense1 + expense2 + expense3

# Calculate remaining balance
remaining_balance = budget - total_expenses

# Display results
print("\n------------------------------")
print("Total Budget     :", budget)
print("Total Expenses   :", total_expenses)
print("Remaining Balance:", remaining_balance)

# Low funds warning
if remaining_balance < 500:
    print("Warning: Low Funds")

print("------------------------------")