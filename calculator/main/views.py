from django.shortcuts import render
from django import forms

def main(request):
    return render(request, 'main/main.html')

def about(request):
    return render(request, 'main/about.html')

def services(request):
    return render(request, 'main/services.html')


