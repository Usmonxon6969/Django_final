from django.urls import path
from mysite.views import index

urlpatterns = [
    path('', index, name='index')
]
