from django.db import models
 
# Create your models here.  
class Member(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    phone=models.CharField(max_length=30)
    password=models.CharField(max_length=12)
    date= models.DateField()
    school=models.TextField()
    year=models.CharField(max_length=4)
    
    class Meta:  
        db_table = "Member"
   
    
    def __str__(self):
        return self.name

    
    
    
   
  
    