import sqlite3
import csv
import sys
def vam():

    db = sqlite3.connect("./databases/attendance.db")
    c = db.cursor()
    query = "SELECT name FROM sqlite_master WHERE TYPE='table';"
    res = c.execute(query)
    print "ALL AVAILABE ATTENDANCES"
    i=01
    for name in res:
        sys.stdout.write(str(i)  + " " +name[0]+"\t\t")
        #print str(i)  + " " +name[0]
        
        if(i%3==0):
            print ""
        i+=1
    print "\n\n"

    branch = raw_input("Enter Branch (CS,EE,EC,MM,ME,CE) : ")
    semester = raw_input("Enter Semester (I,II,III,IV,V,VI,VII,VII) : ")
    month = raw_input("Enter Month (1,2,3,4,5,6,7,8,9,10,11,12) : ")
    year = raw_input("Enter Year : ")


    try :
        tn = branch+"_"+semester+"_"+month+"_"+year
        csvWriter = csv.writer(open("./attendances/"+tn+".csv", "w"))
        c.execute("SELECT * FROM {}".format(tn))
        csvWriter.writerow([d[0] for d in c.description])
        rows = c.fetchall()
        csvWriter.writerows(rows)
        print "Find required attendance at /attendances/"+branch+"_"+semester+"_"+month+"_"+year+".csv"
    except:
        print "Could not find attendance datails for given query"
    print "Press enter to go back to main menu."
    raw_input()
    return


#vam()
