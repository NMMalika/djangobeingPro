from django.shortcuts import render
from datetime import datetime


# Create your views here.
def home(request):
    context={
        "name": ["John", "Doe", "Smith", "Jane"],
        "can_display_name": True,
    }

    return render(request, "home.html", context)
