from django.shortcuts import render, redirect
from .models import Contact, Skill, Project, Photo
from resume.views import index
from django.core.mail import send_mail


def get_contact(request):
    if request.method == 'POST':

        # GET form values
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        data = Contact.objects.create(name=name, email=email, message=message)
        data.save()

        send_mail(
            name + ' sent you a message',
            message + ' \n' + email,
            'shaikhsohel.011@gmail.com',
            ['shaikhsohel.0112@gmail.com'],
            fail_silently=True
        )

        skill = Skill.objects.order_by('-date_added')

        projects = Project.objects.all()

        photo = Photo.objects.order_by('-date_added')[0]

        context = {
        'skill': skill,
        'projects': projects,
        'photo': photo
        }

        return render(request, 'index.html', context)
    return render(request, 'index.html')



