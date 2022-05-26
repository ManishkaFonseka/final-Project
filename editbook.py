# Variable declaration
edit_col=0
edit_bknum=0
where_bknum=0
edit_title=""
edit_author=""
edit_publisher=""
edit_ISBN=0
edit_price=0
edit_location=""
edit_subcode=0
edit_pubyr=0


def bookedit(db,cursor):
    print('List of Columns\n--------------\n1 : Book number\n2 : Tile\n3 : Author\n4 : Publisher\n5 : ISBN number\n6 : Price\n7 : Location\n8 : Subject code\n9 : Published year\n')
    while True:
            try:
                edit_col=int(input("Enter the column number relevant to the column you want to edit : "))
            except ValueError:
                print("Please enter a valid number\n")
                continue
            else:
                if edit_col>0 and edit_col<10:
                    break
                else:
                    print("wrong column number given, Try again\n")
                    continue
    if edit_col==1: # update book number
        while True:  # Get valid integers from user
            try:
                edit_bknum=int(input("Enter the  new book number to be updated : "))
                where_bknum=int(input("Enter the book old book number : "))
                break
            except ValueError:
                print("Enter a valid number\n")
                continue
        uptxt = "UPDATE book_tbl SET Book_No='"+str(edit_bknum)+"'WHERE Book_No="+str(where_bknum)
        cursor.execute(uptxt)
        db.commit()
        print("\n",cursor.rowcount,"Record/s Updated") # Print change occured
    
    elif edit_col==2: # Update title
        edit_title=input("Enter the new Title name to be updated : ")
        while True:  # Get valid integer from user
            try:
                where_bknum=int(input("Enter the book number where Title should be updated : "))
                break
            except ValueError:
                print("Please enter a valid number\n")
                continue
        uptxt = "UPDATE book_tbl SET Title='"+edit_title+"'WHERE Book_No="+str(where_bknum)
        cursor.execute(uptxt)
        db.commit()
        print("\n",cursor.rowcount,"Record/s Updated") # Print change occured
    
    elif edit_col==3: # Update Author
        edit_author=input("Enter the new Author name to be updated : ")
        while True: # Get valid integer from user
            try:
                where_bknum=int(input("Enter the book number where Author should be updated : "))
                break
            except ValueError:
                print("Please enter a valid number\n")
                continue
        uptxt = "UPDATE book_tbl SET Author='"+edit_author+"'WHERE Book_No="+str(where_bknum)
        cursor.execute(uptxt)
        db.commit()
        print("\n",cursor.rowcount,"Record/s Updated") # Print change occured
    
    elif edit_col==4: # Update Publisher
        edit_publisher=input("Enter the new Publisher name to be updated : ")
        while True:  # Get valid integer from user
            try:
                where_bknum=int(input("Enter the book number where publisher should be updated : "))
                break
            except ValueError:
                print("Please enter a valid number\n")
                continue
        uptxt = "UPDATE book_tbl SET Publisher='"+edit_publisher+"'WHERE Book_No="+str(where_bknum)
        cursor.execute(uptxt)
        db.commit()
        print("\n",cursor.rowcount,"Record/s Updated") # Print change occured

    elif edit_col==5: # Update ISBN number
        while True:
            try: # Get valid integers from user
                edit_ISBN=int(input("Enter the new ISBN number to be updated : "))
                where_bknum=int(input("Enter the book number where ISBN number should be updated : "))
                break
            except ValueError:
                print("Please enter a valid number\n")
                continue
        uptxt = "UPDATE book_tbl SET ISBN_No='"+str(edit_ISBN)+"'WHERE Book_No="+str(where_bknum)
        cursor.execute(uptxt)
        db.commit()
        print("\n",cursor.rowcount,"Record/s Updated") # Print change occured

    elif edit_col==6: # Update Price
        while True:
            try: # Get valid integers from user
                edit_price=int(input("Enter the new price to be updated : "))
                where_bknum=int(input("Enter the book number where price should be updated : "))
                break
            except ValueError:
                print("Please enter a valid number\n")
                continue
        uptxt = "UPDATE book_tbl SET Price='"+str(edit_price)+"'WHERE Book_No="+str(where_bknum)
        cursor.execute(uptxt)
        db.commit()
        print("\n",cursor.rowcount,"Record/s Updated") # Print change occured

    elif edit_col==7: # Update Location
        edit_location=str(input("Enter the new Location name to be updated : "))
        while True:
            try: # Get valid integer from user
                where_bknum=int(input("Enter the book number where location should be updated : "))
                break
            except ValueError:
                print("Please enter a valid number\n")
                continue
        uptxt = "UPDATE book_tbl SET Location='"+edit_location+"'WHERE Book_No="+str(where_bknum)
        cursor.execute(uptxt)
        db.commit()
        print("\n",cursor.rowcount,"Record/s Updated") # Print change occured
    
    elif edit_col==8: # Update Subject code
        while True:
            try: # Get valid integers from user
                edit_subcode=int(input("Enter the new Subject code to be updated : "))
                where_bknum=int(input("Enter the book number where Subject code should be updated : "))
                break
            except ValueError:
                print("Please enter a valid number\n")
                continue
        uptxt = "UPDATE book_tbl SET Subject_code='"+str(edit_subcode)+"'WHERE Book_No="+str(where_bknum)
        cursor.execute(uptxt)
        db.commit()
        print("\n",cursor.rowcount,"Record/s Updated") # Print change occured
    
    elif edit_col==9: # Update Published year
        while True:
            try: # Get valid integers from user
                edit_pubyr=int(input("Enter the new Published year to be updated : "))
                where_bknum=int(input("Enter the book number where Published year should be updated : "))
                break
            except ValueError:
                print("Please enter a valid number\n")
                continue
        uptxt = "UPDATE book_tbl SET Publish_yr='"+str(edit_pubyr)+"'WHERE Book_No="+str(where_bknum)
        cursor.execute(uptxt)
        db.commit()
        print("\n",cursor.rowcount,"Record/s Updated") # Print change occured
