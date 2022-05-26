# Variable declaration
sub_code=0
sub_name=""

def subjectadd (db,cursor):
    while True:
        try:
            sub_code=int(input("Enter the subject code to be inserted : "))
        except ValueError:
            print("Wrong input given. Please enter a valid book number\n")
            continue
        else:
            break
    sub_name=input("Enter the subject name to be inserted : ")

    # SQL statements to insert data
    SQL_text="INSERT INTO subject_tbl(Subject_code,Subject_name) VALUES (%s,%s);"
    SQL_values=(sub_code,sub_name)
    cursor.execute(SQL_text,SQL_values) # execute command
    db.commit() # commit changes
    print()
    print(cursor.rowcount,"Record/s added") # Print change occured