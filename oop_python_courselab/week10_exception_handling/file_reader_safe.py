try:
    with open("data.txt", "r") as file:
        content_nbs = file.read()
        print(content_nbs)
except FileNotFoundError:
    print("File does not exist")
finally:
    print("Finished file read attempt.")

#Nicole B. Sambile