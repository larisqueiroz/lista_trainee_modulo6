from django.db import models

# Create your models here.
class Iris(models.Model):
    features= models.CharField(max_length=20)
    label= models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.features
        #return list((self.features).split(","))