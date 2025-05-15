expenses = [{"item": "Food", "amount": 1500}]


def opener():
    print('Welcome to your Expense Tracker','\n', '\n')

    tasks = ['Add Expense', 'View Expenses', 'View Total', 'Exit']
    count = 1

    print('Options')
    for i in tasks:
        print(count, i)
        count += 1

def condition():
    
    while True:
        opener()
    
        choice = int(input('Choose the serial number of any option to continue: '))
        if choice == 1:
            item = input('Enter item name: ')
            amount = int(input('Enter amount: '))
            expenses.append({'item': item, 'amount': amount})
            print(expenses)
            print('Enpense added!', '\n')
        elif choice == 2:
            for item in expenses:
                print('Item:',item['item'], 'and Amount:', item['amount'], '\n')
        elif choice == 3:
            total_amount = 0
            for item in expenses:
                print('Item:',item['item'], 'and Amount:', item['amount'])
                total_amount += item['amount']
            print(total_amount, '\n')
        elif choice == 4:
            print('Thank you!', '\n')
            break
        else:
            print('Wrong option', '\n')


def expense_tracker():

    condition()

expense_tracker()