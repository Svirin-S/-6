class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def average_rating(self):
        count = 0
        number_of_ratings = []
        for key in self.grades:
            for evaluations in self.grades[key]:
                count += evaluations
                number_of_ratings.append(evaluations)
        return count / len(number_of_ratings)

    def grading(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.courses_attached:
                lecturer.courses_attached[course] += [grade]
            else:
                lecturer.courses_attached[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        some_student = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_rating()}' \
                       f'\nКурсы в процессе изучения: {",".join(self.courses_in_progress)}\nЗавершенные курсы: {",".join(self.finished_courses)}'
        return(some_student)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.received_estimates = {}

    def average_rating(self):
        count = 0
        number_of_ratings = []
        for key in self.received_estimates:
            for evaluations in self.received_estimates[key]:
                count += evaluations
                number_of_ratings.append(evaluations)
        return count / len(number_of_ratings)

    def __str__(self):
        some_student = f'Имя: {self.name}\nФамилия: {self.surname}\n{self.average_rating()} '
        return some_student


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
        some_student = f'Имя: {self.name}\nФамилия: {self.surname}'
        return some_student


student1 = Student('Max', 'Petrov', 'M')
student1.courses_in_progress += ['Payton']

cool_mentor = Reviewer('Petr', 'Sidorov')
cool_mentor.courses_attached += ['Payton']

cool_mentor.rate_hw (student1, 'Payton', 4)
cool_mentor.rate_hw (student1, 'Payton', 7)

lecturer1 = Lecturer('Serge', 'Petrov')
lecturer1.courses_attached += ['Payton']

student1.grading(lecturer1, 'Payton', 7)



print (student1)
print()
print(cool_mentor)
print()
print(lecturer1)






