import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import get_user_model

from .forms import PurposesForm
from .models import Purposes
from .filters import PurposesFilter
from .utils import paginator

User = get_user_model()


@login_required
def index(request):
    purposes_d = Purposes.objects.filter(user=request.user)
    purpose_filter = PurposesFilter(request.GET, queryset=purposes_d)
    purposes_d = purpose_filter.qs
    context = {
        'page_obj': paginator(request, purposes_d),
        'purpose_filter': purpose_filter,
    }
    return render(request, 'purposes/index.html', context)


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
    return redirect('purposes:index')


@login_required
def purpose_complete(request, purpose_pk):
    purpose_d = get_object_or_404(Purposes, pk=purpose_pk)
    purpose_d.date_complete = datetime.datetime.now()
    purpose_d.save()
    return redirect('purposes:index')
