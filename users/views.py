from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import UserRegisterForm

class RegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.send_welcome_email(user.email)
        return super().form_valid(form)

    def send_welcome_email(self, user_email):
        subject = 'Добро пожаловать в SkyStore!'
        message = (
            'Здравствуйте!\n\n'
            'Спасибо за регистрацию в нашем магазине SkyStore.\n'
            'Мы рады приветствовать вас в нашей команде!\n\n'
            'С уважением,\n'
            'Команда SkyStore'
        )
        send_mail(
            subject,
            message,
            None,  # используется DEFAULT_FROM_EMAIL
            [user_email],
            fail_silently=False,
        )
