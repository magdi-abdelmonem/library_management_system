from distutils.command.upload import upload
from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Book (models.Model):
    x=[
        ('availble','availble'),
        ('sold','sold'),
        ('rental','rental'),
    ]
    title=models.CharField(max_length=250)
    author=models.CharField(max_length=50)
    photo_book=models.ImageField(upload_to='photos',null=True,blank=True)
    photo_author=models.ImageField(upload_to='photos',null=True,blank=True)
    pages=models.IntegerField(null=True,blank=True)
    prices=models.DecimalField(max_digits=100,decimal_places=4,null=True,blank=True)
    rental_price_day=models.DecimalField(max_digits=5,decimal_places=4,null=True,blank=True)
    rental_period=models.IntegerField(null=True,blank=True)
    total_rental=models.DecimalField(max_digits=5,decimal_places=4,null=True,blank=True)
    active=models.BooleanField(default=True)
    status=models.CharField(max_length=50,choices=x,null=True,blank=True)
    category=models.ForeignKey(Category,on_delete=models.PROTECT,null=True,blank=True)
    

    def __str__(self):
        return self.title