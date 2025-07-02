from django.shortcuts import render
from django.http import JsonResponse
from .models import Task
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
def home(request):
    return render(request, 'index.html')

def get_tasks(request):
    tasks= list(tasks.onject.values())
    return JsonResponse(tasks, safe=False)


@csrf_exempt
def add_task(request):
    if request.method =='POST':
        data = json.loads(request.body)
        Task.object.create(title=data['title'])
        return JsonResponse({'status': 'Task added'})