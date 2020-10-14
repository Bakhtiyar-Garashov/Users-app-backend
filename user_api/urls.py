from django.contrib import admin
from django.urls import path,include
from .views import Users,UsersDetail


urlpatterns = [
    
    path('users',Users.as_view(),name="users"),
    path('users/<int:id>',UsersDetail.as_view(),name="users detail"),
]
