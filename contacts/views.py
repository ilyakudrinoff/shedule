from django.shortcuts import render, redirect, get_object_or_404
from .models import Contacts, PreMeeting, Relationship, Facts, Sectors
from .forms import ContactsForm, PremeetingForm, RelationshipForm, FactsForm


def index(request):
    contacts = Contacts.objects.filter(user=request.user)
    context = {
        'contacts': contacts,
    }
    return render(request, 'contacts/index.html', context)


def contact_create(request):
    form = ContactsForm(request.POST)
    link = 'contacts:contact_create'
    context = {
        'form': form,
        'link': link,
    }
    if form.is_valid() or request.POST:
        Contacts(name=request.POST.get('name'), last_name=request.POST.get('last_name'), photo=request.POST.get('photo'),
                 status=request.POST.get('status'), krug=request.POST.get('krug'), sector=Sectors.objects.get(pk=request.POST.get('sector')),
                 ois=request.POST.get('ois'), first_info=request.POST.get('first_info'), user=request.user).save()
        return redirect('contacts:index')
    return render(request, 'contacts/form_create.html', context)


def contact_card(request, contact_pk):
    contact = Contacts.objects.get(pk=contact_pk)
    meets_t = PreMeeting.objects.filter(contact=contact)
    rship_t = Relationship.objects.filter(contact=contact)
    facts_t = Facts.objects.filter(contact=contact)

    context = {
        'contact': contact,
        'contact_pk': contact_pk,
        'meets': meets_t,
        'rship': rship_t,
        'facts': facts_t,
    }
    return render(request, 'contacts/contact_card.html', context)


def contact_edit(request, contact_pk):
    contact = get_object_or_404(Contacts, pk=contact_pk)
    link = 'contacts:contact_edit'
    if request.method == 'POST':
        form = ContactsForm(request.POST, instance=contact)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            return redirect('contacts:contact_card', contact_pk)
    else:
        form = ContactsForm(request.POST, instance=contact)
    return render(request, 'contacts/form_edit.html', {'form': form, 'link': link, })


def contact_delete(request, contact_pk):
    Contacts(pk=contact_pk).delete()
    return redirect('contacts:index')


def meets(request, contact_pk):
    meets_t = PreMeeting.objects.filter(contact=Contacts.objects.get(pk=contact_pk))
    context = {
        'meets_t': meets_t,
    }
    return render(request, 'contacts/meets.html', context)


def meet_create(request, contact_pk):
    form = PremeetingForm(request.POST)
    link = 'contacts:meet_create'
    context = {
        'form': form,
        'link': link,
        'contact_pk': contact_pk,
    }
    if form.is_valid() or request.POST:
        PreMeeting(name=request.POST.get('name'), problem=request.POST.get('problem'), plan=request.POST.get('plan'),
                   result=request.POST.get('result'), contact=Contacts.objects.get(pk=contact_pk)).save()
        return redirect('contacts:contact_card', contact_pk)
    return render(request, 'contacts/form_create.html', context)


def meet_edit(request, meet_pk):
    meet = get_object_or_404(PreMeeting, pk=meet_pk)
    link = 'contacts:meet_edit'
    if request.method == 'POST':
        form = PremeetingForm(request.POST, instance=meet)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            return redirect('contacts:contact_card', meet.contact.pk)
    else:
        form = PremeetingForm(request.POST, instance=meet)
    return render(request, 'contacts/form_edit.html', {'form': form, 'link': link, })


def relationship_create(request, contact_pk):
    form = RelationshipForm(request.POST)
    link = 'contacts:relationship_create'
    context = {
        'form': form,
        'link': link,
        'contact_pk': contact_pk,
    }
    if form.is_valid() or request.POST:
        Relationship(commitment_intensity=request.POST.get('commitment_intensity'),
                     initiative_reciprocity=request.POST.get('initiative_reciprocity'),
                     emotional_involment=request.POST.get('emotional_involment'),
                     openness_trust=request.POST.get('openness_trust'),
                     contact=Contacts.objects.get(pk=contact_pk)).save()
        return redirect('contacts:contact_card', contact_pk)
    return render(request, 'contacts/form_create.html', context)


def relationship_edit(request, relationship_pk):
    rship = get_object_or_404(PreMeeting, pk=relationship_pk)
    link = 'contacts:relationship_edit'
    if request.method == 'POST':
        form = RelationshipForm(request.POST, instance=rship)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            return redirect('contacts:contact_card', rship.contact.pk)
    else:
        form = RelationshipForm(request.POST, instance=rship)
    return render(request, 'contacts/form_edit.html', {'form': form, 'link': link, })


def facts(request, contact_pk):
    facts_t = Facts.objects.filter(contact=Contacts.objects.get(pk=contact_pk))
    context = {
        'facts_t': facts_t,
    }
    return render(request, 'contacts/facts.html', context)


def fact_create(request, contact_pk):
    form = FactsForm(request.POST)
    link = 'contacts:fact_create'
    context = {
        'form': form,
        'link': link,
        'contact_pk': contact_pk,
    }
    if form.is_valid() or request.POST:
        Facts(fact=request.POST.get('fact'), contact=Contacts.objects.get(pk=contact_pk)).save()
        return redirect('contacts:contact_card', contact_pk)
    return render(request, 'contacts/form_create.html', context)


def fact_edit(request, contact_pk, fact_pk):
    fact = get_object_or_404(PreMeeting, pk=fact_pk)
    link = 'contacts:fact_edit'
    if request.method == 'POST':
        form = FactsForm(request.POST, instance=fact)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            return redirect('contacts:contact_card', fact.contact.pk)
    else:
        form = FactsForm(request.POST, instance=fact)
    return render(request, 'contacts/form_edit.html', {'form': form, 'link': link, })
