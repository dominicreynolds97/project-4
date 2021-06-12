from jwt_auth.populated import PopulatedUserSerializer
from django.urls import path
from django.urls.resolvers import URLPattern
from .views import LoginUserView, RegisterUserView, UserDetailView

urlpatterns = [
    path('register/', RegisterUserView.as_view()),
    path('login/', LoginUserView.as_view()),
    path('users/<int:pk>/', UserDetailView.as_view())
]