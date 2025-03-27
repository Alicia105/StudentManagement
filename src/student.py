import random

#Create a new student account
def createStudent():
    student=dict()

    #Enter name
    name=input("Enter your first name :")
    student["name"]=name

    #Enter last name
    lastName=input("Enter your last name :")
    student["lastName"]=lastName

    #Enter age
    while True :
        try:
            age=int(input("Enter your age :"))
            student["age"]=age
            break
        except:
            raise ValueError("Please enter a number")

    #Enter date of birth
    dateOfBirth=input("Enter your date of birth as DD/MM/YYYY :")
    student["dateOfBirth"]=dateOfBirth

    #Enter major
    major=input("Enter your major :")
    student["major"]=major

    #Create course list
    list=[]
    student["courses"]=list

    #Create id    
    r=random(0,1000)
    id='A'+str(r)
    student["id"]=id
    
    #Create mail
    mail=name[0]+lastName+"@school.edu"
    print("----Your account was succesfully created----")
    print(f"Your email is : {mail}")
    print(f"Your id is : {id}")

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
def modifyStudent():
    return



    

    
