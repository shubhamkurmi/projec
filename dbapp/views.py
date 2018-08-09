from django.shortcuts import render
from .models import product

def input(request):
    return render(request,'input.html')
def insert(request):
    pid1=int(request.GET['t1'])
    pname1=request.GET['t2']
    pcost1=float(request.GET['t3'])
    pmdt1=request.GET['t4']
    pexpdt1=request.GET['t5']
    F=product(pid=pid1,pname=pname1,pcost=pcost1,pmdt=pmdt1,pexpdt=pexpdt1)
    F.save()
    return render(request,'link.html')
def display(request):
    recs=product.objects.all()
    return render(request,'display.html',{'records':recs})