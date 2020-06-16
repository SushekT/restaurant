from django.shortcuts import render
from meals.models import Meals, Category
from blog.models import Post
from aboutus.models import Why_Choose_Us

# Create your views here.
def home(request):
    meal_list = Meals.objects.all()
    categories = Category.objects.all()
    posts = Post.objects.all()[1:3]
    latest_post = Post.objects.last()
    why = Why_Choose_Us.objects.all()
    context = {
        'meal_list': meal_list,
        'categories' : categories,

        'posts': posts,
        'latest_post': latest_post,
        'why': why
    }

    return render(request, 'home/index.html', context)
