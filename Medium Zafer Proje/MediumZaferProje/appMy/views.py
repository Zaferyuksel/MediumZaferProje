from django.shortcuts import render
from .models import *
# Create your views here.


def index(request):
    products = Article.objects.all()[0:6]
    butons = Category.objects.all().order_by("?")[0:9]
    articles = Article.objects.all()

    context ={
        "products": products,
        "butons":butons,
        "articles":articles,
    }
    return render(request,'index.html',context)

def Detail(request,id):
    product= Article.objects.get(id=id)

    context={
        "product":product
    }

    return render(request,'detail.html',context)

def Login(request):

    return render(request,'login.html')

def Profil(request):

    return render(request,'profil.html')


def Register(request):

    return render(request,'register.html')

def Write(request):

    return render(request,'write.html')