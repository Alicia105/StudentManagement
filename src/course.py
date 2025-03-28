import encrypt
list_course=[]

#check if course exists
def checkCourseExist(list,id):
    for l in list:
        if l.get("ID")==id:
            return True
    return False

#check unique ID course-->to modify, do the same for student ID
def uniqueIDCourse():
#def uniqueIDCourse(list):
    while True :
        try:
            id=input("Enter course ID :")
            #checkCourseExist(list,id)
            return id
        except ValueError :
            print("This ID is already taken. Enter a different one.")

#Create a course--good
def createCourse():
    course=dict()

    #Enter course name
    courseName=input("Enter course name :")
    course["course Name"]=courseName

    #Enter course id-->take care here
    id=uniqueIDCourse()
    course["ID"]=id.upper()

    #Enter number of student 
    n=0   
    course["Number of students"]=n

    #Enter maximum number of student able to register
    print("Enter maximum number of students :")
    maxNumber=encrypt.checkEnteredNumberIsInt()
    course["Max Number of students"]=maxNumber
    
    #Enter course semester
    semester=input("Enter course semester :")
    course["semester"]=semester

    #Enter professor name
    profName=input("Enter professor name  :")
    course["Professor Name"]=profName
       
    #Print course info
    print(f"----{id} course was succesfully created----")
    print(f"Number of students registered : {n}")
    print(f"Max number of students : {maxNumber}")
    print(f"Course semester : {semester}")
    print(f"Professor Name :{profName}")
    print("--------------------------------------------")
    print("\n")

    return course

#Add a new course to the list of existing courses--good
def addCourse(listCourse,course):
    listCourse.append(course)
    return listCourse

#Remove a course  to the list of existing courses--good
def deleteCourse(listCourse,id):
    for course in listCourse:
        if course.get("ID")==id :
            listCourse.remove(course)
    return listCourse

#Modify a course info--good
def modifyCourse(course):
    print("What do you want to modify ?")
    print("1.Name")
    print("2.ID")
    print("3.Number of students registered")
    print("4.Max number of students")
    print("5.Semester")
    print("6.Professor")
    print("7.Exit")

    x=encrypt.checkEnteredNumberIsInt()

    match x:
        case 1 :
            courseName=input("Enter course name :")
            course["course Name"]=courseName
            
        case 2 :
            id=uniqueIDCourse()
            course["ID"]=id.upper()
           
        case 3:
            while True :
                try:
                    print("Enter number of student registered:")
                    numStudent=encrypt.checkEnteredNumberIsInt()
                    course["Number of students"]=numStudent
                    break
                except:
                    raise ValueError("Please enter a number")
        case 4:
            while True :
                try:
                    print("Enter maximum number of student :")
                    maxNumber=encrypt.checkEnteredNumberIsInt()
                    course["Max Number of students"]=maxNumber
                    break
                except:
                    raise ValueError("Please enter a number")
            
        case 5:
            semsester=input("Enter course semester :")
            course["semester"]=semsester

        case 6:
            profName=input("Enter professor name  :")
            course["Professor Name"]=profName
        
        case 7:
            return
        case _:
            raise ValueError ("Option not supported")
    
    return
