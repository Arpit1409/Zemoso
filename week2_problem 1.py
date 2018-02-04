#Problem 1
balance = float(input("Balance: "))
monthlyPaymentRate = float(input("Monthly Payment Rate: "))
annualInterestRate = float(input("Annual Interest Rate: "))
for i in range(12):
    balance = balance - (balance * monthlyPaymentRate) + ((balance - (balance * monthlyPaymentRate)) * (annualInterestRate/12))
print("Remaining balance:", round(balance, 2))