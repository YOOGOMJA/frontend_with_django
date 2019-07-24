from django.shortcuts import render

# Create your views here.

def home(req):
    print('home!!')
    return render(req , 'app_1/index.html')