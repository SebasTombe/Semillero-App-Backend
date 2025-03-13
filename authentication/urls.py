from django.urls import path, include
from .views import LoginView, LogoutView, SignupView

urlpatterns = [
    
    path('login/',
         LoginView.as_view(), name='login'),

    path('logout/',
         LogoutView.as_view(), name='logout'),
    
    path('signup/',
         SignupView.as_view(), name='signup'),
]