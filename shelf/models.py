from django.db import models
import uuid

# Create your models here.
class Book(models.Model):
    bookid =  models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    fileUrl = models.CharField(max_length=100)
    coverphoto = models.ImageField(upload_to='media/')
    author = models.CharField(max_length=150)
    category = models.CharField(max_length=50,null=True)

    def __str__(self):
        return str(self.name)
    
    def number_of_likes_per_book(self):
        return Analytic.objects.filter(bookid=self.bookid).count()
    
class Analytic(models.Model):
    bookid = models.ForeignKey(Book,on_delete=models.CASCADE)
    email = models.EmailField()

class Reader(models.Model):
    #readerid = models.AutoField()
    name = models.CharField(max_length=250)
    email = models.EmailField(primary_key=True)
    photoid = models.CharField(max_length=250)
    points = models.IntegerField(default=0,null=False)

    def __str__(self):
        return str(self.name)

class ShelfBook(models.Model):
    bookid = models.ForeignKey(Book,on_delete=models.CASCADE)
    email = models.EmailField()

class Comment(models.Model):
    comment_id = models.CharField(primary_key=True, max_length=100,db_column="Comment Id")
    bookid = models.ForeignKey(Book, on_delete=models.CASCADE)
    email = models.EmailField()
    user_name = models.CharField(max_length=250,db_column="User Name")
    message = models.CharField(max_length=250, db_column="Message")
    upvotes = models.IntegerField(default=0, db_column="Upvotes")
