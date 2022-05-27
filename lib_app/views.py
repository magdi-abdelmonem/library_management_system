from django.shortcuts import render,redirect,get_object_or_404


from .models import *
from .forms import Bookform,Category, Categoryform


def books (request):
    search=Book.objects.all()
    title=None
    if 'search_name' in request.GET:
        title = request.GET['search_name']
        if title:
            search=search.filter(title__icontains=title)

    context={
        'category': Category.objects.all(),
        'book': search,
        'cate':Categoryform(),
        }
    return render(request,'pages/books.html',context)




def delete (request,id):
    book_delete=get_object_or_404(Book,id=id)
    
    if request.method == 'POST':
        
        book_delete.delete()
        return redirect('/')
      
        


    context={
           #"form":Bookform(),
        }
    return render(request,'pages/delete.html')





def index (request):
    if request.method == 'POST':
        dataform=Bookform(request.POST,request.FILES)
        if dataform.is_valid():
            dataform.save()
            return redirect('/')
        catform=Categoryform(request.POST)
        if catform.is_valid():
            catform.save()
            return redirect('/')
    context={
        'category': Category.objects.all(),
        'book': Book.objects.all(),
        'form': Bookform(),
        'cate':Categoryform(),
        'allbook':Book.objects.filter(active=True).count(),
        'allavailble':Book.objects.filter(status='availble').count(),
        'allsold':Book.objects.filter(status='sold').count(),
        'allarental':Book.objects.filter(status='rental').count(),
        'gain_sold':Book.objects.filter(prices__range=(0,10000)),
        }
    return render (request,'pages/index.html',context)
    


def update(request,id):
    book_id=get_object_or_404(Book,id=id)
    if request.method == 'POST':
        book_save=Bookform(request.POST, request.FILES, instance=book_id)
        if book_save.is_valid():
            book_save.save()
            return redirect('/')

    else :
        
        book_save=Bookform(instance=book_id)
        print(id)
        
        


    context={
            'form':book_save,
        }
    return render(request,'pages/update.html',context)
