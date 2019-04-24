from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.

def MyView(request):
    return render(request,'welcomepage.html')

