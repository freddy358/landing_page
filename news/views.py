from django.shortcuts import render, redirect
from .models import *
from .forms import ContactForm
def home(request):
    context={}
    context["name"]=MainName.objects.first()
    context["menu_list"] = Menu.objects.all()
    context["main"] = Main.objects.last()
    context["portfolio"] = Portfolio.objects.all()
    context["about"] = About.objects.last()
    context["contact_form"] = ContactForm()
    context["footer"] = Footer.objects.all()
    context["title"] = MainTitle.objects.last()
    context["icons"] = Icon.objects.all()


    if request.method=="POST":
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            context["contact_form"]=ContactForm()

    return render(request, "index.html", context)

# Create your views here.



