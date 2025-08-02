from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='category_icons/', blank=True, null=True)
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='subcategories'
    )
    is_active = models.BooleanField(default=True)
    class Meta:
        verbose_name_plural = "Categories"   

    def __str__(self):
        return self.name
