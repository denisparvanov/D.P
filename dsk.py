
class Student:
    def __init__(self, st_name, st_yo, st_sex, st_grade, st_paralel):
        self.st_name = st_name
        self.yo = st_yo
        self.sex= st_sex
        self.grade = st_grade
        self.paralel= st_paralel
    def __repr__(self):
        return self.st_name

students = []
st_1 = Student("Denis", 18, "male", 12, "German")
students.append(st_1)
st_2 = Student("Ivan", 17, "male", 11, "Spanish")
students.append(st_2)
st_3 = Student("P", 18, "female", 12, "German")
students.append(st_3)
st_4 = Student("Roki Tenev",18, "male", 12,"Spanish")
students.append(st_4)
st_5 = Student("Sashe", 18, "male", 12, "Spanish")
students.append(st_5)

#def sort_name(students):
    #students.sort(key=lambda students:students[1])
    #print(students)
def paral(searched_paralel, students):
    for e in students:
        if e.paralel == searched_paralel:
            print(e.st_name)
def klas (searched_grade, students):
    is_here = False
    for u in students:
        if u.grade == searched_grade:
            is_here = True
            print(u.yo)
        if not is_here:
            print("Nqma takuv klas !")
def god (searched_yo,students):
    for a in students:
        if a.yo == searched_yo:
            print("The students are indeed this years old !")
            print(a.st_name)
        if searched_yo not in students:
            print("There are no students this years old !")

#sort_name(students)
paral("German",students)
klas(12,students)
god(17,students)