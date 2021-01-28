import csv


class Lecturer:
    def __init__(self, course, lecturer):
        self.course = course
        self.lecturer = lecturer


class Student:
    def __init__(self, course, user):
        self.course = course
        self.user = user


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


class SameCourse:
    def __init__(self, name):
        self.name = name


allUsers = list()
allCourses = list()
allLecturers = list()
physicalPresence = list()

oddCourses = list()
evenCourses = list()

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

with open('belegung-ws2019-anon.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    take = list()
    for row in csv_reader:
        user = allUsers.index(row[0])
        course = allCourses.index(row[1])
        lecturer = allLecturers.index(row[2])
        take.append(LmuData(user, course, lecturer))
        line_count += 1
takes = ""
for entries in take:
    takes += f'takes(User{entries.user}, Course{entries.course}, Lecturer{entries.lecturer})\n'

with open('courses-lecturers.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    lecturers = list()
    for row in csv_reader:
        course = allCourses.index(row[0])
        lecturer = allLecturers.index(row[1])
        lecturers.append(Lecturer(course, lecturer))
        line_count += 1

lec = ""
for entries in lecturers:
    lec += f'taughtBy(course{entries.course}, lecturer{entries.lecturer})\n'

sameLec = ""
for i in range(len(allLecturers)):
    sameLec += f'sameLecturer(lecturer{i}, {i})\n'

sameCourse = ""
for i in range(len(allLecturers)):
    sameCourse += f'sameCourse(Course{i}, Course{i})\n'

sameStu = ""
for i in range(len(allUsers)):
    sameStu += f'User{i},'

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
for entries in students:
    stu += f'participate(Course{entries.course},User{entries.user})\n'

# Wochenzyklen
with open('courses-users.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    students = list()
    for row in csv_reader:
        course = allCourses.index(row[0])
        user = allUsers.index(row[1])
        if course % 2 == 0:
            evenCourses.append(Student(course, user))
        if course % 2 == 1:
            oddCourses.append(Student(course, user))
        line_count += 1

odd = ""
for entries in oddCourses:
    odd += f'participate(Course{entries.course},User{entries.user})\n'

even = ""
for entries in evenCourses:
    even += f'participate(Course{entries.course},User{entries.user})\n'

# Präsenzveranstaltungen <= 100
with open('courses-countStudents.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    numStu = list()
    for row in csv_reader:
        course = allCourses.index(row[0])
        count = row[1]
        intCount = int(count)
        if intCount <= 100:
            physicalPresence.append(course)
        line_count += 1

# Präsenzveranstaltungen <= 100
with open('courses-users.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    setUser = set()
    physicalPresentStudents = list()
    physicalPresenceUsers = list()
    for row in csv_reader:
        course = allCourses.index(row[0])
        user = allUsers.index(row[1])
        if course in physicalPresence:
            if user not in setUser:
                physicalPresenceUsers.append(user)
            setUser.add(user)
            physicalPresentStudents.append(Student(course, user))
        line_count += 1

# Präsenzveranstaltungen <= 100 AND Wochenzyklen
with open('courses-users.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0

    evenPhysicalPresentStudents = list()
    oddPhysicalPresentStudents = list()
    for row in csv_reader:
        course = allCourses.index(row[0])
        user = allUsers.index(row[1])
        if course in physicalPresence:
            if course % 2 == 0:
                evenPhysicalPresentStudents.append(Student(course, user))
            if course % 2 == 1:
                oddPhysicalPresentStudents.append(Student(course, user))
        line_count += 1

oddPhyStu = ""
for entries in oddPhysicalPresentStudents:
    oddPhyStu += f'participate(Course{entries.course},User{entries.user})\n'

evenPhyStu = ""
for entries in evenPhysicalPresentStudents:
    evenPhyStu += f'participate(Course{entries.course},User{entries.user})\n'

phyUser = ""
for entries in physicalPresenceUsers:
    phyUser += f'User{entries}\n'

phyStu = ""
for entries in physicalPresentStudents:
    phyStu += f'participate(Course{entries.course},User{entries.user})\n'

numStudents = ""
for entries in numStu:
    numStudents += f'numberParticipants(course{entries.course}, {entries.count})\n'

kartCourses = ""
for entries in numStu:
    kartCourses += f'Course{entries.course},'

with open('courses-countLecturers.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    numLec = list()
    for row in csv_reader:
        course = allCourses.index(row[0])
        count = row[1]
        numLec.append(NumberLecturers(course, count))
        line_count += 1

numLecturers = ""
for entries in numLec:
    numLecturers += f'numberLecturers(course{entries.course}, {entries.count})\n'

with open('belegung-ws2019-anon.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    allUsers = list()
    allCourses = list()
    allLecturers = list()
    data = list()
    for row in csv_reader:
        user = row[0]
        course = row[1]
        lecturer = row[2]
        data.append(LmuData(user, course, lecturer))
        line_count += 1

lmu = ""
for entries in data:
    lmu += f'advisedBy({entries.user}, {entries.course}, {entries.lecturer})\n'

# w = open("allData/courseLecturer.txt", "a")
# w.write(lec)
# w.close()
#
# w = open("allData/participate.csv", "a")
# w.write(stu)
# w.close()
# #
# w = open("allData/physicalPresentStudents.txt", "a")
# w.write(phyStu)
# w.close()


# w = open("allData/odd<=100_Students.txt", "a")
# w.write(oddPhyStu)
# w.close()
#
# w = open("allData/even<=100_Students.txt", "a")
# w.write(evenPhyStu)
# w.close()

#
# w = open("allData/physicalPresentUseres.txt", "a")
# w.write(phyUser)
# w.close()
#
# w = open("allData/numberOfLecturers.txt", "a")
# w.write(numLecturers)
# w.close()
#
# w = open("allData/lmuData.txt", "a")
# w.write(takes)
# w.close()
#
# w = open("allData/sameLecturers.txt", "a")
# # w.write(sameLec)
# # w.close()

w = open("allData/sameCourse.txt", "a")
w.write(sameCourse)
w.close()
#
# w = open("allData/allStudents.txt", "a")
# w.write(sameStu)
# w.close()
#
# w = open("allData/allCourses.txt", "a")
# w.write(kartCourses)
# w.close()
#
# w = open("allData/allUsers.txt", "a")
# w.write(kartCourses)
# w.close()
