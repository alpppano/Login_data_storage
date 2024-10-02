from django.urls import path
from . import views

app_name = 'login_data'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:data_pk>', views.detail, name='detail'),
    path('<int:data_pk>/update/', views.update, name='update'),
    path('<int:data_pk>/delete/', views.delete, name='delete'),
]
