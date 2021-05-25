from django.contrib import admin
from .models import Posts
from import_export import resources
from import_export.admin import ImportExportModelAdmin

######################## Resources class for add import and export botton###########################
class CategoryResources(resources.ModelResource):
    class Meta:
        model = Posts

####################################################################################################


##################### Admins class for configure somethings in the django admin ###################
class PostAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['title','create_date']
    list_display = ['id','title','description','img']
####################################################################################################

############## Registers models in the admin ###########################
admin.site.register(Posts,PostAdmin)
# Register your models here.
