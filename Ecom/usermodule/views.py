from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
        'message':'Sucessfully installed'
    }
    return render (request,'usermodule/index.html',{'message':context['message']})