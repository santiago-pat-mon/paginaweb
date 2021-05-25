from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Posts(models.Model):
    id = models.AutoField(primary_key=True)
    create_date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Fecha de creacion')
    title = models.CharField(max_length=50,verbose_name='Titulo')
    description = RichTextField(verbose_name='Descripcion')
    img = models.ImageField(verbose_name='Imagen')

    class Meta: 
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title