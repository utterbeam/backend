from django.db import models

# Create your models here.

class details(models.Model):
    uid = models.CharField(max_length = 150 , blank = True , null = True)
    idd = models.CharField(max_length = 150 , blank = True , null = True)
    heading = models.CharField(max_length = 150 , blank = True , null = True)
    subText = models.CharField(max_length = 150 , blank = True , null = True)
    writeup = models.CharField(max_length = 1500 , blank = True , null = True)
    imageUrl = models.CharField(max_length = 200 , blank = True , null = True)
  

    def __str__(self):
        return self.idd


class author(models.Model):
    name = models.CharField(max_length = 150 , blank = True , null = True)
    heading = models.CharField(max_length = 150 , blank = True , null = True)
    imageUrl = models.CharField(max_length = 200 , blank = True , null = True)
  

    def __str__(self):
        return self.name
