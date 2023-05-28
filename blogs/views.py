from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from blogs.models import Post, Category, Like
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .forms import AddPostForm


# Create your views here.
def home(request):
    posts = Post.objects.order_by('-post_created_at')
    top_posts = Post.objects.order_by('-likes')[:6]
    category = Category.objects.all()
    data = {
        'posts' : posts,
        'top_posts' : top_posts,
        'category' : category
    }
    return render(request, 'blogs/home.html', data)


def post(request, url):
    post = Post.objects.get(post_url = url)
    # print(post)
    total_likes = post.likes.count()
    post_data = {
        'post' : post,
        'total_likes' : total_likes,
    }
    return render(request, 'blogs/posts.html', post_data)


def category(request, url):
    category = Category.objects.get(cat_url = url)
    # print(post)
    posts = Post.objects.filter(category_name = category)
    data = {
        'posts' : posts,
        'category' : category
    }
    return render(request, 'blogs/category.html', data)


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('blogs:home')
        else:
            messages.error(request, "Invalid username or password")
            # messages.error(request, 'User does not exist.')
    return render(request, 'blogs/login.html', {})

def user_signup(request):
    if request.method == 'POST': 
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email_id = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            try:
                # Check if email is already associated with another user
                if User.objects.filter(email=email_id).exists():
                    messages.error(request, "Email is already associated with another user. Please use a different email.")
                else:
                    # Check if user with the same username already exists
                    if User.objects.filter(username=username).exists():
                        messages.error(request, "Username is already taken. Please choose a different one.")
                    else:
                        user = User.objects.create_user(username=username, password=password, email=email_id)
                        user.first_name = first_name
                        user.last_name = last_name
                        user.save()
                        messages.success(request, "Signup successful! You can now log in.")
                        return redirect('blogs:login')  
            except:
                messages.error(request, "An error occurred during signup. Please try again.")
        else:
            messages.error(request, "Password does not match")
    return render(request, 'blogs/signup.html', {})


def user_logout(request):
    logout(request)
    return redirect('blogs:home')

@login_required
def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
    
    # post.likes.add(request.user)
    return redirect('blogs:post', url = post.post_url)


@login_required
def add_post(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # Assuming you have an author field in your Post model
            post.save()
            return redirect('blogs:home')
    else:
        form = AddPostForm()
    data = {
        'form': form,
    }
    return render(request, 'blogs/addPost.html', data)


def about(request):
    return render(request, 'blogs/about.html', {})