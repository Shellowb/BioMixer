from django.db import models


# Create your models here.
class Doc(models.Model):
    upload = models.FileField(upload_to='recipes/')

    def __str__(self):
        return str(self.pk)

