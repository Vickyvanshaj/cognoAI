from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static   
from django.conf import settings
from . import views
urlpatterns = [
   path('', views.post_list, name='post_list'),
   path('post/<int:pk>/',views.post_detail,name='post_detail'),
   path('post/new/', views.post_new, name='post_new'),
   path('post/<int:pk>/edit', views.post_edit, name='post_edit'),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)