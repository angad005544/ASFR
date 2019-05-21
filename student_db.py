import sqlite3
import datetime
import os
import sys
sem = {"I" : 1,"II" : 2,"III" : 3,"IV" : 4,"V" : 5,"VI" : 6,"VII" : 7,"VIII" : 8}

def get_year(semester):
    curr_year = datetime.datetime.today().year
    s = sem[semester]
    return str(curr_year-s/2)

def asm():
    db = sqlite3.connect(os.path.join("./databases",'students.db'))

    stud = db.cursor()


    branch = raw_input("Branch (CS,EE,EC,CE,MM,ME) : ")
    semester = raw_input("Enter Semester (I,II,III,IV,V,VI,VII,VIII): ")
    ns = int(raw_input("Number of Students : "))
    query = "CREATE TABLE {} (RegNo TEXT)".format(branch+"_"+semester)
    try:
        stud.execute(query)
        for i in range(1,ns+1):
        	insert_query = "INSERT INTO {} VALUES(?)".format(branch+"_"+semester)
        	z=""
        	if(i//10==0):
        		z="00"+str(i)
        	else:
        		z="0"+str(i)
        	stud.execute(insert_query, (get_year(semester)+"UG"+branch+ z,))
        db.commit()
        print "Entered {} students.".format(ns)
        print "Enter any key to go back to main menu."
        raw_input()
    except:
        print "Data already exixts"
        print "Enter any key to go back to main menu."
        raw_input()
    return


def view_db():
	db = sqlite3.connect(os.path.join("./databases",'students.db'))
	conn = db.cursor()
	query = "SELECT name FROM sqlite_master WHERE TYPE='table';"
	res = conn.execute(query)
	print "ALL AVAILABE STUDENTS DATA"
	i=0
	for name in res:
		i = i + 1
		sys.stdout.write(str(i)  + " " +name[0]+"\t\t")
		if(int(i)%4==0):
			print ""
	print "\n\n"

	branch = raw_input("Branch (CS,EE,EC,CE,MM,ME) : ")
	semester = raw_input("Enter Semester (I,II,III,IV,V,VI,VII,VIII): ")
	
	try:
		print "\nSTUDENTS AVAILABE"
		query = "SELECT * FROM {}".format(branch+"_"+semester)
		conn.execute(query)
		rows = conn.fetchall()
		i=0
		for row in rows:
			i+=1
			sys.stdout.write(row[0]+"\t")
			if(i%4==0):
				print ""
			
		print "\n\n"



	except:
		print "Table not found"
	print "Enter any key to go back to main menu."
        raw_input()
	return

def stud_db():
	while(1):
		os.system('clear')
		print "Databases \n"
		print "Enter your choice"
		print "1.Add Students"
		print "2.View Students"
		print "0.Exit"
		choice = raw_input(" >> ")
		if choice == "1" :
			asm()
		elif choice == "2" :
			view_db()
		elif choice == "0" :
			exit()
		else :
			print "Wrong choice try again"



#stud_db()

