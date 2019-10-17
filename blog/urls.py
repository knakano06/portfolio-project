
from django.urls import path

from . import views

urlpatterns = [
    path('', views.allblogs, name = 'allblogs'),

    # look for an int after /blog and save that as the blog id
    # this will look at detail function in view.py and pass in the blog_id
    path('<int:blog_id>/', views.detail, name = 'detail'),
]
