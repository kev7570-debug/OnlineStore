from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView
from .views import RegisterView
from .forms import UserLoginForm  # добавлен импорт

app_name = 'users'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(
        template_name='users/login.html',
        form_class=UserLoginForm  # добавлена строка
    ), name='login'),
    path('logout/', LogoutView.as_view(next_page='users:logged_out'), name='logout'),
    path('logged_out/', TemplateView.as_view(template_name='users/logged_out.html'), name='logged_out'),
]
