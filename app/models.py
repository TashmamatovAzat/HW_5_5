from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование курса')
    duration = models.CharField(max_length=30, verbose_name='Продолжительность курса')
    student = models.ForeignKey('Student', on_delete=models.CASCADE, verbose_name='Студент')
    mentor = models.ForeignKey('Mentor', on_delete=models.CASCADE, verbose_name='Ментор')

    def __str__(self):
        return self.name


class Student(models.Model):
    fullname = models.CharField(max_length=100, verbose_name='ФИО студента')
    birth_date = models.DateField(verbose_name='Дата рождения студента')

    def __str__(self):
        return self.fullname


class Mentor(models.Model):
    fullname = models.CharField(max_length=100, verbose_name='ФИО ментора')
    experience = models.CharField(max_length=20, verbose_name='Опыт работы')

    def __str__(self):
        return self.fullname
