from django.shortcuts import render, redirect
from books.models import Book
from books.models import UserDetails
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required(login_url='home')
def profile(request):
    return render(request, 'profile/profile.html')

@login_required(login_url='home')
def profile_edit(request):
    if request.method == 'POST':
        if request.POST['submit'] == 'profile-pic':
            userdetails = UserDetails.objects.get(user=User.objects.get(username=request.user.username))
            image = request.FILES.get('image', '')
            if image:
                userdetails.image = image
            userdetails.save()
            return redirect('profile')
        elif request.POST['submit'] == 'profile':
            user = User.objects.get(username=request.user.username)
            user.first_name = request.POST['fname']
            user.last_name = request.POST['lname']
            user.save()
            userdetails = UserDetails.objects.get(user=User.objects.get(username=request.user.username))
            print( 'rishav shahil')
            # userdetails = UserDetails(user=User.objects.get(username=request.user.username), gender=gender)
            userdetails.gender = request.POST['gender']
            if request.POST['dob']:
                userdetails.dob =request.POST['dob']
            userdetails.phone =request.POST['phone']
            userdetails.save()
            return redirect('profile')
    return render(request, 'profile/profile-edit.html')

@login_required(login_url='home')
def change_password(request):
    messages = {'message': ''}
    if request.method == 'POST':
        current = request.POST['currentpassword']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']
        user = User.objects.get(id=request.user.id)
        check = user.check_password(current)
        if check:
            if pass1 == pass2:
                user.set_password(pass2)
                user.save()
                messages['message'] = 'Password Change Successfully!!'
                messages['type'] = 'success'
                return render(request, 'profile/profile-change-pass.html', messages)
            else:
                messages['message'] = 'Password Not Matching!!'
                messages['type'] = 'warning'
                return render(request, 'profile/profile-change-pass.html', messages)
        else:
            messages = {'message': 'Please Enter correct password', 'type': 'danger'}
            return render(request, 'profile/profile-change-pass.html', messages)

    return render(request, 'profile/profile-change-pass.html')

@login_required(login_url='home')
def profile_settings(request):
    return render(request, 'profile/profile-settings.html')


@login_required(login_url='home')
def show_book(request):
    books = Book.objects.all()
    return render(request, 'profile/showbook.html', {'books': books})



