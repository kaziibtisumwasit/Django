from django import forms
import datetime # This built in module help to get rightnow date & time

class StudentForms(forms.Form):
      #field_name = forms.FieldType(**option) ##syntax
      name=forms.CharField(max_length=20,label="Enter Your Name")
      age= forms.IntegerField(widget=forms.NumberInput,label="Enter Your Age")
      bio=forms.CharField(widget=forms.Textarea(attrs={'rows' : 5}),label="Tell US About Your Self")
      #attrs={'rows' : field er Hight koto hobe ta define kore dewa}
      Email= forms.EmailField(required=False) #Required by default true kora thake ,false kore dilam tar mane email na diye form submit kora jabe,Email na dile email field e kono error dibe na
      conditions = forms.BooleanField(label="Are You Agreed with this terms & conditions? ")
      date=forms.DateField(label="Menual Date")
      Date = forms.DateField(widget=forms.DateInput(attrs={'type' : 'date'}))
      DateTime = forms.DateTimeField(widget=forms.DateTimeInput(attrs= {'type' : 'datetime-local'}))
      year_choose = ['1999' , '2000' , '2001' , '2003']
      years_range=list(range(1990 ,2081)) #list banlam jar moddhe 1990 theke 2080 porjonto ache
      choose_year=forms.DateField(widget=forms.SelectDateWidget(years=year_choose)) 
      
      dropdown_date_year = forms.DateField(widget=forms.SelectDateWidget(years = years_range))
      
      balance=forms.DecimalField(label="Enter Your Balance")
      
      
      first_name=forms.CharField(initial="My First name") # Ei field e kono data na dile initialy My First name ta thakbe
      
      
      day = forms.DateField(initial= datetime.date.today) # Built in date time import kore initilly ajker date boshiye dilam
      right_Now_date_time=forms.DateTimeField(initial=datetime.datetime.now) #datetime.datetime.now is give rightnow date & time
      right_now_time= forms.TimeField(initial=datetime.datetime.now().time)
      
      
      right_now_on12clock = forms.TimeField(initial = datetime.datetime.now().time,input_formats=['%I:%M:%s %p'],widget=forms.TimeInput(format='%I:%M:%S %p'))
      #Time Input er jonno TimeField
      #datetime theke datetime er moddhe theke now(),now() =>now() function work for get rightNow Date & Time
      #now Function Theke only time ta nilam ... now().time
      
      
      choose_option=[('blue' , 'Blue' ),('black' , 'Black') ,('white' , 'White')]
      # tupple in list
      #choose_option=[('backend_value' , 'Frontend_shows')]
      choose_a_color_from_dropdown=forms.ChoiceField(choices= choose_option)
      choose_option_by_radio_selection= forms.ChoiceField(widget=forms.RadioSelect,choices = choose_option)
      choose_multiple_option= forms.MultipleChoiceField(choices= choose_option )
      multiple_choice_field_by_CheckBox= forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices= choose_option)
      roll_number= forms.IntegerField(help_text="Enter Your 2 digits Roll Number " , max_value= 99) # 99 er beshi value input dewa jabe na.
      Normal_password = forms.CharField(widget=forms.PasswordInput,error_messages={'required' : "Must Enter a Password"})