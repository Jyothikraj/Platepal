from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .frontend_views import register_page
from .views import RegisterView,ProfileView
urlpatterns = [
    path(
        "",
        LoginView.as_view(
            template_name="users/login.html",
            redirect_authenticated_user=True,
            next_page="/home/"
        ),
        name="login"
    ),

    path(
        "logout/",
        LogoutView.as_view(),
        name="logout"
    ),

    path(
        "register/",
        register_page,
        name="register-page"
    ),
]