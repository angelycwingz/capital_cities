from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .models import Capital


# Create your views here.
class HomPageView(ListView):
    model = Capital
    template_name = "home.html"


class NewCapitalView(CreateView):
    model = Capital
    template_name = "capital_new.html"
    fields = ["city", "country"]
