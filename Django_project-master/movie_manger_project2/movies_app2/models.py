from django.db import models

# Create your models here.
class CensorInfo(models.Model):
    rating = models.CharField(max_length=10, null=True)
    ceritified_by = models.CharField(max_length=200, null=True)
    
    
class Director(models.Model):
    name=models.CharField(max_length=300)
    def __str__(self) -> str:
        return self.name
    

class MovieInfo(models.Model):
    title = models.CharField(max_length=250)
    year = models.IntegerField(null=True)
    description = models.TextField()
    cursor_details = models.OneToOneField(CensorInfo,
                                          on_delete=models.SET_NULL,
                                          related_name='movie', null=True)
    directed_by = models.ForeignKey(Director, 
                                    on_delete=models.CASCADE,
                                    related_name='directed_movie', null=True)
    def __str__(self) -> str:
        return self.title

    