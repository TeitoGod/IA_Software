from django.urls import path
from . import views

app_name = 'tiquetera'
urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create_reserva, name='create_reserva'),
    path('create-user', views.create_user, name='create_user')

]