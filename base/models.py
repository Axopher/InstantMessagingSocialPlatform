from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# this is where we are gonna configure our database

class User(AbstractUser):
    name = models.CharField(max_length=200,null=True)
    email = models.EmailField(unique=True,null=True)
    bio = models.TextField(null=True)

    avatar = models.ImageField(null=True,default="avatar.svg")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Room(models.Model):
    host = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    topic = models.ForeignKey(Topic,on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    # null = False is by default and it doesn't allow to have instance of class so that's why null=true which means null value is allowed
    # blank = True it means when we submit out form it can be blank
    participants = models.ManyToManyField(User, related_name='participants', blank=True)
    updated = models.DateTimeField(auto_now=True)
    # every time save method is called timestamp for that moment is generated
    created = models.DateTimeField(auto_now_add=True)
    # unlike auto_now , auto_now_add takes timestamp at the beginning when this instance was created


    # we can specify ordering where new items added on the database is displayed first in order i.e  latest room created
    class Meta:
        # ordering = ['updated','created'] for ascending order
        ordering = ['-updated','-created']

    def __str__(self):
        return self.name

class Message(models.Model):
    # user can have many messages but messages can only have one user 
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    # to establish relationship with the Room we use ForeignKey(Room)
    room = models.ForeignKey(Room,on_delete=models.CASCADE)
    body = models.TextField()
    # we are gonna force the user to write the message TextField(true)
    update=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)

    class Meta:
        # ordering = ['updated','created'] for ascending order
        ordering = ['-update','-created']

    def __str__(self):
        return self.body[0:50]
        # all we want is 50 characters so [0:50]



