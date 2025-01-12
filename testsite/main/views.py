from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import ToDoList, ToDoItem
from .forms import UstvariNovSeznam

def index(response, id):
    #First test view
    ls = ToDoList.objects.get(id=id)

    if response.method == "POST":
        print(response.POST)
        if response.POST.get("Shrani"):
            for item in ls.todoitem_set.all():
                item.complete = response.POST.get("c" + str(item.id)) == "Pritisnjen"
                item.save()

        elif response.POST.get("Nov vnos"):
            txt = response.POST.get("Novi")
            if len(txt) > 2:
                ls.todoitem_set.create(text=txt, complete=False)
            else:
                print("Nepravilni vnos!")



    #i = ls.todoitem_set.get(id=1)
    #return HttpResponse("<h1>%s</h1><br></br><p>%s</p>" %(ls.name, i.text))
    return render(response, "main/list.html", {"ls":ls})

def home(response):
    return render(response, "main/home.html", {})

def create(response):
    if response.method == "POST":
        form = UstvariNovSeznam(response.POST) #Vrednosti shrani samo če je uporabljena metoda POST in ne GET
        if form.is_valid(): #Ta metoda je avtomatično ustvarjena zaradi forms.Form
            n = form.cleaned_data["name"] #Tako dekriptiram podatke, saj jih je metoda POST zakriptirala
            t = ToDoList(name=n)
            t.save()
        return HttpResponseRedirect("/%i" %t.id) #Pokaži nov list
    else:
        form = UstvariNovSeznam()
    return render(response, "main/create.html", {"form":form})