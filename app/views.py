from django.shortcuts import render
from app.models import *



def equijoins(request):
    EMPOBJECTS=Emp.objects.select_related('deptno').all()
    d={'EMPOBJECTS':EMPOBJECTS}
    return render(request,'equijoins.html',d)