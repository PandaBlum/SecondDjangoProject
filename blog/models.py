from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=300)
    date = models.DateTimeField()
    text = models.TextField()
    image = models.ImageField(upload_to='event_images/')

    def get_summary(self):
        return self.text[:70]

    def __str__(self):
        '''Переименовывает созданные объекты в админ-панели в "BLOG -> Posts"'''
        return self.title
