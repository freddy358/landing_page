from django.db import models

class MainName(models.Model):
    title=models.CharField(max_length=255)
    url=models.CharField(max_length=200)

    def __str__(self):
        return self.title

class MainTitle(models.Model):
    sitename=models.CharField(max_length=255)
    mainname=models.CharField(max_length=255)
    portfolioname=models.CharField(max_length=255)
    aboutname=models.CharField(max_length=255)
    contactname=models.CharField(max_length=255)
    footername=models.CharField(max_length=255)

class Menu(models.Model):
    title=models.CharField(max_length=255)
    url=models.CharField(max_length=200)

class Main(models.Model):
    img=models.ImageField(upload_to='photos')
    description=models.CharField(max_length=255)

class Portfolio(models.Model):
    img=models.ImageField(upload_to='photos')
    title = models.CharField(max_length=255, null=True)
    description = models.CharField(max_length=255, null=True)

class About(models.Model):
    description=models.TextField()

class Contact(models.Model):
    name=models.CharField(max_length=255)
    email=models.EmailField()
    number=models.CharField(max_length=255)
    message=models.TextField()
    create_date=models.DateTimeField(auto_now_add=True, null=True, blank=True)
    def __str__(self):
        return f"{self.name}"

class Footer(models.Model):
   title = models.CharField(max_length=255)
   description = models.TextField(null=True,blank=True)

   def __str__(self):
       return f"{self.title}"


class Icon(models.Model):
   icon=models.CharField(max_length=255)
   link=models.URLField()
   section=models.ForeignKey('Footer',on_delete=models.CASCADE)


   def __str__(self):
       return f"{self.icon}"



# Create your models here.
