def student_averages(students):
    result = {}

    for student, grades in students.items():
        avg = sum(grades.values()) / len(grades)
        result[student] = round(avg)

    return result

def assignment_averages(students):
    result = {}
    assignment_totals = {}
    assignment_counts = {}

    for grades in students.values():
        for assignment, score in grades.items():
            if assignment not in assignment_totals:
                assignment_totals[assignment] = 0
                assignment_counts[assignment] = 0

            assignment_totals[assignment] += score
            assignment_counts[assignment] += 1

    for assignment in assignment_totals:
        avg = assignment_totals[assignment] / assignment_counts[assignment]
        result[assignment] = round(avg)

    return result