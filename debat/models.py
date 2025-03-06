from django.db import models

# Create your models here.

#Debate scheme

class Debate(models.Model):
    debat_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField()
    
    def __str__(self):
        return self.title


class Group(models.Model):
    group_id = models.AutoField(primary_key=True)
   

    def __str__(self):
        return self.name
    


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    surname= models.CharField(max_length=100)
    pseudo = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    