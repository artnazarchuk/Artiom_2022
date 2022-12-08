from django.shortcuts import render
from .models import Project

# запрос всех объектов QuerySet
def project_index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context)

# запрос одного объекта через get()
def project_detail(request, pk):
    project_one = Project.objects.get(pk=pk)
    context = {
        'project_one': project_one
    }
    return render(request, 'project_detail.html', context)

