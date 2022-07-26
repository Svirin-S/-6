class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        student_list.append(self.grades)

    def average_rating(self):
        count = 0
        number_of_ratings = []
        for key in self.grades:
            for evaluations in self.grades[key]:
                count += evaluations
                number_of_ratings.append(evaluations)
                result = count / len(number_of_ratings)
                students[self.name] = result
        return result

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Не студент')
            return
        return self.average_rating() < other.average_rating()

    def grading(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.received_estimates:
                lecturer.received_estimates[course] += [grade]
            else:
                lecturer.received_estimates[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        some_student = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {round(self.average_rating(), 1)}' \
                       f'\nКурсы в процессе изучения: {",".join(self.courses_in_progress)}' \
                       f'\nЗавершенные курсы: {",".join(self.finished_courses)}'
        return (some_student)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.received_estimates = {}
        lecturers_list.append(self.received_estimates)

    def average_rating(self):
        count = 0
        number_of_ratings = []
        for key in self.received_estimates:
            for evaluations in self.received_estimates[key]:
                count += evaluations
                number_of_ratings.append(evaluations)
                result = count / len(number_of_ratings)
                lecturers[self.name] = result
            return result

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Не лектор!')
            return
        return self.average_rating() < other.average_rating()

    def __str__(self):
        some_student = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_rating()}'
        return some_student


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
                cours.append(course)
            else:
                student.grades[course] = [grade]
                cours.append(course)
        else:
            return 'Ошибка'

    def __str__(self):
        some_student = f'Имя: {self.name}\nФамилия: {self.surname}'
        return some_student


student_list = []
students = {}
cours = []
lecturers_list = []
lecturers = {}


def best(dictionary):
    count = 0
    name = None
    for key in dictionary:
        if dictionary[key] > count:
            count += dictionary[key]
            name = key
    if dictionary == students:
        return f"Лучший студент '{name}' у него самая высокая средняя оценка"
    else:
        return f"Лучший преподователь '{name}' у него самая высокая средняя оценка"


def course_average(list_):
    sum_of_grades = {}
    rating_list = {}
    grades = {}
    for key in list_:
        for key_and_value in list(key.items()):
            if key_and_value[0] in sum_of_grades:
                rating_list[key_and_value[0]] += key_and_value[1]
            else:
                rating_list[key_and_value[0]] = key_and_value[1]
            for k in key_and_value[1]:
                if key_and_value[0] in sum_of_grades:
                    sum_of_grades[key_and_value[0]] += k
                else:
                    sum_of_grades[key_and_value[0]] = k
    grades = list(sum_of_grades.values())
    list_len_grades = []
    for key_and_value in rating_list.items():
        list_len_grades.append(len(key_and_value[1]))
        res = [q / u for q, u in zip(grades, list_len_grades)]
        for f in res:
            average_rating = f
        if list_ == student_list:
            print(f'Средняя оценка на курсе {key_and_value[0]} среди студентов - {round(average_rating, 1)}')
        else:
            print(f'Средняя оценка на курсе {key_and_value[0]} среди лекторов - {round(average_rating, 1)}')

student1 = Student('Max', 'Petrov', 'M')
student2 = Student('Иван', 'Сидоров', 'M')

student1.courses_in_progress += ['Payton']
student1.courses_in_progress += ['C++']

student2.courses_in_progress += ['Payton']
student2.courses_in_progress += ['C++']
student1.finished_courses += ['Git']
student2.finished_courses += ['Git']

mentor1 = Reviewer('Petr', 'Sidorov')
mentor2 = Reviewer('Кирилл', 'Антипов')

mentor1.courses_attached += ['Payton']
mentor1.courses_attached += ['C++']
mentor2.courses_attached += ['Payton']

mentor1.rate_hw(student1, 'Payton', 4)
mentor1.rate_hw(student1, 'C++', 5)
mentor1.rate_hw(student1, 'C++', 8)
mentor1.rate_hw(student1, 'Payton', 7)
mentor1.rate_hw(student2, 'C++', 7)

mentor2.rate_hw(student2, 'Payton', 9)
mentor2.rate_hw(student2, 'Payton', 7)

lecturer1 = Lecturer('Serge', 'Petrov')
lecturer2 = Lecturer('Сергей', 'Павлов')

lecturer1.courses_attached += ['Payton']
lecturer2.courses_attached += ['Payton']

student1.grading(lecturer1, 'Payton', 3)
student1.grading(lecturer1, 'Payton', 7)

student1.grading(lecturer2, 'Payton', 7)
student2.grading(lecturer2, 'Payton', 5)
print(student1 > student2)
print(lecturer1)
print()
print(lecturer2)
print()
print(student1)
print()
print(student2)
print()
print(mentor1)
print()
print(mentor2)
print()
print(best(students))
print(best(lecturers))
print()
print(student1 > student2)
print()
print(lecturer1 > lecturer2)
print()
course_average(student_list)
print()
course_average(lecturers_list)