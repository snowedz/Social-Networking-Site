from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'account/login.html')

def home(request):
    user = request.user

    context = {'user':user}
    return render(request,'home.html', context)
