from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, ToDoItem

def index(response, name):
    #First test view
    ls = ToDoList.objects.get(name=name)
    #i = ls.todoitem_set.get(id=1)
    #return HttpResponse("<h1>%s</h1><br></br><p>%s</p>" %(ls.name, i.text))
    return HttpResponse("<h1>%s</h1>" %ls.name)