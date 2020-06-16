from django.db import models

# Create your models here.
class AboutUs(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(upload_to='about_us/')

    class Meta:
        verbose_name = 'About Us'
        verbose_name_plural = 'About Us'

    def __str__(self):
        return self.title


class Why_Choose_Us(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Why Choose Us'
        verbose_name_plural = 'Why Choose Us'


class Chef(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    bio = models.TextField()
    image = models.ImageField(upload_to='chef/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Chef'
        verbose_name_plural = 'Chef'
