from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.http import HttpResponse

models = [Family, Name, Otchestvo, Street, Mob]
titles = ['family', 'name', 'otchestvo', 'street', 'mob']


def index(request):

    return render(request, 'phone_book/index.html')


class RecordsList(ListView):
    model = Record
    template_name = 'phone_book/records.html'
    context_object_name = 'records'


def record_create(request):
    pk = ''
    if request.method == "POST":
        form = RecordForm(pk=pk, data=request.POST)
        if form.is_valid():
            lists = []
            for i in range(len(models)):
                lists.append(models[i].objects.values_list('value', flat=True))
                string = form.cleaned_data[titles[i]]
                if string not in lists[i]:
                    new_object = models[i](value=string)
                    new_object.save()
                else:
                    new_object = models[i].objects.get(value=string)
                form.cleaned_data[titles[i]] = new_object
            Record.objects.create(**form.cleaned_data)
            return redirect('records_list')
    else:
        form = RecordForm(pk=pk)

    return render(request, "phone_book/add_content.html", {"form": form})


def record_update(request, pk):
    if request.method == "POST":
        form = RecordForm(pk=pk, data=request.POST)
        if form.is_valid():
            lists = []
            for i in range(len(models)):
                lists.append(models[i].objects.values_list('value', flat=True))
                string = form.cleaned_data[titles[i]]
                if string not in lists[i]:
                    new_object = models[i](value=string)
                    new_object.save()
                else:
                    new_object = models[i].objects.get(value=string)
                form.cleaned_data[titles[i]] = new_object
            Record.objects.get(id=pk).mob.delete()
            Record.objects.filter(id=pk).update(**form.cleaned_data)
            return redirect('records_list')

    else:
        record = Record.objects.get(id=pk)
        form = RecordForm(initial={'name': record.name,
                                   'family': record.family.value,
                                   'otchestvo': record.otchestvo,
                                   'street': record.street,
                                   'house': record.house,
                                   'korp': record.korp,
                                   'apartments': record.apartments,
                                   'mob': record.mob
                                   }, pk=pk)

    return render(request, "phone_book/add_content.html", {"form": form})


class RecordDelete(DeleteView):
    model = Record
    template_name = 'phone_book/delete_content.html'
    success_url = reverse_lazy('records_list')


class FamiliesList(ListView):
    model = Family
    template_name = 'phone_book/families.html'
    context_object_name = 'families'


class FamilyCreate(CreateView):
    form_class = FamilyForm
    model = Family
    template_name = 'phone_book/add_content.html'
    success_url = reverse_lazy('families_list')


class FamilyUpdate(UpdateView):
    form_class = FamilyForm
    model = Family
    template_name = 'phone_book/add_content.html'
    success_url = reverse_lazy('families_list')


class FamilyDelete(DeleteView):
    model = Family
    template_name = 'phone_book/delete_content.html'
    success_url = reverse_lazy('families_list')


class NamesList(ListView):
    model = Name
    template_name = 'phone_book/names.html'
    context_object_name = 'names'


class NameCreate(CreateView):
    form_class = NameForm
    model = Name
    template_name = 'phone_book/add_content.html'
    success_url = reverse_lazy('names_list')


class NameUpdate(UpdateView):
    form_class = NameForm
    model = Name
    template_name = 'phone_book/add_content.html'
    success_url = reverse_lazy('names_list')


class NameDelete(DeleteView):
    model = Name
    template_name = 'phone_book/delete_content.html'
    success_url = reverse_lazy('names_list')


class OtchestvosList(ListView):
    model = Otchestvo
    template_name = 'phone_book/otchestvos.html'
    context_object_name = 'otchestvos'


class OtchestvoCreate(CreateView):
    form_class = OtchestvoForm
    model = Otchestvo
    template_name = 'phone_book/add_content.html'
    success_url = reverse_lazy('otchestvos_list')


class OtchestvoUpdate(UpdateView):
    form_class = OtchestvoForm
    model = Otchestvo
    template_name = 'phone_book/add_content.html'
    success_url = reverse_lazy('otchestvos_list')


class OtchestvoDelete(DeleteView):
    model = Otchestvo
    template_name = 'phone_book/delete_content.html'
    success_url = reverse_lazy('otchestvos_list')


class StreetsList(ListView):
    model = Street
    template_name = 'phone_book/streets.html'
    context_object_name = 'streets'


class StreetCreate(CreateView):
    form_class = StreetForm
    model = Street
    template_name = 'phone_book/add_content.html'
    success_url = reverse_lazy('streets_list')


class StreetUpdate(UpdateView):
    form_class = StreetForm
    model = Street
    template_name = 'phone_book/add_content.html'
    success_url = reverse_lazy('streets_list')


class StreetDelete(DeleteView):
    model = Street
    template_name = 'phone_book/delete_content.html'
    success_url = reverse_lazy('streets_list')


class MobsList(ListView):
    model = Mob
    template_name = 'phone_book/mobs.html'
    context_object_name = 'mobs'


class MobCreate(CreateView):
    form_class = MobForm
    model = Mob
    template_name = 'phone_book/add_content.html'
    success_url = reverse_lazy('mobs_list')


class MobUpdate(UpdateView):
    form_class = MobForm
    model = Mob
    template_name = 'phone_book/add_content.html'
    success_url = reverse_lazy('mobs_list')


class MobDelete(DeleteView):
    model = Mob
    template_name = 'phone_book/delete_content.html'
    success_url = reverse_lazy('mobs_list')
