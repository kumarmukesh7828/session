from django.shortcuts import render
from webapp.forms import NameForm,GfForm,AgeForm

# Create your views here.
def name_view(request):
    form=NameForm()
    return render(request,'myapp/name.html',{'form':form})

def age_view(request):
    name=request.GET['name']
    request.session['name']=name
    form=AgeForm()
    return render(request,'myapp/age.html',{'form':form})


def Gf_view(request):
    age = request.GET['age']
    request.session['age']=age
    form=GfForm()
    return render(request,'myapp/gf.html',{'form':form})
def index(request):
    gf=request.GET['gf']
    request.session['gf']=gf

    return render(request,'myapp/index.html')