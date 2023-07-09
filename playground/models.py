from django.db import models

# Create your models here.

class Bugs(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    subject = models.CharField(max_length=500)

    def __str__(self) -> str:
        return self.title + ' ' + self.subject
