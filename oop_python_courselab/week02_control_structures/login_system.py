correct_username_nbs = "admin"
correct_password_nbs = "1234"
attempts = 0
while attempts < 3:
    username_nbs = input("Enter username: ")
    password_nbs = input("Enter password: ")
    if username_nbs == correct_username_nbs and password_nbs == correct_password_nbs:
        print("Login Successful")
        break
    else:
        print("Invalid Credentials")
        attempts += 1
if attempts == 3:
    print("Account Locked")

#Nicole B. Sambile