from django.db import models

class News(models.Model):
    title = models.CharField(max_length=128)
    author = models.CharField(max_length=128)
    date = models.DateField()
    text = models.TextField()

    #def __str__(self):
        #return self.title