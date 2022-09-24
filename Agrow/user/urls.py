from django.urls import path
from django.contrib.auth import views as auth_views 
from . import views

urlpatterns = [
    path('', views.home,name='agro-home'),
    path('about/', views.about,name='agro-about'),
    path('blog/', views.blog,name='agro-blog'),
    path('info/', views.info,name='agro-info'),
    path('contact/', views.contact,name='agro-contact'),
]