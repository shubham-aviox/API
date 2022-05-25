import pandas as pd

student_file = pd.read_csv('student.csv')
student_detail_file = pd.read_csv('student_detail.csv')

student_file['Id'] = student_file['Roll Number'].astype(str) + student_file ['Phone Number'].astype(str)

s = student_file.drop_duplicates(subset=['Roll Number'])
# t = s.drop_duplicates(subset=['Phone Number'])
# df3 = pd.merge(t, student_detail_file, on = 'Roll Number')
print(student_file)