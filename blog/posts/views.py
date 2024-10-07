from django.shortcuts import render,redirect
from django.conf import settings
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
 