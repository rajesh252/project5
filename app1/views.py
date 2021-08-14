from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def mahesh (request):
    return render(request, 'mahesh.html')