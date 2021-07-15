from django.shortcuts import render

def index(request):
    return render(request, 'coloring/index.html')

def demo(request):
    return render(request, 'coloring/demo.html')

def new_interaction(request):
    return render(request, 'coloring/new_interaction.html')

def main(request):
    return render(request, 'coloring/main.html')

def color1(request):
    return render(request, 'coloring/color1.html')

def color2(request):
    return render(request, 'coloring/color2.html')

def color3(request):
    return render(request, 'coloring/color3.html')