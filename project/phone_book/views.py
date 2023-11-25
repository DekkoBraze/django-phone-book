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


def record_change(request, pk):
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
