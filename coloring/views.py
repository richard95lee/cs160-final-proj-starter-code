from django.shortcuts import render

def index(request):
    return render(request, 'coloring/index.html')

def bedroom(request):
    return render(request, 'coloring/bedroom.html')