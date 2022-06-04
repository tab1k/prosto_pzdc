from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def market(request):
    return render(request, 'main/market.html')


def stock(request):
    return render(request, 'main/stock.html')


def help(request):
    return render(request, 'main/help.html')