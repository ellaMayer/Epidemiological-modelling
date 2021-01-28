import csv


class Lecturer:
    def __init__(self, course, lecturer):
        self.course = course
        self.lecturer = lecturer


class Student:
    def __init__(self, course, user):
        self.course = course
        self.user = user


class Classmates:
    def __init__(self, stud_1, stud_2):
        self.stud_1 = stud_1
        self.stud_2 = stud_2


class NumberStudents:
    def __init__(self, course, count):
        self.course = course
        self.count = count


class NumberLecturers:
    def __init__(self, course, count):
        self.course = course
        self.count = count


class LmuData:
    def __init__(self, user, course, lecturer):
        self.user = user
        self.course = course
        self.lecturer = lecturer


class SameLecturers:
    def __init__(self, name):
        self.name = name


class SameUser:
    def __init__(self, name):
        self.name = name


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
    print(len(allUsers))
    print(len(allLecturers))
    print(len(allCourses))
    print(allCourses[99])

# with open('belegung-ws2019-anon.csv') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     line_count = 0
#     take = list()
#     for row in csv_reader:
#         course = allCourses.index(row[1])
#         if course == 40 or course == 82 or course == 70 or course == 57:
#             user = allUsers.index(row[0])
#             lecturer = allLecturers.index(row[2])
#             take.append(LmuData(user, course, lecturer))
#             line_count += 1
# takes = ""
# for entries in take:
#     takes += f'takes(User{entries.user}, Course{entries.course}, Lecturer{entries.lecturer})\n'
#
# with open('courses-lecturers.csv') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     line_count = 0
#     lecturers = list()
#     for row in csv_reader:
#         course = allCourses.index(row[0])
#         if course == 40 or course == 82 or course == 70 or course == 57:
#             lecturer = allLecturers.index(row[1])
#             lecturers.append(Lecturer(course, lecturer))
#             line_count += 1
#
# lec = ""
# for entries in lecturers:
#     lec += f'taughtBy(Course{entries.course}, Lecturer{entries.lecturer})\n'
#
# sameLec = ""
# for i in range(len(allLecturers)):
#     sameLec += f'sameLecturer(Lecturer{i}, Lecturer{i})\n'
#
# sameStu = ""
# for i in range(len(allUsers)):
#     sameStu += f'sameStudent(User{i}, User{i})\n'
#
# with open('courses-users.csv') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     line_count = 0
#     students = list()
#     for row in csv_reader:
#         course = allCourses.index(row[0])
#         if course == 98 or course == 70:
#             user = allUsers.index(row[1])
#             students.append(Student(course, user))
#             line_count += 1
#
# stu = ""
# for entries in students:
#     stu += f'participate(Course{entries.course}, User{entries.user})\n'

checked = set()

with open('courses-users.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    studs = list()
    cmates = list()
    for row in csv_reader:
        course = allCourses.index(row[0])
        if course == 40 or course == 82 or course == 70 or course == 57:
            user = allUsers.index(row[1])
            studs.append(Student(course, user))
            line_count += 1

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
    str = f"classmates(User{cmate.stud_1.user}+User{cmate.stud_2.user}) \n"
    cla += str



# with open('courses-countStudents.csv') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     line_count = 0
#     numStu = list()
#     for row in csv_reader:
#         course = allCourses.index(row[0])
#         #  if course == 40 or course == 82 or course == 70 or course == 57:
#         count = row[1]
#         numStu.append(NumberStudents(course, count))
#         line_count += 1
#
# numStudents = ""
# for entries in numStu:
#     numStudents += f'numberParticipants(Course{entries.course}, {entries.count})\n'
#
# with open('courses-countLecturers.csv') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     line_count = 0
#     numLec = list()
#     for row in csv_reader:
#         course = allCourses.index(row[0])
#         if course == 40 or course == 82 or course == 70 or course == 57:
#             count = row[1]
#             numLec.append(NumberLecturers(course, count))
#             line_count += 1
#
# numLecturers = ""
# for entries in numLec:
#     numLecturers += f'numberLecturers(Course{entries.course}, {entries.count})\n'
#
# with open('belegung-ws2019-anon.csv') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     line_count = 0
#     allUsers = list()
#     allCourses = list()
#     allLecturers = list()
#     data = list()
#     for row in csv_reader:
#         user = row[0]
#         course = row[1]
#         lecturer = row[2]
#         data.append(LmuData(user, course, lecturer))
#         line_count += 1
#
# lmu = ""
# for entries in data:
#     lmu += f'advisedBy({entries.user}, {entries.course}, {entries.lecturer})\n'
#
# w = open("someData/courseLecturer.txt", "a")
# w.write(lec)
# w.close()
#
# w = open("someData/course98+70.txt", "a")
# w.write(stu)
# w.close()
#
# w = open("someData/numberOfStudents.txt", "a")
# w.write(numStudents)
# w.close()
#
# w = open("someData/numberOfLecturers.txt", "a")
# w.write(numLecturers)
# w.close()
#
# w = open("someData/lmuData.txt", "a")
# w.write(lmu)
# w.close()
#
# w = open("someData/sameLecturers.txt", "a")
# w.write(sameLec)
# w.close()
#
# w = open("someData/sameUsers.txt", "a")
# w.write(sameStu)
# w.close()
#
# w = open("someData/takesUserCourseLecturer.txt", "a")
# w.write(takes)
# w.close()

w = open("someData/classmates3.txt", "a")
w.write(cla)
w.close()
