#O.R.M -> Object Relational Mapping
#Translating dn rows into objects using oop

"""
-> class are related to a whole table
-> attributes are columns
-> instances are rows
"""
import sqlite3
#Create connection to our db
con = sqlite3.connect("ecom2.sqlite3")

#create a cursor 
cur = con.cursor()

class Customer:
    TABLE_NAME ="customers"

    def __init__(self,name,phone):
        self.name=name
        self.phone=phone

    def save (self):
        sql= f"""
            INSERT INTO {self.TABLE_NAME} (name,phone)
            VALUES (?,?)
        """
        cur.execute(sql,(self.name,self.phone))
        con.commit()
        print(f"{self.name} inserted")
            

    @classmethod
    def create_table(cls):
        sql=f"""
           CREATE TABLE IF NOT EXISTS {cls.TABLE_NAME}(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL UNIQUE
        )
        """    
        cur.execute(sql)
        #this persists changes to our db
        con.commit()
        print("Customer table created succesfully")

Customer.create_table()        

customer1=Customer("Collins","07446231783")
#customer1.save()
customer2=Customer("Daud","0799542016")
customer2.save()