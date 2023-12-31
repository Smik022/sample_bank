dat={}
users=[]


def menu():
    while True:
        print(f"Welcome to Smik Bank")
        print(f"1)Open a new account\n2)Login to your account\n3)Exit")
        a=input("Choose your desired option: ")
        if a=="1":
            open()
        elif a=="2":
            login()
        elif a=="3":
            break
        else:
            print("Invalid option")


class Account:
    id=23280000

    def __init__(self,name,pas,balance=0):
        self.id=id
        self.name=name
        self.pas=pas
        self.balance=balance
        Account.id+=1
        dat[self.name]=self.pas
        users.append(self)


def find_user_by_name(name):
    for user in users:
        if user.name == name:
            return user
    return None


def deposit(user,bal):
    user.balance+=int(bal)
    print(f"Amount deposited successfully! Your current balance: {user.balance}")


def withdraw(user,bal):
    user.balance-=int(bal)
    print(f"Amount withdrawn successfully! Your current balance: {user.balance}")


def open():
    name=input("Enter your Name: ")
    pas=input("Enter your password: ")
    return Account(name,pas)


def ui(user):
    while True:
        print(f"Welcome {user.name}! Your Balance is: $ {user.balance}")
        print("1)Deposit Balance\n2)Withdraw amount\n3)Log out")
        n=input("Enter your choice: ")
        if n=="1":
            bal=input("Enter amount to deposit: ")
            deposit(user,bal)
        elif n=="2":
            bal=input("Enter amount to withdraw: ")
            withdraw(user,bal)
        elif n=="3":
            break
    return


def login():
    n=input("Enter your name: ")
    p=input("Enter your password: ")
    if n in dat and dat[n] == p:
        print("Login successful!")
        user = find_user_by_name(n)
        ui(user)
    else:
        print("Invalid credentials. Please try again.")


def main():
    menu()
    exit()
main()
