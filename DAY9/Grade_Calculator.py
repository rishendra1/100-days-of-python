student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}
for thing in student_scores:
       a = student_scores[thing]
       if (a >= 91 and a <= 100):
         student_grades[thing] = "Outstanding"
       if (a >= 81 and a <= 90):
         student_grades[thing] = "Exceeds Expextations"
       if (a >= 71 and a <= 80):
         student_grades[thing] = "Acceptable"
       if (a <= 70):
         student_grades[thing] = "Fail"
print(student_grades)