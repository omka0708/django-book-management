from django.urls import path, include
from .views import UserListAPI, UserDetailAPI, CurrentUserDetailAPI, RegisterAPI, LoginAPI
from knox import views as knox_views

urlpatterns = [
    path('api/auth', include('knox.urls')),
    path('api/auth/register', RegisterAPI.as_view(), name='register'),
    path('api/auth/login', LoginAPI.as_view(), name='login'),
    path('api/auth/logout', knox_views.LogoutView.as_view(), name='logout'),

    path('api/user', CurrentUserDetailAPI.as_view()),
    path('api/users', UserListAPI.as_view()),
    path('api/users/<int:pk>', UserDetailAPI.as_view()),
]
