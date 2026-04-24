def register_nbs():
    username_nbs = input("Enter username: ")
    password_nbs = input("Enter password: ")
    with open("users.txt", "a") as file_nbs:
        file_nbs.write(username_nbs + "," + password_nbs + "\n")
    print("Registration successful!")

def login_nbs():
    username_nbs = input("Enter username: ")
    password_nbs = input("Enter password: ")
    try:
        with open("users.txt", "r") as file_nbs:
            for line_nbs in file_nbs:
                stored_user_nbs, stored_pass_nbs = line_nbs.strip().split(",")
                if username_nbs == stored_user_nbs and password_nbs == stored_pass_nbs:
                    print("Login successful!")
                    return
        print("Invalid credentials!")
    except FileNotFoundError:
        print("No users registered yet!")

def main_nbs():
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        choice_nbs = input("Enter choice: ")
        
        if choice_nbs == "1":
            register_nbs()
        elif choice_nbs == "2":
            login_nbs()
        elif choice_nbs == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

main_nbs()

#Nicole Sambile