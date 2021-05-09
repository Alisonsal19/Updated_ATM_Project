import random
import validation
import database
from getpass import getpass

# database = {
#     4318246141: ["alison", "sal", "ansfanf", "re", 200]
# }

user_auth = "data/auth_session/"


def init():
    print("Welcome to the BANK")
    have_account = int(input("Do you have an account?: 1 (yes) 2 (no) \n"))
    if have_account == 1:
        login()
    elif have_account == 2:
        register()
    else:
        print("Invalid option")
        init()


def login():
    print(" **** LOGIN  **** ")

    user_account_number = input("What is your account number? \n")

    is_valid_accnum = validation.account_number_validation(user_account_number)

    if is_valid_accnum:

        password = getpass("What is your password? \n")
        user = database.auth_user(user_account_number, password)
        
        if user:
            bank_operations(user)

        print("Invalid account or password")
        login()


    else:
        print("Account Number Invalid: check if there's 10 digits")
        init()


def register():
    print(" **** REGISTER ***")

    email = input("What is your email? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = getpass("Create a password? \n")


    account_number = generation_account_number()

    # database[account_number] = [first_name, last_name, email, password, 0]
    user_created = database.create(account_number, first_name, last_name, email, password)

    if user_created:
        print("Your account has been created")
        print("== === == === == ===")
        print("Your account number is: %d" % account_number)
        print("Make sure you keep it safe!")
        print("== === == === == ===")
        login()
    else:
        print("Please try again")
        register()


def bank_operations(user):
    print("Welcome % s %s" % (user[0], user[1]))
    selected_option = int(input("What would you like to do? (1) Deposit (2) Withdrawal (3) Logout (4) Report (5) Exit \n"))

    if selected_option == 1:
        deposit_operation(user)
    elif selected_option == 2:
        withdrawal_operation(user)
    elif selected_option == 3:
        login()
    elif selected_option == 4:
        report_problem() 
    elif selected_option == 5:
        print("Thank you, come again!")
        exit()
    else:
        print("Invalid option selected")
        bank_operations(user)


def withdrawal_operation(user):
    print("********* WITHDRAWAL **********")
    # get current balance
    # get amount to withdraw
    # check if the current balance > withdraw balance
    # deduct withdraw amount form current balance
    # display current balance


    withdrawal_amount = int(input("How much would you like to withdraw? \n"))
    print("You withdrew $%s" % withdrawal_amount + "Take your cash \n ")

    balance = int(user[4])
    updated_balance = str(balance - int(withdrawal_amount))
    print("Current balacne is $ %s" %updated_balance)
    database.withdrawal(user, withdrawal_amount)
    init()
    pass


def deposit_operation(user):
    print("******** DEPOSIT ********")

    # get current balance
    # get account to deposit
    # add deposited amount to current balance
    # display current balance


    depoist_amount = int(input("How much would you like to deposit?"))
    print("Deposit of $ %s \n" %depoist_amount)
    current_balance = int(user[4])
    new_balance = str(current_balance + int(depoist_amount))
    print("Current balance is $ %s \n" %new_balance)
    database.deposit(user, depoist_amount)
    init()
    pass


def report_problem():
    problem_to_report = input("Report: What is the issue? \n")
    print("Thank you for your complaint \n")
    init()
    pass


def set_current_balance(user_details, balance):
    user_details[4] = balance


def get_current_balance(user_details):
    return user_details[4]


def generation_account_number():
    return random.randrange(1111111111, 9999999999)


def logout():
    print("Thank you! Please come again!")


init()
