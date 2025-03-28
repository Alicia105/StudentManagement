import student

def displayMenu():
    print("===========================SCHOOL MANAGEMENT SYSTEM===========================")
    print("Welcome to our platform !")
    print("-----Choose a menu-----")
    print("1. Administrator")
    print("2. Student")
    print("3.Exit")

    while True :
        try :
            a=int(input())
            #showMenu(a)
            return
        except:
            raise ValueError("Enter a valid number")
    
def showMenu(a):
    match(a):
        case 1:
            #to complete
        case 2:
            showStudentMenu(list)
        case 3:
            return
        case _:
            break

    return