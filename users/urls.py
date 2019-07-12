from django.urls import path
from .views import SignUpView
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('Publicos', views.publico, name='publico'),
    path('ComoLLegar/', views.comollegar, name='comollegar'),
    path('Estacionamiento/<int:pk>/', views.detest, name='detest'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('Estacionamiento/nuevo', views.newest, name='newest'),
    path('Arrendar/<int:pk>/edit/', views.arrendar, name='arrendar'),
]