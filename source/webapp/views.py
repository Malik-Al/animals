from django.shortcuts import render

# Create your views here.


def index_view(request, *args, **kwargs):
    return render(request, 'index.html')


def post_view(request, *args, **kwargs):
    print(request.POST)
    numder = request.POST.get('numder')

    return render(request, 'post2.html', context={
        'number': numder
    })


def fpost_view(request, *args, **kwargs):
    print(request.POST)
    numder2 = request.POST.get('numder2')

    return render(request, 'fpost.html', context={
        'number2': numder2
    })


def nex_view(request, *args, **kwargs):
    print(request.POST)
    nex = request.POST.get('nex')

    return render(request, 'nex.html', context={
        'nex': nex
    })