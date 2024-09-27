import sqlite3
conn=sqlite3.connect("pps.db")

def main_menu():
     print(" --> Enter 1 to \'ADD Student\' ")
     print(" --> Enter 2 to \'ADD Marks\' ")
     print(" --> Enter 3 to \'Check Performance\' ")
     print(" --> Enter 4 to \'View list of all Students\' ")
     print(" --> Enter 5 to \'View list of Student's MARKS\' ")
     print(" --> Enter 6 to \'UPDATE previously added DATA\' ")
     print(" --> Enter 7 to \'EXIT\' ")
     ans=int(input("Your response ="))
     if(ans==1):
           add_student()
     elif(ans==2):
           add_marks()
     elif(ans==3):
           Performance()
     elif(ans==4):
           show_list()
     elif(ans==5):
           show_marks_list()
     elif(ans==6):
           update_student()
     elif(ans==7):
           exit()
     else:
           
           print("Please Enter a Valid Input")
           main_menu()
           
def add_student():
     name=input("NAME =")
     Id=int(input("STUDENT ID ="))
     section=input("SECTION =")
     gender=input("GENDER =")
     dob=input("DOB =")
     conn=sqlite3.connect("pps.db")
     conn.execute('insert into student VALUES(?,?,?,?,?)',(name,Id,section,gender,dob))
     conn.commit()
     conn.close()
     print("Data Added Successfully")
     next()

def add_marks():
         print("Enter Name of student whoose marks you wanna add")
         name=input("Name of student =")
         print("")
         print("Enter Marks of student out of 100")
         print("")
         pps=int(input("Marks in PPS ="))
         em=int(input("Marks in EM ="))
         beee=int(input("Marks in BEEE ="))
         cbm=int(input("Marks in CBM ="))
         edp=int(input("Marks in EDP ="))
         conn=sqlite3.connect("pps.db")
         conn.execute('insert into marks VALUES(?,?,?,?,?,?)',(name,pps,em,beee,cbm,edp))
         conn.commit()
         conn.close()
         print("Data Added Successfully")
         next()
         
def show_list():
     conn=sqlite3.connect("pps.db")
     data=conn.execute(" select * from student " )
     print("")
     print("")
     for n in data:
          print(n[0],"        ",n[1],"          ",n[2],"          ",n[3],"          ",n[4])
          print("")

     next()
def show_marks_list():
      conn=sqlite3.connect("pps.db")
      data=conn.execute(" select * from marks " )
      print("")
      print("")
      print("NAME          PPS          EM           BEEE          CBM           EDP")
      print("")
      for n in data:
            print(n[0],"           ",n[1],"         ",n[2],"          ",n[3],"          ",n[4],"          ",n[5])
            print("")
      print("")

      next()
def Performance():
      conn=sqlite3.connect("pps.db")
      name=input("Enter name whose performance you wanna check =")
      num=conn.execute("select PPS,EM,BEEE,CBM,EDP from marks where Name='"+name+"' ")
      for i in num:
            print(f"Total Marks of {name} is = ",i[0]+i[1]+i[2]+i[3]+i[4])
            print(f"Percentage of {name} is = ",((i[0]+i[1]+i[2]+i[3]+i[4])*100)/500)

      conn=sqlite3.connect("pps.db")
      next()

def exit():
      print("")
      print("            \'THANK YOU\'")
      print("            \'SEE YOU SOON\'")

def next():
     print("Enter 1 for \'Main Menu\'")
     print("Enter 0 to \'EXIT\'")
     res=int(input("Your Response ="))
     if(res==1):
           conn=sqlite3.connect("pps.db")
           main_menu()
     elif(res==0):
           exit()
     else:
           print("Please Enter a Valid Input")
           next()

def update_student():
      conn=sqlite3.connect("pps.db")
      print("--> Enter 1 to Update Student Personal Information")
      print("--> Enter 2 to Update Marks of Students")
      ans=int(input("Your Response ="))
      if(ans==1):
            print("--> Enter 1 to Update Name")
            print("--> Enter 2 to Update DOB")
            print("--> Enter 3 to Update ID")
            res=int(input("Your Response ="))
            if(res==1):
                  conn=sqlite3.connect("pps.db")
                  ID=int(input("Enter Id of student whoose Name you wanna Update ="))
                  name=input("Enter Correct Name =")
                  conn.execute('Update student set NAME= ? where ID= ? ',(name,ID))
                  conn.commit()
                  conn.close()
                  print("Data Updated Successfully")
                  next()
            elif(res==2):
                  conn=sqlite3.connect("pps.db")
                  name=input("Enter Name of student whoose DOB you Wanna change =")
                  dob=input("Enter New DOB =")
                  conn.execute('Update student set DOB=? where NAME= ?',(dob,name))
                  conn.commit()
                  conn.close()
                  print("Data Updated Successfully")
                  next()
            elif(res==3):
                  conn=sqlite3.connect("pps.db")
                  name=input("Enter Name of student whoose ID you Wanna change =")
                  id=int(input("Enter New Id ="))
                  conn.execute('Update student set ID=? where NAME=?',(id,name))
                  conn.commit()
                  conn.close()
                  print("Data Updated Successfully")
                  next()
            else:
                  print("Please Enter a Valid Input")
                  update_student()

      elif(ans==2):
            conn=sqlite3.connect("pps.db")
            print("--> Enter 1 to Update PPS Marks ")
            print("--> Enter 2 to Update EM Marks ")
            print("--> Enter 3 to Update BEEE Marks ")
            print("--> Enter 4 to Update CBM Marks ")
            print("--> Enter 5 to Update EDP Marks ")
            rep=int(input("Your Response ="))
            if(rep==1):
                  conn=sqlite3.connect("pps.db")
                  name=input("Enter name of the student Whoose Marks you wanna Update =")
                  new=int(input("Enter new marks ="))
                  conn.execute('Update marks set PPS= ? where NAME=?',(new,name))
                  conn.commit()
                  conn.close()
                  print("Data Updated Successfully")
                  next()
            elif(rep==2):
                  conn=sqlite3.connect("pps.db")
                  name=input("Enter name of the student Whoose Marks you wanna Update =")
                  new=int(input("Enter new marks ="))
                  conn.execute('Update marks set EM=? where NAME=?',(new,name))
                  conn.commit()
                  conn.close()
                  print("Data Updated Successfully")
                  next()
            elif(rep==3):
                  conn=sqlite3.connect("pps.db")
                  name=input("Enter name of the student Whoose Marks you wanna Update =")
                  new=int(input("Enter new marks ="))
                  conn.execute('Update marks set BEEE=? where NAME=?',(new,name))
                  conn.commit()
                  conn.close()
                  print("Data Updated Successfully")
                  next()
            elif(rep==4):
                  conn=sqlite3.connect("pps.db")
                  name=input("Enter name of the student Whoose Marks you wanna Update =")
                  new=int(input("Enter new marks ="))
                  conn.execute('Update marks set CBM=? where NAME= ?',(new,name))
                  conn.commit()
                  conn.close()
                  print("Data Updated Successfully")
                  next()
            elif(rep==5):
                  conn=sqlite3.connect("pps.db")
                  name=input("Enter name of the student Whoose Marks you wanna Update =")
                  new=int(input("Enter new marks ="))
                  conn.execute('Update marks set EDP=? where NAME= ?',(new,name))
                  conn.commit()
                  conn.close()
                  print("Data Updated Successfully")
                  next()

            else:
                  print("Please Enter a Valid Input")
                  update_student()
      else:
            print("Please Enter Valid Input")
            update_student()
def start():
      print("--->> Enter 1 for MAIN MENU")
      print("--->> Enter 2 to EXIT")
      rs=int(input("Your response ="))
      if(rs==1):
            main_menu()
      elif(rs==2):
            exit()
      else:
            print("Please Enter a Valid Input")
            start()


print("")
print("")
print("")
print("")
print("                         \'WELCOME TO STUDENT PERFORMANCE MANAGEMENT SYSTEM \' ")
print("")
print("")
start()