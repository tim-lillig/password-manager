from functions import *


def mainHub():
    state = True
    while state is True:
        os.system("clear")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        tprint("Main Hub")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("(1) Accounts Information")
        print("")
        print("(2) Add Account Information")
        print("")
        print("(3) Edit Existing Account")
        print("")
        print("(4) Delete Account")
        print("")
        print("(5) Quit")
        print("")
        choice = input("")
        os.system("clear")
        if choice == '1':
            database()
        elif choice == '2':
            addAccount()
        elif choice == '3':
            editAccount()
        elif choice == '4':
            deleteAccount()
        elif choice == '5':
            state = False


def percentBar():
    os.system("clear")
    for i in range(101):
        time.sleep(.01)
        print("Loading... " + str(i) + "%", end='\r')
    os.system("clear")


def interface():
    os.system("clear")
    percentBar()
    mainHub()
