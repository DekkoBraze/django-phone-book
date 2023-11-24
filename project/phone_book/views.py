from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.shortcuts import redirect


def index(request):

    return render(request, 'phone_book/index.html')


class RecordsList(ListView):
    model = Record
    template_name = 'phone_book/records.html'
    context_object_name = 'records'


def record_create(request):
    if request.method == "POST":
        form = RecordForm(request.POST)
        if form.is_valid():
            families = Family.objects.values_list('value')
            family_string = form.cleaned_data['family']
            if family_string not in families:
                family = Family(value=family_string)
                family.save()
            else:
                family = Family.objects.get(value=family_string)
            form.cleaned_data['family'] = family
            Record.objects.create(**form.cleaned_data)
            return redirect('records_list')

    else:
        form = RecordForm()

    return render(request, "phone_book/add_content.html", {"form": form})


#class RecordChange(UpdateView):
#    form_class = Record
#    model = Tasks
#    template_name = 'todoapp/change_content.html'
#    success_url = reverse_lazy('tasks')
#
#    def get_context_data(self, *, object_list=None, **kwargs):
#        context = super().get_context_data(**kwargs)
#        c_def = self.get_user_context(title="Изменение задачи")
#        context = dict(list(context.items()) + list(c_def.items()))
#        return context