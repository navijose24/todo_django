from django.shortcuts import render
from django.http import JsonResponse
from .models import Task
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
def home(request):
    return render(request, 'index.html')

def get_tasks(request):
    tasks = list(Task.objects.values())  # now includes 'completed' field
    return JsonResponse({'tasks': tasks})



@csrf_exempt
def add_tasks(request):
    if request.method =='POST':
        data = json.loads(request.body)
        Task.objects.create(title=data['title'])
        return JsonResponse({'status': 'Task added'})
    
@csrf_exempt
def update_task(request, id):
    if request.method == 'POST':
        data = json.loads(request.body)
        task = Task.objects.get(id=id)
        task.completed = data['completed']
        task.save()
        return JsonResponse({'status': 'updated'})
