import os
import re
import csv


class IllStudent:
    def __init__(self, user, percent):
        self.user = user


users = list()
infUsers = list()

with open('samples/coronaKi/<=100/physicalPresentUseres.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        users.append(row[0])

participants = ""

with open('samples/coronaKi/evidencePresent.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        participants += f'{row[0]}, {row[1]}\n'

infectedStudents = {}
for i in range(1, 18):
    infectedStudents[i] = list()

resistantStudents = {}
for i in range(1, 18):
    resistantStudents[i] = list()

# infectedStudents.append(IllStudent("User2569", 1.0))
# resistantStudents.append(IllStudent("User2569", 1.0))

setResistant = set()
aktWeek = 1
evidenceRes = ""
setUsers = set()

# commandLine = f'java -jar tuffy.jar -marginal -i samples/coronaKi/prog.mln -e samples/coronaKi/evidencePresent.csv ' \
#     f'-queryFile samples/coronaKi/query.db -r samples/coronaKi/output/Week1.txt '
# os.system(commandLine)

for i in range(1, 18):

    entries = list()
    getFile = f'samples/coronaKi/outputMap/Week{aktWeek}.txt'
    file = open(getFile, "r")

    for line in file:
        str = f'{line}'
        str = str.replace("\"", " ")
        str = str.replace("(", " ")
        chunks = str.split('\t')
        chunks = chunks[0].split()
        state = chunks[0]
        user = chunks[1]
        if state == "infectious":
            if user not in resistantStudents[aktWeek]:
                infectedStudents[aktWeek].append(user)
            resistantStudents[aktWeek + 1].append(user)
        if state == "resistant":
            resistantStudents[aktWeek].append(user)

    # index = 0
    # for row in entries:
    #     percent = float(row.percent.replace(",", "."))
    #     infectedStudents[aktWeek].append(IllStudent(row.user, percent))
    #     print(infectedStudents[aktWeek])
    #     index += 1

    evidenceInf = ""

    for row in infectedStudents[aktWeek]:
        evidenceInf += f'\nisInfectious({row})'

    for row in resistantStudents[aktWeek]:
        if row not in setResistant:
            evidenceRes += f'\nresistant({row})'
        setResistant.add(row)

    # for row in users:
    #         if row not in setUsers:
    #             evidenceInf += f'\n0.0 isInfectious({row})'
    #         evidenceRes += f'\n0.0 resistant({row})'

    w = open("samples/coronaKi/evidence.db", "a")

    w.write(participants)
    w.write(evidenceInf)
    w.write(evidenceRes)
    w.close()

    aktWeek += 1
    commandLine = f'java -jar tuffy.jar -i samples/coronaKi/prog.mln -e samples/coronaKi/evidence.db ' \
        f'-queryFile samples/coronaKi/query.db -r samples/coronaKi/outputMap/Week{aktWeek}.txt '
    os.system(commandLine)

    os.remove("samples/coronaKi/evidence.db")
