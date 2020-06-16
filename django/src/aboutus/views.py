from django.shortcuts import render
from .models import AboutUs, Why_Choose_Us, Chef
# Create your views here.

def aboutus_list(request):
    about = AboutUs.objects.last()
    why = Why_Choose_Us.objects.all()
    chefs = Chef.objects.all()
    context = {
        'about': about,
        'why' : why,
        'chefs': chefs,
    }

    return render(request, 'AboutUs/about.html', context)

