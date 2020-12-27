# superuser = sam_hake
# password = Sa*******@**4*
from django.db import models 
from django.utils import timezone
# from django.utils.timezone.now()

# declare  model  "GeeksModel" 
class GeeksModel(models.Model):
    title = models.CharField(max_length = 200) 
    description = models.TextField()
    date_T = models.DateTimeField(verbose_name=("Right Now Date"), auto_now_add=True, null=True) 
    # default=timezone.now
    
    def __str__(self): 
        return self.title
    

class contactModel(models.Model):
    name = models.CharField(max_length=100)
    number = models.IntegerField()
    address = models.TextField()
    address2 = models.TextField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    postal_c = models.CharField(max_length=10)

    def __str__(self):
        return self.name






