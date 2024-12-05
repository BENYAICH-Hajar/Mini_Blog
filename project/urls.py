from django.urls import path
from . import views 
from app_ha.views import post_list, edit_post
from django.contrib import admin


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/create/', views.create_post, name='create_post'),
    path('post/<int:hajar>/', views.post_detail, name='post_detail'),
    path('post/<int:hajar>/edit/', views.edit_post, name='edit_post'),
    path('post/<int:hajar>/add_comment/', views.add_comment, name='add_comment'),
    path('post/<int:hajar>/delete/', views.delete_post, name='delete_post'),
    path('comment/<int:hajar>/edit/', views.edit_comment, name='edit_comment'),
    path('comment/<int:hajar>/delete/', views.delete_comment, name='delete_comment'),
    path('', post_list, name='post_list'),  
    path('post/<int:hajar>/edit/', edit_post, name='edit_post'), 
    path('admin/', admin.site.urls),
]


urlpatterns = [
    path('', post_list, name='post_list'),  
    path('admin/', admin.site.urls),
]
