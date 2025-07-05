# accounts/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required

User = get_user_model()


def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        age = request.POST.get("age")
        phone_number = request.POST.get("phone_number")

        # 1. check passwords
        if password1 != password2:
            messages.error(request, "Parollar mos emas!")
            return render(request, "accounts/register.html")

        if int(age) < 16:
            messages.error(request, "Ro‘yxatdan o‘tish uchun kamida 16 yoshda bo‘lish kerak.")
            return redirect('register')

        if not phone_number.isdigit() or len(phone_number) < 9:
            messages.error(request, "Telefon raqam noto‘g‘ri.")
            return redirect('register')

        # 2. username or email check
        if User.objects.filter(username=username).exists():
            messages.error(request, "Bu username allaqachon olingan.")
            return render(request, "accounts/register.html")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Bu email bilan allaqachon ro'yxatdan o'tilgan.")
            return render(request, "accounts/register.html")

        # 3. User create
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password1,
            user_type="customer",
            age=age if age else None,
            phone_number=phone_number
        )
        if request.user.is_authenticated:
            return redirect('home')  # yoki boshqa sahifaga

        # 4. Login
        login(request, user)
        return redirect("home")  # yoki boshqa sahifaga
    return render(request, "accounts/register.html")



@login_required
def profile_view(request):
    user = request.user  # Tizimga kirgan user
    return render(request, 'accounts/profile.html', {'user': user})