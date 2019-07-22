from django.shortcuts import render

# Create your views here.

def projeto(request):
    return render(request, 'index.html')