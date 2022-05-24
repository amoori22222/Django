from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index.html'),

    path('service',views.service, name='service.html'),
    path('gallery', views.gallery, name='gallery.html'),
    path('contact', views.contact, name='contact.html'),
    path('about', views.about, name='about.html'),
]