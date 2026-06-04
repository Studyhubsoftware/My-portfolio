from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from .models import Profile, Skill, Experience, Project, Achievement, ContactMessage


def home(request):
    profile = Profile.objects.first()
    skills_bar = Skill.objects.all()
    pill_skills = Skill.objects.filter(show_in_pills=True)
    work_exp = Experience.objects.filter(type='work')
    education = Experience.objects.filter(type='edu')
    projects = Project.objects.filter(is_featured=True)
    achievements = Achievement.objects.all()

    context = {
        'profile': profile,
        'skills_bar': skills_bar,
        'pill_skills': pill_skills,
        'work_exp': work_exp,
        'education': education,
        'projects': projects,
        'achievements': achievements,
    }
    return render(request, 'main/index.html', context)


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        subject = request.POST.get('subject', '').strip()
        message = request.POST.get('message', '').strip()

        if name and email and subject and message:
            ContactMessage.objects.create(
                name=name, email=email,
                subject=subject, message=message
            )
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'status': 'ok'})
            messages.success(request, 'Message sent! I will get back to you soon ✨')
        else:
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'status': 'error', 'msg': 'All fields required'})
            messages.error(request, 'Please fill all fields.')

    return redirect('home')
