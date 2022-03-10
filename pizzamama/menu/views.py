from django.shortcuts import render
from django.http import HttpResponse
from .models import Pizza

def index(request):

    pizzas =Pizza.objects.all().order_by('prix')
    #pizzas_names_and_prix = [pizza.nom + ": " + str(pizza.prix) +"€ " for pizza in pizzas]
   # pizzas_names_prix_str = ",  ".join(pizzas_names_and_prix)
    #return HttpResponse("les pizzas:  " + pizzas_names_prix_str)
    return render(request, 'menu/index.html', {'pizzas': pizzas})