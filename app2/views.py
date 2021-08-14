from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def rajesh(request):
    return render(request, 'rajesh.html')