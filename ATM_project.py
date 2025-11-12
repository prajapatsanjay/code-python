import random
# Initialize ATM state
balance = random.randint(100, 10000000)
attempts = 3
correct_pin = "1234"
print("Welcome to Python ATM")
name = input("what's your name :")
print("Your bank name is Sabi")

while True:
    option = input("Enter option(yes/no or q to quit): ").lower()
    if  option == "yes":
        print("you selected YES")
        break
    elif option == "no":
        print("you selected no ")
        break
    else:
        print("can i hele you sir")

print("can i hele you sir")

# PIN verification loop
while attempts > 0:
    pin = input('Enter your 4-digit PIN: ')
    if pin == correct_pin:
        print('Correct PIN!')
        break
    else:
        attempts -= 1
        if attempts > 0:
            print(f'INCORRECT PIN. You have {attempts} attempt(s) left, try again.')
        else:
            print('You have exceeded your attempts limit.')
            print('Please take your card.')
            exit()

# Main ATM menu
while True:
    print('\n--- ATM Menu ---')
    print('1: that you say to check balance')
    print('2: that you say to check Deposit')
    print('3: that you say to check Withdraw')
    print('4: Exit')
    
    choice = input('Choose which service you want (1 to 4): ')
    
    if choice == '1':
        print(f'Your current balance is: {balance:,} india repuse')
    
    elif choice == '2':
        try:
            deposit_amount = float(input('Please enter the amount you want to deposit: '))
            if deposit_amount > 0:
                balance += deposit_amount
                print(f'Deposit successful. Your new balance is: {balance:,} india repuse')
            else:
                print('Please enter a positive amount.')
        except ValueError:
            print('Invalid amount. Please enter a number.')
    
    elif choice == '3':
        try:
            withdraw_amount = float(input('Please enter the amount you want to withdraw: '))
            if withdraw_amount > 0:
                if withdraw_amount <= balance:
                    balance -= withdraw_amount
                    print(f'Cash withdrawal successful. Your new balance is: {balance:,} india repuse')
                else:
                    print(f'Sorry, insufficient funds. Current balance is: ${balance:,} india repuse')
            else:
                print('Please enter a positive amount.')
        except ValueError:
            print('Invalid amount. Please enter a number.')
    
    elif choice == '4':
        print('Thank you for using this ATM. Goodbye!')
        break
    
    else:
        print('Invalid choice, please try again')



        
        











































        


# PYTHON ATM PROGRAM BY PYTHONDEX
# Visit https://pythondex.com for more information

# user = {
#     'pin': 1234,
#     'balance':1000
# }

# def widthdraw_cash():
#     while True:
#         amount = int(input("Enter the amount of money you want to widthdraw: "))
#         if amount > user['balance']:
#             print("You don't have sufficient balance to make this widthdrawal")
#         else:
#             user['balance'] = user['balance'] - amount
#             print(f"{amount} Dollars successfully widthdrawn your remaining balance is {user['balance']} Dollars")
#             print('')
#             return False

# def balance_enquiry():
#     print(f"Total balance {user['balance']} Dollars")
#     print('')


# is_quit = False

# print('')
# print("Welcome to the Pythondex ATM")

# pin = int(input('Please enter your four digit pin: '))

# if pin == user['pin']:
#     while is_quit == False:
#         print("what do you want to do")
#         print(" Enter 1 to Widthdraw Cash \n Enter 2 for Balance Enquiry \n Enter 3 to Quit")

#         query = int(input("Enter the number corresponding to the activity you want to do: "))

#         if query == 1:
#             widthdraw_cash()
#         elif query == 2:
#             balance_enquiry()
#         elif query == 3:
#             is_quit = True

#         else:
#             print("Please enter a correct value shown")
# else:
#     print("Entered wrong pin")
        
    


    








