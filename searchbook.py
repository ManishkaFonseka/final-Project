# Variable declaration
search=""


def booksearch(cursor):
    print("Enter any record from following to search a book in the store\nBook number, Book title, Author or Publisher\n")
    search=str(input())
    search_SQL=("SELECT * FROM book_tbl"
                " WHERE Book_No=%s OR Title=%s OR Author=%s OR Publisher=%s ")
    cursor.execute(search_SQL,(search,search,search,search))# execute query and pass string values as tuples
    data=cursor.fetchall()

    for value in data:
        print("Book Number    : ",value[0])
        print("Title          : ",value[1])
        print("Author         : ",value[2])
        print("Publisher      : ",value[3])
        print("ISBN Number    : ",value[4])
        print("Price          : ",value[5])
        print("Location       : ",value[6])
        print("Subject Code   : ",value[7])
        print("Published Year : ",value[8])
    print()