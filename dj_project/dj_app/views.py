from django.shortcuts import render,redirect
from .models import *
def home(request):
    if request.method=="POST":
        s=request.POST["s_no"]
        n=request.POST["name"]
        m=request.POST["mail"]
        c=request.POST["course"]
        d=Tech(s_no=s,name=n,email=m,course=c)
        d.save()
        return redirect('show')
    return render (request,"home.html")
def show(request):
    all=Tech.objects.all()
    return render(request,"show.html",{"result":all})

def update(request,u):
    r=Tech.objects.get(s_no=u)
    if request.method=="POST":
        na=request.POST['name']
        ag=request.POST['mail']
        az=request.POST['course']
        r.name=na
        r.email=ag
        r.course=az
        r.save()
        return redirect('show')
    else:
        return render (request,"update.html",{"ko":r})
    

def delete(request,l):
    g=Tech.objects.get(s_no=l)
    g.delete()
    return redirect('show')