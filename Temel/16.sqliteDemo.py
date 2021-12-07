# -*- coding: utf-8 -*-

import sqlite3

def selectOperasyonlari():
    
    # veri tabanına bağlanma
    
    # eğer veri tabanı ismini yanlış yazarsak, anında 
    # yanlış yazdığımız isimde yeni bir veri tabanı oluşturur
    connection = sqlite3.connect("chinook.db") 
    
    
    # sorgu yazımı
    # cursor = connection.execute("select * from customers")
    
    
    # for row in cursor:
    #     # ilk önce yazdığımız soruguya bakıyoruz ve sorguda tüm tabloyu getir diyoruz
    #     # first name - tabloda ikinci kolona karşılık geliyor o yüzden row[1] yazıyoruz
    #     print("First Name =" + row[1])
    #     print("Last Name =" + row[2] + "\n")
        
        
        
    #--------------------------------------------------------------------------------------
    
    
    
    # cursor = connection.execute("select FirstName,LastName from customers")
    
    
    # for row in cursor:
    #     # sorgu kısmında firstName 1., lastName 2. olduğu için row[0] ve row[1] yazıyoruz
    #     print("First Name =" + row[0])
    #     print("Last Name =" + row[1] + "\n")
    
    
    
    #-------------------------------------- asc ve desc --------------------------------------
    
    # verilerin sıralanması
    
    
    # cursor = connection.execute("""select FirstName,LastName from customers 
    #                             where city='Prague' or city='Berlin'
    #                             order by FirstName,LastName desc""")    # isme göre sırala, ismi aynı olanları da soyisme göre sırala
    
    # for row in cursor:
    #     print("First Name =" + row[0])
    #     print("Last Name =" + row[1] + "\n")
        
        
    
    #-------------------------------------- group by ve having --------------------------------------
    
    
    # order by - her zaman sorgunun sonuna yazılır    
    # cursor = connection.execute("""select city,count(*) from Customers 
    #                             group by city 
    #                             having count(*)>1
    #                             order by count(*) desc""")  # city""")
                                
    # for row in cursor:
    #     print("City =" + row[0])
    #     print("Count=" + str(row[1]) + "\n")                                                                  
                             
    
    
    #-------------------------------------- like --------------------------------------
    
    # like - gibi demek
    # % işareti her hangi bir veya bir kaç harf olabilir diyor
    # %a% - içinde a harfi geçen demek
    # a% - a harfi ile başlayan demek
    # a% - a harfi ile biten demek
    
    cursor = connection.execute("""select FirstName,LastName from customers 
                                where FirstName like '%a%' """)   
    
    for row in cursor:
        print("First Name =" + row[0])
        print("Last Name =" + row[1] + "\n")
    
    
    # db ile bağlantıyı kapatma5
    connection.close()
    
    
#selectOperasyonlari()


#--------------------------------------------- insert ---------------------------------------------



def insertCustomer():
    connection = sqlite3.connect("chinook.db")
    
    # insert sorgusu
    connection.execute("""insert into customers (firstName,lastName,city,email) 
                       values ('Engin','Demiroğ','Ankara','engindemirog@gmail.com')""")
                       
    # insert kısmını veri tabanına yansıtmak yeni değerleri ora eklemek için bunu commit etmemiz gerekiyor
    connection.commit()
    connection.close()
    

#insertCustomer()


#--------------------------------------------- update ---------------------------------------------



def updateCustomer():
    connection = sqlite3.connect("chinook.db")
    
    # update sorgusu
    connection.execute("""update customers set city='İstanbul' where city='Ankara'""")
    
    
    connection.commit()
    connection.close()
    

#updateCustomer()   


#--------------------------------------------- delete ---------------------------------------------



def deleteCustomer():
    connection = sqlite3.connect("chinook.db")
    
    # delete sorgusu
    connection.execute("""delete from customers where city='İstanbul'""")
                      #"""delete from customers where customerid=60"""
    
    
    connection.commit()
    connection.close()
    

#deleteCustomer()   


#--------------------------------------------- join ---------------------------------------------



def joinOperasyonlari():
    connection = sqlite3.connect("chinook.db")
    
    # join sorgusu
    cursor = connection.execute("""SELECT albums.Title, artists.Name FROM artists INNER JOIN albums on artists.ArtistId=albums.ArtistId""")
    
    for row in cursor:
        print("Title=" + row[0] + " Name =" + row[1] + "\n")
        
    connection.close()
    

joinOperasyonlari()
            