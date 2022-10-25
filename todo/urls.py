from django.urls import path
from django.views import View
from todo import views

urlpatterns = [
    path('', views.todo, name='todo'),
    path('delete/<int:pk>/', views.TaskDelete, name='TaskDelete'),
    path('status/<int:pk>/', views.done, name='done'),
    path('login/', views.UserLogin, name='UserLogin'),
    path('register/', views.UserRegister, name='UserRegister'),
    path('logout/', views.UserLogout, name='UserLogout'),
]



