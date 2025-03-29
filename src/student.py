import random
import encrypt
import course

#check if student exists
def checkStudentExist(listStudent,id):
    for l in listStudent:
        if l.get("id")==id:
            return True
    return False

#Create a new student account--good
def createStudent():
    student=dict()

    #Enter name
    name=input("Enter your first name :")
    student["name"]=name

    #Enter last name
    lastName=input("Enter your last name :")
    student["lastName"]=lastName

    #Enter age
    print("Enter your age :")
    age=encrypt.checkEnteredNumberIsInt()
    student["age"]=age
    
    #Enter date of birth
    dateOfBirth=input("Enter your date of birth as DD/MM/YYYY :")
    student["dateOfBirth"]=dateOfBirth

    #Enter major
    major=input("Enter your major :")
    student["major"]=major

    #Enter password
    password=input("Enter your password :").strip()

    #Create course list
    list=[]
    student["courses"]=list

    #Create id    
    r=random.randint(0,1000)
    id='A'+str(r)
    student["id"]=id
    
    #Create mail
    mail=name[0]+lastName+"@school.edu"
    student["mail"]=mail.lower()
    print("\n----Your account was succesfully created----")
    print(f"Your email is : {mail}")
    print(f"Your id is : {id}")
    print(f"Your password is : {password}")
    print("You'll need these infos to log in.")
    print("\n")

    #Encrypt password
    student["password"]=encrypt.encrypt(password)

    return student

def printStudent(student):
    print("----Your personal informations----")
    print(f"Your email is : {student.get("mail")}")
    print(f"Your id is : {student.get("id")}")
    print(f"Your password is : {student.get("password")}")
    print("\n")

def getStudent(listStudent,id):
    for l in listStudent :
        if checkStudentExist(listStudent,id) and l.get("id")==id:
            return l
    return None
    
#Add a new student account to the list of existing student--good
def addStudent(listStudent,student):
    listStudent.append(student)
    return listStudent

#Remove a student account to the list of existing student--good
def deleteStudent(listStudent,id):
    newList = [student for student in listStudent if student.get("id") != id]
    if len(newList) == len(listStudent):
        print("Student not found.")  
    return newList

#Modify a student account--good
def modifyStudent(student):
    print("What do you want to modify ?")
    print("1.Name")
    print("2.Surname")
    print("3.Age")
    print("4.Date of birth")
    print("5.Password")
    print("6.Exit")

    x=encrypt.checkEnteredNumberIsInt()

    match x:
        case 1 :
            name=input("Enter your first name :")
            student["name"]=name
            
        case 2 :
            lastName=input("Enter your last name :")
            student["lastName"]=lastName
           
        case 3:
            print("Enter your age :")
            age=encrypt.checkEnteredNumberIsInt()
            student["age"]=age
        case 4:
            dateOfBirth=input("Enter your date of birth as DD/MM/YYYY :")
            student["dateOfBirth"]=dateOfBirth
            
        case 5:
            password=input("Enter your password :").strip()
            student["password"]=encrypt.encrypt(password)

        case 6:
            return
        case _:
            print ("Option not supported")
    
    return
    
#Student Menu 
#good
def chooseStudentMenu():
    print("===========================Welcome to the student menu===========================")
    print("Choose an option :")
    print("1.Log In")
    print("2.Sign In")
    print("3.Exit")
    
    x=encrypt.checkEnteredNumberIsInt()
    return x

#good
def registerCourseStudent(student,listCourse,id):
    if course.checkCourseExist(listCourse,id) :
        student.get("courses").append(id)
        for l in listCourse :
            if l.get("ID")==id :
                if l.get("Max Number of students")>l.get("Number of students"):
                    l["Number of students"]+=1
                    return student
                else :
                    print("Impossible to register, class is full")
    else :
        print("Course does not exist.")                
    return student

#good
def unregisterCourseStudent(student,listCourse,id):
    if course.checkCourseExist(listCourse,id) :
        student["courses"].remove(id)
        for l in listCourse :
            if l.get("ID")==id :
                l["Number of students"]-=1
                return student
            else:
                print("You are not enrolled in this course.")
    else :
        print("Course does not exist.")

    return student

#good
def actionStudentMenu(student,listStudent,listCourse):
    print("===========================Welcome to the student menu===========================")
    print("Choose an option :")
    print("1.See Profile")
    print("2.Modify personal information")
    print("3.Add courses")
    print("4.Remove courses")
    print("5.Exit")

    x=encrypt.checkEnteredNumberIsInt()

    match x:
        case 1 :
            print(student)           
        case 2 :
            modifyStudent(student)
        case 3:
            id=input("Enter course id :")
            if course.checkCourseExist(listCourse,id):
                registerCourseStudent(student,listCourse,id)
                print("----You were succesfully registered----")
                print(f"Your courses :{student.get("courses")}")
            else :
                print("This course id doesn't exist")

        case 4:
            id=input("Enter course id :")
            if course.checkCourseExist(listCourse,id):
                unregisterCourseStudent(student,listCourse,id)
                print("----You were succesfully unregistered----")
                print(f"Your courses :{student.get("courses")}")
            else :
                print("This course id doesn't exist")

        case 5:
            return 1
        case _:
            print("Option not supported")
    return 0
#good
def showStudentMenu(listStudent,listCourse):
    x=chooseStudentMenu()
    match x:
        case 1 :
            id=input("Enter your id or email :")
            pwd=input("Enter your pwd :")
            student=encrypt.logIn(listStudent,id,pwd)
            if(student!=None):
                t=0
            else:
                return 0
            while(t==0):
                t=actionStudentMenu(student,listStudent,listCourse)
            return 0
        case 2 :
            student=createStudent()
            listStudent=addStudent(listStudent,student)
            return 0
        case 3:
            return 1
        case _:
            print ("Option not supported")
    
    return 0
        

