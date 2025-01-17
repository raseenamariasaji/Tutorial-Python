#Income Tax Calculation
income = float(input("Enter your (annual)salary:"))
tax =0
if income<= 250000:
    tax=0
elif income<=500000:
    tax=((income-250000)*0.05)
elif income<=1000000:
    tax=(((income-500000)*0.2)+(250000*0.05))
else:
    tax=(((income-1000000)*0.3)+(500000*0.2)+(250000*0.05))
print("Total payable income tax:",tax)
