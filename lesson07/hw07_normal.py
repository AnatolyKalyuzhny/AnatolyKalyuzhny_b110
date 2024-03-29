# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать
# в неограниченном кол-ве классов свой определенный предмет.
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе


class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Parent(Person):
    ...


class Teacher(Person):
    def __init__(self, name, subject, classes):
        super().__init__(name)
        self.subject = subject
        self.classes = classes

        for class_item in classes:
            class_item.add_teacher(self)


class Student(Person):
    def __init__(self, name, my_class, mother, father):
        super().__init__(name)
        self.my_class = my_class
        self.mother = mother
        self.father = father

        my_class.add_student(self)


class Subject:
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title


class Class:
    """
    10 А
    """
    def __init__(self, title):
        self.title = title
        self.students = []
        self.teachers = []

    def add_student(self, student):
        self.students.append(student)

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title


class School:
    def __init__(self, name, classes):
        self.name = name
        self.classes = classes

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def get_classes(self):
        print("классы школы: ", self.classes)

    def get_students_in_class(self, class_name):
        print("Студенты школы: ")
        for class_item in self.classes:
            if class_name == class_item.title:
                print(class_item.students)

    def get_teachers_in_class(self, class_name):
        print("Список учителей: ")
        for class_item in self.classes:
            if class_name == class_item.title:
                print(class_item.teachers)

    def get_subjects_in_class(self, class_name):
        print("Список предметов: ")
        for class_item in self.classes:
            if class_name == class_item.title:
                for teacher in class_item.teachers:
                    print(teacher.subject)


first_class = Class("1 А")
second_class = Class("1 Б")

parent1 = Parent("Мистер Боб")
parent2 = Parent("Миссис Боб")
child1 = Student("Ребёнок Боб", first_class, parent1, parent2)
child2 = Student("Ребёнок Боб2", first_class, parent1, parent2)

parent3 = Parent("Мистер Банана")
parent4 = Parent("Миссис Банана")
child3 = Student("Ребёнок Банана", second_class, parent1, parent2)
child4 = Student("Ребёнок Банана2", second_class, parent1, parent2)

subject1 = Subject("Математика")
subject2 = Subject("Литература")
subject3 = Subject("Окружающий мир")

teacher1 = Teacher("Учитель Томат", subject1, [first_class, second_class])
teacher2 = Teacher("Учитель Горошек", subject2, [second_class])
teacher3 = Teacher("Учитель Репка", subject2, [first_class])
teacher4 = Teacher("Учитель Картошка", subject3, [first_class, second_class])

school = School("№ 55", [first_class, second_class])
school.get_students_in_class("1 А")
school.get_subjects_in_class("1 А")
school.get_teachers_in_class("1 А")



