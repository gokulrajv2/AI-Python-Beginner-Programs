
student_name = "Gokul"
college = "Bishop Heber College"

marks = [80, 75, 90, 85, 70]

 def display_details():
    print("\n--- STUDENT DETAILS ---")
    print("Name:", student_name)
    print("College:", college)
def display_marks():
    print("\n--- STUDENT MARKS ---")
    for mark in marks:
        print(mark)

def calculate_total():
    total = 0
    for mark in marks:
        total += mark
    return total

def calculate_average():
    total = calculate_total()
    average = total / len(marks)
    return average

def highest_mark():
    return max(marks)

def lowest_mark():
    return min(marks)

def check_result():
    average = calculate_average()

    if average >= 50:
        print("Result: PASS")
    else:
        print("Result: FAIL")

display_details()
display_marks()

print("\nTotal Marks:", calculate_total())
print("Average Marks:", calculate_average())
print("Highest Mark:", highest_mark())
print("Lowest Mark:", lowest_mark())

check_result()

print("\nProgram Completed Successfully!")
