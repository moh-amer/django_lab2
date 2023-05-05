from django.shortcuts import render, HttpResponse

# Create your views here.


def aboutus(request):
    return render(request, 'about-us.html')
