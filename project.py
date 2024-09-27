import sqlite3
conn=sqlite3.connect("project.db")
conn.execute('''
            create table Student(
             st_id INT AUTO_INCREMENT PRIMARY KEY,
             st_name VARCHAR(50),
             st_year VARCHAR(10),
             st_section VARCHAR(10),
             st_email VARCHAR(25),
             st_phone INT ,
             st_gender VARCHAR(7),
             st_dob VARCHAR(20)
             )
     ''')
conn.close()

"""ins='''
    insert into Student (st_name,st_section, st_email,st_phone,st_gender,st_dob) VALUES
        ('Radha','26','onkardu02@gmail.com','7678685460','feMale','02/07/2004' )
'''
conn.execute(ins)
conn.commit()
conn.close()"""
conn.execute("UPDATE Student SET st_section='20' WHERE st_name='krishn'")
conn.commit()
print("Data Updated Successfully")
conn.close()

















