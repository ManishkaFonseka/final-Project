import mysql.connector
import viewbook
import searchbook
import addbook
import editbook
import deletebook
import addsubject
import bookchapter
import time

# Variable declaration
redo=""
user_need=0
repeat=""

# Open database connection through dict
conDict=                {
    'host':'localhost',
    'database':'doc334_p2_icw',
    'user':'root',
    'password':''
                        }
# connect database
db=mysql.connector.connect(**conDict)

# Prepare cursor object
cursor=db.cursor()
redo="y"

print("\nWelcome to ABC book store !\n")
time.sleep(1.5)
# Ask user what to do
while redo=="Y" or redo=="y":
    print("\nEnter '1' to view books and other information on books in the store\nEnter '2' to search for a book\nEnter '3' to add a book to the store\nEnter '4' to edit a book\nEnter '5' to delete a book\nEnter '6' to create or view a chapter of a book\nEnter '7' to add a new subject category\n")
    while True:
        try:
            user_need=int(input())
        except ValueError:
            print("Enter only digits as inputs\n")
            continue
        else:
            if user_need>0 and user_need<8:
                break
            else:
                print("Wrong input given. Please enter a number from 1 to 7\n")
                continue
    print()


    if user_need==1: # view book
        while True:
            viewbook.bookview(cursor)
            repeat=input("Do you want to view again press 'y' for yes and 'n' for no [y/n] : ")
            if repeat=='y' or repeat=="Y":
                print()
                continue
            elif repeat=='n' or repeat=='N':
                print()
                break
            else:
                print("Enter valid input\n")
                repeat=input("Do you want to view again press 'y' for yes and 'n' for no [y/n] : ")
                if repeat=='y' or repeat=="Y":
                    continue
                elif repeat=='n' or repeat=='N':
                    break
                else:
                    break
        redo=input("Do you want a another task to be done. Press 'Y' for yes and any other input to exit the program : ")


    elif user_need==2: # Search for a book
        while True:
            searchbook.booksearch(cursor)
            repeat=input("Do you want to search again press 'y' for yes and 'n' for no [y/n] : ")
            if repeat=='y' or repeat=="Y":
                print()
                continue
            elif repeat=='n' or repeat=='N':
                print()
                break
            else:
                print("Enter valid input\n")
                repeat=input("Do you want to search again press 'y' for yes and 'n' for no [y/n] : ")
                if repeat=='y' or repeat=="Y":
                    continue
                elif repeat=='n' or repeat=='N':
                    break
                else:
                    break
        redo=input("Do you want a another task to be done. Press 'Y' for yes and any other input to exit the program : ")


    elif user_need==3: # Enter new books to the store
        while True:
            addbook.newbook(db,cursor)
            repeat=input("Do you want to Add a book again press 'y' for yes and 'n' for no [y/n] : ")
            if repeat=='y' or repeat=="Y":
                print()
                continue
            elif repeat=='n' or repeat=='N':
                print()
                break
            else:
                print("Enter valid input\n")
                repeat=input("Do you want to Add a book again press 'y' for yes and 'n' for no [y/n] : ")
                if repeat=='y' or repeat=="Y":
                    continue
                elif repeat=='n' or repeat=='N':
                    break
                else:
                    break
        redo=input("Do you want a another task to be done. Press 'Y' for yes and any other input to exit the program : ")


    elif user_need==4: # Edit a book
        while True:
            editbook.bookedit(db,cursor)
            repeat=input("Do you want to edit another book press 'y' for yes and 'n' for no [y/n] : ")
            if repeat=='y' or repeat=="Y":
                print()
                continue
            elif repeat=='n' or repeat=='N':
                print()
                break
            else:
                print("Enter valid input\n")
                repeat=input("Do you want to edit another book press 'y' for yes and 'n' for no [y/n] : ")
                if repeat=='y' or repeat=="Y":
                    continue
                elif repeat=='n' or repeat=='N':
                    break
                else:
                    break
        redo=input("Do you want a another task to be done. Press 'Y' for yes and any other input to exit the program : ")


    elif user_need==5: # delete book
        while True:
            deletebook.bookdelete(db,cursor)
            repeat=input("Do you want to delete another book press 'y' for yes and 'n' for no [y/n] : ")
            if repeat=='y' or repeat=="Y":
                print()
                continue
            elif repeat=='n' or repeat=='N':
                print()
                break
            else:
                print("Enter valid input\n")
                repeat=input("Do you want to delete another book press 'y' for yes and 'n' for no [y/n] : ")
                if repeat=='y' or repeat=="Y":
                    continue
                elif repeat=='n' or repeat=='N':
                    break
                else:
                    break
        redo=input("Do you want a another task to be done. Press 'Y' for yes and any other input to exit the program : ")


    elif user_need==6: # create or view chapter of book
        while True:
            bookchapter.bookchap(db,cursor)
            repeat=input("Do you want to create or view a chapter again press 'y' for yes and 'n' for no [y/n] : ")
            if repeat=='y' or repeat=="Y":
                print()
                continue
            elif repeat=='n' or repeat=='N':
                print()
                break
            else:
                print("Enter valid input\n")
                repeat=input("Do you want to create or view a chapter again press 'y' for yes and 'n' for no [y/n] : ")
                if repeat=='y' or repeat=="Y":
                    continue
                elif repeat=='n' or repeat=='N':
                    break
                else:
                    break
        redo=input("Do you want a another task to be done. Press 'Y' for yes and any other input to exit the program : ")


    elif user_need==7 : # add new subject to subject table
        while True:
            addsubject.subjectadd(db,cursor)
            repeat=input("Do you want to add another subject press 'y' for yes and 'n' for no [y/n] : ")
            if repeat=='y' or repeat=="Y":
                print()
                continue
            elif repeat=='n' or repeat=='N':
                print()
                break
            else:
                print("Enter valid input\n")
                repeat=input("Do you want to add another subject press 'y' for yes and 'n' for no [y/n] : ")
                if repeat=='y' or repeat=="Y":
                    continue
                elif repeat=='n' or repeat=='N':
                    break
                else:
                    break
        redo=input("Do you want a another task to be done. Press 'Y' for yes and any other input to exit the program : ")


db.close()