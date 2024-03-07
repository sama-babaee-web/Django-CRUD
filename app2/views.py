from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import FormView
from app2.forms import NumberForm
from app2.models import Number


class NumberFormView(FormView):
    template_name = "app2/home.html"
    form_class = NumberForm


def form_test(request, *args, **kwargs):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    form = NumberForm()
    data = {}
    if is_ajax:
        form = NumberForm(request.POST)
        if form.is_valid():
            data['username'] = form.cleaned_data.get('username')
            data['number'] = form.cleaned_data.get('number')
            data['status'] = 'ok'
            new_number = Number(
                username=data['username'],
                number=data['number']
            )
            new_number.save()
            return JsonResponse(data)
        else:
            data['status'] = 'error'
            return JsonResponse(data)

    context = {
        'form':form
    }

    return render(request, 'app2/home.html', context)



