from django.urls import path
from .views import get_index,pruebaDatos

urlpatterns = [
    path('prueba',pruebaDatos, name = 'indexLocales'),
    path('',get_index, name = 'indexLocales'),
    path('Detalle',DetailCategory, name='detailCategory')
]
