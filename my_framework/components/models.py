import quopri


# Класс-Абстрактный пользователь
class User:
    pass


# Класс-Преподаватель
class Teacher(User):
    pass


# Класс-Студент
class Student(User):
    pass


# Класс-Фабрика пользователей
class UserFactory:
    types = {
        'student': Student,
        'teacher': Teacher
    }

    @classmethod
    def create(cls, type_):
        return cls.types[type_]()

    # @classmethod
    # def get(cls, type_):
    #     return cls.types[type_]()
    #
    # @classmethod
    # def delete(cls, type_):
    #     return cls.types[type_]()
    #
    # @classmethod
    # def update(cls, type_):
    #     return cls.types[type_]()


# Класс-Курс
class Course:

    def __init__(self, name,course_type):
        self.name = name
        self.type = course_type
        # self.category.courses.append(self)

# Класс-Тип курсов курсов
class CourseType:
    auto_id = 0
    def __init__(self, name):
        self.name = name
        self.id = CourseType.auto_id
        CourseType.auto_id += 1

# Класс-Интерактивный курс
class InteractiveCourse(Course):
    pass


# Класс-Курс в записи
class RecordCourse(Course):
    pass


# Класс-Фабрика курсов
class CourseFactory:
    types = {
        'interactive': InteractiveCourse,
        'record': RecordCourse
    }

    @classmethod
    def create(cls, type_, name, category):
        return cls.types[type_](name, category)


# Класс-Категория
class Category:

    auto_id = 0

    def __init__(self, name, category):
        self.id = Category.auto_id
        Category.auto_id += 1
        self.name = name
        self.category = category
        self.courses = []
        self.teachers = []

    def course_count(self):
        result = len(self.courses)
        if self.category:
            result += self.category.course_count()
        return result


# Класс-Основной интерфейс проекта
class Engine:
    def __init__(self):
        self.teachers = []
        self.students = []
        self.courses = []
        self.categories = []
        self.type_courses = []

    @staticmethod
    def create_type_course(name):
        return CourseType(name)

    @staticmethod
    def create_user(type_):
        return UserFactory.create(type_)

    @staticmethod
    def create_category(name, category=None):
        return Category(name, category)

    def find_category_by_id(self, id):
        for item in self.categories:
            print('item', item.id)
            if item.id == id:
                return item
        raise Exception(f'Нет категории с id = {id}')

    @staticmethod
    def create_course(type_, name,category):
        return CourseFactory.create(type_, name,category)

    @staticmethod
    def create_course_with_type(type_, name,category):
        return CourseFactory.create(type_, name,category)

    def get_course(self, name):
        for item in self.courses:
            if item.name == name:
                return item
        return None

    @staticmethod
    def decode_value(val):
        val_b = bytes(val.replace('%', '=').replace("+", " "), 'UTF-8')
        val_decode_str = quopri.decodestring(val_b)
        return val_decode_str.decode('UTF-8')