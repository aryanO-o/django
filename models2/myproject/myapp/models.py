from django.db import models

# Create your models here.

class MenuCategory(models.Model):
    menu_category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.menu_category_name

class Menu(models.Model):
    menu_item = models.CharField(max_length=100)
    price = models.IntegerField(null=False)
    category_id = models.ForeignKey(MenuCategory, on_delete=models.PROTECT, default=None, related_name='category_name')

    def __str__(self):
        return self.menu_item + ' ' + str(self.price) + ' ' + str(self.category_id)