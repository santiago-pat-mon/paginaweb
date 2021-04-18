from django.db import models

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    img = models.ImageField()

    class Meta: 
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.name


class Business(models.Model):
    nit = models.IntegerField(primary_key=True)
    mission = models.TextField()
    vision = models.TextField()
    email = models.EmailField()
    facebook = models.CharField(max_length=60)
    instagram = models.CharField(max_length=60)
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=20)
    img = models.ImageField()

    category = models.ForeignKey(Category, null=False, on_delete=models.CASCADE)

    class Meta: 
        verbose_name = 'Negocio'
        verbose_name_plural = 'Negocios'

    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    desciption = models.TextField()
    price = models.FloatField()
    stock = models.IntegerField()
    img = models.ImageField()

    business = models.ForeignKey(Business, null=False, on_delete=models.CASCADE)

    class Meta: 
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.name


class Local(models.Model):
    name = models.CharField(max_length=10, primary_key=True)
    width = models.FloatField()
    deep = models.FloatField()
    aviable = models.BooleanField()
    rent = models.FloatField()
    administration = models.FloatField()

    business = models.ForeignKey(Business, null=True, on_delete=models.CASCADE)

    class Meta: 
        verbose_name = 'Local'
        verbose_name_plural = 'Locales'

    def __str__(self):
        return self.name

# Create your models here.
