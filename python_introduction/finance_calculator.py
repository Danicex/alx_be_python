monthly_icome = int(input('Enter your monthly income: '))
monthly_expese = int(input('Enter your total monthly expenses: '))

savings = monthly_icome - monthly_expese
yearly_savings = savings * 12 + (savings * 12 * 0.05)

print(f"your monthly savings after: ${savings}")
print(f"Projected savings after one year, with interest, is: ${yearly_savings}")