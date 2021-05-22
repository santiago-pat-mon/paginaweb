from django.db import models

# Create your models here.

class Posts(models.Model):
    id = models.AutoField(primary_key=True)
    create_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    title = models.CharField(max_length=50)
    description = models.TextField()
    img = models.ImageField()

    class Meta: 
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title