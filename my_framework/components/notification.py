import jsonpickle
# from simba_framework.templator import render


# поведенческий паттерн - наблюдатель
# Курс



class Observer:

    def update(self, subject):
        pass


class Subject:
    #
    # def __init__(self):
    #     self.observers = []

    def notify_student(self,site):
        text = 'Вы присоеденились к курсу'
        for item in self.observers:
            item.update(self, text,site,'student')

    def notify_teacher(self, observer):
        text = 'К вам присоединился студент'
        for item in observer:
            item.update(self, text)


class SmsNotifier(Observer):

    def update(self, subject):
        print('SMS->', 'к нам присоединился',)


class EmailNotifier(Observer):

    def update(self, subject, text,site,type_data):
        if type_data =='student':
            for course in subject.course:
                print(f'EMAIL->{text}', site.find_course_by_id(int(course)).name)
        else:
            pass

class BaseSerializer:

    def __init__(self, obj):
        self.obj = obj

    def save(self):
        return jsonpickle.dumps(self.obj)

    @staticmethod
    def load(data):
        return jsonpickle.loads(data)

# поведенческий паттерн - Стратегия
class ConsoleWriter:

    def write(self, text):
        print(text)


#
#
class FileWriter:

    def __init__(self, file_name):
        self.file_name = file_name

    def write(self, text):
        with open(self.file_name, 'a', encoding='utf-8') as f:
            f.write(f'{text}\n')
