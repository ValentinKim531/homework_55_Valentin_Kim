from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

from webapp.models import To_do


def index_view(request: WSGIRequest):
    tasks = To_do.objects.exclude(is_deleted=True)
    context = {
        'tasks': tasks
    }
    if "Delete" in request.POST:
        checkedlist = request.POST.getlist('checkedbox')
        print(checkedlist)
        for i in range(len(checkedlist)):
            print('da')
            print(i)
            todo = To_do.objects.filter(id=int(checkedlist[i]))
            print(todo)
            todo.delete()
    return render(request, 'index.html', context=context)
