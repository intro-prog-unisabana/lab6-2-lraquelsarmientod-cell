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

