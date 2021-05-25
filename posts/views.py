from django.shortcuts import render

# Create your views here.
def home(request):
    ctx = {'numeros':123}
    return render(request,'posts/index.html',ctx)
