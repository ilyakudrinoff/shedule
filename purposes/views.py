import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import get_user_model

from .forms import TasksForm, PurposesForm
from .models import Tasks, Purposes

User = get_user_model()


@login_required
def index(request):
    return render(request, 'purposes/index.html')


@login_required
def purposes(request):
    purposes_d = Purposes.objects.filter(deadline__year=datetime.datetime.year)
    context = {
        'purposes': purposes_d,
    }
    return render(request, 'purposes/purposes.html', context)


@login_required
def purpose(request, purpose_pk):
    purpose_d = get_object_or_404(Purposes, pk=purpose_pk)
    tasks = Tasks.objects.filter(purpose=purpose_pk)
    context = {
        'purpose_d': purpose_d,
        'tasks': tasks,
    }
    return render(request, 'purposes/purpose_detail.html', context)


@login_required
def task(request, task_pk):
    task_d = get_object_or_404(Tasks, pk=task_pk)
    context = {
        'task_d': task_d,
    }
    return render(request, 'purposes/task_detail.html', context)


@login_required
def purpose_create(request):
    form = PurposesForm(request.POST)
    context = {
        'form': form,
    }
    if form.is_valid() or request.POST:
        Purposes(name=request.POST.get('name'),
                 description=request.POST.get('description'),
                 deadline=request.POST.get('deadline'),
                 user=form.cleaned_data['user']).save()
        return redirect('purpose:purposes', username=request.user)
    return render(request, 'purpose/purpose_create.html', context)


@login_required
def task_create(request, purpose_pk):
    form = TasksForm(request.POST)
    context = {
        'form': form,
    }
    if form.is_valid() or request.POST:
        Tasks(name=request.POST.get('name'),
              description=request.POST.get('description'),
              deadline=request.POST.get('deadline'),
              purpose=purpose_pk).save()
        return redirect('purpose:purpose_detail', purpose=purpose_pk)
    return render(request, 'purpose/purpose_create.html', context)


@login_required
def purpose_edit(request, purpose_pk):
    purpose_d = get_object_or_404(Purposes, pk=purpose_pk)
    form = PurposesForm(request.POST or None, instance=purpose_d)
    if not form.is_valid() or request.GET:
        context = {'form': form}
        return render(request, 'purposes/purpose_create.html', context)
    form.save()
    return redirect('purposes:purpose_detail', purpose_pk)


@login_required
def task_edit(request, task_pk):
    task_d = get_object_or_404(Tasks, pk=task_pk)
    form = TasksForm(request.POST or None, instance=task_d)
    if not form.is_valid() or request.GET:
        context = {'form': form}
        return render(request, 'purposes/task_create.html', context)
    form.save()
    return redirect('purposes:task_detail', task_pk)
