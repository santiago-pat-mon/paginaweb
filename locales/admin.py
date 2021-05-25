from django.contrib import admin

from .models import Category,Business,Product,Local,Imagen
from import_export import resources
from import_export.admin import ImportExportModelAdmin

######################## Resources class for add import and export botton###########################
class CategoryResources(resources.ModelResource):
    class Meta:
        model = Category


class BussinesResources(resources.ModelResource):
    class Meta:
        model = Business

class ProductResources(resources.ModelResource):
    class Meta:
        model = Product


class LocalResources(resources.ModelResource):
    class Meta:
        model = Local

####################################################################################################

##################### Admins class for configure somethings in the django admin ###################
class CategoryAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name','img',]
    resource_class = CategoryResources


class BussinesAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['name','nit','phone']
    list_display = ['nit','name','phone','category']
    resource_class = BussinesResources

class ProductAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['id','name','bussines']
    list_display = ['name','desciption','price','stock','business']
    resource_class = ProductResources

class LocalAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['name','aviable']
    list_display = ['name','width','deep','aviable','rent','administration']


####################################################################################################

############## Registers models in the admin ###########################

admin.site.register(Category, CategoryAdmin)
admin.site.register(Business, BussinesAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Local, LocalAdmin)
admin.site.register(Imagen)
