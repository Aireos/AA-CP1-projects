

class BankAccount:
    
#setting what their balance is to use later
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
        
#setting the definition for what happens when they want to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False
        
# Setting the definition for what happens when they want to withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False
        
#creating the definition for what happens when they want to check their balance
    def get_balance(self):
        return self.balance
        
#creating the definition for what happens when they want to create an account
def create_account():
    account_number = input("Enter account number: ")
    initial_balance = float(input("Enter initial balance: "))
    return BankAccount(account_number, initial_balance)
    
#start of what they will see
def main():
    accounts = {}
    while True:
        
        #asking what they want to do.
        print("\n1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")
        
        # variable: choice = the option they want to do out of the options above
        choice = input("Enter your choice (1-5): ")
        
        #if we look above we can see that choice 1 was creating an account.
        if choice == '1':
            #using definition made above
            account = create_account()
            #adding account to list of all accounts
            accounts[account.account_number] = account
            #telling the user that it was successful
            print(f"Account {account.account_number} created successfully!")

        #setting what happens for all the other options
        elif choice in ['2', '3', '4']:
            
            #because we are not making an account we need to know what their account number is to know what info to use
            account_number = input("Enter account number: ")
            
            #double checking that it is a real account
            if account_number in accounts:
                account = accounts[account_number]

                #if we look above we can see that choice 2 was depositing.
                if choice == '2':
                    
                    #asking how much they want to deposit
                    amount = float(input("Enter deposit amount: "))
                    
                    #setting what happens if they have said money
                    if account.deposit(amount):
                        print(f"Deposited ${amount:.2f} successfully!")

                    #setting what happens if they don't have said money
                    else:
                        print("Invalid deposit amount.")

                #if we look above we can see that choice 3 was withdrawing.
                elif choice == '3':

                    #asking how much they want to withdraw
                    amount = float(input("Enter withdrawal amount: "))

                    #setting what happens if they have said money
                    if account.withdraw(amount):
                        print(f"Withdrawn ${amount:.2f} successfully!")

                    #setting what happens if they don't have said money
                    else:
                        print("Invalid withdrawal amount or insufficient funds.")

                #we know that choice four we don't have do a elif for so we do an else
                else:
                    print(f"Current balance: ${account.get_balance():.2f}")
                    
            #setting what happens if the account is fake
            else:
                print("Account not found.")
                
        #if we look above we can see that choice 5 was exciting.
        elif choice == '5':
            print("Thank you for using our banking system. Goodbye!")
            break
            
        #just in case they enter higher or lower then 1-5
        else:
            print("Invalid choice. Please try again.")

# I do not understand what this is for.
if __name__ == "__main__":
    main()
