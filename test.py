import time
import mysql.connector


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


print("***** Enter digits as inputs *****")
time.sleep(1.5)
while True:
    try: # error handling for integer values

        do=int(input("Enter 1 to read a chapter and enter 2 to write a chapter : "))
    except ValueError:
        print("Wrong input given. Please try again\n")
        continue
    else:
        if do>0 and do<3:
            break
        else:
            print("Wrong input. Please press 1 or 2\n")
            continue

if do==1: # read a book chapter
    while True:
        try:
            bknum=int(input("\nPlease enter the book number of the chapter              : "))
            bkchap=int(input("Please enter the chapter number                          : "))
        except ValueError:
            print("Please insert correct numbers\n")
            continue
        else:
            try:
                file1=open("bkchap\\Book_"+str(bknum)+"_Chap_"+str(bkchap)+".txt","r")
            except FileNotFoundError:
                print("The file you searched cannot be found. Try again")
                continue
            else:
                break
    print()
    print(file1.read(),"\n")
    file1.close()
    

elif do==2: # write a book chapter
    print()
    while True:
        try:
            bknum=int(input("\nPlease enter the book number of the chapter              : "))
            bkchap=int(input("Please enter the chapter number                          : "))
        except ValueError:
            print("Please insert correct numbers\n")
            continue
        else:
            break
    chaptitle=input("Please enter the chapter title : ")
    file2=open("bkchap\\Book_"+str(bknum)+"_Chap_"+str(bkchap)+".txt","w")
    select_book=("SELECT Book_No, Title FROM book_tbl WHERE Book_No="+str(bknum))
    cursor.execute(select_book)
    data=cursor.fetchall()
    for value in data:
        print("Book :",value[0],value[1],"Chapter",bkchap,chaptitle)

    chap_cont=input("Enter the Chapter content :\n")
    file2.write(""+value[1]+" chapter "+str(bkchap)+" "+chaptitle+"\n\n"+chap_cont+"")
    time.sleep(1)
    print("File was created in bkchap folder\n")

    start_pg=int(input("Enter the starting page number : "))
    ending_pg=int(input("Enter the ending page number  : "))
    bk_chap_tbl_SQL=("INSERT INTO bk_chapter_tbl(Book_No, Title, Chapter_No, Start_page, End_page) VALUES ('"+str(bknum)+"','"+chaptitle+"','"+str(bkchap)+"','"+str(start_pg)+"','"+str(ending_pg)+"')")
    cursor.execute(bk_chap_tbl_SQL)
    db.commit()
    print("\n",cursor.rowcount,"Record was updated in database") # print change occured

    file2.close()