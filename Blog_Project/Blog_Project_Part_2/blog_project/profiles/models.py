from django.db import models
from author.models import Author
# Create your models here.

class Profile(models.Model):
      name=models.CharField(max_length=50)
      about=models.TextField()
      author=models.OneToOneField(Author,on_delete=models.CASCADE, default=None)
      #on_delete mane holo author author ti delete kore dile ki hobe ta = er pore bole dite hobe
      #.models.CASCADE mane holo delete hole 

      #author ta migration er pore add korechi tai migration aber kkorte hobe ei app er upor
      #alada kore migration korte gele migration hobe na.default e value set kore dite hobe.
      #tai default value noone set kore dilam
      #py manage.py magrate profiles ---> profiles app ta migrate hobe
      #py manage.py migrate Profiles


      def __str__(self):
            return self.name
      #object jokhon create hobe oi object er nam ja enter korbe oi nam ei dekhabe
      

      

