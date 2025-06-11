from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CustomUserCreationForm, PostForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login  
from django.contrib.auth.decorators import login_required
from .utils import optimize_image
from .models import CustomUser, Post
from django.contrib.auth.decorators import login_required



def index(request):
    return render(request, 'index.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def user_login(request):  
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)  
            return redirect('polls:index')
        else:
            messages.error(request, 'Невірний логін або пароль')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                user = form.save(commit=False)
                user.email = form.cleaned_data['email']
                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']
                if 'image' in request.FILES:
                    optimized_image, new_name = optimize_image(request.FILES['image'], max_size=(300, 300))
                    user.image_small.save(new_name, optimized_image, save=False)
                    optimized_image, new_name = optimize_image(request.FILES['image'], max_size=(600, 600))
                    user.image_medium.save(new_name, optimized_image, save=False)
                    optimized_image, new_name = optimize_image(request.FILES['image'], max_size=(1200, 1200))
                    user.image_large.save(new_name, optimized_image, save=False)
                user.save()
                return redirect('polls:index')
            except Exception as e:
                messages.error(request, f'Помилка при реєстрації: {str(e)}')
        else:
            messages.error(request, 'Виправте помилки в формі')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def users(request):
    users = CustomUser.objects.all()
    return render(request, 'users.html', {'users': users})

def post_list(request):
    posts = Post.objects.select_related('author').order_by('-created_at')
    return render(request, 'posts/post_list.html', {'posts': posts})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            
            if 'image' in request.FILES:
                optimized_image, new_name = optimize_image(request.FILES['image'], max_size=(1200, 1200))
                post.image.save(new_name, optimized_image, save=False)
            
            post.save()
            return redirect('polls:post_list')
    else:
        form = PostForm()
   
    return render(request, 'posts/create_post.html', {'form': form})
