import sqlite3
import os
import random

present_students = ['2015UGCS055','2015UGCS056','2015UGCS057','2015UGCS058','2015UGCS059']

present_stud = {'2015UGCS055':'1','2015UGCS056':'1','2015UGCS057':'1','2015UGCS058':'1','2015UGCS059':'1'}

def mam(semester, branch, present_students, d, m, y):
	d,m,y = str(d), str(m), str(y)
	db1 = sqlite3.connect(os.path.join('./databases/','attendance.db'))
	db2 = sqlite3.connect(os.path.join('./databases/','students.db'))
	atten =  db1.cursor()
	stud = db2.cursor()

	table_name = branch + "_" + semester + "_" + m + "_" + y
	table_exists = 'SELECT name FROM sqlite_master WHERE type ="table" AND name =:t_n'
	if(not atten.execute(table_exists,{'t_n' : table_name}).fetchone()):
		nd = 31#get_no_of_days(int(m), int(y))
		values = "( 'RegNo' TEXT, "
		for i in range(1,nd+1):
			if(i!=nd):
				values = values + "'" + str(i) + "/" + m + "/" + y + "'" +" TEXT, "
			else :
				values = values + "'" + str(i) + "/" + m + "/" + y + "'" +" TEXT "
		values = values + " ) "
		create_table = 'CREATE TABLE {0} {1};'.format(table_name,values)
		atten.execute(create_table)
		try:
			all_students = stud.execute('SELECT * FROM {}'.format(branch+"_"+semester)).fetchall()
		except:
			print "Student data misssig "
			return
		for s in all_students:
			st = s[0]
			atten.execute("INSERT INTO {}('RegNo') VALUES(?)".format(table_name),(st,))
	for regno in present_students:
		update_command = "UPDATE {} SET {} = 'P' WHERE RegNo=?".format(table_name,"'"+d+"/"+m+"/"+y+"'")
		atten.execute(update_command,(regno,))
	print "Attendance marked"
	db1.commit()
	db2.commit()

def attendance_generator(branch,present):
	present_student = {}
	roll = "2015UG"+str(branch)
	for x in range(1,present):
		reg = random.randint(1,90)
		reg = str(1000+reg)
		regno = roll + reg[1:4]
		present_student[regno]='1'
	return present_student

#for month in range(1,12):
	#for i in range(1,30):
		#presentes = attendance_generator("CS",30+random.randint(1,40))
		#mam("VI","CS",presentes,i,month,2018)