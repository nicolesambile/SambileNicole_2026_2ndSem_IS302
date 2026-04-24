def calculate_average(grade1_nbs, grade2_nbs, grade3_nbs):
    return (grade1_nbs + grade2_nbs + grade3_nbs) / 3

def get_remark(average_nbs):
    if average_nbs >= 90:
        return "Excellent"
    elif average_nbs >= 85:
        return "Very Good"
    elif average_nbs >= 80:
        return "Good"
    elif average_nbs >= 75:
        return "Fair"
    else:
        return "Failed"

# Main program
grade1_nbs = float(input("Enter grade 1: "))
grade2_nbs = float(input("Enter grade 2: "))
grade3_nbs = float(input("Enter grade 3: "))
average_nbs = calculate_average(grade1_nbs, grade2_nbs, grade3_nbs)
remark_nbs = get_remark(average_nbs)
print(f"Average: {average_nbs:.2f}")
print(f"Remark: {remark_nbs}")

#Nicole Sambile