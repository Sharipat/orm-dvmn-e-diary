from datacenter.models import Schoolkid, Mark, Chastisement, Lesson, Commendation
import random
from django.db import models
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

commendations = (
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
    'Теперь у тебя точно все получится!')


def get_student(schoolkid):
    try:
        return Schoolkid.objects.get(full_name__contains=schoolkid)
    except Schoolkid.DoesNotExist:
        return "Имя ученика введено с ошибкой"
    except Schoolkid.MultipleObjectsReturned:
        return "Ошибка: введено несколько учеников"


def fix_marks(schoolkid):
    return Mark.objects.filter(schoolkid=get_student(schoolkid), points__lt=4).update(points=5)


def remove_chastisements(schoolkid):
    return Chastisement.objects.filter(schoolkid=get_student(schoolkid)).delete()


def create_commendation(schoolkid, subject):
    student = get_student(schoolkid)
    year_of_study = student.year_of_study
    group_letter = student.group_letter
    lesson = Lesson.objects.filter(year_of_study=year_of_study,
                                   group_letter=group_letter, subject__title=subject).order_by('-date').first()
    text = random.choice(commendations)
    teacher = lesson.teacher
    subject = lesson.subject
    created = lesson.date
    new_compliment = Commendation.objects.create(schoolkid=student, text=text, teacher=teacher, created=created,
                                                 subject=subject)
    new_compliment.save()
    return new_compliment


def main():
    try:
        student_input = input('Введите фамилию и имя \n>')
        fix_marks(student_input)
        remove_chastisements(student_input)
        subject_input = input('Введите название предмета \n>')
        create_commendation(student_input, subject_input)
    except AttributeError:
        return "Попробуйте ввести другой предмет"


if __name__ == '__main__':
    main()
