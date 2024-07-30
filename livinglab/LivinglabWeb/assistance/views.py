from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def mainpage(request):
    # template = loader.get_template('assistance/mainpage.html')
    return render(request, 'assistance/mainpage.html')

def psy_1(request):
    return render(request, 'assistance/psy/psy-1.html')

def psy_2(request):
    return render(request, 'assistance/psy/psy-2.html')

def psy_3(request):
    return render(request, 'assistance/psy/psy-3.html')

def eco_1(request): 
    return render(request, 'assistance/eco/eco-1.html')

def eco_2(request):
    return render(request, 'assistance/eco/eco-2.html')

def eco_3(request):
    return render(request, 'assistance/eco/eco-3.html')

def eco_4(request):
    return render(request, 'assistance/eco/eco-4.html')

def eco_5(request):
    return render(request, 'assistance/eco/eco-5.html')

def eco_6(request):
    return render(request, 'assistance/eco/eco-6.html')

def eco_7(request):
    return render(request, 'assistance/eco/eco-7.html')

def eco_8(request):
    return render(request, 'assistance/eco/eco-8.html')

def eco_9(request):
    return render(request, 'assistance/eco/eco-9.html')

def law_1(request):
    return render(request, 'assistance/law/law-1.html')

def law_2(request):
    return render(request, 'assistance/law/law-2.html')

def law_3(request):
    return render(request, 'assistance/law/law-3.html')

def law_4(request):
    return render(request, 'assistance/law/law-4.html')

def law_5(request):
    return render(request, 'assistance/law/law-5.html')

def law_6(request):
    return render(request, 'assistance/law/law-6.html')

def int_1(request):
    return render(request, 'assistance/int/int-1.html')

def int_2(request):
    return render(request, 'assistance/int/int-2.html')

def int_3(request):
    return render(request, 'assistance/int/int-3.html')

def int_4(request):
    return render(request, 'assistance/int/int-4.html')

def int_5(request):
    return render(request, 'assistance/int/int-5.html')

def int_6(request):
    return render(request, 'assistance/int/int-6.html')

def int_7(request):
    return render(request, 'assistance/int/int-7.html')