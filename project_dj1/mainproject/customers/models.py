from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    LIVE=1
    DElETE=0
    DELETE_CHOICES=((LIVE, 'LIVE'), (DElETE, 'DELETE'))
    name=models.CharField(max_length=200)
    address=models.TextField()
    user=models.OneToOneField(User, related_name='customer_profile', 
                              on_delete=models.CASCADE, null=True)
    phone=models.CharField(max_length=10)
    delete_status=models.IntegerField(choices=DELETE_CHOICES, default=LIVE)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateField(auto_now=True)
    
    def __str__(self) -> str:
        return self.name
    
    
        
    
    
