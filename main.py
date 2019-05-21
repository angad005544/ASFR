import os
import sys
import cv2
import training_module
import student_db
import take_attendance_module
import mark_attendance_module
import view_attendance_module

menu_actions = {}

#print "in the main section"

def main_menu():
	os.system('clear')

	print "Welcome,\n"
	print "Please choose your option:"
	print "1.Take Attendance"
	print "2.View Attendance"
	print "3.Add Students"
	print "4.View Students"
	print "\n0.Quit"
	choice = raw_input(" >> ")
	#fucntion call for menu options
	exec_menu(choice)
	return 

def exec_menu(choice):
	os.system('clear')
	ch = choice.lower()
	if ch == '':
		menu_actions['main_menu']();
	else:
		try:
			menu_actions[ch]()
		except KeyError:
			print "Invalid selection, Please try again.\n"
			menu_actions[main_menu]()
	return

def take_attendance():
	take_attendance_module.am()
	menu_actions['main_menu']()
	return

def view_attendance():
	view_attendance_module.vam()
	menu_actions['main_menu']()
	return

def add_students():
	student_db.asm()
	menu_actions['main_menu']()
	return
def view_students():
	student_db.view_db()
	menu_actions['main_menu']()
	return


def exit():
	sys.exit()

menu_actions = {
	'main_menu':main_menu,
	'1':take_attendance,
	'2':view_attendance,
	'3':add_students,
	'4':view_students,
	'0':exit
}

main_menu()



