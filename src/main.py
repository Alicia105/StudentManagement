import encrypt
from student import * 
from course import *
from administrator import *
import administrator
import student
import course
import requests

API_URL = "http://127.0.0.1:5000"

def printMenu():
    print("===========================SCHOOL MANAGEMENT SYSTEM===========================")
    print("Welcome to our platform !")
    print("-----Choose a menu-----")
    print("1. Administrator")
    print("2. Student")
    print("3.Exit")
    return

def displayMenu(API_URL):
    listAdmin=get_all_admins_database(API_URL)
    listStudent=get_all_students_database(API_URL)
    listCourse=get_all_courses_database(API_URL)

    t=0
    while t!=1 :
        printMenu()
        a=encrypt.checkEnteredNumberIsInt()
        t=showMenu(a,listAdmin,listStudent,listCourse,API_URL)
    return t

def showMenu(a,listAdmin,listStudent,listCourse,API_URL):
    match(a):
        case 1:
            t=0
            while t==0:
                t=administrator.showAdminMenu(listAdmin,listStudent,listCourse,API_URL)
            return 2
        case 2:
            t=0
            while t==0:
                t=student.showStudentMenu(listStudent,listCourse,API_URL)
            return 2
        case 3:
            return 1
        case _:
            print("Option not supported")

    return 0

def main():
    t=0
    while t==0 :
        t=displayMenu(API_URL)
    print("Thank you for using the School Management System!")
    print("--------------------------------------------------")
    return    

main()