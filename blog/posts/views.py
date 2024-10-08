from django.shortcuts import render,redirect
from django.conf import settings
from django.contrib.auth.models import User , auth
from django.contrib import messages
from .models import Blog

# Create your views here.

def blog(request):
  
  blogs = Blog.objects.all()

  return render(request , 'blog.html' , {'MEDIA_URL' : settings.MEDIA_URL , 'blogs': blogs})


def create_blog(request):

  if request.method == 'POST':

    Title = request.POST['title']
    Category = request.POST['category']
    Description = request.POST['description']

    # create a new blog instance

    blog = Blog(title = Title , category = Category , description = Description)
  
    # Save the new Blog Instance
    blog.save()
    
    # Redirect to the blog page
    return redirect('/')

  else:
    return render(request , 'create.html' , {'MEDIA_URL' : settings.MEDIA_URL})
  

def register(request):
 
 if request.method == 'POST':

  Username = request.POST['username']
  Email = request.POST['email']
  Password = request.POST['password']
  Re_password = request.POST['re-password']

  if Password == Re_password:

    if User.objects.filter(username = Username).exists():

      messages.info(request , 'Username already Exists')
      return redirect('register')
    
    elif User.objects.filter(email = Email).exists():

      messages.info(request , 'Email already registered')
      return redirect('register')
    
    else:

      user = User.objects.create_user(username=Username , email=Email ,  password=Password)

      user.save()
      messages.info(request , "User Created Successfully")

      return redirect('login')
  
  else:

    messages.info(request , ' Password does not match')
    return redirect('register')


 else:

  return render(request ,  'register.html' , {'MEDIA_URL' : settings.MEDIA_URL})

def login(request):
 
  return render(request ,   'login.html' , {'MEDIA_URL' : settings.MEDIA_URL})

 