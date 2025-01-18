#Simple Interest Calculation
amount = float(input("Enter the principal amount:"))
time = int(input("Enter the time period(in years):"))
rate = float(input("Enter the rate of interest:"))
print("{:<10} {:<15} {:<15}".format("Year", "Interest", "Total Amount"))
print("-"*40)
total_si = 0
for year in range(1, time + 1):
    total_si = (amount * year * rate) / 100
    total_amt = amount + total_si
    print("{:<10} {:<15.2f} {:<15.2f}".format(year, total_si, total_amt))
print("\nTotal Interest: {:.2f}".format(total_si))
print("Total amount: {:.2f}".format(total_amt))