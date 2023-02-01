"""Модуль, содержащий контроллеры веб-приложения"""
from my_framework.templator import render
from components.models import Engine
from components.decorators import AppRoute

site = Engine()
routes = {}

# Класс-контроллер - Страница "главная страница"
@AppRoute(routes=routes, url='/')
class Index:
    def __call__(self,request):
        return '200 OK', render('schedule.html')

# Класс-контроллер - Страница "о компании"
@AppRoute(routes=routes, url='/about/')
class About:
    def __call__(self,request):
        return '200 OK', render('about.html')

# Класс-контроллер - Страница "обратная связь"
@AppRoute(routes=routes, url='/feedback/')
class Feedback:
    def __call__(self,request):
        return '200 OK', render('feedback.html')


#LIST

# Класс-контроллер - Страница "Список категорий"
@AppRoute(routes=routes, url='/category-list/')
class CategoryList:

    def __call__(self, request):

        return '200 OK', render('category.html',
                                objects_list=site.categories)

# Класс-контроллер - Страница "Список учителей"
@AppRoute(routes=routes, url='/teacher-list/')
class TeachersList:

    def __call__(self, request):

        return '200 OK', render('teachers.html',
                                objects_list=site.teachers)

# Класс-контроллер - Страница "Список курсов"
@AppRoute(routes=routes, url='/course-list/')
class CoursesList:

    def __call__(self, request):

        return '200 OK', render('courses.html',
                                objects_list=site.courses)

# Класс-контроллер - Страница "Список студентов"
@AppRoute(routes=routes, url='/student-list/')
class StudentsList:

    def __call__(self, request):

        return '200 OK', render('teachers.html',
                                objects_list=site.students)

# Класс-контроллер - Страница "Список типов обучения"
@AppRoute(routes=routes, url='/type-course-list/')
class TypeCoursesList:

    def __call__(self, request):

        return '200 OK', render('type_courses.html',
                                objects_list=site.type_courses)



#CREATE


# Класс-контроллер - Страница "Список типов обучения"
@AppRoute(routes=routes, url='/type-course-create/')
class TypeCoursesCreate:

    def __call__(self, request):

        if request['method'] == 'POST':
            data = request['data']
            name = site.decode_value(data['name'])
            new_type = site.create_type_course(name)
            site.type_courses.append(new_type)
            return '200 OK', render('type_courses.html',
                                    objects_list=site.type_courses)

# Класс-контроллер - Страница "Создать категорию"
@AppRoute(routes=routes, url='/create-category/')
class CreateCategory:

    def __call__(self, request):

        if request['method'] == 'POST':
            data = request['data']
            name = site.decode_value(data['name'])
            category_id = data.get('category_id')
            category = None
            if category_id:
                category = site.find_category_by_id(int(category_id))
                category['name'] = name
                category['category'] = category
            new_category = site.create_category(name, category)
            site.categories.append(new_category)

        #     return '200 OK', render('category.html',
        #                             objects_list=site.categories)
        # else:
        #     categories = site.categories
        return '200 OK', render('category.html',
                                    categories=site.categories)

#UPDATE

#DELETE

#COPY