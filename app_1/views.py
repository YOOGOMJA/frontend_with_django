from django.shortcuts import render

# Create your views here.

def home(req):
    print('home!!')
    return render(req , 'app_1/index.html')

def slide(req):
    print('slide')
    return render(req , 'app_1/slide.html')