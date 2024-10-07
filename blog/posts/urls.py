from django.urls import path 
from . import views

urlpatterns = [
  path('' , views.blog , name = 'blog' ) , # '' - blank means home url
  path('create-blog' , views.create_blog , name =  'create-blog')
]