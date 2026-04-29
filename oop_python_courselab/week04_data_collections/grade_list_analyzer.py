grades_nbs = []

for i in range(5):
    grade = float(input(f"Enter grade {i + 1}: "))
    grades_nbs.append(grade)

average_grade_nbs = sum(grades_nbs) / len(grades_nbs)
print(f"\nAverage Grade: {average_grade_nbs:.1f}")
print("Highest Grade:", max(grades_nbs))
print("Lowest Grade:", min(grades_nbs))

#Nicole B. Sambile