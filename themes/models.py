from django.db import models


# Create your models here.
class Lessons(models.Model):
    lessons_title = models.CharField(max_length=255, verbose_name='Lesson title')

    def __str__(self):
        return self.lessons_title

