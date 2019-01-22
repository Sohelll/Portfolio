from django.shortcuts import render
from contact.models import Skill, Project, Photo


def index(request):
    
    skill = Skill.objects.order_by('-date_added')

    projects = Project.objects.all()
    photo = Photo.objects.order_by('-date_added')[0]

    context = {
        'skill': skill,
        'projects': projects,
        'photo': photo,
    }

    return render(request, 'index.html', context)
