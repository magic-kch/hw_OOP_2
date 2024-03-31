class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lector) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    def sr_grade(self):
        sum_ = 0
        count = 0
        for v in self.grades.values():
            try:
                sum_ += sum(v)
                count += len(v)
            except:
                sum_ += v
                count += 1
        return sum_ / count

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {self.sr_grade():.2f}\n'
                f'Курсы в процессе изучения: {",".join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {",".join(self.finished_courses)}')

    def __lt__(self, other):
        if not isinstance(other, Student):
            return print('Такого студента нет')
        return self.sr_grade() < other.sr_grade()

    def __eq__(self, other):
        if not isinstance(other, Student):
            return print('Такого студента нет')
        return self.sr_grade() == other.sr_grade()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lector(Mentor):
    def __init__(self,name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def sr_grade(self):
        sum_ = 0
        count = 0
        for v in self.grades.values():
            try:
                sum_ += sum(v)
                count += len(v)
            except:
                sum_ += v
                count += 1
        return sum_ / count

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {self.sr_grade():.2f}')

    def __lt__(self, other):
        if not isinstance(other, Lector):
            return print('Такого лектора нет')
        return self.sr_grade() < other.sr_grade()

    def __eq__(self, other):
        if not isinstance(other, Lector):
            return print('Такого лектора нет')
        return self.sr_grade() == other.sr_grade()


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
        return f'Имя: {self.name}\nФамилия: {self.surname}'

def all_sr_grade_students(students: list, course: str):
        sum_ = 0
        count = 0
        for student in students:
            if course in student.grades:
                sum_ += student.sr_grade()
                count += 1
        return sum_ / count

def all_sr_grade_lectors(lectors: list, course: str):
    sum_ = 0
    count = 0
    for lector in lectors:
        if course in lector.grades:
            sum_ += lector.sr_grade()
            count += 1
    return sum_ / count

an_old_lecturer = Lector("Tony", "Stark")
an_old_lecturer.courses_attached += ['Python']

newby_lecturer = Lector("Steve", "Rogers")
newby_lecturer.courses_attached += ['Git']

best_student = Student('Peter', 'Parker', 'spider')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']

student_2 = Student('Mary', 'Jane', 'girl')
student_2.courses_in_progress += ['Git']
student_2.courses_in_progress += ['Python']

best_student.rate_lecturer(an_old_lecturer, 'Python', 10)
best_student.rate_lecturer(an_old_lecturer, 'Python', 10)
best_student.rate_lecturer(an_old_lecturer, 'Python', 5)
best_student.rate_lecturer(an_old_lecturer, 'Git', 5)

student_2.rate_lecturer(newby_lecturer, 'Git', 10)
student_2.rate_lecturer(newby_lecturer, 'Git', 1)
student_2.rate_lecturer(newby_lecturer, 'Git', 3)
student_2.rate_lecturer(newby_lecturer, 'Python', 10)

cool_mentor = Reviewer('Jarvis', 'Robot')
cool_mentor.courses_attached += ['Python']

big_boss_mentor = Reviewer('Big', 'Boss')
big_boss_mentor.courses_attached += ['Git']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 7)
cool_mentor.rate_hw(best_student, 'Python', 10)

big_boss_mentor.rate_hw(student_2, 'Git', 10)
big_boss_mentor.rate_hw(student_2, 'Git', 10)
big_boss_mentor.rate_hw(student_2, 'Git', 10)
big_boss_mentor.rate_hw(student_2, 'Git', 4)
big_boss_mentor.rate_hw(student_2, 'Git', 7)
big_boss_mentor.rate_hw(student_2, 'Git', 5)

print(best_student.grades, best_student.name, best_student.surname)
print(an_old_lecturer.grades, an_old_lecturer.name, an_old_lecturer.surname)
print(cool_mentor)
print(an_old_lecturer)
print(best_student)
print(newby_lecturer)

print(newby_lecturer < an_old_lecturer)
print(best_student < student_2)

print(f"Средняя оценка за домашние задания по всем студентам на курсе Python: {all_sr_grade_students([best_student, student_2], 'Python'):.2f}")
print(f"Средняя оценка за домашние задания по всем студентам на курсе Git: {all_sr_grade_students([best_student, student_2], 'Git'):.2f}")
print(f"Средняя оценка за лекции всех лекторов на курсе Git: {all_sr_grade_lectors([an_old_lecturer, newby_lecturer], 'Git'):.2f}")
print(f"Средняя оценка за лекции всех лекторов на курсе Python: {all_sr_grade_lectors([an_old_lecturer, newby_lecturer], 'Python'):.2f}")