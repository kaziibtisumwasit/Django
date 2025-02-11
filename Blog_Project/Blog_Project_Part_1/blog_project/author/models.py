from django.db import models

# Create your models here.

class Author(models.Model):
      name=models.CharField(max_length=100)#charField dile max_length must be dite hobe
      bio=models.TextField()
      phone_no=models.CharField(max_length=14)


      def __str__(self):
            return self.name
      #class teke je author ta create hoise ota object nam de dekhabe
      #oi object je nam e create hoise oi nam e dehate hole __str__ use korte hobe
      #__str__ is a builtin dundar method of python
