# create record
# update
# read
# delete
# CRUD

# find user
import os
import validation
from datetime import datetime


user_db_path = "data/user_record/"
auth_session = "data/auth_session"

def create(user_account_number, first_name, last_name, email, password):
    #  create a file
    # name file - account_number.txt
    # add user to file
    # return true
    user_data = first_name + "," + last_name + "," + email + "," + password + "," + str(0)

    if does_account_number_exist(user_account_number):
        return False

    if does_email_exists(email):
        print("User already exists")
        return False

    completion_status = False

    try:
        f = open(user_db_path + str(user_account_number) + ".txt", "x")
        # f.write(str(user_details))

    except FileExistsError:
        does_file_contain_data = read(user_db_path + str(user_account_number) + ".txt")
        if not does_file_contain_data:
            delete(user_account_number)
        
    else:
        f.write(str(user_data))
        completion_status = True

    finally:
        f.close()
        return completion_status


def read(user_account_number):
    # find user with account number
    # fetch content of the file
    is_vaild_account_number = validation.account_number_validation(user_account_number)
    try:
        if is_vaild_account_number:
            f = open(user_db_path + str(user_account_number) + ".txt", "r")
        else:
            f = open(user_db_path + user_account_number, "r")

    except FileNotFoundError:
        print("User not found")

    except FileExistsError:
        print("User doesn't exists")

    except TypeError:
        print("Invalid account number format")

    else:
        return f.readline()

    return False


def update(user_account_number, user_details):
    print("Update records")
    #  find user with account number
    # fetch the content of the file
    # update the content of the file
    # save file
    # return true
    user = user_details[0] + "," + user_details[1] + "," + user_details[2] + "," + user_details[3] + "," +user_details[4] 

    try:
        f = open(user_db_path + str(user_account_number) + ".txt" , "w")
        f.write(user)
        return True
    except:
        return False




def delete(user_account_number):
    # find user with account number
    # delete user record
    # return true

    delete_successful = False

    if os.path.exists(user_db_path + str(user_account_number) + ".txt"):
       
        try:
            os.remove(user_db_path + str(user_account_number) + ".txt")
            delete_successful = True

        except FileNotFoundError:
            print("User not found")

        finally:
            return delete_successful


def does_email_exists(email):
    # print("find user")
    # find user record in data folder

    all_users = os.listdir(user_db_path)
    for user in all_users:
        user_list = str.split(read(user), ',')
        if email in user_list:
            return True
    return False


def does_account_number_exist(account_number):
    all_users = os.listdir(user_db_path)
    for user in all_users:
        if user == str(account_number) + ".txt":
            return True
    return False


def auth_user(account_number, password):
    if does_account_number_exist(account_number):
        user = str.split(read(account_number), ',')
        if password == user[3]:
            return user

    return False


def auth_session_login (user_account_number):
    print (" **** ENTRY LOG ****")

    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

    try:

       # f = open("data/auth_session/" + str(user_account_number) + ".txt", "x")
       f = open(user_db_path + str(user_account_number) + ".txt", "x")

    except FileExistsError:
        print("Unable to create file record")

    else:
        time = datetime.datetime.now()
        with open("data/auth_session/" + str(user_account_number) + ".txt", "w") as f:
            f.write("Login entry recorded: ", dt_string)
    return True



def auth_session_logout (user_account_number):
    logout_successful = False

    if os.path.exists(user_db_path + str(user_account_number) + ".txt"):
       
        try:
            os.remove(user_db_path + str(user_account_number) + ".txt")
            logout_successful = True

        except FileNotFoundError:
            print("Unable to logout")

        finally:
            return logout_successful


# print(does_email_exists("arimail"))

# print(read(4318246141))
# print(read({"One": "Two"}))

# print(does_email_exists(1520529976))


