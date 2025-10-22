from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<h1>Hello, world!</h1>")

def second_page(request):
    return render(request,"second_page.html")

def third_page(request):
    return render(request,"third_page.html")

def foth_page(request):
    return render(request,"foth_page.html")

def fifth_page(request):
    return render(request,"fifth_page.html")

def sit_page(request):
    return render(request,"sit_page.html")

def seventh_page(request):
    return render(request,"seventh_page.html")