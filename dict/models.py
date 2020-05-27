from django.db import models

# Create your models here.

class Dictionary(models.Model):
    word = models.CharField(max_length=50)
    meaning = models.TextField(verbose_name='Definition')

    def __str__(self):
        return str(self.word)
    class Meta:
        verbose_name_plural = 'Dictionaries'
        verbose_name = 'Dictionary'