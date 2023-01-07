#!/usr/bin/env python3
import mysql.connector
import time

mycon = mysql.connector.connect(host='localhost', user='root', passwd='project', database='hms')
cursor = mycon.cursor()
if mycon.is_connected() == False:
    print('con fail')


# --------------------FUNCTIONS--------------------
# -------------------------------------------------
# --------------------------------------------new warden --------------------------------------------
def wardadd():
    name = input('Enter Name :')
    empid = input('Enter Employee ID : ')
    contact = input('Enter Contact :')
    username = input('Enter username of choice : ')
    passwd = input('Enter password : ')
    passconf = input('Confirm Password :')
    while passwd != passconf:
        passconf = input('Password not matching. Try Again ! --> ')
        passconf = input('Confirm Password :')

    details = (name, contact, username, passwd, empid)
    cursor.execute(details)

    return


# --------------------------------------------add student--------------------------------------------

def addstu():
    name = input('Enter Name :')
    contact = input('Enter Contact :')
    Address = input('Enter Address : ')
    adm = input('Enter Admission No. :')
    h_name = input('Enter Hostel Name :')
    Rm_no = input('Enter Room NO :')
    details = (name, contact, Address, adm, h_name, Rm_no)
    cursor.execute(details)
    return


# --------------------------------------------fee generation--------------------------------------------

def calcfee():
    admno = input('Enter Admission no : ')
    cursor.execute(f'select hostel_name from student where Adm_no = {admno}')
    hostel =cursor.fetchone()
    for a in hostel:
        hos = str(a)
        cursor.execute(f'select tot_due from {hos} where Adm_no = {admno}')
        fee= cursor.fetchone()
        print('Fee Due : INR',fee)


# --------------------------------------------fee payment--------------------------------------------

def payfee():
    admno = int(input('Enter Admission no : '))
    cursor.execute(f'select hostel_name from student where Adm_no = {admno}')
    hostel = cursor.fetchone()
    for a in hostel:
        hos = str(a)
        cursor.execute(f'update {hos} set tot_due = 0 where Adm_no = {admno}')
        cursor.execute(f'update {hos} set fee = 0 where Adm_no = {admno}')
        cursor.execute(f'update {hos} set fine = 0 where Adm_no = {admno}')
    print('..')
    time.sleep(2)
    print('..')
    print('Fee Paid Successfully!')


# --------------------------------------------guest entry--------------------------------------------

def guest():
    nam = str(input('Enter Name :'))
    con = str(input('Enter Contact :'))
    stu = input('Enter Student Name : ')
    roomno = input('Enter Room No : ')
    rel = input('Enter Relation : ')
    cursor.execute(f'INSERT INTO guest(name,contact,student,room_no,relation) Values(\"{nam}\",{con},\"{stu}\",{roomno},\"{rel}\")')



# --------------------------------------------login--------------------------------------------
def log():
    empid = input('Enter Employee ID : ')
    passwd = input('Enter Password : ')
    st = f"Select passwd from warden where empid = {empid}"
    cursor.execute(st)
    data = cursor.fetchone()
    i = 0

    for a in data:
        if a != passwd:
            print(3 - i, 'Attemps Left !')
            passwd = input('Enter Password : ')
            i = i + 1
            print(3 - i, 'Attemps Left !')
        else:
            break


# -------------------------------------------Retrieving hostel data -------------------------------------------
def hostel_data():
    print('Hostels Available: ')
    print('1.ARAVALI')
    print('2.HIMALAYA')
    print('3.SHIVALIK')
    print('4.NILGIRI')
    hostel = ''
    hos = int(input('Choose Hostel : '))
    if hos == 1:
        hostel = 'aravali'
    elif hos == 2:
        hostel = 'himalaya'
    elif hos == 3:
        hostel = 'shivalik'
    elif hos == 4:
        hostel = 'nilgiri'
    print(hostel)
    cursor.execute(f'Select * from {hostel}')
    da = cursor.fetchall()
    for i in da :
        print(i)


# -------------------------------------------Retrieving data -------------------------------------------

def data():
    adm = input('Enter Student Adm No. :')
    st = f'select * from student where Adm_no={adm}'
    cursor.execute(st)
    dat = cursor.fetchall()
    print(dat)



# ---------------------------------------------------END FUNCTIONS---------------------------------------------------
# --------------------------------------------------------------------------------------------------------------

# ---------------------LogIN-------------------

print('**  LOGIN  **')

log()

# main program
while True:
    print('')
    print('\"HOSTEL MANAGEMENT SYSTEM\"')

    print('')
    print('1.Guest Entry')
    print('2.General Operations')
    choice = int(input('Preferred operation : '))
    if choice == 1:
        guest()
    elif choice == 2:
        print('Available Operations : ')
        print('')
        print('1. View Student Details')
        print('2. Fee payment')
        print('3. Add New Student')
        print('4. Add New Warden ')
        print('5. Get Hostel Detail')
        op = int(input('Preferred operation : '))
        if op == 1:
            data()
        elif op == 2:
            calcfee()
            dec = input('PAY DUE FEE Y/N : ')
            deci = dec.lower()
            if deci == 'y':
                payfee()
            else:
                continue
        elif op == 3:
            addstu()
        elif op == 4:
            wardadd()
        elif op == 5:
            hostel_data()
    else:
        print('Invalid Choice ')
        break
