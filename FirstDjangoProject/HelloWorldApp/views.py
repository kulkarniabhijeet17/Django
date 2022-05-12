from django.shortcuts import render

# Create your views here.

def hello(request):
    return HttpResponse('Hello World')

def home(request):
    return render(request, 'home.html', {'name': 'Abhijeet'})

def add(request):
    return render(request, 'add.html')

def addition(request):
    # if request.GET:
        # num1 = int(request.GET['num1'])
        # num2 = int(request.GET['num2'])
    if request.POST:
        num1 = int(request.POST['num1'])
        num2 = int(request.POST['num2'])
        res = num1 + num2
    return render(request, 'add.html', {"result" : res})