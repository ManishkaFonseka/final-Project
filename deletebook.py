# Variable declaration
del_num=0
conf_del=""

def bookdelete(db,cursor):
    while True:
        try:
            del_num=int(input("Enter the book number to be deleted : "))
        except ValueError:
            print("Wrong input given. Please enter a valid book number\n")
            continue
        else:
            break

    # Show the data going to be deleted
    cursor.execute('SELECT Book_No,Title FROM book_tbl WHERE Book_No ="'+str(del_num)+'"')

    data=cursor.fetchall() # Fetch data
    for value in data:
        print("\nAre you sure you want to delete","(book",value[0],"-",value[1],")\n") # confirm book
    while True:
        conf_del=input("Enter 'y' for yes and 'n' for no [y/n] : ") # confirm delete
        if conf_del=='y'or conf_del=='Y': # if yes delete book
            cursor.execute('DELETE FROM book_tbl WHERE Book_No="'+str(del_num)+'"')
            db.commit() # commit changes
            print(cursor.rowcount,"Record/s deleted") # show change occured
            break

        elif conf_del=='n' or conf_del=='N': # if no dont delete book
            print(value[1],"Book was not deleted")
            break

        else: # if wrong input repeat asking delete confirmation
            print("Invalid input please try again\n")
            continue
