import imp
import os
import platform
from tkinter import Menu
from  Database import *
from Functions import *

def MenuSet():
    print("Enter 1: To Add Customer: ")
    print("Enter 2: To View Customer: ")
    print("Enter 3: To View Deposit Money: ")
    print("Enter 4: To Close Account : ")
    print("Enter 5: To View All Customer Details: ")

    try: 
        userInput = int(input("Please Select an Above Option:"))
    except ValueError:
        exit("\n Hy! That's Not A Number")
    else:
        print("\n")
        if userInput == 1:
            AccInsert()
        elif userInput == 2:
            AccView()
        elif userInput == 3:
            AccDeposit()
        elif userInput == 4:
            closeAcc()
        elif userInput == 5:
            AccView()    
        else:
            print("Enter correct choice ... :")


def runAgain():
    runAgn = input("\n Want To Run Again Y/n:")
    while runAgn.lower() == 'y':
        if platform.system() == "Windows":
            print(os.system('cls'))
        else:
            print(os.system('clear'))
        MenuSet()


MenuSet()
runAgain()