#This is code generated using Nested loop with the imagination of atm machine operating process.

print("Welcome To Sangmo Resunga Bank.")
print("Bank of your Choice;'Where The Money Never Ends'")
print("Insert your card and donot forget to take your card before withdrawl.")
go_to_home_screen = "Y"
pin_code_attempt = 5
balance= 400000
minimum_balance= 5000
while pin_code_attempt >=0:
    pin_code = int(input("Please Enter your four digits Pin Code : "))
    if pin_code == 1234:
        print("Welcome, We are ready for transection.")
        while go_to_home_screen not in ("No", "no","N","n"):
            print("Please press 1 to check your current Balance.\n")
            print("Please press 2 to withdraw cash.\n")
            print("Please press 3 to Wired deposite your cash.\n")
            print("Please press 4 to return your card.\n")
            press = int(input("Please choose your option: "))
            if press == 1:
                print("your current balance is NPR.", balance, "\n")
                go_to_home_screen = input("Would you like to go to Home Screen?")
                if go_to_home_screen in ("No", "no","N","n"):
                    print("Thank you. Have a good time.")
                    break
            elif press == 2:
                press2= 'Y'
                withdrawl=float(input("Enter your withdrawl amount: "))
                if withdrawl in (1000, 2000,3000,5000,10000,15000,20000,25000,50000,100000):
                    balance=balance-withdrawl
                    balance_quary = 'y'
                    remaining_balance= input("Do you want withdrawl receipt?")
                    if remaining_balance not in ("No", "no","N","n"):
                        print ("Your Remaining Balance is NPR.", balance)
                    go_to_home_screen = input("Would you like to go to Home Screen?")
                    if go_to_home_screen in ("No", "no","N","n"):
                        print("Thank you. Have a good time.")
                        break
                elif withdrawl not in (1000, 2000,3000,5000,10000,15000,20000,25000,50000,100000):
                    print("Invalid amount figure. Please try again \n")
                    break
                   
                elif withdrawl>=(balance-minimum_balance):
                    print("You donot have sufficient balance.")
                    break
            elif press==3:
                press3='Y'
                deposite_amount = float(input("Enter the amount you want to deposite: "))
                balance= balance +  deposite_amount
                print("NPR",deposite_amount,"is successfully deposited. Your Current balance is NPR. ",balance)
                go_to_home_screen = input("Would you like to go to Home Screen?")
                if go_to_home_screen in ("No", "no","N","n"):
                    print("Thank you. Have a good time.")
                    break
            elif press == 4:
                print("your card is sucessfully returned. Please re-insert card for tansection procedure.")
            else:
                print("Your transection is Terminated. \n Please re-enter pin code for tansection and insert number as per instruction.")
                break
    elif pin_code != 1234:
        print("The transection pin code you entered is incorrect.\nPlease verify your pin code.")
        pin_code_attempt= pin_code_attempt -1
        if pin_code_attempt==1:
            print("You have 1 attempt left. \n Please verify your pin code. \n Otherwise your card will be blocked.")
        elif pin_code_attempt==0:
            print("oops! Multiple attempts. \n Your Card is blocked.\n Please contact Bank customer care service. ")
            break
 
    

                        



