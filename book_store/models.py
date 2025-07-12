from django.db import models

# Create your models here.
class Book(models.Model):
    slug=models.SlugField()
    name =models.CharField(" Book Name",max_length=255)
    description = models.TextField("Description")
    rate=models.DecimalField("Rate",max_digits=2, decimal_places=1, default=0.00)
    views=models.IntegerField("Views",default=0)
 
    def __str__(self):
     return f"Title {self.name}" 