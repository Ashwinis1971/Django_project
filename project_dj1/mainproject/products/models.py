from django.db import models

# data model for order
class Product(models.Model):
    LIVE=1
    DElETE=0
    DELETE_CHOICES=((LIVE, 'LIVE'), (DElETE, 'DELETE'))
    
    title=models.CharField(max_length=100)
    price=models.FloatField()
    description=models.TextField()
    image=models.ImageField(upload_to='media/')
    priority=models.IntegerField(default=0)
    delete_status=models.IntegerField(choices=DELETE_CHOICES, default=LIVE)
    created_at=models.DateTimeField()
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        self.title
            
    