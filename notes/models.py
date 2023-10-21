from django.db import models

# Create your models here.


class Note(models.Model):    
    title=models.CharField(max_length=50,null=False,default="your_default_value_here" )
    content=models.TextField(default="your_default_value_here")
    
    def __str__(self):
        return self.title
    
    