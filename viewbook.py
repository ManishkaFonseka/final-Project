# Variable declaration
more=""


def bookview(cursor):
    cursor.execute("SELECT Book_No,Title,Author FROM book_tbl;") # Execute SQL query
    data=cursor.fetchall() # Fetch data

    for value in data:
        print("book",value[0],":",value[1],"by",value[2])

    while True:
        more=(input("Enter book No. to view more info on that book or, type exit to exit setup : "))
        if more.isdigit():
            print()
            cursor.execute("SELECT * FROM book_tbl WHERE Book_No=%s;",list(more)) # Execute SQL query
            data=cursor.fetchall() # Fetch data
            for value in data:
                print("Book No        : ",value[0])
                print("Title          : ",value[1])
                print("Author         : ",value[2])
                print("Publisher      : ",value[3])
                print("ISBN No.       : ",value[4])
                print("Price          : ",value[5])
                print("Location       : ",value[6])
                print("subject code   : ",value[7])
                print("published year : ",value[8])
                print()
            break
                
        elif more=="Exit" or more=="exit":
            break
        else:
            print("Enter valid input\n")
            continue