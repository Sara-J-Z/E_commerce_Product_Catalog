from django.db import models

# # Create your models here.
# class Product(models.Model):
#     name = models.CharField(max_length=255)
#     description = models.TextField()
#     # brand = models.ForeignKey('Brand', on_delete=models.CASCADE)
#     # category = models.ForeignKey('Category', on_delete=models.CASCADE)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     image = models.ImageField(upload_to='products/')
#     is_active = models.BooleanField(default=True)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.name