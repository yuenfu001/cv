from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *
from .forms import CreateInfoForm
# Create your views here.

def index(request):
    return render(request, "index.html")

def display(request):
    call_names = Name.objects.all()
    #count_total_names = Name.objects.all().count()
    total_names = call_names.count()
    call_states = State.objects.all()
    total_states = call_states.count()


    cont = {
        "total_names":call_names,
        "count_all_names":total_names,
        "states":call_states,
        "count_state":total_states
    }
    return render(request, "display.html", context=cont)

def hmmm(request):
    return render(request,"oyebola.html")

def personal(request, pk):
    person = Name.objects.get(id=pk)

    cont = {
        "infos":person
    }
    return render(request, "personal.html", context=cont)

def CreateInfo(request):
    create_info  = CreateInfoForm(request.POST or None)

    cont = {
        "person_info":create_info
    }

    if request.method == "POST":
        if create_info.is_valid():
            create_info.save()
            return redirect("disp")

    return render(request, "forms.html", cont)

