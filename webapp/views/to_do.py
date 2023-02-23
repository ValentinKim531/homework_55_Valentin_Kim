from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404
from webapp.forms import TodoForm
from webapp.models import To_do, StatusChoice


def add_view(request: WSGIRequest):
    if request.method == "GET":
        form = TodoForm()
        return render(request, 'to_do_create.html',
                      context={
                          'choices': StatusChoice.choices,
                          'form': form
                      })

    form = TodoForm(data=request.POST)
    if not form.is_valid():
        return render(request, 'to_do_create.html',
                      context={
                          'choices': StatusChoice.choices,
                          'form': form
                      })

    else:
        to_do = To_do.objects.create(**form.cleaned_data)
        return redirect('to_do_detail', pk=to_do.pk)


def update_view(request, pk):
    to_do = get_object_or_404(To_do, pk=pk)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=to_do)
        if form.is_valid():
            to_do.save()
            return redirect('to_do_detail', pk=to_do.pk)
    else:
        form = TodoForm(instance=to_do)
    return render(request, 'to_do_update.html',
                  context={'form': form,
                           'to_do': to_do,
                           'choices': StatusChoice.choices})


def detail_view(request, pk):
    to_do = get_object_or_404(To_do, pk=pk)
    return render(request, 'to_do.html', context={
        'to_do': to_do
    })


def delete_task(request, pk):
    to_do = get_object_or_404(To_do, pk=pk)
    return render(request, 'to_do_confirm_delete.html', context={'to_do': to_do})


def confirm_delete_task(request, pk):
    to_do = get_object_or_404(To_do, pk=pk)
    to_do.delete()
    return redirect('index')
