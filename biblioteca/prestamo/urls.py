from django.urls import path
from . import views

app_name = 'prestamo'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:l_id>/',views.prestar,name='prestar'),
    path('<int:l_id>/pres',views.prestando,name='prestando')
]