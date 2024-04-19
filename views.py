from django.shortcuts import render,redirect
from . import models
from django.http import HttpResponse

# Create your views here.


def addtask(request):
    data = dict(request.GET)
    T_id = int(data['T_id'][0])
    T_name = data['T_name'][0]
    T_description = data['T_description'][0]

    data = models.Todo(T_id,T_name,T_description)
    data.save()
    return redirect("/todolist")

def todolist(request):
    data = list(models.Todo.objects.all().values())
    return render(request,'todolist.html',{'data':data})

def deletetask(request):

    data = dict(request.GET)

    dT_id = int(data['dT_id'][0])

    data = models.Todo.objects.filter(T_id=dT_id).delete()

    return redirect("/todolist")

