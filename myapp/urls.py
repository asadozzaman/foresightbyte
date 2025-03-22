# flake8: noqa
# Basic Lib Import

from django.urls import include, path
from myapp.views import front


# Routing Implement
urlpatterns = [
        path('', front, name='front'),
    
    
]


