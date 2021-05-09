
def account_number_validation(account_number):
    # check if account number is not empty
    # if account number is 10 digits
    # if the account number is an integer

    if account_number:
        try:
            int(account_number)
            if len(str(account_number)) == 10:  # len = length
                return True
        except ValueError:
            return False
        except TypeError:
            return False

    return False
