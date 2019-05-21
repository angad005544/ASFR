import cv2
import os
import numpy as np
import face_recognition
import training_module
import mark_attendance_module
import datetime as dt



subjects = ["Chaitanya","Phanindra","Angad","Praneeth","Ashutosh","Praneeth","Dhoni","Modi","Salman","RakulPreet","SomeOne","Katrina","UnknownPerson"]
branch_dcode = {'01':'CS','02':'ME','03':'CE'}     
course_dcode = {'01':'UG','02':'PG' }
def draw_rectangle(img, rect,r,g,b):
    (x, y, w, h) = rect
    cv2.rectangle(img, (x, y), (x+w, y+h), (b, g, r), 5)
    
def draw_text(img, text, x, y,r,g,b):
    cv2.putText(img, text, (x, y), cv2.FONT_HERSHEY_PLAIN, 1.5, (b, g, r), 4)


def get_name_lable(name):
    name = 1000 + int(name)
    print"int hteh name"
    print name
    name = str(name)
    #res = name[0:4]+course_dcode[name[4:6]]+branch_dcode[name[6:8]]+name[8:11]
    res="2015UGCS"+str(name[1:4])
    return res

def predict(test_img,face_recognizer):
    
    img = test_img.copy()
    face, rect = detect_face(img)
    if(face==None):
        return -1, 12

    label, confidence = face_recognizer.predict(face)

    print label
    print confidence

    label_text = get_name_lable(label)
    

    if confidence<200:
        
        return 1, label_text
    else:
        return 0, " "


def detect_face(img):
    #print "face detingo \n\n"
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    face_cascade = cv2.CascadeClassifier('opencv-files/lbpcascade_frontalface.xml')

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.4, minNeighbors=5);
    #print "trying to detect face"
    if (len(faces) == 0):
        return None, None
    
    (x, y, w, h) = faces[0]
    
    return gray[y:y+w, x:x+h], faces[0]



def attendance():
	face_recognizer = training_module.training_recogniser() #training_recogniser()
	#two check conditions required
	#student table f
	#image data
	print "All Fine"
	present = {}
	cap = cv2.VideoCapture(0)
	while(1):
		ret,frame = cap.read()
		frame = cv2.flip(frame,1)#to prevent lateral inversion
		face,rect = detect_face(frame)

		if(rect != None):
			res,index = predict(frame,face_recognizer)
			if(res == 1):
				draw_rectangle(frame,rect,0,255,0)
				#for counting studenst present
				present[str(index)]='1'
			else :
				draw_rectangle(frame,rect,255,0,0)
		#customising frame
		frame = cv2.copyMakeBorder(frame,0,0,150,0,cv2.BORDER_CONSTANT,value=[0,0,0])
		y=20
		font = cv2.FONT_HERSHEY_COMPLEX
		for stud in present:
			cv2.putText(frame, stud, (20,y), font, 0.5, (255, 255, 255), 1)
			y+=20
		#setting window location
		winname = "ASFR"
		cv2.namedWindow(winname)
		cv2.moveWindow(winname,40,30)
		
		cv2.imshow("ASFR",frame)

		if(cv2.waitKey(1) & 0xFF == ord('q')):
			break

	cap.release()
	cv2.destroyAllWindows()
	return present

def am():

    branch = raw_input("Enter Branch (CS,MM,ME,EC,EE,CE) : ")
    semester = raw_input("Enter Semester (I,II,III,IV,V,VI,VII,VIII) : ")

    present_students = attendance()
    print "\tNo of students present : {}".format(len(present_students))
    print "\tDate : ",dt.datetime.today()
    print "\tSemester : ",semester
    print "\tBranch : ",branch
    ch = str(raw_input("Do you want to mark attendance (y/n): "))
    if(ch=='y' or ch=='Y'):
        mark_attendance_module.mam(semester,branch,present_students,dt.datetime.today().day,dt.datetime.today().month,dt.datetime.today().year)
    print "Press enter to go back to main menu."
    raw_input()
    return

#am()