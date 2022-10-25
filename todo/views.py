from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import HttpResponse, redirect
from .forms import CreateForm, CreateUser
from .models import Create
from django.contrib.auth import logout, login, authenticate


@login_required(login_url='login/')
def todo(request):
    TaskList = Create.objects.all()
    todoform = CreateForm()
    if request.method == 'POST':
        todoform = CreateForm(request.POST)
        if todoform.is_valid():
            todoform.save()
            return redirect('/')
    context = {'todoform': todoform, 'TaskList': TaskList}
    return render(request, 'todo/main.html', context)


@login_required(login_url='login/')
def TaskDelete(request, pk):
    DeleteTask = Create.objects.get(id=pk)
    DeleteTask.delete()
    return redirect('todo')


@login_required(login_url='login/')
def done(request, pk):
    TaskList = Create.objects.get(id=pk)
    TaskList.status = "DONE"
    TaskList.save()
    return redirect('todo')


def UserLogin(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        upassword = request.POST.get('password')
        user = authenticate(request, username=uname, password=upassword)
        if user is not None:
            login(request, user)
            return redirect('todo')
        else:
            messages.info(request, 'invalid')
    context = {}
    return render(request, 'todo/login.html', context=context)


def UserRegister(request):
    form = CreateUser()
    if request.method == 'POST':
        form = CreateUser(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Login Created for user ' + user)
            return redirect('UserLogin')

    context = {'form': form}
    return render(request, 'todo/register.html', context=context)


def UserLogout(request):
    logout(request)
    return redirect('UserLogin')

