
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
            if course in lecturer.grade:
                lecturer.grade[course] += [grade]
            else:
                lecturer.grade[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашнее задание: {round(sum(int(''.join(map(str,q))) for q in self.grades.values()) / len(self.grades.values()), 2)}\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}\nЗавершенные курсы: {', '.join(self.finished_courses)}"

    def __lt__(self, other):
        if round(sum(int(''.join(map(str,q))) for q in self.grades.values()) / len(self.grades.values()), 2) < round(sum(int(''.join(map(str, q))) for q in other.grades.values()) / len(other.grades.values()), 2):
            return f'Успеваемость студента {self.name} {self.surname} ниже успеваемости студента {other.name} {other.surname}'
        else:
            return f'Успеваемость студента {self.name} {self.surname} выше успеваемости студента {other.name} {other.surname}'



class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grade = {}



class Lecturer(Mentor):
    grades = {}

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {round(sum(int(''.join(map(str,q))) for q in self.grade.values()) / len(self.grade.values()), 2)}"

    def __lt__(self, other):
        if round(round(sum(int(''.join(map(str,q))) for q in self.grade.values()) / len(self.grade.values()), 2)) < round(sum(int(''.join(map(str,q))) for q in other.grade.values()) / len(other.grade.values()), 2):
            return f'Средняя оценка лектора {self.name} {self.surname} ниже средней оценки лектора {other.name} {other.surname}'
        else:
            return f'Средняя оценка лектора {self.name} {self.surname} выше средней оценки лектора {other.name} {other.surname}'



class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


student_1 = Student('Ruoy', 'Eman', 'your_gender')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['Git']

student_2 = Student('Alex', 'Nell', 'your_gender')
student_2.courses_in_progress += ['Git']
student_2.courses_in_progress += ['Java']

reviewer_1 = Reviewer('Nick', 'Lots')
reviewer_1.courses_attached += ['Python']
reviewer_1.courses_attached += ['Git']

reviewer_2 = Reviewer('Mike', 'Kors')
reviewer_2.courses_attached += ['Git']
reviewer_2.courses_attached += ['Java']

reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Git', 10)

reviewer_2.rate_hw(student_2, 'Java', 9)
reviewer_2.rate_hw(student_2, 'Git', 9)

Lecturer_1 = Lecturer('Nick', 'Lots')
Lecturer_1.courses_attached += ['Python']
Lecturer_1.courses_attached += ['Git']

Lecturer_2 = Lecturer('Mike', 'Kors')
Lecturer_2.courses_attached += ['Git']
Lecturer_2.courses_attached += ['Java']

student_1.rate_lecturer(Lecturer_1,'Python', 10 )
student_1.rate_lecturer(Lecturer_1,'Git', 10)

student_2.rate_lecturer(Lecturer_2,'Java', 9 )
student_2.rate_lecturer(Lecturer_2, 'Git', 9)

print(student_1)
print(student_2)
print(Lecturer_1)
print(Lecturer_2)

print(student_1.__lt__(student_2))
print(student_2.__lt__(student_1))
print(Lecturer_1.__lt__(Lecturer_2))
print(Lecturer_2.__lt__(Lecturer_1))

list_students = [student_1, student_2]


def avg_student_grade(list, course_1):
    student_grade =[]
    for student in list:
        for course, grade in student.grades.items():
            if course == course_1:
                student_grade.append(int(''.join(map(str, grade))))
    return f'Средняя оценка студентов на курсе {course_1} составляет {round (sum (student_grade) / len(student_grade), 2)}'


print(avg_student_grade(list_students, 'Git'))
print(avg_student_grade(list_students, 'Java'))
print(avg_student_grade(list_students, 'Python'))

list_lecturer = [Lecturer_1, Lecturer_2]

def avg_lecturer_grade(list, course_2):
    lecturer_grade =[]
    for lecturer in list:
        for course, grade in lecturer.grades.items():
            if course == course_2:
                for g in grade:
                    lecturer_grade.append(g)
    return f'Средняя оценка лекторов на курсе {course_2} составляет {round (sum (lecturer_grade) / len(lecturer_grade), 2)}'

print(avg_lecturer_grade(list_lecturer, 'Git'))
print(avg_lecturer_grade(list_lecturer, 'Java'))
print(avg_lecturer_grade(list_lecturer, 'Python'))





