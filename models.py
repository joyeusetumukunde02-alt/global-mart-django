from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# If later you want to extend the user:
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.user.username
class AvailableProduct(models.Model):
    av_name=models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    av_image=models.ImageField(upload_to='pictures/')
    manufactured_date=models.DateTimeField()
    likes = models.ManyToManyField(User, related_name='liked_products', blank=True)

class order(models.Model):
    your_name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.IntegerField()
    your_destination=models.CharField(max_length=200)
    av_name=models.CharField(max_length=100)
    product_price=models.IntegerField()
    image=models.ImageField(upload_to='pictures/')
    date_order=models.DateTimeField()
    def __str__(self):
        return self.name_of_product
class department(models.Model):
     dept_name=models.CharField(max_length=200)
     def __str__ (self):
         return self.dept_name
class employee(models.Model):
    fist_name=models.CharField(max_length=50)
    las_name=models.CharField(max_length=50)
    tel=models.IntegerField()
    national_id=models.IntegerField()
    email=models.EmailField((""), max_length=254)
    joinig_date=models.DateTimeField(auto_created=True)
    photos=models.ImageField(upload_to='pictures/')
    salary=models.IntegerField()
    dept_name=models.ForeignKey(department,on_delete=models.CASCADE)
    def __str__(self):
        return self.fist_name
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey('AvailableProduct', on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.user.username} - {self.text[:20]}"
class Product(models.Model):
    
    CATEGORY_CHOICES = [
        ('phone', 'Phones'),
        ('computer', 'Computers'),
        ('accessory', 'Accessories'),
    ]

    av_name = models.CharField(max_length=200)
    price = models.IntegerField()
    av_image = models.ImageField(upload_to="product_images/")
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.av_name
    



        

