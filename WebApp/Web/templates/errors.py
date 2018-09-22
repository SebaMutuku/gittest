from django.shortcuts import  render
from django.conf import  settings

def error_404(request):
    context={'project_name':settings.PROJECT_NAME}
    return render(request,'Web/error_404,html',context)

def error_500(request):
    context = {'project_name': settings.PROJECT_NAME}
    return render(request, 'Web/error_500,html', context)