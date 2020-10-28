print ("Please use your account to log-in the system")
usernameInput = input("Username :")
passwordInput = input("Password :")
while usernameInput != "admin" or passwordInput != "1234":

    if usernameInput != "admin" or passwordInput != "1234":
            print ("Please try again")
            usernameInput = input("Username :")
            passwordInput = input("Password :")

    if usernameInput == "admin" and passwordInput == "1234":
            print ("You logged in success!!")



