from django.urls import path
from .import views


app_name = 'tasks'

urlpatterns = [
    path('list/', views.tasks_list, name='list'),
    path('create/', views.tasks_create, name='create'),
    path('detail/<int:pk>/', views.tasks_detail, name='detail'),
    path('update/<int:pk>/', views.tasks_update, name='update'),
    path('delete/<int:pk>/', views.tasks_delete, name='delete'),
]