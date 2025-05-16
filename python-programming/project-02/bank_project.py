class Bank_system():
    def __init__(self, balance):
        self.balance = balance

    def deposit(self):
        confirm_deposit = input('Are you sure you want to deposit? yes/no \n')
        if confirm_deposit == 'yes':
            deposit_amount = eval(input('How much Do you want to Deposit? \n'))
            self.balance += deposit_amount
            print('You have successfully deposited {}, \n Your new balance is {}'.format(deposit_amount, self.balance))
        
    def withdraw(self):
        confirm_withdraw = input('Are you sure you want to withdraw? yes/no \n')
        if confirm_withdraw == 'yes':
            withdrawal_amount = eval(input('How much do you want to withdraw? \n'))
            if withdrawal_amount > self.balance:
                print('Insufficient balance. \n Would you like to request an over draft')
                comfirm_overdraft = input('yes/no')
                if comfirm_overdraft == 'yes':
                    print('Your request is under review, an email will be sent to you soon')
            else:
                self.balance -= withdrawal_amount
                print('You have successfully withdrawn {}, \n Your new balance is {}'.format(withdrawal_amount, self.balance))

    def my_balance(self):
        print('Your balance is: {}'.format(self.balance))


def gtbank(balance):
    bank_system = Bank_system(balance)

    print('Welcome to your bank.\n \n Choose the serial number of any option to continue')
    print('1. Withdraw \n2. Deposit \n3.Check balance')
    option = eval(input(''))
    if option == 1:
        bank_system.withdraw()
    elif option == 2:
        bank_system.deposit()
    elif option == 3:
        bank_system.my_balance()
    else:
        print('Invalid option')


gtbank(1500)