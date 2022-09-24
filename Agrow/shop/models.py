from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 50)

    @staticmethod
    def get_all_categories():
        return Category.objects.all()


    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length = 50)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default = 1)
    description = models.CharField(max_length=200, default='')
    image = models.ImageField(upload_to='products/')

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category = category_id);

        else:
            return Product.get_all_products();