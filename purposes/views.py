import datetime
import pandas as pd

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import get_user_model

from .forms import TasksForm, PurposesForm
from .models import Tasks, Purposes

User = get_user_model()


@login_required
def index(request):
    purposes_d = Purposes.objects.filter(user=request.user)
    context = {
        'purposes': purposes_d,
    }
    return render(request, 'purposes/index.html', context)


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
def purpose_create(request):
    form = PurposesForm(request.POST)
    context = {
        'form': form,
    }
    if form.is_valid() or request.POST:
        Purposes(name=request.POST.get('name'),
                 description=request.POST.get('description'),
                 deadline=request.POST.get('deadline'), user=request.user).save()
        return redirect('purposes:index')
    return render(request, 'purposes/purpose_create.html', context)


@login_required
def purpose_edit(request, purpose_pk):
    purpose_d = get_object_or_404(Purposes, pk=purpose_pk)
    form = PurposesForm(request.POST or None, instance=purpose_d)
    if not form.is_valid() or request.GET:
        context = {'form': form}
        return render(request, 'purposes/purpose_create.html', context)
    form.save()
    return redirect('purposes:purpose', purpose_pk)


def purpose_complete(request, purpose_pk):
    purpose_d = get_object_or_404(Purposes, pk=purpose_pk)
    purpose_d.date_complete = datetime.datetime.now()
    purpose_d.save()
    Tasks.objects.filter(purpose=Purposes.objects.get(pk=purpose_pk)).delete()
    return redirect('purposes:index')


@login_required
def task(request, task_pk):
    task_d = get_object_or_404(Tasks, pk=task_pk)
    context = {
        'task_d': task_d,
    }
    return render(request, 'purposes/task_detail.html', context)


@login_required
def task_create(request, purpose_pk):
    form = TasksForm(request.POST)
    context = {
        'form': form,
        'purpose_pk': purpose_pk,
    }
    if form.is_valid() or request.POST:
        Tasks(name=request.POST.get('name'),
              description=request.POST.get('description'),
              deadline=request.POST.get('deadline'),
              purpose=Purposes.objects.get(pk=purpose_pk)).save()
        return redirect('purposes:index')
    return render(request, 'purposes/task_create.html', context)


@login_required
def task_edit(request, task_pk):
    task_d = get_object_or_404(Tasks, pk=task_pk)
    form = TasksForm(request.POST or None, instance=task_d)
    if not form.is_valid() or request.GET:
        context = {'form': form}
        return render(request, 'purposes/task_create.html', context)
    form.save()
    return redirect('purposes:index')


def task_complete(request, task_pk):
    task_d = get_object_or_404(Tasks, pk=task_pk)
    task_d.date_complete = datetime.datetime.now()
    task_d.save()
    return redirect('purposes:index')


def task_delete(request, task_pk):
    Tasks(pk=task_pk).delete()
    return redirect('purposes:index')


def friends(request):
    pass


def results(request):
    purposes_r = Purposes.objects.all()
    df = pd.DataFrame(Purposes.objects.all())
    # df.sort_values('date_complete')
    print(purposes_r)

    context = {
        'purposes': purposes_r,
    }
    return render(request, 'purposes/results.html', context)
