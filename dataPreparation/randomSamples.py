import itertools
import csv


class Student:
    def __init__(self, course, user):
        self.course = course
        self.user = user


import random

read_for = open("allData/allStudents.txt", "r")
students = [line for line in read_for.readlines()]

stringCourses = students[0]

allStudents = stringCourses.split(",")
del allStudents[-1]
print(len(allStudents))

print("länge")

sampling = random.choices(allStudents, k=1000)

print(sampling)
print(len(sampling))

allUsers = list()
allCourses = list()
allLecturers = list()

with open('belegung-ws2019-anon.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    setUser = set()
    setCourse = set()
    setLecturer = set()
    index = 0
    for row in csv_reader:
        user = row[0]
        lecturer = row[2]
        course = row[1]
        if user not in setUser:
            allUsers.append(user)
        setUser.add(user)

        if lecturer not in setLecturer:
            allLecturers.append(lecturer)
        setLecturer.add(lecturer)

        if course not in setCourse:
            allCourses.append(course)
        setCourse.add(course)

with open('courses-users.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    students = list()
    for row in csv_reader:
        course = allCourses.index(row[0])
        user = allUsers.index(row[1])
        students.append(Student(course, user))
        line_count += 1

stu = ""
print(len(students))
for entries in students:
    string = f'User{entries.user}'
    if string in sampling:
        #        stu += f'participate(Course{entries.course},User{entries.user})\n'
        stu += f'participate(Course{entries.course},User{entries.user})\n'

list = ""
for entries in sampling:
    list += f'{entries}\n'

# w = open("randomCourses.txt", "a")
# w.write(list)
# w.close()
#
# w = open("stichprobe/randomStudents.txt", "a")
# w.write(list)
# w.close()
#
w = open("stichprobe/randomParticipate3.csv", "a")
w.write(stu)
w.close()


# w = open("stichprobe/GraphData2.csv", "a")
# w.write(stu)
# w.close()
