import random
import encrypt

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
    password=input("Enter your password :")

    #Create course list
    list=[]
    student["courses"]=list

    #Create id    
    r=random.randint(0,1000)
    id='A'+str(r)
    student["id"]=id
    
    #Create mail
    mail=name[0]+lastName+"@school.edu"
    print("----Your account was succesfully created----")
    print(f"Your email is : {mail}")
    print(f"Your id is : {id}")
    print(f"Your password is : {password}")
    print("You'll need these infos to log in.")
    print("\n")

    #Encrypt password
    student["password"]=encrypt.encrypt(password)

    return student

#Add a new student account to the list of existing student
def addStudent(listStudent,student):
    listStudent.append(student)
    return

#Remove a student account to the list of existing student
def deleteStudent(listStudent):
    id=input("Enter your id :")
    for student in listStudent:
        if student.get("id")==id :
            listStudent.remove(student)
    return

#Modify a student account
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
            while True :
                try:
                    age=int(input("Enter your age :"))
                    student["age"]=age
                    break
                except:
                    raise ValueError("Please enter a number")
        case 4:
            dateOfBirth=input("Enter your date of birth as DD/MM/YYYY :")
            student["dateOfBirth"]=dateOfBirth
            
        case 5:
            password=input("Enter your password :")
            student["password"]=encrypt(password)

        case 6:
            return
        case _:
            raise ValueError ("Option not supported")
    
    return
    

#Student Menu 

def chooseStudentMenu():
    print("===========================Welcome to the student menu===========================")
    print("Choose an option :")
    print("1.Log In")
    print("2.Sign In")
    print("3.Exit")
    
    x=encrypt.checkEnteredNumberIsInt()
    return x
        
def actionStudentMenu(student):
    print("===========================Welcome to the student menu===========================")
    print("Choose an option :")
    print("1.See Profile")
    print("2.Modify personal information")
    print("3.Add/Remove courses")
    print("4.Exit")

    x=encrypt.checkEnteredNumberIsInt()

    match x:
        case 1 :
            print(student)           
        case 2 :
            modifyStudent(student)
        case 3:
            return #to complete
        case 4:
            return
        case _:
            raise ValueError ("Option not supported")
    return


def showStudentMenu(list):
    x=chooseStudentMenu()
    match x:
        case 1 :
            id=input("Enter your id or email :")
            pwd=input("Enter your pwd :")
            student=encrypt.login(list,id,pwd)

        case 2 :
            student=createStudent()
            addStudent(list,student)
            
        case 3:
            return
        case _:
            raise ValueError ("Option not supported")
    
    return
        
def main():
    s=createStudent()
    print(s)

main()
    

    
