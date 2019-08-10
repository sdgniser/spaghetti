from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include

from .views import *

app_name = 'users'
urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('update/', UserUpdateView.as_view(), name='update'),
    path('<slug:pk>/', UserView.as_view(), name='profile'),
]
