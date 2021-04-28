#Account views
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from datetime import datetime
from django.contrib.auth.models import User, auth
from books.models import UserDetails
def registration(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        username = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password2 == password1:
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exist!')
                return redirect('home')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1, first_name=fname,
                                                last_name=lname)
                user.save()
                userdetails = UserDetails(user=User.objects.filter(username=username)[0])
                userdetails.save()
                return redirect('add')
        else:
            print('password not match')
            messages.error(request, 'Password not Matching. Try Again!! ')
            return redirect('index')
    else:
       return render(request, 'accounts/index.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Incorrect Email or Password')
            return redirect('index')
    else:
        return redirect('index')

def logout(request):
    auth.logout(request)
    return redirect('index')


def index(request):
    return render(request, 'accounts/index.html')

def about(request):
    return render(request, 'accounts/about.html')

def contact(request):
    contact = Contact()
    if request.method == 'POST':
        contact.name = request.POST['name']
        contact.email = request.POST['email']
        contact.phone = request.POST['phone']
        if contact.phone == '':
            contact.phone = 0
        print(contact.phone)
        contact.feedback = request.POST['feedback']
        contact.subscribe = request.POST.get('subscribe', False)
        if contact.subscribe == 'on':
            contact.subscribe = True
        contact.date = datetime.today()
        contact.save()
        if request.POST['submit'] == 'contact':
            messages.success(request, '  Form Submitted Successfully!')
        elif request.POST['submit'] == 'contactus':
            return render(request, 'book/contactus.html', {'message': 'Form Submitted Succesfully'})
    return render(request, 'accounts/contact.html')

