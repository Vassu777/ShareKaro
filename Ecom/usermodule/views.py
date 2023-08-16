from django.shortcuts import render
from .forms import CustomerForm
# Create your views here.
def CustomerSignIn(request):
    forms = CustomerForm()
    return render (request,'usermodule/index.html',{'form':forms})