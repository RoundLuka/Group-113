import random

students = [
    "ერეკლე გაჩეჩილაძე",
    "გიგია სისაური",
    "ნერსე ლომსაძე",
    "ზაზა ჩიდრაშვილი",
    "დემეტრე ესართია",
    "ლაშა გრიგალაშვილი",
    "ლუკა ლილუაშვილი",
    "მათე მუჯირი",
    "მირიან ბოლქვაძე",
    "ლუკა თათიაშვილი",
    "მათე სამხარაძე",
    'ბესო თორღვაიძე'
]

captain1 = ["გიორგი ჩაფიძე"]
captain2 = ["სანდრო ქეშელაშვილი"]
captain3 = ["ანრი ანდღულაძე"]
captain4 = ["ანდრია ტაბატაძე"]



random.shuffle(students)


for i in range(3):
    if students: captain1.append(students.pop())
    if students: captain2.append(students.pop())
    if students: captain3.append(students.pop())
    if students: captain4.append(students.pop())

print("პირველი გუნდი " + str(captain1))
print("მეორე გუნდი " + str(captain2))
print("მესამე გუნდი " + str(captain3))
print("მეოთხე გუნდი " + str(captain4))