stipend = 50
expenses = 80
growth_rate = 0.02
months = 10

total_borrowed = 0

for month in range(1, months + 1):
    total_borrowed += max(0, expenses - stipend)
    expenses *= (1 + growth_rate)

print(f"Загальна сума боргу за {months} місяців: {total_borrowed:.2f} грн.")
