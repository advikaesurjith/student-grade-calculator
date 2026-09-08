import tkinter as tk
from tkinter import messagebox


# --------------------------------
# Calculate Grade
# --------------------------------

def calculate_grade():
    student_name = name_entry.get().strip()

    # Check student name
    if student_name == "":
        messagebox.showerror(
            "Error",
            "Please enter the student name."
        )
        return

    total_marks = 0
    subject_count = 0

    # Read all subject marks
    for subject_entry, marks_entry in subject_entries:

        subject_name = subject_entry.get().strip()
        marks_text = marks_entry.get().strip()

        # Ignore completely empty rows
        if subject_name == "" and marks_text == "":
            continue

        # Subject name missing
        if subject_name == "":
            messagebox.showerror(
                "Error",
                "Please enter the subject name."
            )
            return

        # Marks missing
        if marks_text == "":
            messagebox.showerror(
                "Error",
                f"Please enter marks for {subject_name}."
            )
            return

        # Check whether marks are a number
        try:
            marks = float(marks_text)
        except ValueError:
            messagebox.showerror(
                "Error",
                f"Please enter a valid number for {subject_name}."
            )
            return

        # Check marks range
        if marks < 0 or marks > 100:
            messagebox.showerror(
                "Error",
                f"Marks for {subject_name} must be between 0 and 100."
            )
            return

        total_marks += marks
        subject_count += 1

    # Check if at least one subject was entered
    if subject_count == 0:
        messagebox.showerror(
            "Error",
            "Please enter at least one subject and marks."
        )
        return

    # Calculate maximum marks
    maximum_marks = subject_count * 100

    # Calculate percentage
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

    # Display results
    result_name.config(
        text=f"Student Name : {student_name}"
    )

    result_total.config(
        text=f"Total Marks : {total_marks:.2f} / {maximum_marks}"
    )

    result_percentage.config(
        text=f"Percentage : {percentage:.2f}%"
    )

    result_grade.config(
        text=f"Grade : {grade}"
    )


# --------------------------------
# Main Window
# --------------------------------

window = tk.Tk()

window.title("Student Grade Calculator")

# Increased height so the complete result is visible
window.geometry("650x820")

window.resizable(False, False)

window.configure(
    bg="#f5f7fa"
)


# --------------------------------
# Title
# --------------------------------

title = tk.Label(
    window,
    text="Student Grade Calculator",
    font=("Arial", 26, "bold"),
    bg="#f5f7fa",
    fg="#1f2937"
)

title.pack(
    pady=(15, 3)
)


subtitle = tk.Label(
    window,
    text="Enter student details and subject marks",
    font=("Arial", 11),
    bg="#f5f7fa",
    fg="#6b7280"
)

subtitle.pack(
    pady=(0, 12)
)


# --------------------------------
# Student Information
# --------------------------------

student_frame = tk.Frame(
    window,
    bg="white",
    padx=25,
    pady=18
)

student_frame.pack(
    padx=35,
    fill="x"
)


name_label = tk.Label(
    student_frame,
    text="Student Name",
    font=("Arial", 11, "bold"),
    bg="white",
    fg="#374151"
)

name_label.pack(
    anchor="w"
)


name_entry = tk.Entry(
    student_frame,
    font=("Arial", 12),
    relief="solid",
    bd=1
)

name_entry.pack(
    fill="x",
    pady=(7, 0),
    ipady=7
)


# --------------------------------
# Subjects Section
# --------------------------------

subjects_frame = tk.Frame(
    window,
    bg="white",
    padx=25,
    pady=18
)

subjects_frame.pack(
    padx=35,
    pady=8,
    fill="x"
)


subjects_title = tk.Label(
    subjects_frame,
    text="Subjects & Marks",
    font=("Arial", 15, "bold"),
    bg="white",
    fg="#1f2937"
)

subjects_title.grid(
    row=0,
    column=0,
    columnspan=2,
    sticky="w",
    pady=(0, 10)
)


# Column headings

subject_heading = tk.Label(
    subjects_frame,
    text="Subject",
    font=("Arial", 10, "bold"),
    bg="white",
    fg="#6b7280"
)

subject_heading.grid(
    row=1,
    column=0,
    sticky="w",
    padx=(0, 15),
    pady=3
)


marks_heading = tk.Label(
    subjects_frame,
    text="Marks / 100",
    font=("Arial", 10, "bold"),
    bg="white",
    fg="#6b7280"
)

marks_heading.grid(
    row=1,
    column=1,
    sticky="w",
    pady=3
)


# --------------------------------
# Subject Input Rows
# --------------------------------

subject_entries = []


for i in range(6):

    subject_entry = tk.Entry(
        subjects_frame,
        font=("Arial", 11),
        relief="solid",
        bd=1
    )

    subject_entry.grid(
        row=i + 2,
        column=0,
        sticky="ew",
        padx=(0, 15),
        pady=4,
        ipady=5
    )


    marks_entry = tk.Entry(
        subjects_frame,
        font=("Arial", 11),
        relief="solid",
        bd=1,
        width=12
    )

    marks_entry.grid(
        row=i + 2,
        column=1,
        sticky="w",
        pady=4,
        ipady=5
    )


    subject_entries.append(
        (subject_entry, marks_entry)
    )


subjects_frame.columnconfigure(
    0,
    weight=1
)


# --------------------------------
# Calculate Button
# --------------------------------

calculate_button = tk.Button(
    window,
    text="Calculate Grade",
    font=("Arial", 12, "bold"),
    bg="#2563eb",
    fg="white",
    activebackground="#1d4ed8",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    command=calculate_grade
)

calculate_button.pack(
    padx=35,
    fill="x",
    ipady=10
)


# --------------------------------
# Result Section
# --------------------------------

result_frame = tk.Frame(
    window,
    bg="white",
    padx=25,
    pady=15
)

result_frame.pack(
    padx=35,
    pady=8,
    fill="x"
)


result_title = tk.Label(
    result_frame,
    text="Result",
    font=("Arial", 16, "bold"),
    bg="white",
    fg="#1f2937"
)

result_title.pack(
    pady=(0, 8)
)


result_name = tk.Label(
    result_frame,
    text="Student Name :",
    font=("Arial", 11),
    bg="white",
    fg="#6b7280"
)

result_name.pack(
    pady=2
)


result_total = tk.Label(
    result_frame,
    text="Total Marks :",
    font=("Arial", 11),
    bg="white",
    fg="#6b7280"
)

result_total.pack(
    pady=2
)


result_percentage = tk.Label(
    result_frame,
    text="Percentage :",
    font=("Arial", 11),
    bg="white",
    fg="#6b7280"
)

result_percentage.pack(
    pady=2
)


result_grade = tk.Label(
    result_frame,
    text="Grade :",
    font=("Arial", 22, "bold"),
    bg="white",
    fg="#2563eb"
)

result_grade.pack(
    pady=(4, 0)
)


# --------------------------------
# Start Application
# --------------------------------

window.mainloop()