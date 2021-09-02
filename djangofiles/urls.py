from django.urls import path
from . import views
from django.contrib.auth import views as view_auth
from .forms import UserLoginForm

urlpatterns = [
    path(
        'login/',
        view_auth.LoginView.as_view(
            template_name="registration/login.html",
            authentication_form=UserLoginForm
        ),
        name='login'
    )
]