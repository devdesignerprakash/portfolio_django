from django.db import models
from django.contrib.auth.models import User

class Skill(models.Model):
      name=models.CharField(max_length=100)
      proficiency=models.IntegerField(help_text="Proficiency out of 100")
      def __str__(self):
            return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=100, blank=True)
    phone=models.CharField(max_length=60, blank=True)
    linkedin = models.URLField(blank=True)
    website=models.URLField(blank=True)
    github = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    city=models.CharField(max_length=50,blank=True)
    insta=models.URLField(blank=True)
    def __str__(self):
        return self.user.username
    


class Education(models.Model):
     type=models.CharField(max_length=50,blank=True)
     profile=models.OneToOneField(Profile, on_delete=models.CASCADE,related_name='education' )


class ContactInquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Inquiry from {self.name}"
    
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', null=True, blank=True)
    url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title




# Create your models here.
