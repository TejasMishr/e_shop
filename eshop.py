#connection
import mysql.connector as sq
db=sq.connect(host="localhost",user="root",passwd="12345")
if db.is_connected():
    print("successfully connected to mysql database")
cursor=db.cursor()
import os.path
from os import path
def write():
        with open("fcheck.txt","w") as f:
            f.write("1")
def write1():
        with open("fcheck.txt","w") as f:
            f.write("0")
def read1():
    with open("fcheck.txt","r") as f:
        c=f.readlines()
        if c[0]=='0':
            tsk=("create database e_shop")
            cursor.execute(tsk)
            tsk1=("use e_shop")
            cursor.execute(tsk1)            
            tsk2=("create table userdata(Name varchar(40),PhoneNo char(10),UserID char(16))")
            cursor.execute(tsk2)
            tsk3=("create table data(PhoneNo char(10),UserID char(16),Catagary varchar(30),Item varchar(56),OrderNo char(20),CardNO char(16))")
            cursor.execute(tsk3)
            write()
   
if path.isfile("fcheck.txt")==False:
    write1()
if path.isfile("fcheck.txt")==True:
            read1()
            tk1=("use e_shop")
            cursor.execute(tk1)
multi=True
import random	

print(" ..................Hi!!! >>WELCOME TO Adiham Shopping<<................")
print("1.Login \n2.Signup(For New User)")
m=int(input("Enter Your Choice :"))
li=[]
li1=[]

#.............signup user.............
def signup():
    
     b=str(input("Enter phone no.:"))
     while len(b)!=10 or b.isdigit()==False or b[0]=='0':
         print ("Invalid ph no!!! Please Check and Try Again")
         b=str(input("enter ph no:"))
     li.append(b)
     global yy    
     yy=b
       
     if len(b)==10:
         
         c=str(input("userid:"))
         d=str(input("Confirm userid:"))
         e=c
         while d!=c:
             print("Incorrect Userid!!Check Userid")
             d=str(input("Confirm userid:"))
         li.append(c)
         global lmd
         lmd=d
         cname=str(input("Enter name: "))
         li.append(cname)         
     if d==c:
             tsk=("INSERT INTO userdata(Name,PhoneNo,UserID)VALUES('{}',{},'{}')".format(li[2],li[0],li[1]))
             cursor.execute(tsk)
             db.commit()
             print("Account created")
             print()
             print("Please login")





#.................login user......................
def b():
     z=0
     be=str(input("Enter phone no. :"))
     while len(be)!=10:
         print("Invalid Phone Number")
         be=str(input("Enter phone no. :"))
     
     c=str(input("Enter userid"))
     tsk=("SELECT PhoneNO,UserID FROM userdata")
     cursor.execute(tsk)
     data=cursor.fetchall()
     
     
     for x in range (1):
         for y in range(len(data)):
             frstdata=data[y]
             ph_no=frstdata[0]
             user_id=frstdata[1]
             if ph_no==be and user_id==c :

                 li.append(be)
                 li.append(c)
                 li1.append(be)
                 li1.append(c)
                 
                 z=1               
                 
     if z==1:     
         print("successfully logged in")
     else:
         print("userid and phone no. do not match!!!please enter again")
         b()
         
def login():
    b()
    
if m==1:
    b()
if m==2:
     signup()
     login()
while m!=1 and m!=2:
    print("Invalid Choice")
    m=int(input("1.Login\n2.Signup\n Enter Your choice:"))
    if m==1:
        b()
    if m==2:
        signup()
        
#...................starting program after successfully login....................

def cat():
    
    print("            ~~~~~CATEGORIES~~~~~                    ")
    print("1. ELECTRONICS")
    print("2.  GROCERY")
    print("3. HOME  DECOR")
    a=int(input("choose category"))
    while a!=1 and a!=2 and a!=3:
        print("Invalid choice")
        cat()
    if a==1:
        cat="Electronics"
        print( )
        print("                                                                ELECTRONICS")
        print("1.MOBILES")
        print("2.LAPTOPS")
        print("3.LED TVS")
       
        
        b=int(input("enter the desired category of product :"))
        if b==1:
            print( )
            print("                                                               MOBILE BRANDS")
            print( )
            print("1.SAMSUNG")
            print("2.ONE PLUS")
            print("3.VIVO")
            c=int(input("select desired brand :"))
            if c==1:
                print( )
                
                print("                                                 SAMSUNG SMARTPHONE SERIES")
                print( )
                print("1.S SERIES")
                print("2.M SERIES")
                print("3.A SERIES")
                d=int(input("select the desired series of samsung smartphones:"))
                  


                if d==1:
                      print( )
                      print("1.SAMSUNG GALAXY S8")
                      print("2.SAMSUNG GALAXY  S9")
                      print("3.SAMSUNG GALAXY  S10")
                      e=int(input("enter desired smartphone :"))
                     
                      if e==1:
                             print( )
                             global zz
                             zz="SAMSUNG GALAXY S8"
                             print("-------------SAMSUNG GALAXY S8-------------")                 
                             print("#####KEY FEATURES####")
                             print("*4 GB RAM:64 GB ROM:Expandable Upto 256 GB")
                             print("15.75cm(6.2 inch)Quad HD+ Display")
                             print("12 MP Rear Camera:8 MP Front Camera")
                             print("3500 mAh Battery")
                             print("Exynos 8895 Octa Core 2.3 GHz Processor")
                             print("Price---------41,900/-")
                             print("Rating----------------4.3")
                             print("Buy Now")
                             
                             item="SAMSUNG GALAXY S8"

                             
                      elif e==2:
                             print( )
                             zz="SAMSUNG GALAXY  S9"
                             print("-----------SAMSUNG GALAXY  S9-----------")
                             print("#####KEY FEATURES####")
                             print("4 GB RAM:64 GB ROM:Expandable Upto 256 GB")
                             print("15.84cm(6.3 inch)Quad HD+ Display")
                             print("12 MP Rear Camera:8 MP Front Camera")
                             print("3750 mAh Battery")
                             print("Exynos 9810 Octa Core 2.3 GHz Processor")
                             print("Price----------49,990/-")
                             print("Rating----------------4.2")
                             print("Buy Now")

                            
                             item="SAMSUNG GALAXY S9"

                             
                      elif e==3:
                             print( )
                             zz="SAMSUNG GALAXY S10"
                             print("------------SAMSUNG GALAXY S10----------")
                             print("#####KEY FEATURES####")
                             print("8 GB RAM:128 GB ROM:Expandable Upto 256 GB")
                             print("15.49cm(6.1 inch)Quad HD+ Display")
                             print("16MP+12 MP Rear Camera:10 MP Front Camera")
                             print("3500 mAh Battery")
                             print("Exynos 9 9820 Octa Core 2.3 GHz Processor")
                             print("Price---------61,900/-")
                             print("Rating----------------4.4")
                             print("Buy Now")
                             
                             item="SAMSUNG GALAXY S10"
                             
                elif d==2:
                      print( )
                      print("1.SAMSUNG GALAXY M10")
                      print("2.SAMSUNG GALAXY M20")
                      print("3.SAMSUNG GALAXY M30")
                      f=int(input("enter desired smartphone :"))
                      if f==1:
                            print( )
                            zz="SAMSUNG GALAXY M10"
                            print("---------SAMSUNG GALAXY M10---------")
                            print("#####KEY FEATURES####")
                            print("3 GB RAM:32 GB ROM:Expandable Upto 256 GB")
                            print("15.8cm(6.22 inch) HD+ Display")
                            print("13 MP Rear Camera:8 MP Front Camera")
                            print("3400 mAh Battery")
                                   
                            print("Price---------8,918/-")
                            print("Rating----------------4.3")
                            print("Buy Now")
                                                         
                            item="SAMSUNG GALAXY M10"
                             
                      elif f==2:
                            print( )
                            zz="SAMSUNG GALAXY M20"
                            print("---------SAMSUNG GALAXY M20---------")
                            print("#####KEY FEATURES####")
                            print("3 GB RAM:32 GB ROM:Expandable Upto 512 GB")
                            print("16 cm(6.3 inch)Full HD+ Display")
                            print("8 MP+8 MP  Dual Rear Camera:8 MP Front Camera")
                            print("5000 mAh Battery")
                            print("Exynos 9 9510 Octa Core 2.1 GHz Processor")
                            print("Price---------10,900/-")
                            print("Rating----------------4.3")
                            print("Buy Now")
                                                         
                            item="SAMSUNG GALAXY M20"
                             
                      else:
                            print( )
                            zz="SAMSUNG GALAXY M30"
                            print("----------SAMSUNG GALAXY M30----------")
                            print("#####KEY FEATURES####")
                            print("4 GB RAM:64 GB ROM:Expandable Upto 512 GB")
                            print("16.26 cm(6.4 inch)Full HD+ Display")
                            print("13 MP Rear Camera:10 MP Front Camera")
                            print("5000 mAh Battery")
                            print("Exynos 9 9820 Octa Core 2.3 GHz Processor")
                            print("Price---------15,500/-")
                            print("Rating----------------4.4")
                            print("Buy Now")
                                                         
                            item="SAMSUNG GALAXY M30"
                             
                else:
                      print( )
                      print("1.SAMSUNG GALAXY A10")
                      print("2.SAMSUNG GALAXY A20")
                      g=int(input("enter desired smartphone :"))
                      if g==1:
                            print( )
                            zz="SAMSUNG GALAXY A10"
                            print("----------SAMSUNG GALAXY A10----------")
                            print("#####KEY FEATURES####")
                            print("2 GB RAM:32 GB ROM:Expandable Upto 512 GB")
                            print("15.75 cm(6.2 inch) HD+ Display")
                            print("13 MP Rear Camera:5 MP Front Camera")
                            print("3400 mAh Battery")
                            print("Exynos  7884 Processor")
                            print("Price---------9,999/-")
                            print("Rating----------------4.3")
                            print("Buy Now")
                                                         
                            item="SAMSUNG GALAXY A10"
                             
                      elif g==2:
                            print( )
                            zz="SAMSUNG GALAXY A20"
                            print("----------SAMSUNG GALAXY A20----------")
                            print("#####KEY FEATURES####")
                            print("3 GB RAM:32 GB ROM:Expandable Upto 512 GB")
                            print("16.26 cm(6.4 inch) HD+ Display")
                            print("13 MP +5MP Rear Camera:8 MP Front Camera")
                            print("4000 mAh Battery")
                            print("Exynos 7884B  Processor")
                            print("Price---------11,500/-")
                            print("Rating----------------4.3")
                            print("Buy Now")
                                                         
                            item="SAMSUNG GALAXY A20"
                             
            elif c==2:
                  print( )
                            
                  print("1.ONE PLUS 5")
                  print("2.ONE PLUS 7")
                  print("3.T SERIES")
                  g=int(input("enter desired smartphone :"))
                  if g==1:
                        print( )
                        zz="ONE PLUS 5"
                        print("----------ONE PLUS 5---------")
                        print("#####KEY FEATURES####")
                        print("8 GB RAM:128 GB ROM:Expandable Upto 512 GB")
                        print("13.97 cm(5.5 inch)Full HD Display")
                        print("16 MP +20MP Rear Camera:16 MP Front Camera")
                        print("3300 mAh Battery")
                        print("Qualcomm Snapdragon 835 Processor")
                                              
                        print("Price---------37,999/-")
                        print("Rating----------------4.4")
                        print("Buy Now")
                                                     
                        item="One Plus 5"
                             
                  elif g==2:
                        print( )
                        zz="ONE PLUS 7"
                        print("---------ONE PLUS 7--------")
                        print("#####KEY FEATURES####")
                        print("6 GB RAM:128 GB ROM:Expandable Upto 512 GB")
                        print("16.28 cm(6.41 inch)Full HD+ Display")
                        print("48 MP +5MP Rear Camera:16 MP Front Camera")
                        print("3700 mAh Battery")
                        print("Price---------32,890/-")
                        print("Rating----------------4.6")
                        print("Buy Now")
                        item="One Plus 7"
                  elif g==3:
                        print( )
                        print("1.ONE PLUS 6T")
                        print("2.ONE PLUS 7T")
                        h=int(input("enter desired smartphone :"))
                        if h==1:
                              print( )
                              zz="ONE PLUS 6T"
                              print("----------ONE PLUS 6T--------")
                              print("#####KEY FEATURES####")
                              print("6 GB RAM:128 GB ROM")
                              print("16.28 cm(6.41 inch) HD Display")
                              print("16 MP +20MP Rear Camera:16 MP Front Camera")
                              print("4000 mAh Battery")
                              print("Quallcom Snapdragon 835 Processor")
                              print("Price---------32,999/-")
                              print("Rating----------------4.7")
                              print("Buy Now")
                              item="One Plus 6T"
                        else:
                              print( )
                              zz="ONE PLUS 7T"
                              print("---------ONE PLUS 7T---------")
                              print("#####KEY FEATURES####")
                              print("6 GB RAM:128 GB ROM")
                              print("16.33 cm(6.44 inch) FHD+ Display")
                              print("20 MP +20MP Rear Camera:32 MP Front Camera")
                              print("4000 mAh Battery")
                              print("Quallcom Snapdragon 835 Processor")
                              print("Price---------36,999/-")
                              print("Rating----------------4.7")
                              print("Buy Now")
                              item="One Plus 7T"
            elif c==3:
                  print( )
                  print("1.VIVO Z1 PRO")
                  print("2. VIVO Y Series")
                  print("3.VIVO V Series")
                  i=int(input("enter desired smartphone or series :"))
                  if i==1:
                        print( )
                        zz="VIVO Z1 PRO"
                        print("------------VIVO Z1 PRO------------")
                        print("#####KEY FEATURES####")
                        print("6 GB RAM:64 GB ROM")
                        print("16.59 cm(6.53 inch) FHD+ Display")
                        print("16 MP+8MP +2MP Rear Camera:32 MP Front Camera")
                        print("5000 mAh Battery")
                        print("Quallcom Snapdragon 712 AI Octa Core 2.3 GHz Processor")
                        print("Price---------14,990/-")
                        print("Rating----------------4.5")
                        print("Buy Now")
                        item="VIVO Z1 PRO"
                  elif i==2:
                        
                        print("1. VIVO Y 15")
                        print("2. VIVO Y 17")
                        print("3. VIVO Y90")
                        j=int(input("enter desired smartphone"))
                        if j==1:
                              zz="VIVO Y15"
                              print("---------VIVO Y 15--------")
                              print("#####KEY FEATURES####")
                              print("4 GB RAM:64 GB ROM")
                              print("16.213cm(6.35 inch) HD Display")
                              print("13 MP +8MP+2MP Rear Camera:16 MP Front Camera")
                              print("5000 mAh Battery")
                              print("Quallcom Snapdragon 665 Processor")
                              print("Price---------12,950/-")
                              print("Rating----------------4.4")
                              print("Buy Now")
                              item="VIVO Y 15"
                        elif j==2:
                              zz="VIVO Y17"
                              print("---------VIVO Y 17---------")
                              print("#####KEY FEATURES####")
                              print("4 GB RAM:128 GB ROM")
                              print("16.13 cm(6.35 inch) HD+Display")
                              print("13 MP+8MP +2MP Rear Camera:20 MP Front Camera")
                              print("5000 mAh Battery")
                              print("MTK Helio P35 Processor")
                              print("Price---------14,990/-")
                              print("Rating----------------4.4")
                              print("Buy Now")
                              item="VIVO Y 17"
                        elif j==3:
                              zz="VIVO Y90"
                              print("---------VIVO Y 90---------")
                              print("#####KEY FEATURES####")
                              print("2 GB RAM:16 GB ROM")
                              print("15.8 cm(6.22 inch) HD+ Display")
                              print("8 MP Rear Camera:5 MP Front Camera")
                              print("4030 mAh Battery")
                              print("MTK Helio A22 Processor")
                              print("Price---------6,999/-")
                              print("Rating----------------4.3")
                              print("Buy Now")
                              item="VIVO Y 90"
                  elif i==3:
                        print("1.VIVO V11")
                        print("2.VIVO V15")
                        print("3.VIVO V17 PRO")
                        k=int(input("enter desired smartphone :"))
                        if k==1:
                              zz="VIVO  V11"
                              print("---------VIVO V11--------")
                              print("#####KEY FEATURES####")
                              print("6 GB RAM:64 GB ROM")
                              print("16.0 cm(6.3 inch) FHD+ Display")
                              print("16 MP +5MP Rear Camera:25 MP Front Camera")
                              print("3315 mAh Battery")
                              print("MTK P60 Octa Core 2.0 GHz Processor")
                              print("Price---------19,990/-")
                              print("Rating----------------4.5")
                              print("Buy Now")
                              item="VIVO V11"
                        elif k==2:
                              zz="VIVO V15"
                              print("---------VIVO V15---------")
                              print("#####KEY FEATURES####")
                              print("6 GB RAM:64 GB ROM")
                              print("16.59 cm(6.53 inch) FHD+ Display")
                              print("12 MP+5MP +8MP Rear Camera:32 MP Front Camera")
                              print("4000 mAh Battery")
                              print("MTK P60 Processor")
                              print("Price---------16,999/-")
                              print("Rating----------------4.4")
                              print("Buy Now")
                              item="VIVO V15"
                        elif k==3:
                              zz="VIVO V17 PRO"
                              print("---------VIVO V17 PRO---------")
                              print("#####KEY FEATURES####")
                              print("8 GB RAM:128 GB ROM")
                              print("16.36 cm(6.44 inch) FHD+ Display")
                              print("48 MP+13MP+8MP +2MP Rear Camera:32 MP+8MP Front Camera")
                              print("4100 mAh Battery")
                              print("Quallcom Snapdragon 675 AIE Processor")
                              print("Price---------29,990/-")
                              print("Rating----------------4.6")
                              print("Buy Now")
                              item="VIVO V17"
        elif b==2:
              print("                                                          LAPTOP BRANDS")
              print("1. DELL")
              print("2. HP")
              print("3. ASUS")
              l=int(input("Select the desired brand :"))
              if l==1:
                    print("                                                      DELL LAPTOPS")
                    print( )
                    zz="DELL 14 3000"
                    print("1.           DELL 14 3000")
                    print("           HIGHLIGHTS")
                    print("#Pre installed genuine windows 10 OS")
                    print("#Light laptop without optical disk drive")
                    print("#14 inch HD LED Display")
                    print("#Core i3:7th generation")
                    print("# 4 GB RAM:1 TB  HDD")
                    print("Price---------32,284/-")
                    print("Rating--------4.2")
                    print( )
                    zz="DELL 14 3002"
                    print("2.           DELL 14 3002")
                    print("           HIGHLIGHTS")
                    print("#LINUX")
                    print("#Light laptop without optical disk drive")
                    print("#14 inch HD LED Display")
                    print("#Core i3:7th generation")
                    print("# 4 GB RAM:1 TB  HDD")
                    print("Price---------29,284/-")
                    print("Rating--------4.3")
                    print( )
                    zz="DELL VOSTRO 3000"
                    print("3.           DELL VOSTRO 3000")
                    print("           HIGHLIGHTS")
                    print("#LINUX")
                    print("#Light laptop without optical disk drive")
                    print("#14 inch HD LED Display")
                    print("#Core i5:8th generation")
                    print("# 8 GB RAM:1 TB  HDD")
                    print("Price---------39,284/-")
                    print("Rating--------4.2")
                    print( )
                    zz="DELL  INSPIRON 15 3000"
                    print("4.           DELL INSPIRON 15 3000")
                    print("           HIGHLIGHTS")
                    print("#Pre installed genuine windows 10 OS")
                    print("#Light laptop without optical disk drive")
                    print("#15.6 inch HD LED Display")
                    print("#Core i3:7th generation")
                    print("# 4 GB RAM:1 TB  HDD")
                    print("Price---------30,284/-")
                    print("Rating--------4.8")
                    choice=int(input("Select the desired laptop :"))
                    if choice==1:
                           print("Buy now")
                           item="DELL 14 3002"
                    elif choice==2:
                        
                        print("Buy now")
                        item="DELL 14 3000"
                    elif choice==3:
                      
                        print("Buy now")
                        item="DELL VOSTRO 3000"
                    elif choice==4:
                        print("Buy now")
                        item="DELL INSPIRON 15 3000"
              elif l==2:
                    print("                                                     HP LAPTOPS")
                    zz="HP 15q APU Dual Core A9"
                    print("1. HP 15q APU Dual Core A9           ")
                    print("           HIGHLIGHTS")
                    print("#Pre installed genuine windows 10 OS")
                    print("#Light laptop with optical disk drive")
                    print("#15.6 inch HD LED Display")
                    print("#Core i3:7th generation")
                    print("# 4 GB RAM:1 TB  HDD")
                    print("Price---------26,284/-")
                    print("Rating--------4.2")
                    print( )
                    zz="HP 14q"
                    print("2.           HP 14q ")
                    print("           HIGHLIGHTS")
                    print("#WINDOWS 10 HOME")
                    print("#Light laptop without optical disk drive")
                    print("#14 inch HD LED Display")
                    print("#Core i5:8th generation")
                    print("# 8 GB RAM:1 TB  HDD")
                    print("Price---------42,284/-")
                    print("Rating--------4.3")
                    print( )
                    zz="HP 15q"
                    print("3.       HP 15q")
                    print("           HIGHLIGHTS")
                    print("#WINDOWS 10 DOS")
                    print("#Light laptop with optical disk drive")
                    print("#15.6 inch HD LED Display")
                    print("#Core i3:7th generation")
                    print("# 8 GB RAM:1 TB  HDD")
                    print("Price---------30,284/-")
                    print("Rating--------4.3")
                    print( )
                    zz="HP Pavillion x360 Foldable"
                    print("4.           HP Pavillion x360 Foldable")
                    print("           HIGHLIGHTS")
                    print("#Pre installed genuine windows 10 OS")
                    print("#Light laptop without optical disk drive")
                    print("#14 inch HD LED Display")
                    print("#Core i5:8th generation")
                    print("# 4 GB RAM:512 GB  HDD")
                    print("Price---------42,990/-")
                    print("Rating--------4.6")
                    choice=int(input("Select the desired laptop :"))
                    if choice==1:
                           print("Buy now")
                           item="HP 15q APU Dual Core A9"
                    elif choice==2:
                        
                        print("Buy now")
                        item="HP 14q"
                    elif choice==3:
                      
                        print("Buy now")
                        item="HP 15q"
                    elif choice==4:
                        print("Buy now")
                        item="HP Pavillion x360 Foldable"
              if l==3:
                    print("                                                       ASUS LAPTOPS")
                    print( )
                    zz="ASUS VIVOBOOK 14"
                    print("1.           ASUS  VIVOBOOK 14")
                    print("           HIGHLIGHTS")
                    print("#WINDOWS 10 HOME")
                    print("#Light laptop without optical disk drive")
                    print("#14 inch HD LED Display")
                    print("#Core i3:7th generation")
                    print("# 4 GB RAM:256 GB  SSD")
                    print("Price---------33,284/-")
                    print("Rating--------4.4")
                    print( )
                    zz="ASUS X"
                    print("2.           ASUS X")
                    print("           HIGHLIGHTS")
                    print("#WINDOWS 10 HOME")
                    print("#Light laptop without optical disk drive")
                    print("#15.6 inch HD LED Display")
                    print("#Core i3:7th generation")
                    print("# 4 GB RAM:1 TB  HDD")
                    print("Price---------25,284/-")
                    print("Rating--------4.3")
                    print( )
                    zz="ASUS VIVOBOOK Ryzen 5"
                    print("3.           ASUS VIVOBOOK Ryzen 5")
                    print("           HIGHLIGHTS")
                    print("#WINDOWS 10 DOS")
                    print("#Light laptop without optical disk drive")
                    print("#15.6 inch HD LED Display")
                    print("#Core i3:7th generation")
                    print("# 8 GB RAM:1 TB  HDD")
                    print("Price---------35,284/-")
                    print("Rating--------4.2")
                    print( )
                    zz="ASUS VIVOBOOK 15"
                    print("4.           ASUS VIVOBOOK 15")
                    print("           HIGHLIGHTS")
                    print("#Pre installed genuine windows 10 OS")
                    print("#Light laptop without optical disk drive")
                    print("#15.6 inch HD LED Display")
                    print("#Core i5:8th generation")
                    print("# 8 GB RAM:1 TB  HDD")
                    print("Price---------36,900/-")
                    print("Rating--------4.1")
                   
                    choice=int(input("Select the desired laptop :"))
                    if choice==1:
                           print("Buy now")
                           item="ASUS  VIVOBOOK 14"
                    elif choice==2:
                        
                        print("Buy now")
                        item="Asus x"
                    elif choice==3:
                      
                        print("Buy now")
                        item="ASUS VIVOBOOK Ryzen 5"
                    elif choice==4:
                        print("Buy now")
                        item="ASUS VIVOBOOK 15"
        elif b==3:
            print("1.  SAMSUNG")
            print("2.  LG")
            print("3.  SONY")
            r=int(input("Select desired brand of LED TVS"))
            if r==1:
                print(" What is your preffered screen size?")
                print("1.    28--32 inches")
                print("2.   39--43 inches")
                s=int(input("Select desired size range"))
                if s==1:
                    print( )
                    zz="SAMSUNG 7 in 1"
                    print("1.  SAMSUNG 7 in 1")
                    print("# 28 inches")
                    print("# HD Ready 1366*768 Pixels")
                    print("#Sound Output:10 W")
                    print("#Refresh Rate:50 Hz")
                    print("#Price-----15,999/-")
                    print("#Rating------4.3")
                    print( )
                    zz="SAMSUNG SERIES 4"
                   
                    print("2.  SAMSUNG SERIES 4")
                    print("# 28 inches")
                    print("# HD Ready 1366*768 Pixels")
                    print("#Sound Output:20 W")
                    print("#Refresh Rate:60 Hz")
                    print("#Price-----17,499/-")
                    print("#Rating------4.3")
                    print( )
                    zz="SAMSUNG N 4200"
                   
                    print("3.  SAMSUNG N 4200")
                    print("# 32 inches")
                    print("# HD Ready 1366*768 Pixels")
                    print("#Sound Output:10 W")
                    print("#Refresh Rate:60 Hz")
                    print("#Price-----22,499/-")
                    print("#Rating------4.3")
                    print( )
                    zz="SAMSUNG 4"
                   
                    print("4.  SAMSUNG 4")
                    print("# 32 inches")
                    print("# HD Ready 1366*768 Pixels")
                    print("#Sound Output:10 W")
                    print("#Refresh Rate:50 Hz")
                    print("#Price-----24,999/-")
                    print("#Rating------4.3")
                    choice=int(input("Select desired LED TV"))
                    if choice==1:
                           print("Buy now")
                           item="SAMSUNG 7 in 1"
                    elif choice==2:
                        
                        print("Buy now")
                        item="Samsung Series 4"
                    elif choice==3:
                      
                        print("Buy now")
                        item="SAMSUNG NKL 4200"
                    elif choice==4:
                        print("Buy now")
                        item="SAMSUNG 4"


                    
                elif s==2:
                    zz="SAMSUNG SUPER 6"
                    print("1.  SAMSUNG SUPER 6")
                    print("# 40 inches")
                    print("# Ultra HD 3840*2160 Pixels")
                    print("#Sound Output:20 W")
                    print("#Refresh Rate:100 Hz")
                    print("#Price-----37,999/-")
                    print("#Rating------4.3")
                    print( )
                    zz="SAMSUNG MAX"
                  
                    print("2.  SAMSUNG MAX")
                    print("# 40 inches")
                    print("# ULTRA HD 3840*2160 Pixels")
                    print("#Sound Output:40 W")
                    print("#Refresh Rate:100 Hz")
                    print("#Price-----39,499/-")
                    print("#Rating------4.3")
                    print( )
                    zz="SAMSUNG NK 4200"
                  
                    print("3.  SAMSUNG NK 4200")
                    print("# 43 inches")
                    print("# ULTRA HD  3840*2160 Pixels")
                    print("#Sound Output:40 W")
                    print("#Refresh Rate:80 Hz")
                    print("#Price-----33,499/-")
                    print("#Rating------4.3")
                    print( )
                    zz="SAMSUNG NOVA 5"
                 
                    print("4.  SAMSUNG NOVA 5")
                    print("# 43 inches")
                    print("#  4K 1366*768 Pixels")
                    print("#Sound Output:40 W")
                    print("#Refresh Rate:120 Hz")
                    print("#Price-----40,999/-")
                    print("#Rating------4.3")
                
                    choice=int(input("Select desired LED TV"))
                    if choice==1:
                           print("Buy now")
                           item="SAMSUNG SUPER 6"
                    elif choice==2:
                        
                        print("Buy now")
                        item="Samsung Max"
                    elif choice==3:
                      
                        print("Buy now")
                        item="SAMSUNG NKL 4200"
                    elif choice==4:
                        print("Buy now")
                        item="SAMSUNG NOVA 5"
            elif r==2:
                print(" What is your preffered screen size?")
                print("1.    28--32 inches")
                print("2.   43--50 inches")
                u=int(input("Select desired size range"))
                if u==1:
                    print( )
                    zz="LG LJ57"
                   
                    print("1.  LG  LJ57")
                    print("# 28 inches")
                    print("# HD Ready 1366*768 Pixels")
                    print("#Sound Output:20 W")
                    print("#Refresh Rate:60 Hz")
                    print("#Price-----19,999/-")
                    print("#Rating------4.4")
                    print( )
                    zz="LG LM56"
                   
                    print("2.  LG LM56")
                    print("# 28 inches")
                    print("# HD Ready 1366*768 Pixels")
                    print("#Sound Output:10 W")
                    print("#Refresh Rate:60 Hz")
                    print("#Price-----17,499/-")
                    print("#Rating------4.3")
                    print( )
                    zz="LG LR59"
                   
                    print("3.  LG LR59")
                    print("# 32 inches")
                    print("# HD Ready 1366*768 Pixels")
                    print("#Sound Output:20 W")
                    print("#Refresh Rate:60 Hz")
                    print("#Price-----18,499/-")
                    print("#Rating------4.3")
                    print( )
                    zz="LG P44"
                   
                    print("4.  LG P44")
                    print("# 32 inches")
                    print("# HD Ready 1366*768 Pixels")
                    print("#Sound Output:20 W")
                    print("#Refresh Rate:50 Hz")
                    print("#Price-----21,999/-")
                    print("#Rating------4.2")
                    choice=int(input("Select desired LED TV"))
                    if choice==1:
                           print("Buy now")
                           item="LG  LJ57"
                    elif choice==2:
                        
                        print("Buy now")
                        item="LG LR59"
                    elif choicez==3:
                      
                        print("Buy now")
                        item="LG LR59"
                    elif choice==4:
                        print("Buy now")
                        item="LG P44"
                elif u==2:
                    zz="LG 43UK"
                    print("1.  LG 43UK")
                    print("# 43 inches")
                    print("# Ultra HD 3840*2160 Pixels")
                    print("#Sound Output:20 W")
                    print("#Refresh Rate:100 Hz")
                    print("#Price-----41,999/-")
                    print("#Rating------4.5")
                    print( )
                    zz="LG  U MAX"
                  
                    print("2.  LG U MAX")
                    print("# 43 inches")
                    print("# ULTRA HD 3840*2160 Pixels")
                    print("#Sound Output:40 W")
                    print("#Refresh Rate:100 Hz")
                    print("#Price-----42,499/-")
                    print("#Rating------4.4")
                    print( )
                    zz="LG  L SUPER"
                  
                    print("3.  LG L SUPER")
                    print("# 50 inches")
                    print("# ULTRA HD  3840*2160 Pixels")
                    print("#Sound Output:40 W")
                    print("#Refresh Rate:80 Hz")
                    print("#Price-----39,499/-")
                    print("#Rating------4.3")
                    print( )
                    zz="LG SUPREME 43"
                 
                    print("4.  LG SUPREME 43")
                    print("# 43 inches")
                    print("#  4K 1366*768 Pixels")
                    print("#Sound Output:40 W")
                    print("#Refresh Rate:120 Hz")
                    print("#Price-----45,999/-")
                    print("#Rating------4.4")
                    choice=int(input("Select desired LED TV"))
                    if choice==1:
                           print("Buy now")
                           item="LG 43UK"
                    elif choice==2:
                        
                        print("Buy now")
                        item="LG U MAX"
                    elif choice==3:
                      
                        print("Buy now")
                        item="LG L SUPER"
                    elif choice==4:
                        print("Buy now")
                        item="LG SUPREME 43"
            elif r==3:
                print(" What is your preffered screen size?")
                print("1.    28--32 inches")
                print("2.   43--55 inches")
                w=int(input("Select desired size range"))
                if w==1:
                    print( )
                    zz="SONY BRAVIA W622F"
                   
                    print("1.  SONY BRAVIA W622F")
                    print("# 28 inches")
                    print("# HD Ready 1366*768 Pixels")
                    print("#Sound Output:30 W")
                    print("#Refresh Rate:50 Hz")
                    print("#Price-----23,999/-")
                    print("#Rating------4.4")
                    print( )
                    zz="SONY BRAVIA R202F"
                   
                    print("2.  SONY BRAVIA R202F")
                    print("# 28 inches")
                    print("# HD Ready 1366*768 Pixels")
                    print("#Sound Output:20 W")
                    print("#Refresh Rate:50 Hz")
                    print("#Price-----18,499/-")
                    print("#Rating------4.4")
                    print( )
                    zz="SONY BRAVIA W422F"
                   
                    print("3.  SONY BRAVIA R422F")
                    print("# 32 inches")
                    print("# HD Ready 1366*768 Pixels")
                    print("#Sound Output:30 W")
                    print("#Refresh Rate:50 Hz")
                    print("#Price-----24,499/-")
                    print("#Rating------4.4")
                    print( )
                    zz="SONY BRAVIA W202G"
                   
                    print("4.  SONY BRAVIA R202G")
                    print("# 32 inches")
                    print("# HD Ready 1366*768 Pixels")
                    print("#Sound Output:20 W")
                    print("#Refresh Rate:50 Hz")
                    print("#Price-----18,999/-")
                    print("#Rating------4.3")
                    choice=int(input("Select desired LED TV"))
                    if choice==1:
                           print("Buy now")
                           item="SONY BRAVIA W622F"
                    elif choice==2:
                        
                        print("Buy now")
                        item="SONY BRAVIA R202F"
                    elif choice==3:
                      
                        print("Buy now")
                        item="SONY BRAVIA R422F"
                    elif choice==4:
                        print("Buy now")
                        item="SONY BRAVIA R202G"



                    
                elif w==2:
                    zz="SONY BRAVIA W622F"
                    print("1.  SONY BRAVIA W662F")
                    print("# 43 inches")
                    print("# Full HD 1920*1080 Pixels")
                    print("#Sound Output:10 W")
                    print("#Refresh Rate:100 Hz")
                    print("#Price-----46,999/-")
                    print("#Rating------4.5")
                    print( )
                    zz="SONY BRAVIA W800F"
                  
                    print("2.  SONY BRAVIA W800F")
                    print("# 43 inches")
                    print("# ULTRA HD 3840*2160 Pixels")
                    print("#OS:Android")
                    print("#Sound Output:40 W")
                    print("#Refresh Rate:100 Hz")
                    print("#Price-----49,499/-")
                    print("#Rating------4.4")
                    print( )
                    zz="SONY BRAVIA X7002G"
                  
                    print("3.  SONY BRAVIA X7002G")
                    print("# 55 inches")
                    print("# ULTRA HD  3840*2160 Pixels")
                    print("#Sound Output:20 W")
                    print("#Refresh Rate:50 Hz")
                    print("#Price-----76,499/-")
                    print("#Rating------4.3")
                    print( )
                    zz="SONY BRAVIA X800G"
                 
                    print("4.  SONY BRAVIA X800G")
                    print("# 55 inches")
                    print("#  4K 3840*2160 Pixels")
                    print("#Sound Output:20 W")
                    print("#Refresh Rate:80 Hz")
                    print("#Price-----88,999/-")
                    print("#Rating------4.4")
                    choice=int(input("Select desired LED TV"))
                    if choice==1:
                           print("Buy now")
                           item="SONY BRAVIA W662F"
                    elif choice==2:
                        
                        print("Buy now")
                        item="SONY BRAVIA W800F"
                    elif choice==3:
                      
                        print("Buy now")
                        item="SONY BRAVIA X7002G"
                    elif choice==4:
                        print("Buy now")
                        item="SONY BRAVIA X800G"

#-----------------------------------------------------------------------------------------------------------
    elif a==2:
        cat="Grocery"
        print("                                                                 Grocery Items")
        print("1.  EDIBLE OILS")
        print("2.  FLOUR")
        print("3.  SPICES")
        l=int(input("select the desired range of product"))
        if l==1:
            print("---------EDIBLE OILS---------")
            print("1. MUSTARD OIL")
            print("2. REFINED OIL")
            print()
            m=int(input("Select desired edible oil"))
            if m==1:
                  print("----------MUSTARD OIL----------")
                  print(" 1.KOLHU")
                  print("2.TOWER")
                  n=int(input("Select the company name:"))
                  if n==1:
                      zz="KOLHU"
                      print("-----------KOLHU-------------")
                      print("1. 1 L PACKS")
                      print("Date of mfg--Dec.  2019")
                      print("Date of expiry-----Nov. 2020")
                      print("Price-----90/-")
                      print("2.  2 L PACKS")
                      print("Date of mfg--Dec.  2019")
                      print("Date of expiry-----Nov. 2020")
                      print("Price-----190/-")
                      print("3.  5 L PACKS")
                      print("Date of mfg--Dec.  2019")
                      print("Date of expiry-----Nov. 2020")
                      print("Price-----460/-")
                      choice=int(input("select desired package"))
                      if choice==1:
                            print("Buy now")
                            item="KOLHU1kg"
                      elif choice==2:
                                print("Buy now")
                                item="KOLHU 2 kg"
                      elif choice==3:
                      
                              print("Buy now")
                              item="KOLHU 5kg"
                  if n==2:
                      zz="TOWER"
                      print("-----------TOWER-------------")
                      print("1. 1 L PACKS")
                      print("Date of mfg--Dec.  2019")
                      print("Date of expiry-----Nov. 2020")
                      print("Price-----100/-")
                      print("2.  2 L PACKS")
                      print("Date of mfg--Dec.  2019")
                      print("Date of expiry-----Nov. 2020")
                      print("Price-----210/-")
                      print("3.  5 L PACKS")
                      print("Date of mfg--Dec.  2019")
                      print("Date of expiry-----Nov. 2020")
                      print("Price-----510/-")
                      z=int(input("select desired package"))
                  if z==1:
                      print("Buy now")
                      item="TOWER 1kg"
                  elif z==2:
                      print("Buy now")
                      item="TOWER 2 kg"
                  elif z==3:
                      
                      print("Buy now")
                      item="TOWER 3kg"
            elif m==2:
                  print("---------REFINED OIL---------")
                  print("1. FORTUNE")
                  print("2. EMAMI:")
                  o=int(input("select desired refined oil brand"))
                  if o==1:
                      zz="FORTUNE"
                      print("-----------FORTUNE-------------")
                      print("1. 1 L PACKS")
                      print("Date of mfg--Dec.  2019")
                      print("Date of expiry-----Nov. 2020")
                      print("Price-----95/-")
                      print("2.  2 L PACKS")
                      print("Date of mfg--Dec.  2019")
                      print("Date of expiry-----Nov. 2020")
                      print("Price-----190/-")
                      print("3.  5 L PACKS")
                      print("Date of mfg--Dec.  2019")
                      print("Date of expiry-----Nov. 2020")
                      print("Price-----490/-")
                      choice=int(input("select desired package"))
                  if choice==1:
                      print("Buy now")
                      item="FORTUNE 1kg"
                  elif choice==2:
                      print("Buy now")
                      item="FORTUNE 2 kg"
                  elif choice==3:
                      
                      print("Buy now")
                      item="FORTUNE 3kg"
                  if o==2:
                      zz="EMAMI"
                      print("-----------EMAMI-------------")
                      print("1. 1 L PACKS")
                      print("Date of mfg--Dec.  2019")
                      print("Date of expiry-----Nov. 2020")
                      print("Price-----90/-")
                      print("2.  2 L PACKS")
                      print("Date of mfg--Dec.  2019")
                      print("Date of expiry-----Nov. 2020")
                      print("Price-----180/-")
                      print("3.  5 L PACKS")
                      print("Date of mfg--Dec.  2019")
                      print("Date of expiry-----Nov. 2020")
                      print("Price-----460/-")
                      choice=int(input("select desired package"))
                  if choice==1:
                      print("Buy now")
                      item="-EMAMI 1kg"
                  elif choice==2:
                      print("Buy now")
                      item="-EMAMI 2 kg"
                  elif choice==3:
                      
                      print("Buy now")
                      item="-EMAMI 3kg"
        elif l==2:
            print("---------FLOUR---------")
            print("1. WHEAT FLOUR")
            print("2. CORN FLOUR")
            print( )
            p=int(input("Select desired flour"))
            if p==1:
                  zz="WHEAT FLOUR"
                  print("----------WHEAT FLOUR----------")
                  print(" 1.AASHIRVAAD")
                  print("2.PATANJALI")
                  n=int(input("Select the company name:"))
                  if n==1:
                      print("-----------AASHIRVAAD-------------")
                      print("1. 1 KG PACKS")
                      print("Date of mfg--Dec.  2019")
                      print("Date of expiry-----Nov. 2020")
                      print("Price-----40/-")
                      print("2.  2 KG PACKS")
                      print("Date of mfg--Dec.  2019")
                      print("Date of expiry-----Nov. 2020")
                      print("Price-----80/-")
                      print("3.  5 KG PACKS")
                      print("Date of mfg--Dec.  2019")
                      print("Date of expiry-----Nov. 2020")
                      print("Price-----200/-")
                      q=int(input("select desired package"))
                  if q==1:
                      print("Buy now")
                      item="AASHIRVAAD 1kg"
                  elif q==2:
                      print("Buy now")
                      item="AASHIRVAAD 2 kg"
                  elif q==3:
                      
                      print("Buy now")
                      item="AASHIRVAAD 3kg"
                  elif n==2:
                      print("-----------PATANJALI-------------")
                      print("1. 1 KG PACKS")
                      print("Date of mfg--Dec.  2019")
                      print("Date of expiry-----Nov. 2020")
                      print("Price-----60/-")
                      print("2.  2 KG PACKS")
                      print("Date of mfg--Dec.  2019")
                      print("Date of expiry-----Nov. 2020")
                      print("Price-----110/-")
                      print("3.  5 KG PACKS")
                      print("Date of mfg--Dec.  2019")
                      print("Date of expiry-----Nov. 2020")
                      print("Price-----300/-")
                      choice=int(input("select desired package"))
                      if choice==1:
                                print("Buy now")
                                item="Patanjali 1kg"
                      elif choice==2:
                                print("Buy now")
                                item="patanjali 2 kg"
                      elif choice==3:
                                print("Buy now")
                                item="Cupatanjali 3kg"
            elif p==2:
                  zz="CORN FLOUR"
                  print("---------CORN FLOUR---------")
                  print("1. AASHIRVAAD")
                  print("2. PATANJALI")
                  o=int(input("select desired refined oil brand"))
                  if o==1:
                      print("-----------AASHIRVAAD-------------")
                      print("1. 1 KG PACKS")
                      print("Date of mfg--Dec.  2019")
                      print("Date of expiry-----Nov. 2020")
                      print("Price-----60/-")
                      print("2.  2 KG PACKS")
                      print("Date of mfg--Dec.  2019")
                      print("Date of expiry-----Nov. 2020")
                      print("Price-----120/-")
                      print("3.  5 KG PACKS")
                      print("Date of mfg--Dec.  2019")
                      print("Date of expiry-----Nov. 2020")
                      print("Price-----300/-")
                      choice=int(input("select desired package"))
                      if choice==1:
                             print("Buy now")
                             item="AASHIRVAAD 1kg"
                      elif choice==2:
                             print("Buy now")
                             item="AASHIRVAAD 2 kg"
                      elif choice==3:
                      
                                print("Buy now")
                                item="AASHIRVAAD 3kg"
                  if o==2:
                      print("-----------PATANJALI-------------")
                      print("1. 1 KG PACKS")
                      print("Date of mfg--Dec.  2019")
                      print("Date of expiry-----Nov. 2020")
                      print("Price-----70/-")
                      print("2.  2 KG PACKS")
                      print("Date of mfg--Dec.  2019")
                      print("Date of expiry-----Nov. 2020")
                      print("Price-----140/-")
                      print("2.  5 KG PACKS")
                      print("Date of mfg--Dec.  2019")
                      print("Date of expiry-----Nov. 2020")
                      print("Price-----350/-")
                      t=int(input("select desired package"))
                      if t==1:
                              print("Buy now")
                              item="Patanjali 1kg"
                      elif t==2:
                             print("Buy now")
                             item="patanjali 2 kg"
                      elif t==3:
                      
                             print("Buy now")
                             item="Cupatanjali 3kg"
        elif l==3:
            print("                                                            SPICES BRANDS")
            print(" 1.  SALZ AND AROMA")
            print("2.    EVEREST")
            y=int(input("Select desired spices' brand"))
            if y==1:
                zz="NUTMEF:SALZ AND AROMA"
                print("1.     NUTMEG(Jayaphal)")
                print("        PRODUCT  DETAILS")
                print("# Powdered Form")
                print("#Quantity-------75 g")
                print("# Aromatic flavour")
                print("# Max Shelf Life-----12 months")
                print("# Price--------221/-")
                print("Rating--------4.1")
                print( )
                zz="WHITE PEPPER:SALZ AND AROMA"
                print("2.     WHITE  PEPPER")
                print("        PRODUCT  DETAILS")
                print("# Whole Form")
                print("#Quantity-------350 g")
                print("# Spicy and Pungent flavour")
                print("# Max Shelf Life-----12 months")
                print("# Price--------548/-")
                print("Rating--------4.2")
                print( )
                zz="Cumin:SALZ AND AROMA"
                print("3.     Cumin(Jeera)")
                print("        PRODUCT  DETAILS")
                print("# Powdered Form")
                print("#Quantity-------85 g")
                print("# Bitter and Slight Pungent flavour")
                print("# Max Shelf Life-----12 months")
                print("# Price--------200/-")
                print("Rating--------4.0")
                print( )
                zz="RED CHILLI:SALZ AND AROMA"
                print("4.     RED CHILLI ")
                print("        PRODUCT  DETAILS")
                
                print("# Powdered Form")
                print("#Quantity-------250 g")
                print("# Hot and Spicy flavour")
                print("# Price--------250/-")
                print("# Max Shelf Life-----12 months")
                print("Rating--------4.1")
                print( )
                zz="CLOVE:SALZ AND AROMA"
                print("5.     CLOVE(Laung)")
                print("        PRODUCT  DETAILS")
             
                print("# Powdered Form")
                print("#Quantity-------250 g")
                print("# Strong and Pungent flavour")
                print("# Max Shelf Life-----12 months")
                print("# Price--------570/-")
                print("Rating--------4.1")
                print( )
                choice=int(input("Select desired spice"))
                if choice==1:
                    print("Buy now")
                    item="NUTMEG(Jayaphal)"
                elif choice==2:
                    print("Buy now")
                    item="WHITE  PEPPER"
                elif choice==3:
                    print("Buy now")
                    item="Cumin(Jeera)"
                elif choice==4:
                    print("Buy now")
                    item="RED CHILLI"
                elif choice==5:
                    print("Buy now")
                    item="CLOVE(Laung)"

            elif y==2:
                zz="CORIANDER:EVEREST"
                print("1.     CORIANDER")
                print("        PRODUCT  DETAILS")
                print("# Powdered Form")
                print("#Quantity-------250 g")
                print("# Spicy flavour")
                print("# Max Shelf Life-----12 months")
                print("# Price--------60/-")
                print("Rating--------4.1")
                print( )
                zz="KITCHEN KING:EVEREST"
                print("2.     KITCHEN KING")
                print("        PRODUCT  DETAILS")
                print("# Powdered Form")
                print("#Quantity-------100 g")
                print("# Spicy and Pungent flavour")
                print("# Max Shelf Life-----12 months")
                print("# Price--------70/-")
                print("Rating--------4.2")
                print( )
                zz="CHICKEN MASALA:EVEREST"
                print("3.     CHICKEN MASALA")
                print("        PRODUCT  DETAILS")
                print("# Powdered Form")
                print("#Quantity-------100 g")
                print("# Spicy and Slight Pungent flavour")
                print("# Max Shelf Life-----12 months")
                print("# Price--------80/-")
                print("Rating--------4.2")
                print( )
                zz="SAMBHAR MASALA:EVEREST"
                print("4.     SAMBHAR MASALA ")
                print("        PRODUCT  DETAILS")
                print("# Powdered Form")
                print("#Quantity-------100 g")
                print("# Hot and Spicy flavour")
                print("# Price--------75/-")
                print("# Max Shelf Life-----12 months")
                print("Rating--------4.1")
                print( )
                zz="SHAHI PANEER MASALA:EVEREST"
                print("5.     SHAHI PANEER MASALA")
                print("        PRODUCT  DETAILS")
             
                print("# Powdered Form")
                print("#Quantity-------100 g")
                print("# Strong and Pungent flavour")
                print("# Max Shelf Life-----12 months")
                print("# Price--------80/-")
                print("Rating--------4.1")
                print( )
                ab=int(input("Select desired spice"))
                if ab==1:
                    print("Buy now")
                    item="CORIANDER"
               
                elif ab==2:
                    print("Buy now")
                    item=" KITCHEN KING"

                elif ab==3:
                    print("Buy now")
                    item="CHICKEN MASALA"

                elif ab==4:
                    print("Buy now")
                    item="SAMBHAR MASALA"

                elif ab==5:
                    print("Buy now")
                    item="SHAHI PANEER MASALA"


#----------------------------------------------------------------------------------------------------------
                  
    elif a==3:
        cat="Home Decor."
        print("                      -----------------@ HOME DECOR--------------     ")
        print("1.Paintings")
        print("2.flower vases")
        print("3.curtains")
        b=int(input("Select your choice"))
        if b==1:
            print("                       ----------->>>Paintings<<<------------  ")
            print()
            print("1.Glass paintings")
            print("2.Canvas paintings")
            c=int(input("Select your choice"))
            if c==1:
                print("                   --------$$Glass Paintings$$--------")
                print()
                print("1.Inspirational paintings")
                print("2.Spiritual paintings")
                d=int(input("Select your choice"))
                if d==1:
                    print("               ------#Inspirational paintings------")
                    print()
                    print("1.Portrait")
                    print("2.Landscape")
                    e=int(input("Select your choice"))
                    if e==1:
                        print("                 ----**Portrait**----")
                        print()
                        zz="INSPIRATIONAL PAINTING"
                        print("1.NEVER GIVE UP","       RATINGS~4.0 ")
                        print("  SPECS:   20cm X 40cm   ")
                        print("           Wooden frame")
                        print("  Price: Rs 1,000")
                        print("2.be++","       RATINGS~4.5 ")
                        print("  SPECS:   30cm X 60cm   ")
                        print("           Steel frame")
                        print("           Blackish red")
                        print("  Price: Rs 10,000")
                        print("3.Work hard","       RATINGS~4.9 ")
                        print("  SPECS:   100cm X 300cm   ")
                        print("           Designer Steel frame")
                        print("           Vibgyor")
                        print("  Price: Rs 15,000")
                        f=int(input("select the product"))
                        item="Inspirational portrait Painting"
                        if (f==1 or f==2 or f==3):
                            print("Buy Now")
                    elif e==2:
                        print("                 ----**Landscape**----")
                        print()
                        print("1.NEVER GIVE UP","       RATINGS~4.0 ")
                        print("  SPECS:   80cm X 60cm   ")
                        print("           Wooden frame")
                        print("  Price: Rs 1,000")
                        print("2.be++","       RATINGS~4.5 ")
                        print("  SPECS:   50cm X 30cm   ")
                        print("           Steel frame")
                        print("           Blackish red")
                        print("  Price: Rs 10,000")
                        print("3.Work hard","       RATINGS~4.9 ")
                        print("  SPECS:   400cm X 300cm   ")
                        print("           Designer Steel frame")
                        print("           Vibgyor")
                        print("  Price: Rs 15,000")
                        f=int(input("Select your choice"))
                        item="Inspirational Landscape Painting"
                        if (f==1 or f==2 or f==3):
                            print("Buy Now")
                        
                elif d==2:
                    print("               ------#Spritual paintings------")
                    print()
                    print("1.Portrait")
                    print("2.Landscape")
                    e=int(input("Select your choice"))
                    if e==1:
                        zz="SPIRITUAL PAINTINGS"
                        print("                 ----**Portrait**----")
                        print()
                        print("1.Lord shiva","       RATINGS~4.0 ")
                        print("  SPECS:   20cm X 40cm   ")
                        print("           Black Wooden frame")
                        print("  Price: Rs 2,000")
                        print("2.Goddess Laxmi","       RATINGS~4.5 ")
                        print("  SPECS:   30cm X 60cm   ")
                        print("           Steel frame")
                        print("           golden image")
                        print("  Price: Rs 12,000")
                        print("3.Lord Ram","       RATINGS~4.9 ")
                        print("  SPECS:   100cm X 300cm   ")
                        print("           Designer Steel frame")
                        print("           Bluish Red")
                        print("  Price: Rs 15,000")
                        f=int(input("Select your choice"))
                        item="Spritual portrait Painting"
                        if (f==1 or f==2 or f==3):
                            print("Buy Now")
                    elif e==2:
                        print("                 ----**Landscape**----")
                        print()
                        print("1.Lord ganesha","       RATINGS~4.0 ")
                        print("  SPECS:   50cm X 20cm   ")
                        print("           Wooden frame")
                        print("  Price: Rs 1,000")
                        print("2.Vaishno Devi Maa","       RATINGS~4.5 ")
                        print("  SPECS:   50cm X 30cm   ")
                        print("           Steel frame")
                        print("           Blackish red")
                        print("  Price: Rs 15,000")
                        print("3.Lord Ram, Laxman, Sita","       RATINGS~4.9 ")
                        print("  SPECS:   400cm X 300cm   ")
                        print("           Designer Steel frame")
                        print("           Golden,Red")
                        print("  Price: Rs 25,000")
                        f=int(input("Select your choice"))
                        item="spiritual Landscape Painting"
                        if (f==1 or f==2 or f==3):
                            print("Buy Now")                 
            elif c==2:
                print("                   --------$$Canvas Paintings$$--------")
                print()
                print("1.Inspirational paintings")
                print("2.Spiritual paintings")           
                d=int(input("Select your choice"))
                if d==1:
                    print("               ------#Inspirational paintings------")
                    print()
                    print("1.Portrait")
                    print("2.Landscape")
                    e=int(input("Select your choice"))
                    if e==1:
                        zz="INSPIRATIONAL PAINTINGS"
                        print("                 ----**Portrait**----")
                        print()
                        print("1.NEVER GIVE UP","       RATINGS~4.0 ")
                        print("  SPECS:   20cm X 40cm   ")
                        print("           Wooden frame")
                        print("  Price: Rs 1,000")
                        print("2.be++","       RATINGS~4.5 ")
                        print("  SPECS:   30cm X 60cm   ")
                        print("           Steel frame")
                        print("           Blackish red")
                        print("  Price: Rs 5,000")
                        print("3.Work hard","       RATINGS~4.9 ")
                        print("  SPECS:   100cm X 300cm   ")
                        print("           Designer Steel frame")
                        print("           Vibgyor")
                        print("  Price: Rs 8,000")
                        f=int(input("Select your choice"))
                        item="Inspirational portrait Painting"
                        if (f==1 or f==2 or f==3):
                            print("Buy Now")             
                    elif e==2:
                        print("                 ----**Landscape**----")
                        print()
                        print("1.NEVER GIVE UP","       RATINGS~4.0 ")
                        print("  SPECS:   80cm X 60cm   ")
                        print("           Wooden frame")
                        print("  Price: Rs 2,000")
                        print("2.be++","       RATINGS~4.5 ")
                        print("  SPECS:   50cm X 30cm   ")
                        print("           Steel frame")
                        print("           Blackish red")
                        print("  Price: Rs 5,000")
                        print("3.Work hard","       RATINGS~4.9 ")
                        print("  SPECS:   400cm X 300cm   ")
                        print("           Designer Steel frame")
                        print("           Vibgyor")
                        print("  Price: Rs 9,000")
                        f=int(input("Select your choice"))
                        item="Inspirational Landscape Painting"
                        if (f==1 or f==2 or f==3):
                            print("Buy Now")             
                elif d==2:
                    zz="SPIRITUAL PAINTINGS"
                    print("               ------#Spritual paintings------")
                    print()
                    print("1.Portrait")
                    print("2.Landscape")
                    e=int(input("Select your choice"))
                    if e==1:
                        print("                 ----**Portrait**----")
                        print()
                        print("1.Lord shiva","       RATINGS~4.0 ")
                        print("  SPECS:   20cm X 40cm   ")
                        print("           Black Wooden frame")
                        print("  Price: Rs 1,000")
                        print("2.Goddess Laxmi","       RATINGS~4.5 ")
                        print("  SPECS:   30cm X 60cm   ")
                        print("           Steel frame")
                        print("           golden image")
                        print("  Price: Rs 8,000")
                        print("3.Lord Ram","       RATINGS~4.9 ")
                        print("  SPECS:   100cm X 300cm   ")
                        print("           Designer Steel frame")
                        print("           Bluish Red")
                        print("  Price: Rs 9,000")
                        f=int(input("Select your choice"))
                        item="Portrait spiritual Painting"
                        if (f==1 or f==2 or f==3):
                            print("Buy Now")     
                    elif e==2:
                        print("                 ----**Landscape**----")
                        print()
                        print("1.Lord ganesha","       RATINGS~4.0 ")
                        print("  SPECS:   50cm X 20cm   ")
                        print("           Wooden frame")
                        print("  Price: Rs 900")
                        print("2.Vaishno Devi Maa","       RATINGS~4.5 ")
                        print("  SPECS:   50cm X 30cm   ")
                        print("           Steel frame")
                        print("           Blackish red")
                        print("  Price: Rs 7,000")
                        print("3.Lord Ram, Laxman, Sita","       RATINGS~4.9 ")
                        print("  SPECS:   400cm X 300cm   ")
                        print("           Designer Steel frame")
                        print("           Golden,Red")
                        print("  Price: Rs 15,000")
                        f=int(input("Select your choice"))
                        item="Landscape Spiritual Painting"
                        if (f==1 or f==2 or f==3):
                            print("Buy Now")      
        elif b==2:
             print("                       ----------->>Flower Vases<<<------------  ")
             print("1.Table Flower vases")
             print("2.Floor Flower vases")
             c=int(input("Select your choice"))
             if c==1:
                zz="TABLE FLOWER VASES"
                print("                   --------$$Table Flower vases$$--------")
                print()
                print("1.Glass vase")
                print("2.Wooden vase")
                d=int(input("Select material type"))
                if d==1:
                    print("               ------#Glass vase------")
                    print("1.Small")
                    print("2.Long")
                    e=int(input("Select your choice"))
                    if e==1:
                        print("                 ----**Small**----")
                        print("1.EDRIC GLASS VASE","       RATINGS~4.0 ")
                        print("  SPECS:   8 inch BLUE  ")
                        print("           Narrow neck shape")
                        print("  Price: Rs 1,000")
                        print("2.KENT GLASS VASE","       RATINGS~4.5 ")
                        print("  SPECS:   10 inch   ")
                        print("           Cylinderical")
                        print("           Blackish red")
                        print("  Price: Rs 2,000")
                        print("3.ANTARA GLASS VASE","       RATINGS~4.9 ")
                        print("  SPECS:   9 inch   ")
                        print("           Cycle shaped")
                        print("           White")
                        print("  Price: Rs 1,000")
                        f=int(input("Select your choice"))
                        item="wooden Base Small"
                        if (f==1 or f==2 or f==3):
                            print("Buy Now")
                    elif e==2:
                        print("                 ----**Long**----")
                        print()
                        print("1.ELEGANT GLASS VASE","       RATINGS~4.0 ")
                        print("  SPECS:   35 inch BLUE  ")
                        print("           Round shaped")
                        print("  Price: Rs 20,000")
                        print("2.KENT GLASS VASE","       RATINGS~4.5 ")
                        print("  SPECS:   32 inch   ")
                        print("           Cylinderical")
                        print("           Blackish red")
                        print("  Price: Rs 15,000")
                        print("3.FAMOUS GLASS VASE","       RATINGS~4.9 ")
                        print("  SPECS:   40 inch   ")
                        print("           Conical")
                        print("           White")
                        print("  Price: Rs 18,000")
                        f=int(input("Select your choice"))
                        item="Glass Base Long"
                        if (f==1 or f==2 or f==3):
                            print("Buy Now")
                if d==2:
                    print("               ------#Wooden vase------")
                    print("1.Small")
                    print("2.Long")
                    e=int(input("Select your choice"))
                    if e==1:
                        print()
                        print("                 ----**Small**----")
                        print()
                        print("1.EDRIC GLASS VASE","       RATINGS~4.0 ")
                        print("  SPECS:   8 inch BLUE  ")
                        print("           Narrow neck shape")
                        print("  Price: Rs 1,000")
                        print("2.KENT GLASS VASE","       RATINGS~4.5 ")
                        print("  SPECS:   10 inch   ")
                        print("           Cylinderical")
                        print("           Blackish red")
                        print("  Price: Rs 2,000")
                        print("3.ANTARA GLASS VASE","       RATINGS~4.9 ")
                        print("  SPECS:   9 inch   ")
                        print("           Cycle shaped")
                        print("           White")
                        print("  Price: Rs 1,000")
                        f=int(input("Select your choice"))
                        item="wooden Base Samll"
                        if (f==1 or f==2 or f==3):
                            print("Buy Now")
                    elif e==2:
                        print("                 ----**Large**----")
                        print()
                        print("1.ELEGANT GLASS VASE","       RATINGS~4.0 ")
                        print("  SPECS:   35 inch BLUE  ")
                        print("           Round shaped")
                        print("  Price: Rs 20,000")
                        print("2.KENT GLASS VASE","       RATINGS~4.5 ")
                        print("  SPECS:   32 inch   ")
                        print("           Cylinderical")
                        print("           Blackish red")
                        print("  Price: Rs 15,000")
                        print("3.FAMOUS GLASS VASE","       RATINGS~4.9 ")
                        print("  SPECS:   40 inch   ")
                        print("           Conical")
                        print("           White")
                        print("  Price: Rs 18,000")
                        f=int(input("Select your choice"))
                        item="wooden Base Long"
                        if (f==1 or f==2 or f==3):
                            print("Buy Now")
             elif c==2:
                zz="FLOOR FLOWER VASES"
                print("                   --------$$Floor Flower vases$$--------")
                print()
                print("1.Glass vase")
                print("2.Wooden vase")
                d=int(input("Select your choice"))
                if d==1:
                    print()
                    print("               ------#Glass vase------")
                    print("1.Small")
                    print("2.Long")
                    e=int(input("Select your choice"))
                    if e==1:
                        print("                 ----**Small**----")
                        print()
                        print("1.EDRIC GLASS VASE","       RATINGS~4.0 ")
                        print("  SPECS:   20 inch BLUE  ")
                        print("           Narrow neck shape")
                        print("  Price: Rs 5,000")
                        print("2.KENT GLASS VASE","       RATINGS~4.5 ")
                        print("  SPECS:   25 inch   ")
                        print("           Cylinderical")
                        print("           Blackish red")
                        print("  Price: Rs 8,000")
                        print("3.ANTARA GLASS VASE","       RATINGS~4.9 ")
                        print("  SPECS:   22 inch   ")
                        print("           Cycle shaped")
                        print("           White")
                        print("  Price: Rs 10,000")
                        f=int(input("Select your choice"))
                        item="Glass Base Small"
                        if (f==1 or f==2 or f==3):
                            print("Buy Now")
                    elif e==2:
                        print("                 ----**Long**----")
                        print()
                        print("1.ELEGANT GLASS VASE","       RATINGS~4.0 ")
                        print("  SPECS:   40 inch BLUE  ")
                        print("           Round shaped")
                        print("  Price: Rs 25,000")
                        print("2.KENT GLASS VASE","       RATINGS~4.5 ")
                        print("  SPECS:   42 inch   ")
                        print("           Cylinderical")
                        print("           Blackish red")
                        print("  Price: Rs 30,000")
                        print("3.FAMOUS GLASS VASE","       RATINGS~4.9 ")
                        print("  SPECS:   45 inch   ")
                        print("           Conical")
                        print("           White")
                        print("  Price: Rs 32,000")
                        f=int(input("Select your choice"))
                        item="Glass Base Long"
                        if (f==1 or f==2 or f==3):
                            print("Buy Now")
                elif d==2:
                    print("               ------#Wooden vase------")
                    print("1.Small")
                    print("2.Long")
                    e=int(input("Choose your size"))
                    if e==1:
                        print("                 ----**Small**----")
                        print()
                        print("1.EDRIC GLASS VASE","       RATINGS~4.0 ")
                        print("  SPECS:   8 inch BLUE  ")
                        print("           Narrow neck shape")
                        print("  Price: Rs 1,000")
                        print("2.KENT GLASS VASE","       RATINGS~4.5 ")
                        print("  SPECS:   10 inch   ")
                        print("           Cylinderical")
                        print("           Blackish red")
                        print("  Price: Rs 2,000")
                        print("3.ANTARA GLASS VASE","       RATINGS~4.9 ")
                        print("  SPECS:   9 inch   ")
                        print("           Cycle shaped")
                        print("           White")
                        print("  Price: Rs 1,000")
                        f=int(input("Choose your vase"))
                        item="wooden Base Small"
                        if (f==1 or f==2 or f==3):
                            print("Buy Now")
                    elif e==2:
                        print("                 ----**Long**----")
                        print()
                        print("1.ELEGANT GLASS VASE","       RATINGS~4.0 ")
                        print("  SPECS:   35 inch BLUE  ")
                        print("           Round shaped")
                        print("  Price: Rs 20,000")
                        print("2.KENT GLASS VASE","       RATINGS~4.5 ")
                        print("  SPECS:   32 inch   ")
                        print("           Cylinderical")
                        print("           Blackish red")
                        print("  Price: Rs 15,000")
                        print("3.FAMOUS GLASS VASE","       RATINGS~4.9 ")
                        print("  SPECS:   40 inch   ")
                        print("           Conical")
                        print("           White")
                        print("  Price: Rs 18,000")
                        item="Wooden Base Long"
                        f=int(input("Choose your vase"))
                        if (f==1 or f==2 or f==3):
                            print("Buy Now")                    
        elif b==3:
            print("                       ----------->>>Curtains<<<------------  ")
            print("1.Window Pane Curtains")
            print("2.Door Curtains")
            d=int(input("Choose the curtains type:"))
            if d==1:
                zz="WINDOW PANE CURTAINS"
                print("               ------#Window Pane Curtains------")
                print("1.Panel Pair Curtains")
                print("2.SinglePair Curtains")
                e=int(input("Choose the type:"))
                if e==1:
                    print("                 ----**Panel Pair Curtains**----")
                    print()
                    print("1.Linen Panel Pair Curtains","       RATINGS~4.5 ")
                    print("  SPECS:   15 inches  ")
                    print("           White colored")
                    print("  Price: Rs 700")
                    print("2.Symbol Panel Pair Curtains","       RATINGS~4.2 ")
                    print("  SPECS:   10 inches ")
                    print("           Silk ")
                    print("           Blue coloured")
                    print("  Price: Rs 800")
                    print("3.Best Pair Curtains","       RATINGS~4.9 ")
                    print("  SPECS:   12 inches   ")
                    print("           cotton")
                    print("           Sky Blue")
                    print("  Price: Rs 1,000")
                    f=int(input("Choose your curtains:"))
                    item="Panel Pair Curtains"
                    if (f==1 or f==2 or f==3):
                        print("Buy Now")
                elif e==2:
                    print("                 ----**Single Panel Curtains**----")
                    print()
                    print("1.Linen Panel Curtains","       RATINGS~4.5 ")
                    print("  SPECS:   15 inches  ")
                    print("           White colored")
                    print("  Price: Rs 500")
                    print("2.Symbol Panel Pair Curtains","       RATINGS~4.2 ")
                    print("  SPECS:   10 inches ")
                    print("           Silk ")
                    print("           Blue coloured")
                    print("  Price: Rs 700")
                    print("3.Best Panel Curtains","       RATINGS~4.9 ")
                    print("  SPECS:   12 inches   ")
                    print("           cotton")
                    print("           Sky Blue")
                    print("  Price: Rs 900")
                    f=int(input("Choose your curtains:"))
                    item="Single Panel Curtains"
                    if (f==1 or f==2 or f==3):
                        print("Buy Now")
            elif d==2:
                print()
                zz="DOOR CURTAINS"
                print("               ------#Door Curtains------")
                print("1.Panel Pair Curtains")
                print("2.SinglePair Curtains")
                e=int(input("Choose your type:"))
                if e==1:
                    print("                 ----**Panel Pair Curtains**----")
                    print()
                    print("1.Linen Panel Pair Curtains","       RATINGS~4.5 ")
                    print("  SPECS:   70 inches  ")
                    print("           Maroon colored")
                    print("  Price: Rs 1,500")
                    print("2.Symbol Panel Pair Curtains","       RATINGS~4.2 ")
                    print("  SPECS:   55 inches ")
                    print("           Silk ")
                    print("           Blue coloured")
                    print("  Price: Rs 2,000")
                    print("3.Best Pair Curtains","       RATINGS~4.9 ")
                    print("  SPECS:   65 inches   ")
                    print("           cotton")
                    print("           Sky Blue")
                    print("  Price: Rs 2,500")
                    f=int(input("Choose your curtains:"))
                    item="Panel Pair Curtains"
                    if (f==1 or f==2 or f==3):
                        print("Buy Now")
                elif e==2:  
                    print("                 ----**Single Panel Curtains**----")
                    print()
                    print("1.Linen Panel Curtains","       RATINGS~4.5 ")
                    print("  SPECS:   65 inches  ")
                    print("           White colored")
                    print("  Price: Rs 2,500")
                    print("2.Symbol Panel Pair Curtains","       RATINGS~4.2 ")
                    print("  SPECS:   70 inches ")
                    print("           Silk ")
                    print("           Blue coloured")
                    print("  Price: Rs 1,500")
                    print("3.Best Panel Curtains","       RATINGS~4.9 ")
                    print("  SPECS:   75 inches   ")
                    print("           cotton")
                    print("           Sky Blue")
                    print("  Price: Rs 900")
                    f=int(input("Choose your curtains:"))
                    item="Single Panel Curtains"
                    if (f==1 or f==2 or f==3):

                        print("Buy Now")
    li1.append(cat)
    li1.append(item)
cat()
bo=random.randint(10000000,99999999)
bo=str(bo)
li1.append(bo)
def payment():
        l=random.randint(100000,999999)
        p=random.randint(100000,999999)
        print()
        print("..........................Pay  through............................")
        m=int(input(" *  1. Debit Card           2. Credit Card :  "))
        if m!=1 and m!=2:
            payment()
            
        if m==2:
             
             bbd=str(input(" *  Enter Card Number :  "))
             while len(bbd)!=16 or bbd.isdigit()==False:
                 print (" !!!!!!!!!  Invalid Cardno !!!!!!!!")
                 bbd=str(input(" *  Enter Card Number :  "))
             if len(bbd)==16:
                 c=int(input(" *  Enter CVV   :  "))
                 d=int(input(" *  Confirm CVV :  "))
                 e=c
                 while d!=c:
                     print(" *  Check CVV :  ")
                     d=int(input(" *  Confirm CVV :  "))
                 if d==c:
                    print(' ##  Your OTP :  ',l)
                    j=int(input(' *  Enter OTP :   '))
                    while j!=l:
                         l=random.randint(100000,999999)
                         print(' !!!!! Invalid OTP !!!!!')
                         print(' *  New OTP :   ',l)
                         j=int(input(' *  Enter OTP :   '))
                    if j==l:
                          print("  #####Payment Accomplished #####")
                    li1.append(bbd)
        if m==1:
             
             bbd=str(input(" *  Enter Card Number :  "))
             while len(bbd)!=16 or bbd.isdigit()==False:
                 print (" !!!!! Invalid Card Number !!!!! ")
                 bbd=str(input(" *  Enter Card Number :  "))
             if len(bbd)==16:
                 c=int(input("*  Enter CVV   :  "))
                 d=int(input("*  Confirm CVV :  "))
                 e=c
                 while d!=c:
                     print(" *  Check CVV")
                     d=int(input(" *  Confirm CVV"))
                 if d==c:
                    print(' ##  Your OTP :  ',l)
                    j=int(input(' *  Enter OTP :  '))
                    while j!=l:
                         l=random.randint(100000,999999)
                         print(' !!!!!! Invalid OTP !!!!!')
                         print(' *  New OTP :  ',l)
                         j=int(input(' *  Enter OTP'))
                    if j==l:
                          print(" ## Payment Successful ##")
                    li1.append(bbd)
        
payment()
task=("INSERT INTO data(PhoneNo,UserID,Catagary,Item,OrderNo,CardNO)VALUES('{}','{}','{}','{}','{}','{}')".format(li1[0],li1[1],li1[2],li1[3],li1[4],li1[5]))
cursor.execute(task)
db.commit()


def usrdata():
    def fetchall():
            cursor.execute("select * from data")
            data1=cursor.fetchall()
            for x in data1:
                      print(x)

    def fetchone():
               r=input("Enter Userid. to find latest Order:")
               r=(r,)
               q=("select * from data where userid=%s")
               cursor.execute(q,r)
               data1=cursor.fetchone()
               for x in data1:
                           print(x)
    fetchall()
    fetchone()  
def Cancel():
    task="delete from data where orderno='{}'".format(li1[4])
    sure=input("Are You Sure To Cancel Order y/n")
    if sure=='y':
               print("Your order has been cancelled")
               cursor.execute(task)
               db.commit()
    else:
        about()
def about():

    print('----------------------------Developers---------------------------:')
    print("Shivam Kumar")
    print("Tejas")
    print("Govind")
    print("Ranjeet")
    print("Shivam Sharma")
    print("Jyoti singh")
    print('Thank you for visiting!!')

def see():
    print("Phone Number",li1[0])
    print("User Id",li1[1])
    print("Order No",li1[3])
    print("Item Ordered",li1[2])
    about()
print("1.About us")
print("2.See account details")
print("3.cancel Order")
print("4.See All Orders")
print("5.Exit")

llo=int(input("Enter choice:"))
if llo==1:
         about()
if llo==2:
         see()
if llo==3:
         Cancel()
if llo==4:
         usrdata()
if llo==5 :
         print('Thank you for visiting')
if llo!=1 and llo!=2:
    print('Thank you for visiting!!')




               
