from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('service/',views.service,name='service'),
    path('portfolio/',views.portfolio,name='portfolio'),
    path('blog/',views.blog,name='blog'),
    path('single_blog/',views.single_blog,name='single_blog'),
    path('contact/',views.contact,name='contact'),
    path('element/',views.element,name='element'),
]
