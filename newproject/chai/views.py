from django.shortcuts import render

# Create your views here.
def allchai(request):
    return render(request,"chai/allchai.html")