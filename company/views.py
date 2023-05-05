from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, 'index.html')

def aboutus(request):
    return render(request, 'about-us.html')

def contactus(request):
    return render(request, 'contact-us.html')

employees = ["Mohamed","Ahmed", "Ali", "Hossam"]
def getemps(request):
    return render(request, 'employees.html', {"emps": employees})