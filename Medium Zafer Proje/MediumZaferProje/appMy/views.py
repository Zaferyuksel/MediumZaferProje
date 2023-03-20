from django.shortcuts import render

# Create your views here.


def index(request):

    return render(request,'index.html')

def Detail(request):

    return render(request,'detail.html')

def Login(request):

    return render(request,'login.html')

def Profil(request):

    return render(request,'profil.html')


def Register(request):

    return render(request,'register.html')

def Write(request):

    return render(request,'write.html')