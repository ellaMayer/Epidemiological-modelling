import csv


class Student:
    def __init__(self, course, user):
        self.course = course
        self.user = user


class Classmates:
    def __init__(self, stud_1, stud_2):
        self.stud_1 = stud_1
        self.stud_2 = stud_2


with open('GraphData2.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    studs = list()
    cmates = list()
    for row in csv_reader:
        course = row[0]
        user = row[1]
        studs.append(Student(course, user))

checked = set()

for i in range(len(studs)):
    j = i + 1
    for j in range(len(studs) - 1):
        stud_i = studs.__getitem__(i)
        stud_j = studs.__getitem__(j + 1)
        if stud_i.course == stud_j.course and stud_i.user != stud_j.user and stud_j not in checked:
            checked.add(stud_i)
            cmates.append(Classmates(stud_i, stud_j))

cla = ""
for cmate in cmates:
    str = f"{cmate.stud_1.user},{cmate.stud_2.user} \n"
    cla += str

print(cla)