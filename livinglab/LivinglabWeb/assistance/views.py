from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def mainpage(request):
    # template = loader.get_template('assistance/mainpage.html')
    return render(request, 'assistance/mainpage.html')

def psy_1(request):
    # template = loader.get_template('assistance/psy-1.html')
    return render(request, 'assistance/psy-1.html')