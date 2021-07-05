from django.shortcuts import render, redirect

#Data models
from .models import *

from posts.models import Posts
# Django


# Create your views here.

def get_index(request):
    return render(request,'locales/index.html')

def DetailCategory(request):
    return redirect('detailCategory')


def pruebaDatos(request):


    objects={'categories':showCategories(),'posts':showPosts()}
    return render(request,'locales/pruebaDatos.html',objects)
    # return render(request, 'locales/index.html')


def showCategories():
    categories = Category.objects.all()
    ctx = categories

    return ctx


def showPosts():
    posts = Posts.objects.all()
    ctx = posts
    
    return ctx


def showBussinesInCategory(request,id):
    business_in_category = Business.objects.filter(category=id)
    ctx = {'business' : business_in_category}

    return render(request,'categoryDetail.html',ctx)


def showBussines(request,id):
    bns = Business.objects.get(id=id)
    ctx = {'bussines' : bns}
    
    return render (request,'bussines.html',ctx)


def showProductsInBussines(id):
    product = Product.objects.filter(business = id)
    ctx={'product' : product}
    return ctx


def showProductsDetails(request,id):
    
    respuesta = Product.objects.get(id = id)
    ctx = {'product' : respuesta}

    return render (request, 'product.html') 

