from Main import BankAccount

customer_dict = {}              # use account no. as key and class object(customer account) as value
mobile_acc_link = {}            # use mobile no. as key and store account no. as value, for linking purpose

def new_cust():
    name = input('Enter the name of customer: ')
    mobile_no = int(input('Enter the mobile number of customer: '))
    initial_depo = int(input('Enter the initial deposit amount: '))
    if initial_depo <= 0:
        print('Invalid Amount')
        return
    pin = int(input('Create PIN: '))
    customer = BankAccount(name=name, mobile_no=mobile_no, initial_depo=initial_depo, pin=pin)
    customer_dict[customer.cust_acc_num] = customer                 # acct. no. stored as key and oject as value
    mobile_acc_link[customer.mobile_no] = customer.cust_acc_num     # mobile no. linked
    print('New User Created!')
    print(f'Welcome {customer.name} to Corporate Bank. {customer.cust_acc_num} is your account number')

def login():
    account_no = int(input('Enter your Account Number: '))
    account_pin = int(input('Enter your Account PIN: '))
    if account_no in customer_dict.keys() and account_pin == customer_dict[account_no].pin :
        print(f'\n{customer_dict[account_no].name} Logged in')
        customer_dict[account_no].basic_details()
    else:
        print('Account either not exist or the pin is wrong')
        return
    while True:
        user_input1 = input('''Press 1 for deposit:
Press 2 for withdrawl:
Press 3 for money transfer:
Press 4 to log out\n''')
        if user_input1 == '1':
            customer_dict[account_no].deposit()
        elif user_input1 == '2':
