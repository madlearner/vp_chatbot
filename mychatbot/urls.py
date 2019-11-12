from django.urls import path
from . import views

urlpatterns = [
	path('', views.first_function, name= 'first_function'),
	path('slack/', views.slack, name= 'slack')
]