name_nbs = input("Enter student name: ")
course_nbs = input("Enter course: ")
with open("students.txt", "a") as file_nbs:
    file_nbs.write(name_nbs + "," + course_nbs + "\n")

print("\nStudent Records")
with open("students.txt", "r") as file_nbs:
    for line_nbs in file_nbs:
        print(line_nbs.strip())

#Nicole Sambile