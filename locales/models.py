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
    name = models.CharField(max_length=30, unique=True)
    mission = models.TextField()
    vision = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    facebook = models.CharField(max_length=60)
    instagram = models.CharField(max_length=60)  
    
    img = models.ImageField()

    category = models.ForeignKey(Category, null=False, on_delete=models.CASCADE)

    class Meta: 
        verbose_name = 'Negocio'
        verbose_name_plural = 'Negocios'

    def __str__(self):
        return self.name

# class ProductManager(Manager):
#     def create_product(self,id,name,desciption,price,stock,business):
#         product = self.create(id=id, name = business+' - '+name, desciption=desciption,price=price,stock=stock)
#         product.save()
#         return product


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)
    desciption = models.TextField()
    price = models.FloatField()
    stock = models.IntegerField()

    business = models.ForeignKey(Business, null=False, on_delete=models.CASCADE)

    # objects = ProductManager()
    class Meta: 
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name='{} - {}'.format(self.business, self.name)
        super(Product,self).save(*args,**kwargs)
        
        


class Imagen(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    img = models.ImageField()

    product = models.ForeignKey(Product,to_field='name', null=False, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Img Producto'
        verbose_name_plural = 'Imgs Producto'

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
