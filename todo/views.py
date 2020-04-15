from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils import timezone
from . models import Todo

# Create your views here.
def home(request):
    data = Todo.objects.all().order_by('-added_date')
    stuff_for_front_end = {
        'data' : data
    }
    return render(request, 'todo/index.html', stuff_for_front_end)

def add_todo(request):
    added_date = timezone.now()
    item = request.POST.get('item')
    data = Todo.objects.create(added_date=added_date, text=item)
    data.save()
    return HttpResponseRedirect("/")

def delete_todo(request, todo_id):
    Todo.objects.filter(id=todo_id).delete()
    return HttpResponseRedirect('/')