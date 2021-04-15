from datacenter.models import Schoolkid, Mark, Chastisement, Lesson, Commendation, Subject
import random
from django.core.exceptions import ObjectDoesNotExist

#Функция для имени ученика
def our_student(schoolkid):
    try:
        student = Schoolkid.objects.get(full_name__contains=schoolkid)
        return student
    except ObjectDoesNotExist:
        return ('Ошибка ввода')


#Переменная с именем ученика
student = our_student(schoolkid)

#Функция исправления оценок, где schoolkid - 'Фамилия Имя' ученика#

def fix_marks(schoolkid):
    marks = Mark.objects.filter(schoolkid=student, points__lt=4).update(points=5)
    return marks

#Функция удаления замечаний, где schoolkid - 'Фамилия Имя' ученика#

def remove_chastisements(schoolkid):
    chastisements = Chastisement.objects.filter(schoolkid=student)
    chastisements.delete()
    return chastisements #показывает пустой список, означающий, что замечаний больше нет

#Список, из которого в случайном порядке берется похвала для ученика#

commendations = [
'Молодец!',
'Отлично!',
'Хорошо!',
'Гораздо лучше, чем я ожидал!',
'Ты меня приятно удивил!',
'Великолепно!',
'Прекрасно!',
'Ты меня очень обрадовал!',
'Именно этого я давно ждал от тебя!',
'Сказано здорово – просто и ясно!',
'Ты, как всегда, точен!',
'Очень хороший ответ!',
'Талантливо!',
'Ты сегодня прыгнул выше головы!',
'Я поражен!',
'Уже существенно лучше!',
'Потрясающе!',
'Замечательно!',
'Прекрасное начало!'
'Так держать!',
'Ты на верном пути!',
'Здорово!',
'Это как раз то, что нужно!',
'Я тобой горжусь!',
'С каждым разом у тебя получается всё лучше!',
'Мы с тобой не зря поработали!',
'Я вижу, как ты стараешься!',
'Ты растешь над собой!',
'Ты многое сделал, я это вижу!',
'Теперь у тебя точно все получится!']


#Функция добавления похвалы, где schoolkid - 'Фамилия Имя' ученика, а subject - 'Предмет'#

def create_commendation(schoolkid, subject):
    #Переменная some_lesson находит требуемый предмет по литере класса, году начала обучения ученика и названию предмета#
    try:
        some_lesson = Lesson.objects.filter(year_of_study = student.year_of_study, group_letter = student.group_letter,
                                        subject__title = subject).order_by('-date').first()
        print(some_lesson)
    except AttributeError:
        return ("Попробуйте ввести другой предмет")
    new_compliment = Commendation.objects.create(schoolkid=student, text=random.choice(commendations), teacher=some_lesson.teacher, subject=some_lesson.subject, created=some_lesson.date )
    new_compliment.save()
    return new_compliment


