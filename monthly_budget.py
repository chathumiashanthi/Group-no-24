# monthly_budget.py

# Ask for total monthly budget
budget = float(input("Enter your total monthly budget: "))

total_expenses = 0

# Loop to enter multiple expenses
while True:
    expense = input("Enter an expense (or type 'done' to finish): ")

    if expense.lower() == "done":
        break

    total_expenses += float(expense)

# Calculate remaining balance
remaining_balance = budget - total_expenses

# Display results
print("\n------------------------------")
print("Total Budget     :", budget)
print("Total Expenses   :", total_expenses)
print("Remaining Balance:", remaining_balance)

# Warning for low balance
if remaining_balance < 500:
    print("Warning: Low Funds")

print("------------------------------")