from django.db import models

# Create your models here.
class Contents(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255,choices=(('about','about'),('slider','slider'),('article','article'),('service', 'service'),('portifolio', 'portifolio'),))
    image = models.ImageField()
    description = models.TextField()

    def  __str__(self):
        return self.title