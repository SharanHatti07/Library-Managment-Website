from django.shortcuts import render
from django.http import HttpResponse
from .models import books
# Create your views here.

def index(request):
    bookList = books.objects.values()

    return render(request,'index.html', {'books':bookList})

def view(request):
    return render(request,'view.html')

def delete(request,rid):
    
    p.delete()
    return redirect()