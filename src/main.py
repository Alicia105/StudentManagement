import encrypt
import student
import administrator

def printMenu():
    print("===========================SCHOOL MANAGEMENT SYSTEM===========================")
    print("Welcome to our platform !")
    print("-----Choose a menu-----")
    print("1. Administrator")
    print("2. Student")
    print("3.Exit")
    return

def displayMenu():
    listAdmin=[]
    listStudent=[]
    listCourse=[]

    t=0
    while t!=1 :
        printMenu()
        a=encrypt.checkEnteredNumberIsInt()
        t=showMenu(a,listAdmin,listStudent,listCourse)
    return t

def showMenu(a,listAdmin,listStudent,listCourse):
    match(a):
        case 1:
            t=0
            while t==0:
                t=administrator.showAdminMenu(listAdmin,listStudent,listCourse)
            return 2
        case 2:
            t=0
            while t==0:
                t=student.showStudentMenu(listStudent,listCourse)
            return 2
        case 3:
            return 1
        case _:
            print("Option not supported")

    return 0

def main():
    t=0
    while t==0 :
        t=displayMenu()
    print("Thank you for using the School Management System!")
    return    

main()