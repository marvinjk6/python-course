
def assign_grade(mark):
  grade = ""
  if mark >= 90:
    grade = "A"
  elif mark >= 80:
    grade = "B"
  elif mark >= 70:
    grade = "C"
  elif mark >= 60:
    grade = "D"
  elif mark >= 50:
    grade = "E"
  else:
    grade = "F"
  return grade

print(assign_grade(89))