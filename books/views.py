from django.shortcuts import render, redirect
from .models import Book
from django.contrib.auth.decorators import login_required

@login_required(login_url='home')
def add_book(request):
    if request.method == 'POST':
        title = request.POST['title']
        price = request.POST['price']
        author = request.POST['author']
        desc = request.POST['desc']
        img = request.FILES.get('img', '')
        print(img)
        book = Book(title=title, price=price, author=author, desc=desc, img=img)
        book.save()
        return redirect('showbook')
    if request.user.is_anonymous:
        print(request.user.first_name)
    else:
        print('not anonymous', request.user.email, request.user.username)
        return render(request, 'book/addbook.html')

@login_required(login_url='home')
def all_books(request):
    return render(request, 'book/allbooks.html')

@login_required(login_url='home')
def contact_us(request):
    return render(request, 'book/contactus.html')

@login_required(login_url='home')
def edit_book(request):
    if request.method == 'POST':
        book = Book.objects.get(id=request.POST['id'])
        if request.POST['submit'] == 'delete':
            book.delete()
            return redirect('showbook')
        else:
            book.title = request.POST['title']
            book.price = request.POST['price']
            book.author = request.POST['author']
            book.desc = request.POST['desc']
            img = request.FILES.get('image', '')
            if img:
                book.img = request.FILES['image']
            book.save()
            if request.POST['submit'] == 'save':
                return redirect('showbook')
            else:
                return render(request, 'book/editbook.html', {'book': book})
    book = Book.objects.get(id=request.GET['id'])
    return render(request, 'book/editbook.html', {'book': book})

def small(query):
    x, i = '', 1
    for q in query:
        if i < 30:
            x += q
            i += 1
    x += '....'
    query = x
    return query

@login_required(login_url='home')
def search_book(request):
    query = request.GET['query']
    if len(query) >= 78:
        query = small(query)
        books = Book.objects.none()
    elif query == '':
        books = Book.objects.none()
    else:
        titlebooks = Book.objects.filter(title__icontains=query)
        decsbooks = Book.objects.filter(desc__icontains=query)
        pricebooks = Book.objects.filter(price__icontains=query)
        authorbooks = Book.objects.filter(author__icontains=query)
        books = titlebooks.union(decsbooks.union(pricebooks.union(authorbooks)))
    return render(request, 'book/searchbook.html', {'books': books, 'query': query})

@login_required(login_url='home')
def show_book(request):
    books = Book.objects.all()
    return render(request, 'book/showbook.html', {'books': books})



