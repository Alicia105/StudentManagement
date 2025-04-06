import encrypt
import requests


#To communicate with API--------------------------------------------------------------------------------

def send_course_database(API_URL,course_name,professor_name,course_id,number_of_credit_hours,number_of_students,max_number_of_students,semester):
    data = {"course Name":course_name, "Professor Name":professor_name, "ID":course_id,"number of credit hours":number_of_credit_hours,"Number of students":number_of_students,"Max Number of students":max_number_of_students, "semester":semester}
    response = requests.post(f"{API_URL}/courses", json=data)
    print(response.json())

def update_course_database(API_URL,course_name,professor_name,course_id,number_of_credit_hours,number_of_students,max_number_of_students,semester):
    data = {"course Name":course_name, "Professor Name":professor_name, "ID":course_id,"number of credit hours":number_of_credit_hours,"Number of students":number_of_students,"Max Number of students":max_number_of_students, "semester":semester}
    response = requests.put(f"{API_URL}/courses/{course_id}", json=data)
    print(response.json())

def get_course_database(API_URL,courseid):
    response = requests.get(f"{API_URL}/courses/{courseid}")
    if response.status_code == 200:
        courseDB = response.json()
        course=dict()
        course["course Name"]=courseDB["course Name"]
        course["Professor Name"]=courseDB["Professor Name"]
        course["ID"]=courseDB["ID"]
        course["number of credit hours"]=courseDB["number of credit hours"]
        course["Number of students"]=courseDB["Number of students"]
        course["Max Number of students"]=courseDB["Max Number of students"]
        course["semester"]=courseDB["semester"]
        print(f"Course Found: ID: {courseDB["ID"]}, course Name: {courseDB["course Name"]},Professor Name: {courseDB["Professor Name"]}, number of credit hours: {courseDB["number of credit hours"]}, Number of students : {courseDB["Number of students"]}, Max Number of students: {courseDB["Max Number of students"]}, semester : {courseDB["semester"]}")
    else:
        print("Course not found")

def get_all_courses_database(API_URL):
    response = requests.get(f"{API_URL}/courses")
    if response.status_code == 200:
        courseDB = response.json()
        listCourses=[]
        for course in  courseDB :
            c=dict()
            c["course Name"]=course["course Name"]
            c["Professor Name"]=course["Professor Name"]
            c["ID"]=course["ID"]
            c["number of credit hours"]=course["number of credit hours"]
            c["Number of students"]=course["Number of students"]
            c["Max Number of students"]=course["Max Number of students"]
            c["semester"]=course["semester"]
            listCourses.append(c)
        return listCourses
    else:
        print("Failed to retrieve courses") 
        listCourses=[]
        return listCourses      

def delete_course_database(API_URL,courseid):
    requests.delete(f"{API_URL}/courses/{courseid}")
#------------------------------------------------------------------------------------------------------------------

#check if course exists
def checkCourseExist(list,id):
    for l in list:
        if l.get("ID")==id:
            return True
    return False

#check unique ID course-->to modify, do the same for student ID
"""def uniqueIDCourse():
#def uniqueIDCourse(list):
    while True :
        try:
            id=input("Enter course ID :")
            #checkCourseExist(list,id)
            return id
        except ValueError :
            print("This ID is already taken. Enter a different one.")"
"""

def getCourse(listCourse,id):
    for l in listCourse :
        if checkCourseExist(listCourse,l.get("ID")) and l.get("ID")==id:
            return l
    return None

#Create a course--good
def createCourse():
    course=dict()

    #Enter course name
    courseName=input("Enter course name :")
    course["course Name"]=courseName

    #Enter course id-->take care here
    id=input("Enter course ID :")
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

    #Enter number of credit hours
    print("Enter number of credit hours :")
    credit=encrypt.checkEnteredNumberIsInt()
    course["number of credit hours"]=credit

    #Enter professor name
    profName=input("Enter professor name  :")
    course["Professor Name"]=profName
       
    #Print course info
    print(f"----{id} course was succesfully created----")
    print(f"Number of students registered : {n}")
    print(f"Max number of students : {maxNumber}")
    print(f"Course semester : {semester}")
    print(f"Number of credit hours :{credit}")
    print(f"Professor Name :{profName}")
    print("--------------------------------------------")
    print("\n")

    return course

#Add a new course to the list of existing courses--good
def addCourse(listCourse,course,API_URL):
    listCourse.append(course)
    send_course_database(API_URL,course["course Name"],course["Professor Name"],course["ID"],course["number of credit hours"],course["Number of students"],course["Max Number of students"],course["semester"])
    return listCourse

#Remove a course  to the list of existing courses--good
def deleteCourse(listCourse,id,API_URL):
    for c in listCourse :
        if c.get("ID")==id :
            delete_course_database(API_URL,id)
    for course in listCourse:
        if course.get("ID")==id :
            listCourse.remove(course)
    return listCourse

#Modify a course info--good
def modifyCourse(course,API_URL):
    print("What do you want to modify ?")
    print("1.Name")
    print("2.ID")
    print("3.Number of students registered")
    print("4.Max number of students")
    print("5.Semester")
    print("6.Professor")
    print("7.Credit hours")
    print("8.Exit")

    x=encrypt.checkEnteredNumberIsInt()

    match x:
        case 1 :
            courseName=input("Enter course name :")
            course["course Name"]=courseName
            
        case 2 :
            id=input("Enter course ID :")
            course["ID"]=id.upper()
           
        case 3:
            print("Enter number of student :")
            numStudent=encrypt.checkEnteredNumberIsInt()
            course["Number of students"]=numStudent
                
        case 4:
            print("Enter maximum number of student :")
            maxNumber=encrypt.checkEnteredNumberIsInt()
            course["Max Number of students"]=maxNumber
                        
        case 5:
            semsester=input("Enter course semester :")
            course["semester"]=semsester

        case 6:
            profName=input("Enter professor name  :")
            course["Professor Name"]=profName
        
        case 7:
            print("Enter number of credit hours :")
            credit=encrypt.checkEnteredNumberIsInt()
            course["number of credit hours"]=credit
        case 8:
            return
        case _:
            print("Option not supported")
    update_course_database(API_URL,course["course Name"],course["Professor Name"],course["ID"],course["number of credit hours"],course["Number of students"],course["Max Number of students"],course["semester"])    
    return
