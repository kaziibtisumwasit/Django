from django import forms 
from .models import Author ##ei folder er models.py er moddhe theke Author Class ke import korlam



class AuthorForm(forms.ModelForm):   #froms theke ModelForm ke inherite korlam
      class Meta:                 #Jokhon ekti class er extra charactaristic ba extra attribute add korte chai tkhon oi class er moddhe meta class add korte hoi
            #AuthorFrom class er extra attribute ba carectersitic add korar jonno meta class add korechi
            model=Author #models.py file theke Author ke import kore ansilam ota model variable e store korlam
            fields='__all__' #Author class er sob fields use korte chaile __all__ use korte hoi
            ##jodi specific fields nite chai fields=['name','bio'] #list er modde oi field er nam dite hobe
            ##jodi specific fields or field chara baki sob fields nite chai exclude=['name'] #name chara baki sob fields ashbe
