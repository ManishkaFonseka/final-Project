# Variable declaration
Bk_num=0
Bk_title=""
Bk_author=""
Bk_publisher=""
Bk_ISBN=""
Bk_price=""
BK_location=""
Bk_sub_code=""
Bk_year_published=0


def newbook(db,cursor):
    # Read user inputs
    while True: # Error handling to get only integer as user input
        try:
            Bk_num=int(input("Enter the book number : "))
        except ValueError: # if user input is not integer
            print("Please enter valid number as book number\n")
            continue
        else:
            break
    Bk_title=input("Enter the title of the book : ")
    Bk_author=input("Enter the author of the book : ")
    Bk_publisher=input("Enter the publisher of the book : ")  
    Bk_ISBN=input("Enter the ISBN No. of the book : ")
    Bk_price=input("Enter the price of the book : ")
    BK_location=input("Enter the location of the book : ")
    Bk_sub_code=input("Enter the subject code of the book : ")
    while True: 
        try:
            Bk_year_published=int(input("Enter the published year of the book : "))
        except ValueError: 
            print("Enter correct number as published year")
            continue
        else:
            break
    #SQL statement to insert data
    SQL_text=("INSERT INTO book_tbl(Book_No, Title, Author, Publisher, ISBN_No, Price, Location, Subject_code, Publish_yr) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s);")
    SQL_values=(Bk_num,Bk_title,Bk_author,Bk_publisher,Bk_ISBN,Bk_price,BK_location,Bk_sub_code,Bk_year_published)
    cursor.execute(SQL_text,SQL_values) #execute command
    db.commit() # commit changes
    print()
    print(cursor.rowcount,"Record/s added") # print change occured