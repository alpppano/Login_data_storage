from django.shortcuts import render, redirect
from .models import LoginData
from .forms import LoginDataForm

# Create your views here.
def index(request):
    data = LoginData.objects.all()
    context = {
        'data': data,
    }
    return render(request, 'login_data/index.html', context)

def create(request):
    if request.method == 'POST':
        form = LoginDataForm(request.POST)
        if form.is_valid():
            data = form.save()
            return redirect('login_data:detail', data.pk)
    else:
        form = LoginDataForm()
    context = {
        'form': form,
    }
    return render(request, 'login_data/create.html', context)

def detail(request, data_pk):
    data = LoginData.objects.get(pk=data_pk)
    context = {
        'data': data,
    }
    return render(request, 'login_data/detail.html', context)

def update(request, data_pk):
    data = LoginData.objects.get(pk=data_pk)

    if request.method == 'POST':
        form = LoginDataForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('login_data:detail', data.pk)
    else:
        form = LoginDataForm(instance=data)
    context = {
        'data': data,
        'form': form,
    }
    return render(request, 'login_data/update.html', context)

def delete(request, data_pk):
    data = LoginData.objects.get(pk=data_pk)
    data.delete()
    return redirect('login_data:index')