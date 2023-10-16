from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse
from django.template import loader, Template
from todo_list.models import Todo

# Create your views here.
def index(request: HttpRequest):
    todos = Todo.objects.all()
    return render( request, "page.html", {'todos': todos})

def addTodo(request: HttpRequest):
    if( request.method == 'POST' ):

        title = request.POST.get("title")
        description = request.POST.get("description")
        completed = False if request.POST.get("completed") == None else True
        
        newTodo = Todo(title=title, description=description, completed=completed)
        newTodo.save()
        return redirect(to="index")
    
def deleteTodo(request: HttpRequest, id: int):
    todo = get_object_or_404(Todo, pk=id)
    todo.delete()
    return redirect(to="index")