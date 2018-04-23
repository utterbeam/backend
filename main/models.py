from django.db import models

# Create your models here.



class Author_detail(models.Model):
    name = models.CharField(max_length = 150 , blank = True , null = True)
    description = models.CharField(max_length = 350 , blank = True , null = True)
    image_url = models.CharField(max_length = 200 , blank = True , null = True)
    author_id = models.AutoField(primary_key=True)
    twitter = models.CharField(max_length = 150 , blank = True , null = True)
    facebook = models.CharField(max_length = 150 , blank = True , null = True)
    instagram = models.CharField(max_length = 150 , blank = True , null = True)
    pinterest = models.CharField(max_length = 150 , blank = True , null = True)
    blogs = models.CharField(max_length = 250 , blank = True , null = True)
    url = models.CharField(max_length = 150 , blank = True , null = True)
    fb_id = models.CharField(max_length = 150 , blank = True , null = True)


    def __str__(self):
        return self.url    


class write_up(models.Model):
    url = models.CharField(max_length = 150 , blank = True , null = True)
    post_id = models.AutoField(primary_key=True)
    heading = models.CharField(max_length = 150 , blank = True , null = True)
    sub_text = models.CharField(max_length = 150 , blank = True , null = True)
    writeup = models.CharField(max_length = 1500 , blank = True , null = True)
    image_url = models.CharField(max_length = 200 , blank = True , null = True)
    upvotes = models.IntegerField(blank = True , null = True)
    # author = models.ForeignKey(Author_detail, on_delete=models.CASCADE)

    def __str__(self):
        return self.url

