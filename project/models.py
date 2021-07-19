from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


REGION_CHOICES = [
    ('Chuy', 'Чуй'),
    ('Bishkek', 'Бишкек'),
    ('Issyk-Kul', 'Иссык-Куль'),
    ('Naryn', 'Нарын'),
    ('Talas', 'Талас'),
    ('Osh', 'Ош'),
    ('Batken', 'Баткен'),
    ('Jalal-Abad', 'Жалал-Абад'),
]


TYPE_CHOICES = [
    ('1', 'Альянсы для устойчивого развития'),
    ('2', 'Государственное управление, мир и безопасность'),
    ('3', 'Партнерство в сфере миграции'),
    ('4', 'Цифровизация наука, технологии и инновации'),
    ('5', 'Зеленая экономика'),
]


class Feedback(models.Model):
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=20)
    massage = models.TextField()
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.phone}'

    class Meta:
        ordering = ["-created"]
        verbose_name_plural = "Feedbacks"


class Project(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    body = RichTextUploadingField()
    gallery = RichTextUploadingField()
    start_date = models.DateField()
    completion_date = models.DateField()
    region = models.CharField(choices=REGION_CHOICES, max_length=200)
    project_number = models.IntegerField()
    is_finished = models.BooleanField(default=False)
    type = models.CharField(choices=TYPE_CHOICES, max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.completion_date)

    class Meta:
        ordering = ["-created"]
        verbose_name_plural = "Projects"


class News(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    description = models.TextField(max_length=650)
    body = RichTextUploadingField()
    gallery = RichTextUploadingField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created"]
        verbose_name_plural = "News"


class Gallery(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    body = RichTextUploadingField()
    created = models.DateTimeField(auto_now_add=True)
    is_photo = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created"]
        verbose_name_plural = "Galleries"
