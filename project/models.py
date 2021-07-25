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
    message = models.TextField()
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
    start_date = models.DateField()
    completion_date = models.DateField()
    file = models.FileField(upload_to='files/', help_text='Upload your PDF file')
    region = models.CharField(choices=REGION_CHOICES, max_length=200)
    contribution = models.DecimalField(decimal_places=0, max_digits=19)
    project_url = models.CharField(max_length=100, blank=True)
    project_number = models.IntegerField()
    is_finished = models.BooleanField(default=False)
    type = models.CharField(choices=TYPE_CHOICES, max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ["-created"]
        verbose_name_plural = "Projects"


class ProjectGallery(models.Model):
    image = models.ImageField(upload_to='images/')
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.project)

    class Meta:
        ordering = ['-id']
        verbose_name_plural = 'Project Galleries'


class News(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    short_description = models.TextField(max_length=650)
    body = RichTextUploadingField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created"]
        verbose_name_plural = "News"


class NewsGallery(models.Model):
    image = models.ImageField(upload_to='images/')
    news = models.ForeignKey(News, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.news)

    class Meta:
        ordering = ['-id']
        verbose_name_plural = 'News Galleries'


class Chronology(models.Model):
    year = models.IntegerField(unique=True)
    description = models.TextField(max_length=650)

    def __str__(self):
        return str(self.year)

    class Meta:
        ordering = ['year']
        verbose_name_plural = 'Chronologies'


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


class GalleryFiles(models.Model):
    image = models.FileField(upload_to='images/', help_text='you can upload image or video')
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.gallery)

    class Meta:
        ordering = ['-id']
        verbose_name_plural = 'Gallery Files'
