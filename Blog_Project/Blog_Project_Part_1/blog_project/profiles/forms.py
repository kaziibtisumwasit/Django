from django import forms
from .models import Profile #ei app er models er vitor theke Profile class import

class ProfileForm(forms.ModelForm): #django forms theke ModelForms ta import korlam
      class Meta:# ei ProfileForm ke customized korar jonno meta class dilam
            model = Profile
            fields = '__all__' #Profile Class er all Fields ke catch korlam
