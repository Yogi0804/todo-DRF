from django.db import models

# Createyour models here.


class Task(models.Model):
    title = models.CharField(max_length= 200)
    completed = models.BooleanField(default=False,blank=True,null=True)
    

    def __str__(self):
        return self.title
