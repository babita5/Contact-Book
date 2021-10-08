import sqlite3
import re

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
con = sqlite3.connect("contact.db")
c=con.cursor()
sql = """CREATE TABLE IF NOT EXISTS contact_book(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    job TEXT NOT NULL,
    email TEXT NOT NULL,
    phone INTEGER);"""

c.execute(sql)


class ProgramLoop():
    def __init__(self):
        pass

    def loop():
        print("Welcome to Contact Book")
        while True:
            name = input("enter name= ")
            job = input('enter job= ')
            while True:
                email = input("enter email= ")
                if (re.fullmatch(regex,email)):
                    break
                else:
                    print("Invalid email")

            
            while True:
                phone = int(input("enter phone= "))
                if len(str(abs(phone))) == 10:
                    break
                        
                else:
                    print("Invalid phone number")
                
            insert = """INSERT INTO contact_book(name,job,email,phone) 
                        VALUES(?,?,?,?);"""
            c.execute(insert,(name,job,email,phone))
            con.commit()
            decision = input("do you want to add another contact?(Y/N) = ").lower()
            if decision != "y":
                break

            

        # print("Contact List: ", contacts)
        read= "SELECT * FROM contact_book"
        c.execute(read)
        for i in c:
            print(i)

        while True:
            dec = int(input("enter 1 for update, 2 for delete, and 3 for search and other number for exit = "))
            if dec == 1:
                new_name = input("enter name = ")
                new_id = int(input("enter id = "))
                update = "UPDATE contact_book SET name=? WHERE id = ?"
                c.execute(update,(new_name, new_id))
                con.commit()
                read= "SELECT * FROM contact_book"
                c.execute(read)
                for i in c:
                    print(i)
                
            elif dec == 2:
                new = int(input("enter id = "))
                delete = "DELETE FROM contact_book WHERE id = '{}'".format(new)
                c.execute(delete)
                con.commit()
                read= "SELECT * FROM contact_book"
                c.execute(read)
                for i in c:
                    print(i)

            elif dec == 3:
                s = input("enter name = ")
                search = "SELECT * FROM contact_book WHERE name = '{}'".format(s)
                c.execute(search)
                for i in c:
                    print(i)

            else:
                break
    

if __name__=="__main__":
    ProgramLoop.loop()

c.close()
con.close()