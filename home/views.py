from .models import ContactUser, SubscribeUser
from django.shortcuts import render, redirect
from django.contrib import messages

def home(request):
    return render(request, 'index.html')

def contact_form_view(request):
    try:
        if request.method == 'POST':
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            user_mail = request.POST.get('user_mail')
            user_number = request.POST.get('user_number')
            user_message = request.POST.get('user_message')

            ContactUser.objects.create(
                first_name=first_name,
                last_name=last_name,
                user_mail=user_mail,
                user_number=user_number,
                user_message=user_message,
            )
            messages.success(request, "Thank you for Contact us!")
        return redirect('home')
    except Exception as e:
        messages.error(request, str(e))
        return redirect('home')


def subscribe_form_view(request):
    try:
        if request.method == 'POST':
            user_mail = request.POST.get('user_mail')
            SubscribeUser.objects.create(user_mail=user_mail)
            messages.success(request, "Thank you for subscribing!")
        return redirect('home')
    except Exception as e:
        messages.error(request, str(e))
        return redirect('home')
