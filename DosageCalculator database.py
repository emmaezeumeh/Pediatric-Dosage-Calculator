import mysql.connector

# connect the db
db_connection = mysql.connector.connect( 
host= "localhost", 
user= "root", 
passwd= "password")

db_cursor = db_connection.cursor()

# if dosageCalculator_db exists, drop/ remove it
sql = "DROP DATABASE dosageCalculator_db"
db_cursor.execute(sql)

# creating database
db_cursor.execute("CREATE DATABASE dosageCalculator_db") 

# get list of all databases 
db_cursor.execute("SHOW DATABASES") 
for db in db_cursor: 
    print(db)

db_cursor.execute("USE dosageCalculator_db")

# creating the medication table 
db_cursor.execute("CREATE TABLE Medication_Info(medication_id INT AUTO_INCREMENT PRIMARY KEY, "
"generic_Name varchar(60), "
"brand_Name varchar(60), "
"child_dose varchar(20), "
"adult_dose varchar(20)) "
)

# creating the weight table 
db_cursor.execute("CREATE TABLE Weight_Info(weight_id INT AUTO_INCREMENT PRIMARY KEY, " 
"class varchar (20), "
"weight_kg varchar(50))")

# creating the strength table 
db_cursor.execute("CREATE TABLE Strength_Info(strength_id INT AUTO_INCREMENT PRIMARY KEY, " 
"class varchar (20), "
"dose_strength_mg_per_5ml varchar(50))")

# creating the duration table 
db_cursor.execute("CREATE TABLE Duration_Info(duration_id INT AUTO_INCREMENT PRIMARY KEY, " 
"class varchar (20), "
"duration_days varchar(50))")

# creating the frequency table 
db_cursor.execute("CREATE TABLE Frequency_Info(frequency_id INT AUTO_INCREMENT PRIMARY KEY, " 
"class varchar (20), "
"frequency_per_day varchar(50))")

# creating the dosing_rule table 
db_cursor.execute("CREATE TABLE Dosing_Rule_Info(dosing_rule_id INT AUTO_INCREMENT PRIMARY KEY, " 
"class varchar (20), "
"dosing_rule_mg_per_kg_per_day varchar(50))")

# creating the disease table 
db_cursor.execute("CREATE TABLE Disease_Info(disease_id INT AUTO_INCREMENT PRIMARY KEY, " 
"class varchar (20), " 
"disease_type varchar(50), " 
"total_daily_dose varchar(40))") 

# creating the creatinine clearance table 
db_cursor.execute("CREATE TABLE Creatinine_Clearance_Info(CrCl_id INT AUTO_INCREMENT PRIMARY KEY, "
"stage int(10),"
"value varchar(30), "
"dose_mg varchar(30)) ")


#Get tables     
db_cursor.execute("SHOW TABLES") 
for table in db_cursor: 
    print(table)

# insert medication records
add_med_records = "INSERT INTO Medication_Info(generic_Name, brand_Name, child_dose, adult_dose) VALUES (%s, %s, %s, %s)"
medication_val= [
    ("Amoxicillin", "Amoxil", "50mg/kg", "1000mg"),
    ("Diphenylhramine", "Augmentin", "50mg/12.5mg", "1000mg/250mg"),
    ("Ibuprofen", "Amoxil", "50mg/kg", "1000mg"),
    ("Tynelol", "Amoxil", "50mg/kg", "1000mg")
]

    #  insert weight records
add_weight_records ="INSERT INTO Weight_Info(class, weight_kg) VALUES (%s,%s)"
weight_val= [
    ("A","5"), 
    ("B ","10"), 
    ("C ","15"), 
    ("D","20") 
]

#  insert srength records
add_strength_records ="INSERT INTO Strength_Info(class, dose_strength_mg_per_5ml) VALUES (%s,%s)"
strength_val= [
    ("A","125"), 
    ("B ","200"), 
    ("C ","250"), 
    ("D","400") 
]

# insert frequency records
add_freq_records = "INSERT INTO Frequency_Info(class, frequency_per_day) VALUES (%s,%s)"
freq_val= [
    ("OD","1"), 
    ("BD ","2"), 
    ("TID ","3"), 
    ("QID","4")
]

# insert duration records
add_duration_records = "INSERT INTO Duration_Info(class, duration_days) VALUES (%s,%s)"
duration_val= [
    ("A","5"), 
    ("B","10"), 
    ("C","14")  
]

# insert duration records
add_dosing_rule_records = "INSERT INTO Dosing_Rule_Info(class, dosing_rule_mg_per_kg_per_day) VALUES (%s,%s)"
dosing_rule_val= [
    ("A","15"), 
    ("B","50"), 
    ("C","80")  
]

# insert disease records
add_disease_records = "INSERT INTO Disease_Info(class, disease_type) VALUES (%s,%s)"
disease_val= [
    ("A", "Acute Otitis Media"), 
    ("B", "Allergy Relief"), 
    ("C", "Pain Relief") 
]

# insert creatinine clearance records
add_CrCl_records = "INSERT INTO Creatinine_Clearance_Info(stage, value, dose_mg) VALUES (%s, %s, %s)"
CrCl_val= [
    ("1", "CrCl >= 90 mL/min", "500"),
    ("2", "CrCl >= 60-89 mL/min", "500"), 
    ("3", "CrCl >= 30-59 mL/min", "500"), 
    ("4", "CrCl 15-29 mL/min", "250-500"), 
    ("5", "CrCl <15 mL/min", "250-500")
]

#insert records to the database  
db_cursor.executemany(add_med_records, medication_val)
db_cursor.executemany(add_freq_records, freq_val)
db_cursor.executemany(add_weight_records, weight_val)
db_cursor.executemany(add_disease_records, disease_val)
db_cursor.executemany(add_CrCl_records, CrCl_val)
db_cursor.executemany(add_strength_records, strength_val)
db_cursor.executemany(add_duration_records, duration_val)
db_cursor.executemany(add_dosing_rule_records, dosing_rule_val)

db_connection.commit() 
print(db_cursor.rowcount, "Record Inserted")

# show records
db_cursor.execute("SELECT * FROM Medication_Info")
myresult = db_cursor.fetchall()
for x in myresult:
    print(x)

db_cursor.execute("SELECT * FROM Frequency_Info")
myresult = db_cursor.fetchall()
for x in myresult:
    print(x)

db_cursor.execute("SELECT * FROM Creatinine_Clearance_Info")
myresult = db_cursor.fetchall()
for x in myresult:
    print(x)

db_cursor.execute("SELECT * FROM Disease_Info")
myresult = db_cursor.fetchall()
for x in myresult:
    print(x)

db_cursor.execute("SELECT * FROM Duration_Info")
myresult = db_cursor.fetchall()
for x in myresult:
    print(x)


db_cursor.execute("SELECT * FROM Strength_Info")
myresult = db_cursor.fetchall()
for x in myresult:
    print(x)


