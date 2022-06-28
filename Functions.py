from ast import Add
import os 
import platform 
import mysql.connector
import pandas as pd 

mydb = mysql.connector.connect(host = 'localhost', user = 'root', password = 'hossein',database = 'Bank')
myCursor = mydb.cursor()

def AccInsert():
    L = []
    Accno = int(input("Enter the Account number : "))
    L.append(Accno)
    name = input("Enter the Customer Name : ")
    L.append(name)

    age = int(input("Enter Age of Customer: "))
    L.append(age)

    occup = input("Enter the Customer Occupation: ")
    L.append(occup)

    Address = input("Enter the Addres of the Customer: ")
    L.append(Address)

    Mob = int(input("Enter the Mobiel number: "))
    L.append(Mob)

    Aadharno = int(input("Enter the Aadhar number: "))
    L.append(Aadharno)

    Amt = float(input("Enter the Money Deposited: "))
    L.append(Amt)

    AccType = input("Enter the Account Type (Saving/RD/PPf/Current):")
    L.append(AccType)

    cust = (L)

    sql = "INSERT INTO Account(Accno, Name, Age , Occup, Address, Mob, Aadharno, amt, AccType) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"

    myCursor.execute(sql, cust)
    mydb.commit()


def AccView():
    print("Select the search criteria: ")
    print('1. Acc no')
    print('2. Name')
    print('3.Mobile ')
    print('4.Adhar ')
    print('5.View All')
    ch = int(input("Enter the Choice: "))

    if ch == 1:
        s = int(input("Enter ACC no :"))
        rl = (s, )
        sql = "SELECT * FROM account WHERE Accno = %s"
        myCursor.execute(sql,rl)
    elif ch == 2:
        s = input("Enter Name : ")
        rl = (s, )
        sql = "SELECT * FROM account WHERE Name = %s"
    elif ch == 3:
        s = int(input("Enter Mobile No:"))
        rl = (s, )
        sql ="SELECT * FROM account WHERE Mob = %s"
        myCursor.execute(sql, rl)

    elif ch == 4:
        s = input("Ente Adhar :")
        rl = (s, )
        sql = "SELECT * FROM account WHERE Aadharno = %s"
        myCursor.execut(sql, rl)
    elif ch == 5:
        sql = "SELECT * FROM account"
        myCursor.execute(sql)

    res = myCursor.fetchall()
    print("The Customer detial are as follows: ")

    k = pd.DataFrame(res, columns=['AcNo', 'Name', 'Age', 'Occn', 'Add', 'Mob', 'Aadh', 'Amt', 'AccTy'])
    print(k)



def AccDeposit():
    L = []
    Accno = int(input("Enter the Account number: "))
    L.append(Accno)
    Amtdeposit = eval(input("Enter the Amount to be deposited: "))
    L.append(Amtdeposit)
    month = input("Enter month of Salary: ")
    L.append(month)

    cust = (L)
    sql = "INSERT INTO amt(Accno, Amtdeposite, Month) VALUES(%s, %s, %s)"
    myCursor.execute(sql, cust)
    mydb.commit()


def accView():
    print("Please enter the details to view the Money details:")
    Accno = int(input("Enter the Account number of the Customer whose amount is to be viewed:"))
    sql = "SELECT * FROM account INNER JOIN amt ON account.Accno = amt.Accno and amt.Accno = %s"

    rl = (Accno,)
    myCursor.execute(sql, rl)
    res = myCursor.fetchall()

    for x in res:
        print(x)

def closeAcc():
    Accno = int(input("Enter the Account number of the Customer to be closed : "))
    rl = (Accno, )
    sql = "DELETE FROM amt WHERE Accno = %s"
    myCursor.execute(sql, rl)
    sql = "DELETE FROM Account WHERE Accno = %s"
    myCursor.execute(sql, rl)
    mydb.commit()

