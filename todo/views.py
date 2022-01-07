from django.shortcuts import render
from django.http import HttpResponse


#def index(request):
#    return HttpResponse("Hello, world. You're at the todo index.")

def todo_list(request):
    return render(request, 'todo/todo_list.html', {})