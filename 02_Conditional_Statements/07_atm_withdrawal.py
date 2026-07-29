amount = int(input("Enter Withdrawal amount: "))
balance = 5000

if amount <= balance:
    print("Transaction Succesful")
    total= balance - amount
    print("Remaing Balance amount: ", total)

else: 
    print("Insufficient Balance")
    print("Remaining Balance: ", balance)
