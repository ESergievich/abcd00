from django.shortcuts import render, redirect

from .forms import DynamicForm
from .models import FormData


def dynamic_form_view(request):
    if request.method == 'POST':
        form = DynamicForm(request.POST)
        if form.is_valid():
            form_data = {}
            for key, value in request.POST.items():
                if key != 'csrfmiddlewaretoken':
                    form_data[key] = value

            FormData.objects.create(dynamic_data=form_data)
            return redirect('dynamic_form:show_data')
    else:
        form = DynamicForm()

    return render(request, 'dynamic_form/form.html', {'form': form})


def show_data(request):
    dynamic_forms = FormData.objects.all()
    return render(request, 'dynamic_form/data.html', {'dynamic_forms': dynamic_forms})
