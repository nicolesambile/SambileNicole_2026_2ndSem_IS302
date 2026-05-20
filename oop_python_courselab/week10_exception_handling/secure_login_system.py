def load_users(filepath="users.txt"):
    users_nbs = {}
    try:
        with open(filepath, "r") as file:
            for line_nbs in file:
                line_nbs = line_nbs.strip()
                if not line_nbs:
                    continue
                parts_nbs = line_nbs.split(",")
                if len(parts_nbs) != 2:
                    raise ValueError("Invalid user data format")
                username_nbs = parts_nbs[0].strip()
                password_nbs = parts_nbs[1].strip()
                users_nbs[username_nbs] = password_nbs
    except FileNotFoundError:
        raise
    except ValueError:
        raise
    return users_nbs


def main_nbs():
    try:
        users_nbs = load_users("users.txt")
    except FileNotFoundError:
        print("User credentials file not found.")
        return
    except ValueError as err:
        print("Error loading users:", err)
        return

    username_nbs = input("Enter username: ").strip()
    password_nbs = input("Enter password: ").strip()

    if not username_nbs or not password_nbs:
        print("Username and password cannot be empty.")
        return

    if username_nbs in users_nbs and users_nbs[username_nbs] == password_nbs:
        print("Login successful.")
    else:
        print("Login failed. Check username and password.")


if __name__ == "__main__":
    main_nbs()

#Nicole B. Sambile