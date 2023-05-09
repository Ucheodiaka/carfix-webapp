from django.urls import path

from . import views

urlpatterns = [
    # Main Views
    path("", views.index, name="index"),
    path("profile/<query>", views.profile, name="profile"),
    path("register", views.register, name="register"),
    path("logout", views.logout_view, name="logout"),
]