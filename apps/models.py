from django.contrib.auth.models import User
from django.db.models import Model, TextField, ForeignKey, CASCADE
from django.forms import CharField, IntegerField, ImageField
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Category(MPTTModel):
    name = CharField(max_length=50)
    parent = TreeForeignKey('self', CASCADE, null=True, blank=True, related_name='children')

    class Meta:
        verbose_name = 'Ketagoriya'
        verbose_name_plural = 'Ketagoriyalar'

    def __str__(self):
        return self.name
    class MPTTMeta:
        order_insertion_by = ['name']


class Product(Model):
    name = CharField(max_length=255)
    price = IntegerField()
    description = TextField(blank=True)
    features = TextField(blank=True)
    image = ImageField()
    category = ForeignKey(Category, CASCADE)
    owner = ForeignKey(User, CASCADE)

    def __str__(self):
        return self.name


# class ProductImage(Model):
#     image = ImageField(upload_to='images/products')
#     product = ForeignKey('Product', on_delete=CASCADE)
