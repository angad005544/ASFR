import cv2
import os
import numpy as np
import face_recognition


subjects = ["Chaitanya","Phanindra","Angad","Praneeth","Ashutosh","Praneeth","Dhoni","Modi","Salman","RakulPreet","SomeOne","Katrina","UnknownPerson"]

branch_code = {'CS':'01','ME':'02','CE':'03'}     
course_code = {'UG':'01','PG':'02' }


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

def get_int_label(name):
    name = str(name)
    #res = name[0:4]+course_code[name[4:6]]+branch_code[name[6:8]]+name[8:11]
    res=int(name[9:11])
    return res


def prepare_training_data2(data_folder_path):
    
    dirs_branch = os.listdir(data_folder_path)
    
    faces = []
    labels = []
    
    for dir_bname in dirs_branch:
        print dir_bname

        dirs_sem = os.listdir(data_folder_path+"/"+dir_bname)

        for dir_name in dirs_sem:
            print dir_name

            
            subject_dir_path = data_folder_path + "/" + dir_bname + "/" + dir_name
            subject_images_names = os.listdir(subject_dir_path)

            for image_name in subject_images_names:
                if image_name.startswith("."):
                    continue;
                label = get_int_label(image_name)
                image_path = subject_dir_path + "/" + image_name
                image = cv2.imread(image_path)
                #cv2.imshow("Training on image...", cv2.resize(image, (400, 500)))
                #cv2.waitKey(20)
                face, rect = detect_face(image)
                if face is not None:
                    faces.append(face)
                    labels.append(label)
            
    cv2.destroyAllWindows()
    cv2.waitKey(1)
    cv2.destroyAllWindows()
    
    return faces, labels



def prepare_training_data(data_folder_path):
    
    dirs = os.listdir(data_folder_path)
    
    faces = []
    labels = []
    
    for dir_name in dirs:
        
        if not dir_name.startswith("s"):
            continue;
            

        label = int(dir_name.replace("s", ""))
        
        
        subject_dir_path = data_folder_path + "/" + dir_name
        
        subject_images_names = os.listdir(subject_dir_path)
        
        
        for image_name in subject_images_names:
            
           
            if image_name.startswith("."):
                continue;
            
            image_path = subject_dir_path + "/" + image_name

            image = cv2.imread(image_path)
            
            
            cv2.imshow("Training on image...", cv2.resize(image, (400, 500)))
            cv2.waitKey(20)
            
            face, rect = detect_face(image)
            
           
            if face is not None:
                faces.append(face)
                labels.append(label)
            
    cv2.destroyAllWindows()
    cv2.waitKey(1)
    cv2.destroyAllWindows()
    
    return faces, labels





def training_recogniser():
    print "Preparing data..."
    #faces, labels = prepare_training_data("training-data")
    faces, labels = prepare_training_data2("training-images")
    print("Data prepared")

    print("Total faces: ", len(faces))
    print("Total labels: ", len(labels))

    for lable in labels:
        print lable

    face_recognizer = cv2.LBPHFaceRecognizer_create()
    face_recognizer.train(faces, np.array(labels))
    print "Recognizer trainedd$$"
    return face_recognizer

#training_recogniser()




