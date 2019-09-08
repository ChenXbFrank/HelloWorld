from django.http import HttpResponse


# def hello(request):
#     return HttpResponse("Hello Django!")
from django.shortcuts import render


def hello(request):
    context = dict()
    context['hello'] = 'Hello Django Html!'
    return render(request, 'hello.html', context)
