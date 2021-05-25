from django.db import models

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='Nombre',max_length=30)
    img = models.ImageField(verbose_name='Imagen')

    class Meta: 
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.name


class Business(models.Model):
    nit = models.IntegerField(primary_key=True)
    name = models.CharField(verbose_name='Nombre',max_length=30, unique=True)
    mission = models.TextField()
    vision = models.TextField()
    email = models.EmailField()
    phone = models.CharField(verbose_name='Telefono',max_length=20)
    facebook = models.CharField(max_length=60)
    instagram = models.CharField(max_length=60)  
    
    img = models.ImageField()

    category = models.ForeignKey(Category, null=False, on_delete=models.CASCADE, verbose_name='Categoria')

    class Meta: 
        verbose_name = 'Negocio'
        verbose_name_plural = 'Negocios'

    def __str__(self):
        return self.name



class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='Nombre',max_length=50, unique=True)
    desciption = models.TextField(verbose_name='Descripcion')
    price = models.FloatField(verbose_name='Precio')
    stock = models.IntegerField(verbose_name='Cantidad')

    business = models.ForeignKey(Business, null=False, on_delete=models.CASCADE, verbose_name='Negocio')

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
    name = models.CharField(max_length=10, primary_key=True,verbose_name='Nombre')
    width = models.FloatField(verbose_name='Ancho')
    deep = models.FloatField(verbose_name='Profundidad')
    aviable = models.BooleanField(verbose_name='Disponible')
    rent = models.FloatField(verbose_name='Arrendo')
    administration = models.FloatField(verbose_name='Administracion')

    business = models.ForeignKey(Business, blank=True,null=True, on_delete=models.CASCADE)

    class Meta: 
        verbose_name = 'Local'
        verbose_name_plural = 'Locales'

    def __str__(self):
        return self.name

# Create your models here.
