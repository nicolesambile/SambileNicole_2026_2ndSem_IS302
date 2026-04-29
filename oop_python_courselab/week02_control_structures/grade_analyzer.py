name_nbs = input("Enter student name: ")
grade1_nbs = float(input("Enter grade 1: "))
grade2_nbs = float(input("Enter grade 2: "))
grade3_nbs = float(input("Enter grade 3: "))
average_nbs = (grade1_nbs + grade2_nbs + grade3_nbs) / 3
print(f"Average: {average_nbs:.2f}")
if average_nbs >= 90:
    remark = "Excellent"
elif average_nbs >= 85:
    remark = "Very Good"
elif average_nbs >= 80:
    remark = "Good"
elif average_nbs >= 75:
    remark = "Fair"
else:
    remark = "Failed"
print(f"Remark: {remark}")

#Nicole B. Sambile