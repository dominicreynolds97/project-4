from django.urls import path
from django.urls.resolvers import URLPattern
from .views import LoginUserView, RegisterUserView

urlpatterns = [
    path('register/', RegisterUserView.as_view()),
    path('login/', LoginUserView.as_view())
]