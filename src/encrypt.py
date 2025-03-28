import base64

#Encoding the entered password--good
def encrypt(pwd):
    encpwd = base64.b64encode(pwd.encode("utf-8"))
    return encpwd

# Decoding a string--good
def decrypt(pwd):
    try:
        decode=base64.b64decode(pwd).decode("utf-8")
        return decode
    except Exception:
        return None  # Handle invalid encoding

# Logging in--good
def logIn(userList, userId, pwd):
    for user in userList:
        if user.get("id") == userId or user.get("email") == userId:
            storedPassword = user.get("password")
            
            # Ensure password exists
            if storedPassword is None:
                print("Login Failed: No password found.")
                return
            
            # Compare passwords correctly
            if decrypt(storedPassword) == pwd:
                print("Successfully logged in.")
                return user
            else:
                print("Login Failed: Incorrect password.")
                return
    print("Login Failed: User not found.")  # If no match is found
    return None

#good
def checkEnteredNumberIsInt():
    while True :
        try: 
            x=int(input())
            return x
        except ValueError:
            print("Enter a number")
