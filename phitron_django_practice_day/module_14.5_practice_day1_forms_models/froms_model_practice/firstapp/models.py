from django.db import models
import datetime
# Create your models here.


class Studentmodel(models.Model):
      name=models.CharField(max_length=20)#charField is store string value in this field
      intiger_field= models.IntegerField()#Store Integer value
      address= models.TextField(blank=True)
      #autofield use korle must be auto field ke primary key dite hobe
      #ekti model e sudhu matro ekti auto field use kora jabe
      auto_field= models.AutoField(primary_key=True) # automaticly increase Integer value
      # big_auto_field = models.BigAutoField() # automaticly increase Big Integer value
      # Binary_field = models.BinaryField() # it's use for store raw binary data such as image of others files.not showding on admin.programmatically store raw data
      Boolean_field = models.BooleanField(default=False) # Which is store True or False data in this field
      # commaSeparatedIntegerField =  models.CharField(validators=[comma_separated_validator] , max_length= 255)
      date_field= models.DateField(default = datetime.datetime.today) # take only date
      DateTimeField = models.DateTimeField(default = datetime.datetime.now) #take data with time
      DecimalField= models.DecimalField(max_digits=5 ,  decimal_places= 3,default = 00) # max_digit = 5 mane holo decimal value soho total 5 ta digit
      #decimal_place =>> doshomik er pore 3 ta digit ba shonkha thakbe    .ex: 12.534
      duration_field = models.DurationField(blank = True , null = True) # this field store time duration like 1:55:44.....
      Email = models.EmailField(verbose_name = "Enter your email address ",default='example@gmail.com') #verbose is work like label 
      file_field = models.FileField(upload_to='upload_files/')  # Upload or save file into DB ..it's Create a upload_fiels folder in project folder & store uploded files in this folder
      Choose_a_fiel_file_path_field = models.FilePathField(path='media/') #Shows Files from DB from media folder which is in project files globally ..Shows on dropdown menu
      float_field = models.FloatField(default=0.00)
      #foreign__key = models.ForeignKey(with_other_model_which_is_connected_with_this , on_delete = models.CASCADE)
      GeniricIPAddress = models.GenericIPAddressField(null=True,blank=True) #This field store IP address IPv4 & IPv6 #If don't give any value in this field then it will be null & blank.
      image_field = models.ImageField(upload_to = 'Uploaded_image/',blank=True,null =True) #Must install pillow in your VENV..ImageField are optimized for uploading image
      
      #when  makemigratons & migrate a model some field need defalut value ... put some default in those field
      #If you dont want put default value on those field then  set blank = True & null = True .This can accept Empty those filed
      
      
      json_field = models.JSONField(blank=True , null = True) #Store JSON File Or JSON-encoded data
      
      BIO = models.TextField() 
      #many_to_many_field = models.ManyToManyField(this_model_calss name_which_is_connected_with_this)
      #one_to_one_field =  models.OneToOneField(name_that_class_which_is_connected_with_this_one_to_one,on_delete = models.CASCADE)
      #on_delete = Models.CASCADE => mean delete this model_will_be deleted when the connected model will be delete
      #If user delete his account then automaticly delete his post
      #this class is for post so ondelete cascase will be use on this post model
      positive_integer_field = models.PositiveIntegerField(default=00)
      big_positive_integerField= models.PositiveBigIntegerField(default = 00)
      positive_small_integer = models.PositiveSmallIntegerField(default = 00)
      store_urls = models.SlugField(unique=True , blank= True) # this field store URLS
      '''
      # urls.py
      path('post/<slug:slug>/', views.blog_detail, name='blog_detail')
      
      
      Then the URL could look like ==> :http://example.com/post/my-first-post/
      '''
      small_integer_field = models.SmallIntegerField() #this field store Small integer value
      time_field = models.TimeField() # store time value in this field. 
      url_field = models.URLField(default='youtube.com') # store url like : https://djangoproject.com/meet
      UUID_field = models.UUIDField() #this field create Universel Unique ID for this model
      
      #UUID Is content 32 Hexadecimal character which is 0-9 , a-z & seraprated by hypen -
      
      
      
      
      
      
      
      def __str__(self):
            return f"Name : {self.name}"