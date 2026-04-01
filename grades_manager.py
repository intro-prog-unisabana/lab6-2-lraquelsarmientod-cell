def initialize_dict(student_name, subject_grades):
    return {student_name: subject_grades}

def add_student(student_grades={}):
    name = input("Enter student name: ").title()

    subjects = {}

    while True:
        entry = input("Enter subject and grade (or 'exit' to finish): ")

        if entry.lower() == "exit":
            break

        subject, grade = entry.split(",")
        subject = subject.title()
        grade = float(grade)

        subjects[subject] = grade

    student_grades[name] = subjects
    print(f"Student {name} successfully added to the grades management system.")
    return student_grades

def get_students(student_grades, keys):
    result = {}

    for key in keys:
        found = False

        for student in student_grades:
            if student.lower() == key.lower():
                result[student] = student_grades[student]
                found = True
                break

        if not found:
            print(f"{key.title()} not found!")
    return result

def avg_by_student(student_grades, keys=None):
    # Si no hay keys → todos
    if keys is None:
        selected = student_grades
    else:
        selected = get_students(student_grades, keys)

    for student, grades in selected.items():
        avg = sum(grades.values()) / len(grades)
        print(f"{student}: {round(avg, 1)}")