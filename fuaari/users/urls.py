from django.urls import path
from . import views

urlpatterns = [
    path('',views.user,name='home'),
    path('form/',views.create_user,name='create'),
    path('read/',views.user_list,name='read'),
    path('update/<int:pk>',views.edit_user,name='update'),
    path('delete/<int:pk>',views.delete_user,name='delete'),
]
