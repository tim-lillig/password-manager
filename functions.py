import pickle
from art import *
import os
import time
import sys

info = pickle.load(open("accountInfo.dat", "rb"))


def search():
    global accountSearch
    accountSearch = input("Which account would you like to see information about? ")
    try:
        if accountSearch == 'q' or accountSearch == '':
            return
        elif accountSearch == 'ALL':
            os.system("clear")
            print("All Account Names:\n")
            keysList = []
            for keys in info.keys():
                keysList.append(keys)
            keysList.sort()
            for accounts in keysList:
                if accounts == keysList[-1]:
                    print(accounts + "\n")
                else:
                    print(accounts, end=', ')

        else:
            info[accountSearch]
    except:
        print("No account with that name")
        search()


def database():
    global accountSearch
    os.system("clear")
    search()
    if accountSearch == 'q' or accountSearch == '':
        os.system("clear")
        return
    if accountSearch == 'ALL':
        input("")
        return
    os.system("clear")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    tprint(accountSearch)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("USERNAME: {}".format(info[accountSearch]["username"]))
    print("")
    print("PASSWORD: {}".format(info[accountSearch]["password"]))
    print("")
    print("EMAIL: {}".format(info[accountSearch]["email"]))
    print("")
    print("WEBSITE: {}".format(info[accountSearch]["website"]))
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("(1) Search Again")
    print("(2) Edit Account")
    print("(3) Delete Account")
    print("(4) Main Hub")
    print("(5) Quit")
    newChoice = input("")
    if newChoice == "1":
        database()
    if newChoice == "2":
        os.system("clear")
        editSpecificAccount(accountSearch)
    if newChoice == "3":
        deletespecificAccount(accountSearch)
    if newChoice == "4":
        return
    if newChoice == "5":
        os.system("clear")
        sys.exit()


def addAccount():
    websiteName = input("Name of website/program: ")
    if websiteName == 'q' or websiteName == '':
        return
    username = input("Username: ")
    if username == 'q' or username == '':
        return
    password = input("Password: ")
    if password == 'q' or password == '':
        return
    email = input("Email: ")
    if email == 'q' or email == '':
        return
    url = input("Website URL: ")
    if url == 'q' or url == '':
        return
    info[websiteName] = {'username': "{}".format(username),
                         'password': "{}".format(password),
                         'email': "{}".format(email),
                         'website': "{}".format(url)}

    pickle.dump(info, open("accountInfo.dat", "wb"))
    index = 0
    text = '                      |||||||||||||||||||||||||||||||||||'
    emptyText = ''
    os.system("clear")
    print(10 * '\n')
    while index < len(text):
        emptyText += text[index]
        print(emptyText, end='\r')
        if index == 56:
            time.sleep(0.25)
        if text[index] == '|':
            time.sleep(0.05)
        index += 1
    print("                  ----------Account Information Stored----------")
    time.sleep(1)
    return


def editAccount():
    try:
        account = input("Which account would you like to edit?")
        if account == "q" or account == '':
            return
        info[account]
        os.system("clear")
        print("What would you like to change?")
        print("(1) Username")
        print("(2) Password")
        print("(3) Email")
        print("(4) Website URL")
        editChoice = input("")
        os.system("clear")
        if editChoice == "1":
            print("Old Username: {}".format(info[account]['username']))
            newUsername = input("New Username: ")
            info[account]['username'] = newUsername
            pickle.dump(info, open("accountInfo.dat", "wb"))
        if editChoice == "2":
            print("Old Password: {}".format(info[account]['password']))
            newPassword = input("New Username: ")
            info[account]['password'] = newPassword
            pickle.dump(info, open("accountInfo.dat", "wb"))
        if editChoice == "3":
            print("Old Email: {}".format(info[account]['email']))
            newEmail = input("New Email: ")
            info[account]['email'] = newEmail
            pickle.dump(info, open("accountInfo.dat", "wb"))
        if editChoice == "4":
            print("Old Website Name: {}".format(info[account]['website']))
            newWebsiteName = input("New Website Name: ")
            info[account]['website'] = newWebsiteName
            pickle.dump(info, open("accountInfo.dat", "wb"))
    except:
        print("account does not Exist")
        editAccount()


def editSpecificAccount(name):
    account = name
    print("What would you like to change?")
    print("(1) Username")
    print("(2) Password")
    print("(3) Email")
    print("(4) Website URL")
    editChoice = input("")
    if editChoice == "1":
        print("Old Username: {}".format(info[account]['username']))
        newUsername = input("New Username: ")
        info[account]['username'] = newUsername
        pickle.dump(info, open("accountInfo.dat", "wb"))
    if editChoice == "2":
        print("Old Password: {}".format(info[account]['password']))
        newPassword = input("New Username: ")
        info[account]['password'] = newPassword
        pickle.dump(info, open("accountInfo.dat", "wb"))
    if editChoice == "3":
        print("Old Email: {}".format(info[account]['email']))
        newEmail = input("New Email: ")
        info[account]['email'] = newEmail
        pickle.dump(info, open("accountInfo.dat", "wb"))
    if editChoice == "4":
        print("Old Website Name: {}".format(info[account]['website']))
        newWebsiteName = input("New Website Name: ")
        info[account]['website'] = newWebsiteName
        pickle.dump(info, open("accountInfo.dat", "wb"))


def deletion():
    accountName = input("Which account would you like to delete? ")
    try:
        if accountName == 'q' or accountName == '':
            return
        info[accountName]
        yesOrNo = input("Are you sure you want to delete an account's information?(Y/N) ")
        if yesOrNo == 'n' or yesOrNo == 'N' or yesOrNo == '' or yesOrNo == 'q':
            return
        del info[accountName]
        pickle.dump(info, open("accountInfo.dat", "wb"))
        os.system("clear")
        index = 0
        deletingString = ''
        print(10 * '\n')
        while index < 49:
            text = "                            Deleting Account Info"
            if text[index] == ' ':
                deletingString += text[index]
                index += 1
            elif index == 48:
                deletingString += text[index]
                print(deletingString, end='\r')
                time.sleep(1)
                index += 1
            else:
                deletingString += text[index]
                print(deletingString, end='\r')
                time.sleep(0.2)
                index += 1
        print("               ----------Account Information Deleted----------", end='\r')
        time.sleep(2.5)
    except:
        print("Account does not exist")
        deletion()


def deleteAccount():
    os.system("clear")
    deletion()


def deletespecificAccount(name):
    os.system("clear")
    yesOrNo = input("Are you sure you want to delete {} account information??(Y/N) ".format(name))
    if yesOrNo == 'y' or yesOrNo == 'Y':
        del info[name]
        pickle.dump(info, open("accountInfo.dat", "wb"))

        os.system("clear")
        index = 0
        deletingString = ''
        print(10 * '\n')
        while index < 49:
            text = "                            Deleting Account Info"
            if text[index] == ' ':
                deletingString += text[index]
                index += 1
            elif index == 48:
                deletingString += text[index]
                print(deletingString, end='\r')
                time.sleep(1)
                index += 1
            else:
                deletingString += text[index]
                print(deletingString, end='\r')
                time.sleep(0.2)
                index += 1
        print("               ----------Account Information Deleted----------", end='\r')
        time.sleep(2.5)
