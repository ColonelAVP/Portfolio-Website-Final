from django.shortcuts import render
from .models import Home, About, Category, Project, Profile, Gallery
# Create your views here.


def index(request):
    # HOME
    home = Home.objects.latest('updated')
    # ABOUT
    about = About.objects.latest('updated')
    # Profile
    profiles = Profile.objects.filter(about=about)
    # SKills
    categories = Category.objects.all()
    # Projects
    projects = Project.objects.all()
    # Gallery
    gallery = Gallery.objects.all()

    context = {
        'home': home,
        'about': about,
        'profiles': profiles,
        'categories': categories,
        'projects': projects,
        'gallery': gallery,
    }
    return render(request, 'index.html', context)
