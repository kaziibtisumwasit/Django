from django.db import models
from categories.models import Category

from author.models import Author

# Create your models here.


class Post(models.Model):
      title=models.CharField(max_length=50)
      content=models.TextField()
      #ekti post multiple category te thakte pare 
      #multiple categories e ekti post thakte pare ,ektie bola hoi many to many field or relation
      category=models.ManyToManyField(Category)




      #A author has muntiplr posts
      #Multiple post has one author
      #That Means one to many realtion
      #In django we use ForeignKey to create one to many raltion

      #Author er account delete hole tar kora sob post delete hobe ta hole =>>on_delete=models.CASCADE
      #Author er account delete hole tar kora sob post delete hobe na & tar nam e NULL dekhabe =>>on_delete=models.SET_NULL


      author=models.ForeignKey(Author, on_delete=models.CASCADE)


      def __str__(self):
            return self.title
