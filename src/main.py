
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
        except:
            raiseException ValueError("Enter a valid number")
