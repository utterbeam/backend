from django.db import models

# Create your models here.
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver



class keywords(models.Model):
    name = models.CharField(max_length = 150 , blank = True , null = True)
    
    def __str__(self):
        return self.name

class Author_detail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.CharField(max_length = 350 , blank = True , null = True)
    image = models.FileField(blank=True)
    image_url = models.CharField(max_length = 200 , blank = True , null = True)
    author_id = models.AutoField(primary_key=True)
    twitter = models.CharField(max_length = 150 , blank = True , null = True)
    facebook = models.CharField(max_length = 150 , blank = True , null = True)
    instagram = models.CharField(max_length = 150 , blank = True , null = True)
    pinterest = models.CharField(max_length = 150 , blank = True , null = True)
    blogs = models.CharField(max_length = 250 , blank = True , null = True)
    url = models.CharField(max_length = 150 , blank = True , null = True)
    fb_id = models.CharField(max_length = 150 , blank = True , null = True)
    keywords_selected = models.ManyToManyField(keywords , null = True)


    def __str__(self):
        return self.user.username   



class employer_work(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='employer')
    keywords_selected = models.ManyToManyField(keywords , null = True)
    assigned_writer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='writer' ,null = True)
    work_description = models.CharField(max_length = 150 , blank = True , null = True)


    def __str__(self):
        return self.user.username 



@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Author_detail.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.author_detail.save()



class write_up(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.CharField(max_length = 150 , blank = True , null = True)
    post_id = models.AutoField(primary_key=True)
    heading = models.CharField(max_length = 150 , blank = True , null = True)
    sub_text = models.CharField(max_length = 150 , blank = True , null = True)
    writeup = models.CharField(max_length = 1500 , blank = True , null = True)
    image_url = models.CharField(max_length = 200 , blank = True , null = True)
    upvotes = models.IntegerField(blank = True , null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    sentiment_positive = models.CharField(max_length = 200 , blank = True , null = True)
    sentiment_negative = models.CharField(max_length = 200 , blank = True , null = True)
    sentiment_neutral = models.CharField(max_length = 200 , blank = True , null = True)
    plagiarism = models.CharField(max_length = 200 , blank = True , null = True)
    keywords_selected = models.ManyToManyField(keywords , null = True)

    # author = models.ForeignKey(Author_detail, on_delete=models.CASCADE)
    def __str__(self):
        return self.url


