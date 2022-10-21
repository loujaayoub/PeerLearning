from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator

class Skill(models.Model):
        skill_name = models.CharField(max_length=200)
        def __str__(self):
            return self.skill_name

class Education(models.Model):
        education_level = models.CharField(max_length=200)
        
        def __str__(self):
            return self.education_level

class User(AbstractUser):
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    user_image = models.ImageField(upload_to='user_images/',default="avatar.jpg")
    education = models.ForeignKey(Education,on_delete=models.CASCADE, null=True)
    birth_date = models.DateField(null=True)
    gender = models.BooleanField(default=True)
    engagement_score = models.IntegerField(default=0,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ])

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


class UserSkills(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     skill = models.ForeignKey(Skill,on_delete=models.CASCADE)
     score = models.IntegerField(default=0)



