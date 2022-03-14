from django.urls import path
from .import views
urlpatterns =[
    path('' , views.home ,name = 'home'),
    path('about', views.about , name ='about'),
    path('donate',views.donate,name ='donate'),
    path('Contact',views.Contact , name='Contact'),
    path('success',views.success,name="success"),
    path('money',views.money ,name ='money')
]
