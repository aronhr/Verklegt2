from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('', LoginView.as_view(template_name='login/index.html'), name="login-index"),
    path('logout/', LogoutView.as_view(next_page='login'), name="logout")
]
