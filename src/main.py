import student

def displayMenu():
    print("===========================SCHOOL MANAGEMENT SYSTEM===========================")
    print("Welcome to our platform !")
    print("-----Choose a menu-----")
    print("1. Administrator")
    print("2. School staff")
    print("3.Student")
    print("4.Exit")

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
            break
        case 2:
            break
        case 3:
            showMenuStudent(a)
            break
        case _:
            break

    return