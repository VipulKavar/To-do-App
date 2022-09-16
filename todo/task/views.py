from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import TodoForm
from .models import Todo

# Create your views here.
def home(request):
    context = {'todos' : Todo.objects.all().order_by('-created_date')}
    return render(request, 'task/home.html', context)

def create_todo(request):
    if request.method == 'POST':
        forms = TodoForm(request.POST)
        if forms.is_valid():
            forms.save()
            messages.success(request,'Your Todo is created!')
            return redirect('home')
    else:
        forms = TodoForm()

    context = {
        'form':forms
    }
    return render(request, 'task/create.html', context)

def edit_todo(request, pk):
    if request.method == 'POST':
        todo = Todo.objects.get(id=pk)
        forms = TodoForm(request.POST)
        if forms.is_valid():
            todo.title = forms.instance.title
            todo.task_content = forms.instance.task_content
            todo.save()
            messages.success(request,'Your Todo is Updated Successfully!')
            return redirect('home')
    else:
        todo = Todo.objects.get(id=pk)
        forms = TodoForm(instance=todo)
    return render(request, 'task/edit.html', {'form':forms})

def complete(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.complete = True
    todo.save()
    context = {'todos' : Todo.objects.all()}
    return render(request, 'task/home.html', context)

def delete(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    context = {'todos' : Todo.objects.all()}
    return render(request, 'task/home.html', context)

def completed(request):
    todo = Todo.objects.all().filter(complete=True)
    context = {'todos' : todo}
    return render(request, 'task/completed.html', context)