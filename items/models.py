from django.db import models
from django.contrib.auth.models import User
class Catagories(models.Model):
    name=models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = 'Catagories'

class Item(models.Model):
    catagories=models.ForeignKey(Catagories,related_name="items" , on_delete=models.CASCADE)
    name=models.CharField(max_length=150)
    description=models.TextField(blank=True, null=True)
    price=models.FloatField()
    # slug=models.SlugField()
    image=models.ImageField(upload_to="item_images" , null=True, blank=True)
    sold_out=models.BooleanField(default=False)
    created_by=models.ForeignKey(User, related_name="items" , on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
    class Meta:
        verbose_name_plural = 'Items'