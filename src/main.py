import student
import course

def displayMenu():
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
            showMenu(a,listStudent,listCourse)
            return
        except:
            raise ValueError("Enter a valid number")
    
def showMenu(a,listStudent,listCourse):
    match(a):
        case 1:
            #t=0
            #while t==0:
            #to complete
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