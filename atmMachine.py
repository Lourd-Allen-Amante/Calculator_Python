from datetime import datetime

print("Gemini Bank ATM")
balance = 0.00
history = []
time = datetime.now().strftime("%Y-%m-%d")

while True:
    print("[1] Balance [2] Deposit [3] Withdraw [4] History [5] Remove [6] Exit")
    select = int(input("Select an option: "))


    match select:
        case 1:
            print(f"Your current balance: ${balance:.2f}")
        case 2:
           amount = int(input("Enter amount to deposit: "))
           balance += amount
           print(f"Success! Your new balance is: ${balance:.2f}")
           history.append(f"Amount: +{amount:.2f}")
        case 3:
           withdraw = float(input("How much you want to withdraw: "))
           if withdraw <= balance:
             balance -= withdraw
             print(f"Success! Your new balance is: ${balance:.2f}")
             history.append(f"Withdraw: -{withdraw:.2f}")
           else:
             print(f"Error: Insufficient funds! \nYou only have ${balance:.2f} available. Transaction cancelled.")
        case 4:
            print("-----Transaction History------ ")
            if len(history) == 0:
                print ("No transaction found :(")
            else:
                for entry in history:
                    print(time,entry)
        case 5:
            if len(history) > 0:
                print("Removing last transaction...")
                print(f"Success! Transaction {history.pop()} has been reversed.")
            else:
                print("The history is currently empty.")
        case 6:
            print("Thanks!")
            break
        case _:
            print("'Invalid Action")
