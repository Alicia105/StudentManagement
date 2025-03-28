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

#Remove a admin account to the list of existing admin
def deleteAdmin(listAdmin,id):
    for admin in listAdmin:
        if admin.get("id")==id :
            listAdmin.remove(admin)
    return listAdmin

#Modify a admin account
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
#to verify
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
    print("6.Add student")
    print("7.Remove student")
    print("8.Modify student")
    print("9.Register student")
    print("10.Unregister student")
    print("11.Exit")

    x=encrypt.checkEnteredNumberIsInt()

    match x:
        case 1 :
            print(admin)           
        case 2 :
            modifyAdmin(admin)
        case 3:
            course=course.createcourse()
            if course.checkCourseExist(listCourse,ID):
                listCourse=course.addCourse(listCourse,course)               
            else :
                print("This course id already exist")
            
        case 4:
            ID=input("Enter course id :").upper()
            if course.checkCourseExist(listCourse,ID):
                listCourse=course.deleteCourse(listCourse,ID)
            else :
                print("This course id doesn't exist")
            
        case 5:
            ID=input("Enter course id :").upper()
            if course.checkCourseExist(listCourse,ID):
                listCourse=course.modifyCourse(listCourse.get("ID"))
            else :
                print("This course id doesn't exist")   
        case 6:
            student=student.createStudent()
            listStudent=student.addStudent(listStudent,student)
        case 7:
            id=input("Enter student id :")
            if student.checkStudentExist(listStudent,id):
                listStudent=student.deleteStudent(listStudent,id)
            else :
                print("This student id doesn't exist")
        case 8:
            id=input("Enter student id :")
            if student.checkStudentExist(listStudent,id):
                student=student.modifyStudent(student)
            else :
                print("This student id doesn't exist")
        case 9:
            id=input("Enter student id :")
            ID=input("Enter course id :").upper()
            if student.checkStudentExist(listStudent,id):
                if course.checkCourseExist(listCourse,ID):
                    student=student.registerCourseStudent(student,listCourse,ID)
                else :
                    print("This course id doesn't exist")

            else :
                print("This student id doesn't exist")
           
        case 10:
            id=input("Enter student id :")
            ID=input("Enter course id :").upper()
            if student.checkStudentExist(listStudent,id):
                if course.checkCourseExist(listCourse,ID):
                    student=student.unregisterCourseStudent(student,listCourse,ID)
                else :
                    print("This course id doesn't exist")

            else :
                print("This student id doesn't exist")
        
        case 11:
            return 1
        case _:
            print("Option not supported")
    return 0

#to verify
def showAdminMenu(listAdmin,listCourse):
    x=chooseAdminMenu()
    match x:
        case 1 :
            id=input("Enter your id or email :")
            pwd=input("Enter your pwd :")
            admin=encrypt.logIn(listAdmin,id,pwd)
            t=0
            while(t==0):
                t=actionAdminMenu(admin,listCourse)
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
def main():
    l=[]
    c=createAdmin()
    print(c)
    l=addAdmin(l,c)
    print(l)
    l=deleteAdmin(l,c)
    print(l)

main()
    

    