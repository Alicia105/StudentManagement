import student
import course
import administrator

def displayMenu():
    listAdmin=[]
    listStudent=[]
    listCourse=[]
    print("===========================SCHOOL MANAGEMENT SYSTEM===========================")
    print("Welcome to our platform !")
    print("-----Choose a menu-----")
    print("1. Administrator")
    print("2. Student")
    print("3.Exit")

    while True :
        try :
            a=int(input())
            showMenu(a,listAdmin,listStudent,listCourse)
            return
        except:
            raise ValueError("Please enter a valid number")
    
def showMenu(a,listAdmin,listStudent,listCourse):
    match(a):
        case 1:
            t=0
            while t==0:
                t=administrator.showAdminMenu(listAdmin,listCourse)
            return 0
        case 2:
            t=0
            while t==0:
                t=student.showStudentMenu(listStudent,listCourse)
            return 0
        case 3:
            return 1
        case _:
            raise ValueError("Option not supported")

    return 0

def main():
    displayMenu()

main()