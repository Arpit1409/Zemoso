#Problem 1
balance = input("Balance: ")
monthlyPaymentRate = input("Monthly Payment Rate: ")
annualInterestRate = input("Annual Interest Rate: ")
for i in range(12):
    balance = balance - (balance * monthlyPaymentRate) + ((balance - (balance * monthlyPaymentRate)) * (annualInterestRate/12))
print("Remaining balance:", round(balance, 2))