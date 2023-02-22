from django.shortcuts import render, redirect, HttpResponse, reverse

from app01 import models


# Create your views here.

def index(request):
    return render(request, 'index.html')


def book_list(request):
    book_queryset = models.Book.objects.all()
    return render(request, 'book_list.html', locals())


def publish_list(request):
    publish_queryset = models.Publish.objects.all()
    sum_book = models.Book.objects.all()
    return render(request, 'publish_list.html', locals())


def author_list(request):
    author_queryset = models.Author.objects.all()
    return render(request, 'author_list.html', locals())


def book_add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        publish_date = request.POST.get('publish_date')
        publish_id = request.POST.get('publish')
        authors_list = request.POST.getlist('authors')

        book_obj = models.Book.objects.create(name=name, price=price, publish_date=publish_date, publish_id=publish_id)
        book_obj.authors.add(*authors_list)
        return redirect('book_list')

    publish_queryset = models.Publish.objects.all()
    author_queryset = models.Author.objects.all()
    return render(request, 'book_add.html', locals())


def edit_book(request, edit_id):
    edit_obj = models.Book.objects.filter(pk=edit_id).first()
    if request.method == 'POST':
        # print(request.POST)
        name = request.POST.get('name')
        price = request.POST.get('price')
        publish_date = request.POST.get('publish_date')
        publish_id = request.POST.get('publish')
        authors_list = request.POST.getlist('authors')
        models.Book.objects.filter(pk=edit_id).update(name=name, price=price, publish_date=publish_date,
                                                      publish_id=publish_id)
        edit_obj.authors.set(authors_list)
        return redirect('book_list')
    publish_queryset = models.Publish.objects.all()
    author_queryset = models.Author.objects.all()
    return render(request, 'edit_book.html', locals())


def del_book(request,del_id):
    models.Book.objects.filter(pk=del_id).delete()
    return redirect('book_list')