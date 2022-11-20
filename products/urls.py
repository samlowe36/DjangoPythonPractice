from django.urls import path
from . import views


urlpatterns = [         #maps root url (products) to the view function
    path("", views.index),       #don't call it here(no parentheses)
    path("new", views.new)      #starts with new instead of empty because its not the home page
]
