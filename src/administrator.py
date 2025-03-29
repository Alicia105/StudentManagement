import random
import encrypt
import course
import student

#Create a new admin account--good
def createAdmin():
    admin=dict()

    #Enter name
    name=input("Enter your first name :")
    admin["name"]=name

    #Enter last name
    lastName=input("Enter your last name :")
    admin["lastName"]=lastName

    #Enter date of birth
    dateOfBirth=input("Enter your date of birth as DD/MM/YYYY :")
    admin["dateOfBirth"]=dateOfBirth

    #Enter job position
    jobPosition =input("Enter your job position :")
    admin["job position"]=jobPosition

    #Enter job start date 
    startDate=input("Enter your job start date as MM/YYYY :")
    admin["startDate"]=startDate

    #Enter password
    password=input("Enter your password :").strip()

    #Create id    
    r=random.randint(0,1000)
    id='S'+str(r)
    admin["id"]=id
    
    #Create mail
    mail=name[0]+lastName+"@school.edu"
    admin["mail"]=mail.lower()

    print("\n----Your account was succesfully created----")
    print(f"Your email is : {mail}")
    print(f"Your id is : {id}")
    print(f"Your password is : {password}")
    print("You'll need these infos to log in.")
    print("\n")

    #Encrypt password
    admin["password"]=encrypt.encrypt(password)

    return admin

def printadmin(admin):
    print("----Your personal informations----")
    print(f"Your email is : {admin.get("mail")}")
    print(f"Your id is : {admin.get("id")}")
    print(f"Your password is : {admin.get("password")}")
    print("\n")

#Add a new admin account to the list of existing admin--good
def addAdmin(listAdmin,admin):
    listAdmin.append(admin)
    return listAdmin

#Remove a admin account to the list of existing admin--good
def deleteAdmin(listAdmin,id):
    newList = [admin for admin in listAdmin if admin.get("id") != id]
    if len(newList) == len(listAdmin):
        print("Admin not found.")  
    return newList

#Modify a admin account--good
def modifyAdmin(admin):
    print("What do you want to modify ?")
    print("1.Name")
    print("2.Surname")
    print("3.Date of birth")
    print("4.Job Position")
    print("5.Start date")
    print("6.Password")
    print("7.Exit")

    x=encrypt.checkEnteredNumberIsInt()

    match x:
        case 1 :
            name=input("Enter your first name :")
            admin["name"]=name
            
        case 2 :
            lastName=input("Enter your last name :")
            admin["lastName"]=lastName
           
        case 3:
            dateOfBirth=input("Enter your date of birth as DD/MM/YYYY :")
            admin["dateOfBirth"]=dateOfBirth
            
        case 4:
            jobPosition =input("Enter your job position :")
            admin["job position"]=jobPosition
            
        case 5:
            startDate=input("Enter your job start date as MM/YYYY :")
            admin["startDate"]=startDate

        case 6:
            password=input("Enter your password :").strip()
            admin["password"]=encrypt.encrypt(password)
            
        case 7:
            return
        case _:
            print("Option not supported")
    
    return
    
#Admin Menu 
#good
def chooseAdminMenu():
    print("===========================Welcome to the admin menu===========================")
    print("Choose an option :")
    print("1.Log In")
    print("2.Sign In")
    print("3.Exit")
    
    x=encrypt.checkEnteredNumberIsInt()
    return x
#to verify
def actionAdminMenu(admin,listStudent,listCourse):
    print("===========================Welcome to the admin menu===========================")
    print("Choose an option :")
    print("1.See Profile")
    print("2.Modify personal information")
    print("3.Add courses")
    print("4.Remove courses")
    print("5.Modify courses")
    print("6.See courses")
    print("7.Add student")
    print("8.Remove student")
    print("9.Modify student")
    print("10.Register student")
    print("11.Unregister student")
    print("12.See student profile")
    print("13.See all student profiles")
    print("14.See a course")
    print("15.Exit")

    x=encrypt.checkEnteredNumberIsInt()

    match x:
        case 1 :#good
            print(admin)           
        case 2 :#good
            modifyAdmin(admin)
        case 3:#good
            c=course.createCourse()
            if not course.checkCourseExist(listCourse,c.get("ID")) and len(listCourse)>0:
                listCourse=course.addCourse(listCourse,c)               

            elif len(listCourse)==0:
                listCourse=course.addCourse(listCourse,c)  

            else :
                print("This course id already exist")
            
        case 4:#good
            ID=input("Enter course id :").upper()
            if course.checkCourseExist(listCourse,ID):
                listCourse=course.deleteCourse(listCourse,ID)
            else :
                print("This course id doesn't exist")
            
        case 5:#good
            ID=input("Enter course id :").upper()
            if course.checkCourseExist(listCourse,ID):
                c=course.getCourse(listCourse,ID)
                course.modifyCourse(c)
            else :
                print("This course id doesn't exist")   
        case 6:#good
            print(listCourse)
        
        case 7:#good
            s=student.createStudent()
            listStudent=student.addStudent(listStudent,s)
        case 8:#good
            id=input("Enter student id :")
            if student.checkStudentExist(listStudent,id):
                listStudent=student.deleteStudent(listStudent,id)
                print("This student account was succesfully deleted")
            else :
                print("This student id doesn't exist")

        case 9:#good
            id=input("Enter student id :")
            if student.checkStudentExist(listStudent,id):
                s=student.getStudent(listStudent,id)
                student.modifyStudent(s)
            else :
                print("This student id doesn't exist")

        case 10:#good
            id=input("Enter student id :")
            ID=input("Enter course id :").upper()
            if student.checkStudentExist(listStudent,id):
                if course.checkCourseExist(listCourse,ID):
                    s=student.getStudent(listStudent,id)
                    s=student.registerCourseStudent(s,listCourse,ID)
                else :
                    print("This course id doesn't exist")

            else :
                print("This student id doesn't exist")
           
        case 11:#good
            id=input("Enter student id :")
            ID=input("Enter course id :").upper()
            if student.checkStudentExist(listStudent,id):
                if course.checkCourseExist(listCourse,ID):
                    s=student.getStudent(listStudent,id)
                    s=student.unregisterCourseStudent(s,listCourse,ID)
                else :
                    print("This course id doesn't exist")

            else :#good
                print("This student id doesn't exist")
        
        case 12:#good
            id=input("Enter student id :")
            if student.checkStudentExist(listStudent,id):
                s=student.getStudent(listStudent,id)
                print(s)
            else :
                print("This student id doesn't exist")
            
        case 13:#good
            print(listStudent)
        case 14:#good
            ID=input("Enter course id :").upper()
            if course.checkCourseExist(listCourse,ID):
                c=course.getCourse(listCourse,ID)
                print(c)              
            else :
                print("This course id doesn't exist")
        case 15:#good
            return 1
        case _:
            print("Option not supported")
    return 0
#good
def showAdminMenu(listAdmin,listStudent,listCourse):
    x=chooseAdminMenu()
    match x:
        case 1 :
            id=input("Enter your id or email :")
            pwd=input("Enter your pwd :")
            admin=encrypt.logIn(listAdmin,id,pwd)
            t=0
            if(admin!=None):
                t=0
            else:
                return 0
            while(t==0):
                t=actionAdminMenu(admin,listStudent,listCourse)
            return 0
        case 2 :
            admin=createAdmin()
            listAdmin=addAdmin(listAdmin,admin)
            return 0
        case 3:
            return 1
        case _:
            print("Option not supported")
    
    return 0

"""def main():
    lc=[]
    ls=[]
    la=[]
    c=course.createCourse()
    lc=course.addCourse(lc,c)
    print(lc)

    s=student.createStudent()
    ls=student.addStudent(ls,s)
    print(ls)

    a=createAdmin()
    la=addAdmin(la,a)
    print(la)

    while True:
        showAdminMenu(la,ls,lc)

        
    
main()"""
    

    