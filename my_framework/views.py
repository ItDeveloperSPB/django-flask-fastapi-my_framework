"""Модуль, содержащий контроллеры веб-приложения"""

from components.notification import EmailNotifier, SmsNotifier, BaseSerializer
from components.test_data import add_test_data_type_course,add_test_data_student
from components.unit_of_work import UnitOfWork

from framework_kuzya.templator import render
from components.models import Engine, Logger, MapperRegistry
from components.decorators import AppRoute, Debug

logger = Logger('views')
site = Engine()
email_notifier = EmailNotifier()
sms_notifier = SmsNotifier()
UnitOfWork.new_current()
UnitOfWork.get_current().set_mapper_registry(MapperRegistry)
routes = {}

#Test_data
add_test_data_type_course(site)
# add_test_data_course(site)
add_test_data_student(site)

# Класс-контроллер - Страница "главная страница"
@AppRoute(routes=routes, url='/')
class Index:
    @Debug(name="Index")
    def __call__(self,request):
        logger.log('Вход на главную страницу')
        return '200 OK', render('schedule.html')

# Класс-контроллер - Страница "о компании"
@AppRoute(routes=routes, url='/about/')
class About:
    @Debug(name="About")
    def __call__(self,request):
        logger.log('Вход на страницу о компании')
        return '200 OK', render('about.html')

# Класс-контроллер - Страница "обратная связь"
@AppRoute(routes=routes, url='/feedback/')
class Feedback:
    @Debug(name="Feedback")
    def __call__(self,request):
        logger.log('Вход на страницу обратная связь')
        return '200 OK', render('feedback.html')


#LIST

# Класс-контроллер - Страница "Список категорий"
@AppRoute(routes=routes, url='/category-list/')
class CategoryList:
    @Debug(name="CategoryList")
    def __call__(self, request):
        logger.log('Получаем список категорий "В РАЗРАБОТКЕ"')
        return '200 OK', render('category.html',
                                objects_list=site.categories)


# Класс-контроллер - "Создание типов обучения"
@AppRoute(routes=routes, url='/type-course-list/')
class TypeCourses:
    @Debug(name="CoursesList-create-update-delete-detail")
    def __call__(self, request):
        method = request['method'].upper()
        mapper = MapperRegistry.get_current_mapper('type_course')
        if method == 'CREATE':
            logger.log('Создание типов обучения')
            data = request['data']
            name = site.decode_value(data['name'])
            mapper.insert(name)
            UnitOfWork.get_current().commit()
            return '200 OK', render('type_courses.html',
                                    objects_list=mapper.all())

        elif method == 'DELETE':
            logger.log('Удаление типов обучения')
            id = int(request['data']['id'])
            obj = mapper.find_by_id(id)
            mapper.delete(obj)
            UnitOfWork.get_current().commit()
            return '200 OK', render('type_courses.html',
                                    objects_list=mapper.all())

        elif method == 'UPDATE':
            logger.log('Обновление типов обучения')
            id = int(request['data']['id'])
            name = request['data']['name']
            obj = mapper.find_by_id(id)
            obj.name = name
            mapper.update(obj)
            return '200 OK', render('type_courses.html',
                                    objects_list=mapper.all())

        elif method == 'DETAIL':
            logger.log('Детализация типов обучения')
            id = int(request['data']['id'])
            result = mapper.find_by_id(id)
            return '200 OK', render('include/update_course_type.html',
                                    id=result.id,
                                       name=result.name)

        elif method == 'GET':
            logger.log('Список типов обучения')
            return '200 OK', render('type_courses.html',
                                    objects_list=mapper.all())


@AppRoute(routes=routes, url='/course-list/')
class Courses:
    @Debug(name="Courses-create-update-delete-detail")
    @Debug(name="TypeCoursesList")
    def __call__(self, request):
        method = request['method'].upper()
        if method == 'CREATE':
            logger.log('Создание обучения')
            name = request['data']['name']
            type_course = request['data']['type_course']
            list_type_course = []
            for i in type_course:
                list_type_course.append(site.find_type_course_by_id(int(i)))
            name = site.decode_value(name)
            new_type = site.create_course(name,list_type_course)
            # Добавляем наблюдателей на курс
            new_type.observers.append(email_notifier)

            site.courses.append(new_type)
            return '200 OK', render('courses.html',
                                    objects_list=site.courses,objects_list_type_course=site.type_courses)


        elif method == 'DELETE':
            logger.log('Удаление обучения')
            id = int(request['data']['id'])
            result = site.delete_course(id)
            return '200 OK', render('courses.html',
                                    objects_list=result)

        # elif method == 'UPDATE':
        #     logger.log('Обновление обучения')
        #     id = int(request['data']['id'])
        #     name = request['data']['name']
        #     result = site.type_course_update(id,name)
        #     return '200 OK', render('type_courses.html',
        #                             objects_list=result)
        #
        # elif method == 'DETAIL':
        #     logger.log('Детализация  обучения')
        #     id = int(request['data']['id'])
        #     result = site.type_course_detail(id)
        #     return '200 OK', render('include/update_course_type.html',
        #                             id=result.id,
        #                                name=result.name)
        else:
            logger.log('Список курсов')
            return '200 OK', render('courses.html',
                                    objects_list=site.courses,objects_list_type_course=site.type_courses)


# Класс-контроллер - Страница "Список студентов"
@AppRoute(routes=routes, url='/student-list/')
class Students:
    @Debug(name="Students-create-update-delete-detail")
    @Debug(name="StudentsList")
    def __call__(self, request):
        method = request['method'].upper()
        if method == 'CREATE':
            logger.log('Добавить ученика')
            data = request['data']
            for k,v in data.items():
                data[k] =site.decode_value(v)

            student = site.create_user('student',data)
            # Добавляем наблюдателей на курс
            student.observers.append(email_notifier)
            site.students.append(student)
            student.add_student(site)

            return '200 OK', render('students.html',
                                    objects_list=site.students,list_course=site.courses)

        elif method == 'DELETE':
            logger.log('Удаление обучения')
            id = int(request['data']['id'])
            result = site.delete_student(id)
            return '200 OK', render('students.html',
                                    objects_list=site.students,list_course=site.courses)

        # elif method == 'UPDATE':
        #     logger.log('Обновление обучения')
        #     id = int(request['data']['id'])
        #     name = request['data']['name']
        #     result = site.type_course_update(id,name)
        #     return '200 OK', render('type_courses.html',
        #                             objects_list=result)
        #
        # elif method == 'DETAIL':
        #     logger.log('Детализация  обучения')
        #     id = int(request['data']['id'])
        #     result = site.type_course_detail(id)
        #     return '200 OK', render('include/update_course_type.html',
        #                             id=result.id,
        #                                name=result.name)
        elif method == 'GET':
            logger.log('Получаем список студентов')
            return '200 OK', render('students.html',
                                    objects_list=site.students,list_course=site.courses)


# Класс-контроллер - Страница "Список учителей"
@AppRoute(routes=routes, url='/teacher-list/')
class Teachers:
    @Debug(name="Teachers-create-update-delete-detail")
    @Debug(name="TeachersList")
    def __call__(self, request):
        method = request['method'].upper()
        if method == 'CREATE':
            logger.log('Создание обучения')
            name = request['data']['name']
            type_course = request['data']['type_course']
            list_type_course = []
            for i in type_course:
                list_type_course.append(site.find_type_course_by_id(int(i)))
            name = site.decode_value(name)
            new_type = site.create_course(name,list_type_course)
            # Добавляем наблюдателей на курс
            new_type.observers.append(email_notifier)

            site.courses.append(new_type)
            return '200 OK', render('courses.html',
                                    objects_list=site.courses,objects_list_type_course=site.type_courses)


        elif method == 'DELETE':
            logger.log('Удаление обучения')
            id = int(request['data']['id'])
            result = site.delete_course(id)
            return '200 OK', render('courses.html',
                                    objects_list=result)

        # elif method == 'UPDATE':
        #     logger.log('Обновление обучения')
        #     id = int(request['data']['id'])
        #     name = request['data']['name']
        #     result = site.type_course_update(id,name)
        #     return '200 OK', render('type_courses.html',
        #                             objects_list=result)
        #
        # elif method == 'DETAIL':
        #     logger.log('Детализация  обучения')
        #     id = int(request['data']['id'])
        #     result = site.type_course_detail(id)
        #     return '200 OK', render('include/update_course_type.html',
        #                             id=result.id,
        #                                name=result.name)
        elif method == 'GET':
            logger.log('Получаем список учителей')
            return '200 OK', render('teachers.html',
                                    objects_list=site.teachers)


# контроллер 404
class NotFound404:
    @Debug(name='NotFound404')
    def __call__(self, request):
        return '404 WHAT', '404 PAGE Not Found'

#API(Доделать интерфейс) для разных api
#http://127.0.0.1:8080/api/course
@AppRoute(routes=routes, url='/api/')
class CourseApi:
    @Debug(name='CourseApi')
    def __call__(self, request):
        path = request.get('path')
        if path:
            try:
                return '200 OK', BaseSerializer(site.__dict__.get(path.split('/')[2])).save()
            except:
                return '200 OK', BaseSerializer("not").save()
        else:
            return '200 OK', BaseSerializer(site.courses).save()
