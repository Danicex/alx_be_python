monthly_icome = int(input('Enter your monthly income: '))
monthly_expenses = int(input('Enter your total monthly expenses: '))

monthly_savings = monthly_icome - monthly_expenses
yearly_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

print(f"your monthly savings after: ${monthly_savings}")
print(f"Projected savings after one year, with interest, is: ${yearly_savings}")