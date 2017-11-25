import string
import random
import json

logged_in = False  # mark the status of the user
cur_user = 'dch'
cur_pass = '111'


def print_title(s):
    for x in range(10):
        print '-',
    print s,
    for x in range(10):
        print '-',
    print ''
    return


def generate_random_account(size=6, chars=string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def log_in():
    global logged_in
    print 'Please log in'
    temp_user = raw_input('--> Username: ')
    temp_pass = raw_input('--> Password: ')
    accounts = data["accounts"]
    valid = False
    for ac in accounts:
        if ac["name"] == temp_user and ac["password"] == temp_pass:
            logged_in = True
            valid = True
            break
    if valid:
        print "Log in successfully!"
    else:
        print "Username or Password Incorrect!"

    return valid


def create_account():
    print_title('Create Account')
    print 'Please type in the information:'

    name = raw_input("--> Name of client: ")
    address = raw_input("--> Address: ")
    email = raw_input("--> E-mail: ")
    telephone = raw_input("--> Telephone: ")
    init_balance = raw_input('--> Initial Balance: ')
    password = raw_input('--> Password: ')

    save_data(name, address, email, telephone, init_balance, password)

    print 'Successfully Created The Account!'

    return


def show_info():
    print_title('Show Info')
    account = raw_input("-->Account Number: ")
    password = raw_input("--> Password: ")
    accounts = data["accounts"]
    for ac in accounts:
        if ac["account"] == account and ac["password"] == password:
            print "Balance:", ac["init_balance"]
            print "Address:", ac["address"]
            print "Telephone:", ac["telephone"]
            print "E-mail:", ac["email"]
            print "Account Number:", ac["account"]
            print "Name:", ac["name"]
            return
    print "Info Not Found!"
    return


def withdraw():
    print_title('Withdraw')
    account = raw_input('--> Account Number: ')
    password = raw_input('--> Password: ')
    amount = raw_input('--> Amount to withdraw: ')
    accounts = data["accounts"]
    count = 0
    for ac in accounts:
        if ac["account"] == account and ac["password"] == password:
            if int(ac["init_balance"]) > amount:
                data["accounts"][count]["init_balance"] = str(int(ac["init_balance"])-int(amount))
            else:
                print "Not enough balance to withdraw!"
            return
        count = +1

    with open('data.json', 'w') as f:
        json.dump(data, f)
    return


def deposit():
    print_title('Deposit')
    account = raw_input('--> To Account Number: ')
    name = raw_input('--> To Name: ')
    amount = raw_input('--> Amount to deposit')
    accounts = data["accounts"]
    count = 0
    for ac in accounts:
        if ac["account"] == account and ac["name"] == name:
            data["accounts"][count]["init_balance"] = str(int(ac["init_balance"])+int(amount))
            with open('data.json', 'w') as f:
                json.dump(data, f)
            return
        count += 1

    return


def transfer():
    print_title('Transfer')
    account_to = raw_input('--> Account Number To: ')
    name_to = raw_input('--> Name To: ')
    account_from = raw_input('--> Account Number From: ')
    name_from = raw_input('--> Name From: ')
    amount = raw_input('--> Amount To Transfer: ')
    password = raw_input('--> Password: ')

    accounts = data["accounts"]

    count_from = 0
    for ac in accounts:
        if ac["account"] == account_from and ac["name"] == name_from and ac["password"] == password:
            if int(ac["init_balance"]) > amount:
                data["accounts"][count_from]["init_balance"] = str(int(ac["init_balance"]) - int(amount))
            else:
                print "Not enough balance to transfer!"
            return
        count_from += 1

    count_to = 0
    for ac in accounts:
        if ac["account"] == account_to and ac["name"] == name_to:
            if int(ac["init_balance"]) > amount:
                data["accounts"][count_to]["init_balance"] = str(int(ac["init_balance"]) + int(amount))
            else:
                print "Not enough balance to transfer!"
            return
        count_to += 1
    with open('data.json', 'w') as f:
        json.dump(data, f)


def change_info():
    print_title('Change Info: ')
    account = raw_input('--> Account Number: ')

    accounts = data["accounts"]
    count = 0
    temp_data = ""
    exist = False
    for ac in accounts:
        if ac["account"] == account:
            exist = True
            temp_data = ac
            break
        count += 1

    if not exist:
        print "Account does not exist!"
        return

    print "Please type in the field you want to change, leave blank if do not want any change to that field:"
    telephone = raw_input("--> Telephone:")
    email = raw_input("--> E-mail:")
    address = raw_input("--> Address:")
    password = raw_input("--> Password:")
    name = raw_input("--> Name:")
    print "Please confirm your password:"
    password_t = raw_input('--> Password: ')

    if password_t == temp_data["password"]:
        if telephone != "":
            temp_data["telephone"] = telephone
        if email != "":
            temp_data["email"] = email
        if address != "":
            temp_data["address"] = address
        if password != "":
            temp_data["password"] = password
        if name != "":
            temp_data["name"] = name
    else:
        print "Password incorrect!"
        return

    data["accounts"][count] = temp_data

    with open('data.json', 'w') as f:
        json.dump(data, f)

    return


def change_pass():
    print_title('Change Password')
    account = raw_input('--> Account Number: ')
    accounts = data["accounts"]
    count = 0
    temp_data = ""
    exist = False
    for ac in accounts:
        if ac["account"] == account:
            exist = True
            temp_data = ac
            break
        count += 1

    if not exist:
        print "Account does not exist!"
        return

    password = raw_input('--> Please confirm your old Password: ')

    if password != temp_data["password"]:
        print "Password incorrect!"
        return

    password_new = raw_input("--> New password:")
    temp_data["password"] = password_new

    data["accounts"][count] = temp_data

    with open('data.json', 'w') as f:
        json.dump(data, f)

    return


def save_data(name, add, ema, tel, init_b, pas):

    num = generate_random_account(6)
    data["accounts"].append({
        "account": num,
        "name": name,
        "address": add,
        "email": ema,
        "telephone": tel,
        "init_balance": init_b,
        "password": pas
    })

    with open('data.json', 'w') as f:
        json.dump(data, f)
    return


def choose_operation_menu():
    print_title('Welcome to BATMm - ATM machine system')
    print "please choose your operation:"
    print "You have following options: "
    print "create_account", "log_in", "exist"
    op = raw_input("--> ")
    if op == "create_account":
        create_account()
    elif op == "log_in":
        if log_in():
            while logged_in:
                choose_operation()
    elif op == "exist":
        return False
    else:
        print "operation not exist!"

    return True


def choose_operation():
    global logged_in;
    print_title('Thank you for logging into BATMm - ATM machine system')
    print "please choose your operation:"
    print "You have following options:"
    print "show_info", "withdraw", "deposit", "transfer", "change_info", "change_pass", "log_out"
    op = raw_input("--> ")
    if op == "show_info":
        show_info()
    elif op == "withdraw":
        withdraw()
    elif op == "deposit":
        deposit()
    elif op == "transfer":
        transfer()
    elif op == "change_info":
        change_info()
    elif op == "change_pass":
        change_pass()
    elif op == "log_out":
        logged_in = False
    else:
        print "operation not exist!"

    return True


# main codes

# Load User account data
with open('data.json') as data_file:
    data = json.load(data_file)

while choose_operation_menu():
    pass

