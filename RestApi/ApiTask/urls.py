from django.conf.urls import url
from .views import UserRegistrationView
from .views import UserLoginView
from .views import UserProfileView


urlpatterns = [
    url('signup', UserRegistrationView.as_view()),
    url('signin', UserLoginView.as_view()),
    url('profile', UserProfileView.as_view()),

    ]
