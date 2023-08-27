from django.urls import path
from crud.views.user_profile_view import UserProfileAPIView
from crud.views.user_view import RegisterUserAPIView


urlpatterns = [
    path("user/", UserProfileAPIView.as_view(), name="user-profile"),
    path("register/", RegisterUserAPIView.as_view(), name="register"),
]
