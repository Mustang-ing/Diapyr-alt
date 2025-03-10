from datetime import timezone
from django.db import models

# Create your models here.



class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    surname= models.CharField(max_length=100)
    age = models.IntegerField()
    kind = models.CharField(max_length=100)
    email = models.EmailField()
    pseudo = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Group(models.Model):
    group_id = models.AutoField(primary_key=True)
    step = models.IntegerField()
    user = models.ForeignKey(User,null=True, on_delete=models.SET_NULL)
   

    def __str__(self):
        return self.name


class Debate(models.Model):

    class Debate_Kind(models.TextChoices):
        Society = 'Society'
        Politics = 'Politics'
        Science = 'Science'
        Philosophy = 'Philosophy'
        Religion = 'Religion'
        General = 'General'
        #More if you want 

    debat_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100,null=False,default="")
    creator_email = models.EmailField(null=True)
    max_per_group = models.IntegerField(null=False)
    end_date = models.DateTimeField(null=False)
    time_between_round = models.IntegerField(null=False)
    num_pass = models.IntegerField(null=False)
    step = models.IntegerField(default=1)
    description = models.TextField(default="")
    date = models.DateTimeField(default=timezone.now)
    channel_created = models.BooleanField(default=False)
    type = models.CharField(max_length=100, choices=Debate_Kind.choices,default=Debate_Kind.General)
    users = models.ManyToManyField(User)
    group = models.ForeignKey(Group, null=True, on_delete=models.SET_NULL)

    #List User ?
    # List Group ?
    def __str__(self):
        return self.title
    

""""
class Admin(User):
    debat = models.ForeignKey(Debate, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
"""


    