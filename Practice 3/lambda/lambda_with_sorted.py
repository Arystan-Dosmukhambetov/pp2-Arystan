students = [
    {"name": "Ali", "grade": 85},
    {"name": "Sara", "grade": 92},
    {"name": "Tom", "grade": 78}
]

sorted_students = sorted(students, key=lambda x: x["grade"])

print(sorted_students)
