from django.db import models

# Create your models here.
class Epmloyee(models.Model):
    name= models.CharField(max_length=50)
    title= models.CharField(max_length=50)
    salary=models.IntegerField()
    team=models.ForeignKey("TeamLeader",on_delete=models.CASCADE,blank=True, null=True)
    
    def __str__(self):
        return self.name
    
class TeamLeader(models.Model):
    name=models.CharField(max_length=15,primary_key=True)
    manger=models.ForeignKey(Epmloyee,on_delete=models.PROTECT)

    def __str__(self):
        return self.name