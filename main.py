class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def average_grade_hw(self, grade):
        all_list_grades = []
        for course in self.grades:
            all_list_grades += self.grades[course]
        return round(sum(all_list_grades) / len(all_list_grades), 2)

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student')
            return
        return self.average_grade_hw(self.grades) < other.average_grade_hw(other.grades)

    def __str__(self):
        courses_all_prgs = ', '
        finished_crs = ', '
        res = f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: " \
              f"{self.average_grade_hw(self.grades)}\n" \
              f"Курсы в процессе изучения: {courses_all_prgs.join(self.courses_in_progress)}\n" \
              f"Завершенные курсы: {finished_crs.join(self.finished_courses)}"
        return res


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grades_lec(self, self_grades):
        all_list_grades = []
        for course in self.grades:
            all_list_grades += self.grades[course]
        return round(sum(all_list_grades) / len(all_list_grades), 2)
    def __lt__(self, other):
        if not isinstance(other, Mentor):
            print('Not a Lecturer')
            return
        return self.average_grades_lec(self.grades) < other.average_grades_lec(self.grades)

    def __str__(self):
        res = f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grades_lec(self.grades)}"
        return res


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
        res = f"Имя: {self.name}\nФамилия: {self.surname}"
        return res


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.finished_courses += ['Ведение в программирование']

any_student = Student('Nikolay', 'Smithov', 'your_gender')
any_student.courses_in_progress += ['Python_backend']
any_student.courses_in_progress += ['Python_frontend']
any_student.finished_courses += ['Ведение в программирование']

cool_reviewer = Reviewer('Mikhail', 'Svetlov')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['Python_backend']
cool_reviewer.courses_attached += ['Python_frontend']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)

cool_reviewer.rate_hw(any_student, 'Python_backend', 10)
cool_reviewer.rate_hw(any_student, 'Python_backend', 9)
cool_reviewer.rate_hw(any_student, 'Python_backend', 9)

best_lecturer = Lecturer('Ivan', 'Petrov')
best_lecturer.courses_attached += ['Python_backend']
best_lecturer.courses_attached += ['Python_frontend']

other_lecturer = Lecturer('Johann ', 'Bach')
other_lecturer.courses_attached += ['Python_backend']
other_lecturer.courses_attached += ['Python_frontend']

any_student.rate_lecture(best_lecturer, 'Python_backend', 10)
any_student.rate_lecture(best_lecturer, 'Python_backend', 10)
any_student.rate_lecture(best_lecturer, 'Python_backend', 10)

any_student.rate_lecture(best_lecturer, 'Python_frontend', 10)
any_student.rate_lecture(best_lecturer, 'Python_frontend', 10)
any_student.rate_lecture(best_lecturer, 'Python_frontend', 9)

any_student.rate_lecture(other_lecturer, 'Python_backend', 10)
any_student.rate_lecture(other_lecturer, 'Python_backend', 10)
any_student.rate_lecture(other_lecturer, 'Python_backend', 9)

any_student.rate_lecture(other_lecturer, 'Python_frontend', 10)
any_student.rate_lecture(other_lecturer, 'Python_frontend', 10)
any_student.rate_lecture(other_lecturer, 'Python_frontend', 9)

print(cool_reviewer)
print()
print(best_lecturer)
print()
print(other_lecturer)
print()
print(any_student)
print()
print(best_lecturer > other_lecturer)
print()
print(best_student < any_student)
