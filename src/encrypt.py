import base64

def encrypt(pwd):
    #Encoding the entered password
    encpwd = base64.b64encode(pwd.encode("utf-8"))
    return encpwd

def logIn(list,id,pwd):
    for l in list:
        if l.get("id")==id or l.get("email")==id:
            if l.get("password").compare(encrypt(pwd)):
                print("Successfully logged in.")
                return l
            else:
                print("Login Failed")
                return
    return

def chooseANumberForMenu():
    while True :
        try: 
            x=int(input())
            return x
        except:
            raise ValueError ("Enter a number")
 

def main():
    x=chooseANumberForMenu()

main()