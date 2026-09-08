# Student Grade Calculator

print("=================================")
print("      STUDENT GRADE CALCULATOR")
print("=================================")

# Get student name
student_name = input("Enter student name: ")

# Get number of subjects
num_subjects = int(input("Enter number of subjects: "))

total_marks = 0

# Enter marks for each subject
for i in range(num_subjects):
    subject_name = input(f"\nEnter subject {i + 1} name: ")

    while True:
        try:
            marks = float(input(f"Enter marks for {subject_name} (0-100): "))

            if 0 <= marks <= 100:
                break
            else:
                print("Marks must be between 0 and 100.")

        except ValueError:
            print("Please enter a valid number.")

    total_marks += marks


# Calculate percentage
maximum_marks = num_subjects * 100
percentage = (total_marks / maximum_marks) * 100


# Calculate grade
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"


# Display result
print("\n=================================")
print("           RESULT")
print("=================================")

print("Student Name :", student_name)
print("Total Marks  :", total_marks, "/", maximum_marks)
print("Percentage   :", round(percentage, 2), "%")
print("Grade        :", grade)

print("=================================")