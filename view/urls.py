from django.urls import path

from . import views

urlpatterns = [
    path('', views.animation_showcase, name='home'),
    path('portfolio/', views.home, name='portfolio_home'),
    path('animation/', views.animation_showcase, name='animation_showcase'),
]
