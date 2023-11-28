from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.http import HttpResponse
from django.db.models import Q

# Атрибуты Record, которые представляют собой объекты и связаны через foreign key
attributes = {'family': Family, 'name': Name, 'otchestvo': Otchestvo, 'street': Street, 'mob': Mob}


def index(request):

    return render(request, 'phone_book/index.html')


class RecordsSearch(ListView):
    model = Record
    template_name = 'phone_book/records.html'
    context_object_name = 'records'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Record.objects.filter(
            Q(family__value__icontains=query) |
            Q(name__value__icontains=query) |
            Q(otchestvo__value__icontains=query) |
            Q(street__value__icontains=query) |
            Q(house__icontains=query) |
            Q(korp__icontains=query) |
            Q(apartments__icontains=query) |
            Q(mob__value__icontains=query)
        )
        return object_list


class RecordsList(ListView):
    model = Record
    template_name = 'phone_book/records.html'
    context_object_name = 'records'


def record_create(request):
    pk = ''
    if request.method == "POST":
        form = RecordForm(pk=pk, data=request.POST)
        if form.is_valid():
            for model_string, model in attributes.items():           # Проходимся по моделям из словаря
                lst = model.objects.values_list('value', flat=True)  # Берем список всех значений модели в бд
                string_from_form = form.cleaned_data[model_string]   # Получаем из формы введенное в нее значение
                if string_from_form not in lst:                      # Если новое значение не встречается в бд
                    new_object = model(value=string_from_form)       # Создаем новое значение и сохраняем
                    new_object.save()
                else:
                    new_object = model.objects.get(value=string_from_form)  # Иначе берем ссылку на запись в бд
                form.cleaned_data[model_string] = new_object                # Присваиваем её полю формы
            Record.objects.create(**form.cleaned_data)                      # Создаем запись
            return redirect('records_list')
    else:
        form = RecordForm(pk=pk)

    return render(request, "phone_book/add_content.html", {"form": form})


def record_update(request, pk):
    if request.method == "POST":
        form = RecordForm(pk=pk, data=request.POST)
        if form.is_valid():
            record_query = Record.objects.get(id=pk)  # Получаем ссылки на все старые объекты записи
            old_objects = {
                'family': record_query.family,
                'name': record_query.name,
                'otchestvo': record_query.otchestvo,
                'street': record_query.street,
                'mob': record_query.mob
            }
            for model_string, model in attributes.items():
                lst = model.objects.values_list('value', flat=True)
                string_from_form = form.cleaned_data[model_string]
                if string_from_form not in lst:
                    updated_object = old_objects[model_string]
                    if updated_object.record.all().count() == 1:  # Если привязана только одна (текущая) запись
                        updated_object.value = string_from_form   # Заменяем значение старого объекта
                        updated_object.save()
                    else:                                         # Иначе создаем новый
                        updated_object = model(value=string_from_form)
                        updated_object.save()
                else:
                    updated_object = model.objects.get(value=string_from_form)
                form.cleaned_data[model_string] = updated_object
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
