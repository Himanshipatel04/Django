from django.shortcuts import render
from . models import ChaiVariety,store
from django.shortcuts import get_object_or_404
from .forms import ChaiVarietyForm

# Create your views here.
def allchai(request):
    chais = ChaiVariety.objects.all()
    return render(request,"chai/allchai.html",{'chais':chais})

def chai_details(request,chai_id):
    chai = get_object_or_404(ChaiVariety,pk=chai_id)
    return render(request,"chai/chaidetails.html",{'chai':chai})

def chai_stores_view(request):
    stores = None
    if request.method == 'POST':
        form = ChaiVarietyForm(request.POST)
        if form.is_valid():
           chai_variety =  form.cleaned_data['chai_variety']
           stores = store.objects.filter(chai_varieties=chai_variety)
    else:
        form = ChaiVarietyForm()
    return render(request,"chai/chai_stores.html",{'stores':stores,'forms':form})