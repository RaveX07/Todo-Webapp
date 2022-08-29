from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from .forms import UserForm
from .forms import TodoForm

from .models import Todo
from .models import User

from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)

    Userlist = []
    Todolist = []

    for x in User.objects.all():
        Userlist.append(x)
    for y in Todo.objects.all():
        Todolist.append(y)
    Context = {
        "users": Userlist,
        "todos": Todolist,
        "User": str(request.user),
    }

    return render(request, "home.html", Context)

def user_create_view(request):
    form = UserCreationForm()
    if request.method == 'POST':
        print("This is a Post")
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts/login')
    else:
        form = UserCreationForm()
    
    return render(request, "usercreate.html", {'form': form})

def todo_create_view(request):

    initial_D = {
        'Name': str(request.user),
    }

    form = TodoForm(initial=initial_D)
    form.fields['Name'].widget.attrs['readonly'] = True
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TodoForm(initial=initial_D)
        form.fields['Name'].widget.attrs['readonly'] = True

    context = {
        'form': form
    }

    return render(request, "todocreate.html", context)

def delete_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.delete()
    return redirect('/')