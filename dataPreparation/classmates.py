import csv


class Student:
    def __init__(self, name, course):
        self.name = name
        self.course = course


class Classmates:
    def __init__(self, stud_1, stud_2):
        self.stud_1 = stud_1
        self.stud_2 = stud_2


checked = set()

with open('someData/classmates.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    studs = list()
    for row in csv_reader:

        course = row[0]
        studs.append(course)
        line_count += 1

print(len(studs))

studs = list(set(studs))

print(len(studs))

cla = ""
for stu in studs:
    str = f"{stu} \n"
    cla += str

w = open("someData/classmates3.txt", "a")
w.write(cla)
w.close()


