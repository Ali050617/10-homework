from django.urls import path
from .import views


app_name = 'notes'


urlpatterns = [
    path('list/', views.notes_list, name='list'),
    path('create/', views.notes_create, name='create'),
    path('detail/<int:pk>/', views.notes_detail, name='detail'),
    path('update/<int:pk>/', views.notes_update, name='update'),
    path('delete/<int:pk>/', views.notes_delete, name='delete'),

]
